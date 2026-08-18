#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTO_REPARER.py — réparation BORNÉE des chaînes de monitoring (étape 5, 18/08/2026).

Validée par la famille ACE777 : VERDICT GO-AVEC-RÉSERVE (3/3), confiance moyenne.
Implémente les réserves obligatoires (backoff exponentiel, circuit-breaker
CPU/RAM, vérif hub, mutex fcntl, journal d'audit immuable, cooldown post-
redémarrage). NE TOUCHE JAMAIS au moteur de trading (ACE/HULK).

MODE (doctrine « l'automation propose, l'humain approuve ») :
  --dry-run  (DÉFAUT) : détecte ce qui serait réparé, trace + alerte, NE RELANCE RIEN.
  --actif             : relance réellement (launchctl kickstart) — après GO humain.

Usage :
  python3 auto_reparer.py              # dry-run (observation)
  python3 auto_reparer.py --actif      # réparation réelle (GO requis)
  python3 auto_reparer.py --etat       # affiche l'état des tentatives/backoffs

Stdlib uniquement, macOS, lecture seule sauf l'action bornée. Jamais d'ordre.
"""
import json
import os
import sys
import time
import fcntl
import tempfile
import subprocess
import threading
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent
IM = RACINE / "Index_Maison"
STRATEGIE = IM / "strategie"
THERMO = IM / "thermo"
DATA = IM / "data"
SCRIPTS = IM / "scripts"

RAPPORT_SANTE = THERMO / "sante_index.json"
ETAT_REPARATION = THERMO / "reparations_state.json"
AUDIT = THERMO / "reparations.jsonl"
ALERTE_VOCALE = SCRIPTS / "alerte_vocale.py"
HUB_HEALTH = "http://127.0.0.1:11435/health"
# Marqueur de bascule observation -> actif (GO humain, comme CHAMPION_ACTIF/STOP)
ACTIF_MARKER = STRATEGIE / "AUTO_REPARER_ACTIF"

# KILL-SWITCH (mêmes fichiers que sante_index.py)
KILL_SWITCHES = [STRATEGIE / "STOP", IM / "STOP_ALL"]
MAINTENANCE = STRATEGIE / "MAINTENANCE_PREVUE"

# Whitelist MONITORING uniquement — jamais le moteur de trading (HULK = exclu).
# chaîne sante_index -> services launchd à relancer (ordre = 1er suspect d'abord).
CHAINE_SERVICES = {
    "baleines": ["com.ace777.whales", "com.ace777.pont-onchain"],
    "cpfp":     ["com.ace777.cpfp"],
    "securite": ["com.ace777.veilleuse"],
    "live":     ["com.ace777.hub-cockpit-feed"],
    "saison":   ["com.ace777.saison"],
    # "hulk" : moteur paper trading -> JAMAIS touché ici.
}

MAX_ATTEMPTS = 3            # max tentatives / service / 24h
BACKOFF_SEC = [60, 300, 900]  # backoff exponentiel : 1 min, 5 min, 15 min
WINDOW_SEC = 86400          # fenêtre de 24h pour le compteur
STABILITE_SEC = 300         # un service doit rester stable 5 min avant reset
COOLDOWN_GLOBAL_SEC = 600   # 10 min entre 2 réparations globales
SEUIL_LOAD = 6.0            # circuit-breaker : load average 1 min
SEUIL_SWAP_MB = 2048        # circuit-breaker : swap utilisé > 2 Go
LOCK_PATH = THERMO / "auto_reparer.lock"


# ---------------------------------------------------------------- helpers
def _lire_json(path: Path, defaut):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return defaut


def _ecrire_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, str(path))
    except Exception:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass
        raise


def _append_jsonl(path: Path, entry):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _kill_switch_actif() -> bool:
    return any(k.exists() for k in KILL_SWITCHES)


def _maintenance_prevue() -> bool:
    if not MAINTENANCE.exists():
        return False
    try:
        fin = datetime.fromisoformat(MAINTENANCE.read_text(encoding="utf-8").strip())
        return datetime.now(timezone.utc) < fin
    except Exception:
        return False


def est_actif() -> bool:
    """True si le GO humain a posé le marqueur AUTO_REPARER_ACTIF.
    Par défaut : observation (dry-run) — rien n'est relancé."""
    return ACTIF_MARKER.exists()


def _hub_ok() -> bool:
    """Vérif hub strict avant toute réparation (réserve JUGE)."""
    import urllib.request
    try:
        req = urllib.request.Request(HUB_HEALTH, headers={"User-Agent": "ace777-auto-reparer/1"})
        with urllib.request.urlopen(req, timeout=3) as r:
            d = json.loads(r.read().decode())
        return d.get("status") == "ok"
    except Exception:
        return False


def _charge_ok() -> bool:
    """Circuit-breaker matériel : gèle la réparation si le Mac suffoque (réserve PROTOCOL)."""
    try:
        if os.getloadavg()[0] > SEUIL_LOAD:
            return False
    except Exception:
        pass
    try:
        out = subprocess.check_output(["sysctl", "-n", "vm.swapusage"], text=True,
                                      stderr=subprocess.DEVNULL)
        # "total = 4096.00M  used = 1234.00M  free = ..."
        import re
        m = re.search(r"used\s*=\s*([\d.]+)M", out)
        if m and float(m.group(1)) > SEUIL_SWAP_MB:
            return False
    except Exception:
        pass
    return True


def _proc_vivant(label: str) -> bool:
    try:
        out = subprocess.check_output(["launchctl", "list"], text=True,
                                      stderr=subprocess.DEVNULL)
        if label in out:
            return True
    except Exception:
        pass
    try:
        out = subprocess.check_output(["pgrep", "-fl", label], text=True,
                                      stderr=subprocess.DEVNULL)
        return label in out
    except Exception:
        return False


def _alerter(message: str, ident: str):
    try:
        subprocess.Popen([sys.executable, str(ALERTE_VOCALE), "--message", message,
                          "--id", ident],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         start_new_session=True)
    except Exception:
        pass


def _trace_agora(quoi: str):
    """1 ligne append-only dans la mémoire collab (canon + miroir).
    NON-BLOQUANT (réserve GEMINI) : exécuté dans un thread daemon — une écriture
    AGORA ne doit JAMAIS geler la boucle de santé critique."""
    def _travail():
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
        ligne = f"| {ts} | auto_reparer | ~ | Index_Maison/thermo | {quoi} |"
        cibles = [Path.home() / "Documents/Obsidian_ACE777/Swarm_Bus/09_MEMOIRE_COLLAB.md",
                  IM / "MEMOIRE_COLLAB.md"]
        for cible in cibles:
            try:
                if not cible.exists():
                    continue
                txt = cible.read_text(encoding="utf-8")
                if ligne in txt:
                    continue
                lignes = txt.splitlines()
                ins = None
                for i, ln in enumerate(lignes):
                    if ln.strip().startswith("|---"):
                        ins = i + 1
                        break
                if ins is None:
                    continue
                lignes.insert(ins, ligne)
                fd, tmp = tempfile.mkstemp(dir=str(cible.parent), suffix=".tmp")
                try:
                    with os.fdopen(fd, "w", encoding="utf-8") as f:
                        f.write("\n".join(lignes) + "\n")
                    os.replace(tmp, str(cible))
                except Exception:
                    if os.path.exists(tmp):
                        os.remove(tmp)
                    raise
            except Exception:
                pass
    threading.Thread(target=_travail, daemon=True).start()


# ---------------------------------------------------------------- état
def _charger_etat() -> dict:
    return _lire_json(ETAT_REPARATION, {})


def _sauver_etat(etat: dict):
    _ecrire_json(ETAT_REPARATION, etat)


def _slot(etat: dict, service: str) -> dict:
    if service not in etat:
        etat[service] = {
            "attempts": 0,
            "window_start": time.time(),
            "last_attempt": 0,
            "backoff_level": 0,
            "last_success": 0,
        }
    return etat[service]


def _reset_fenetre(s: dict, now: float):
    if now - s.get("window_start", now) > WINDOW_SEC:
        s["attempts"] = 0
        s["window_start"] = now
        s["backoff_level"] = 0


def _stabilise(s: dict, now: float):
    """Réserve MISSION : après un succès, reset du compteur SEULEMENT si le
    service est resté vivant >= STABILITE_SEC (pas de flapping)."""
    ls = s.get("last_success") or 0
    if ls and (now - ls) >= STABILITE_SEC:
        s["attempts"] = 0
        s["backoff_level"] = 0
        s["last_success"] = 0


# ---------------------------------------------------------------- cœur
def _lancer_kickstart(service: str) -> bool:
    uid = os.getuid()
    r = subprocess.run(["launchctl", "kickstart", "-k", f"gui/{uid}/{service}"],
                       capture_output=True, text=True, timeout=60)
    return r.returncode == 0


def reparer(actif: bool = False) -> dict:
    """Parcourt le dernier rapport de santé et répare (ou propose) les chaînes cassées."""
    now = time.time()
    rapport = _lire_json(RAPPORT_SANTE, {})
    chaines = rapport.get("chaines", []) or []
    etat = _charger_etat()

    res = {"mode": "actif" if actif else "dry-run", "actions": [], "gel": None}

    # Garde-fous globaux
    if _kill_switch_actif():
        res["gel"] = "kill-switch actif"
        return res
    if _maintenance_prevue():
        res["gel"] = "maintenance prévue"
        return res
    if not _charge_ok():
        res["gel"] = "circuit-breaker CPU/RAM"
        return res
    if not _hub_ok():
        res["gel"] = "hub down"
        return res

    # Cooldown global (10 min)
    g = etat.get("_global_last") or 0
    if now - g < COOLDOWN_GLOBAL_SEC:
        res["gel"] = f"cooldown global ({int(COOLDOWN_GLOBAL_SEC - (now - g))}s restants)"
        return res

    # Chaînes cassées -> services whitelistés
    casses = [c for c in chaines if not c.get("ok") and c.get("id") in CHAINE_SERVICES]

    for chaine in casses:
        cid = chaine.get("id")
        for service in CHAINE_SERVICES[cid]:
            s = _slot(etat, service)
            _reset_fenetre(s, now)
            _stabilise(s, now)

            if _proc_vivant(service):
                # déjà vivant : rien à faire, et si stable -> reset déjà fait ci-dessus
                continue
            if s["attempts"] >= MAX_ATTEMPTS:
                res["actions"].append({"service": service, "decision": "skip",
                                       "raison": f"max {MAX_ATTEMPTS} essais/24h atteint"})
                continue
            backoff = BACKOFF_SEC[min(s["backoff_level"], len(BACKOFF_SEC) - 1)]
            if s.get("last_attempt") and (now - s["last_attempt"]) < backoff:
                res["actions"].append({"service": service, "decision": "skip",
                                       "raison": f"backoff {int(backoff)}s pas écoulé"})
                continue

            # Re-vérif stricte JUSTE avant l'action (réserve GEMINI/JUGE : le
            # kill-switch doit être vérifié au moment exact de l'exécution, pas
            # seulement au début du run)
            if _kill_switch_actif() or _maintenance_prevue():
                res["gel"] = "kill-switch/maintenance apparu pendant le run"
                break

            # --- tentative (dry-run = trace seulement) ---
            ts_iso = datetime.now(timezone.utc).isoformat()
            if not actif:
                s["last_attempt"] = now
                s["backoff_level"] = min(s["backoff_level"] + 1, len(BACKOFF_SEC) - 1)
                s["attempts"] += 1
                res["actions"].append({"service": service, "decision": "dry-run",
                                       "raison": "relancerait (observation)"})
                _append_jsonl(AUDIT, {"ts": ts_iso, "service": service, "mode": "dry-run",
                                      "action": "kickstart", "status": "proposé"})
                _alerter(f"Alerte ACE777. Chaîne {cid} cassée : {service} à relancer (observation).",
                         str(int(now)))
                _trace_agora(f"étape5 auto-réparation (dry-run) : {service} à relancer ({cid})")
                continue

            _alerter(f"Alerte ACE777. Tentative de réparation de {service}.", str(int(now)))
            ok = _lancer_kickstart(service)
            s["last_attempt"] = now
            if ok:
                s["last_success"] = now
                s["backoff_level"] = min(s["backoff_level"] + 1, len(BACKOFF_SEC) - 1)
                res["actions"].append({"service": service, "decision": "relancé", "raison": "ok"})
                _append_jsonl(AUDIT, {"ts": ts_iso, "service": service, "mode": "actif",
                                      "action": "kickstart", "status": "ok"})
                _alerter(f"Service {service} relancé.", str(int(now)))
                _trace_agora(f"étape5 auto-réparation : {service} relancé (ok)")
            else:
                s["attempts"] += 1
                s["backoff_level"] = min(s["backoff_level"] + 1, len(BACKOFF_SEC) - 1)
                res["actions"].append({"service": service, "decision": "échec", "raison": "kickstart rc≠0"})
                _append_jsonl(AUDIT, {"ts": ts_iso, "service": service, "mode": "actif",
                                      "action": "kickstart", "status": "échec"})
                _trace_agora(f"étape5 auto-réparation : {service} échec kickstart")

    if res["actions"]:
        etat["_global_last"] = now
        _sauver_etat(etat)
    return res


def main():
    args = [a for a in sys.argv[1:]]
    if "--etat" in args:
        etat = _charger_etat()
        if not etat:
            print("Aucun état de réparation (aucune tentative).")
            return 0
        for k, v in sorted(etat.items()):
            if k.startswith("_"):
                continue
            print(f"  {k}: attempts={v.get('attempts')}/{MAX_ATTEMPTS} "
                  f"backoff_level={v.get('backoff_level')} "
                  f"last_success={datetime.fromtimestamp(v.get('last_success') or 0, timezone.utc).isoformat() if v.get('last_success') else '-'}")
        return 0

    actif = ("--actif" in args) or est_actif()
    # Mutex fcntl : une seule réparation à la fois (réserve MISSION)
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOCK_PATH, "w") as lf:
        try:
            fcntl.flock(lf, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("[AUTO_REPARER] une réparation est déjà en cours (lock).")
            return 0
        try:
            res = reparer(actif=actif)
        finally:
            fcntl.flock(lf, fcntl.LOCK_UN)

    mode = res["mode"]
    if res.get("gel"):
        print(f"[AUTO_REPARER] {mode} — gelé : {res['gel']}")
    elif not res["actions"]:
        print(f"[AUTO_REPARER] {mode} — rien à réparer.")
    else:
        for a in res["actions"]:
            print(f"[AUTO_REPARER] {mode} — {a['service']}: {a['decision']} ({a['raison']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
