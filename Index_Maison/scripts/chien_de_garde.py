#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle : Chien de garde des organes ACE777. Lit le registre, mesure l'âge réel
       des organes (pouls_direct ou produit), crie aux 3 endroits si trop vieux,
       gère l'anti-tempête (1h/organe) et le kill-switch.
Standard : Python 3.9+, stdlib uniquement, atomique, robuste, idempotent.
"""

import os
import sys
import json
import time
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Chemins absolus ou relatifs robustes basés sur la structure ACE777
BASE_DIR = Path(__file__).resolve().parent.parent.parent
INDEX_MAISON = BASE_DIR / "Index_Maison"
REGISTRE_PATH = INDEX_MAISON / "strategie" / "REGISTRE_ORGANES.json"
POULS_DIR = INDEX_MAISON / "pouls"
ETAT_CHIEN = POULS_DIR / ".chien_etat.json"
RAPPORT_JSON = INDEX_MAISON / "thermo" / "CHIEN_RAPPORT.json"
RAPPORT_MD = INDEX_MAISON / "thermo" / "CHIEN_RAPPORT.md"
MEMOIRE_COLLAB = INDEX_MAISON / "MEMOIRE_COLLAB.md"  # conservé (compat) mais PLUS écrit depuis le 18/09
ALERTES_LOG = INDEX_MAISON / "thermo" / "CHIEN_ALERTES.md"  # log dédié des alertes CHIEN
STOP_FILE = INDEX_MAISON / "strategie" / "STOP"
STOP_ALL_FILE = INDEX_MAISON / "strategie" / "STOP_ALL"
MAINT_FILE = INDEX_MAISON / "strategie" / "MAINTENANCE_PREVUE"
ALERTE_VOCALE_SCRIPT = INDEX_MAISON / "scripts" / "alerte_vocale.py"

# ── SENS DÉCLARÉS — l'organe VIVANT mais AVEUGLE (réparation 20/09/2026) ─────
# POURQUOI : un chien qui ne mesure que la FRAÎCHEUR rate la panne la plus
# sournoise — l'organe VIVANT mais AVEUGLE : le process tourne, le produit est
# frais, launchd sort 0... et pourtant il ne peut PLUS DÉCIDER (sa décision
# reste nulle). Prouvé le 20/09 : le signal short BTC (CRITIQUE) a eu son
# `score` à nul pendant ~5 h (rotation de son fichier source à 13:12Z) pendant
# que le chien disait « short-btc vivant », que la veilleuse était verte et que
# la page affichait un bloc vide. Famille R14 : une panne muette est pire qu'une
# panne bruyante, parce qu'on ne la répare jamais.
# MÉCANISME : `strategie/sens_declares.json` déclare, par organe sensible, LE
# champ qui prouve qu'il peut encore décider, la fenêtre tolérée et pourquoi.
# Rien d'implicite : un organe sans sens déclaré n'est PAS jugé aveugle (pas de
# devinette sur les organes dont « décision nulle » est un état normal).
SENS_PATH = INDEX_MAISON / "strategie" / "sens_declares.json"
ETAT_AVEUGLE = POULS_DIR / ".chien_aveugle_etat.json"

# ── LE CRI VIVANT (20/09/2026, GO « incassable auto-réparant ») ──────────────
# POURQUOI : un cri qui n'existe que sous forme de ligne ajoutée à un log est un cri
# MORT — on ne sait pas s'il est encore vrai, ni s'il est déjà résolu, ni s'il a
# vraiment été prononcé. Le 20/09, le chien a crié « short-btc aveugle » une fois :
# impossible de dire, en lisant le log, si l'organe est ENCORE aveugle maintenant.
# Ici le cri devient VIVANT : `thermo/cris.json` ne contient QUE les cris ACTIFS à
# l'instant du cycle (il s'auto-efface quand la cause disparaît), chacun avec depuis
# quand il dure, combien de fois il a été crié, et si la VOIX a réellement été
# lancée (un cri muet est un faux cri : R14). La page vol lit le même fichier —
# une seule vérité entre ce que dit le chien et ce que voit l'humain.
CRIS_JSON = INDEX_MAISON / "thermo" / "cris.json"
REVUE_JSON = INDEX_MAISON / "thermo" / "revue_organes.json"
CRIS_ACTIFS = {}   # clé -> {message, gravite, voix}  (rempli par crier(), vidé à chaque run)

# ── CODE DE SORTIE LAUNCHD (réparation 20/09/2026) ───────────────────────────
# 46 organes MINEUR étaient classés « NON SURVEILLÉS » : chargés par launchd, aucun
# produit déclaré dans le registre, donc RIEN à mesurer — pour eux, toutes les
# colonnes du chien étaient vides. Une panne de l'un d'eux n'aurait été vue nulle
# part (même famille que geopol/croisements-indices figés en silence). Or launchd
# sait DÉJÀ quelque chose de chacun, gratuitement : sa dernière sortie. On ne
# l'invente pas, on le LIT — un job qui sort ≠ 0 est un vrai signal, 0 = il tourne.
# Les codes non nuls VOULUS (canal d'alerte) sont déclarés dans contrat_sortie.json :
# une seule table, partagée avec la page vol (une seule vérité).
CONTRAT_SORTIE_PATH = INDEX_MAISON / "strategie" / "contrat_sortie.json"

def ecriture_atomique(chemin: Path, data_str: str) -> None:
    """Écriture atomique avec mkstemp + os.replace et sauvegarde d'un backup."""
    chemin.parent.mkdir(parents=True, exist_ok=True)
    if chemin.exists():
        try:
            backup_path = chemin.with_suffix(chemin.suffix + ".bak")
            backup_path.write_bytes(chemin.read_bytes())
        except Exception:
            pass

    import tempfile
    fd, tmp_path = tempfíl = tempfile.mkstemp(dir=str(chemin.parent), text=True)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(data_str)
        os.replace(tmp_path, str(chemin))
    except Exception as e:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise e

def verifier_kill_switch() -> bool:
    return STOP_FILE.exists() or STOP_ALL_FILE.exists() or MAINT_FILE.exists()

def charger_json_securise(chemin: Path, defaut=None):
    if not chemin.exists():
        return defaut
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return defaut

def resoudre_chemin_produit(organe_def: dict):
    """Chemin RÉEL du produit d'un organe (None si introuvable).

    UNE SEULE VÉRITÉ (20/09/2026) : cette résolution est utilisée par le chien
    (`evaluer_age_organe`) ET par la revue des organes (`revue_organes.py`). Deux
    résolutions divergentes finiraient par juger deux choses différentes.

    Jetons acceptés :
      dernier:<motif>  = fichier le plus récent matchant le glob (organes quotidiens)
      <motif *>        = IDEM pour tout motif à joker (réparé 20/09/2026 : un motif
                         comme `hulk-mexc/runs/SUIVI_SETUP_*.jsonl` était traité comme
                         un chemin LITTÉRAL, jamais trouvé → l'organe tombait dans
                         « sans produit » et n'était jugé que sur sa sortie launchd,
                         donc JAMAIS sur son produit : une panne de ce produit
                         (suivi-setup-red, produit figé) était invisible. Même
                         famille que le faux vert du gardien « Chien » de la page vol.)
      <date_compact>   = 20260910 (L2_…)
      <date>           = 2026-09-10 (VEILLE_HUB_…)
    """
    mode = organe_def.get("mode", "produit")
    nom = organe_def.get("organe")

    if mode == "pouls_direct":
        return POULS_DIR / f"{nom}.json"

    chemin_prod = organe_def.get("chemin_pouls_ou_produit")
    if not chemin_prod:
        # Repli par défaut selon les normes ACE777
        if nom == "hub":
            return BASE_DIR.parent / "prise-ia" / "heartbeat.json"
        if nom == "thermo":
            return INDEX_MAISON / "thermo" / "live.json"
        return POULS_DIR / f"{nom}.json"

    if chemin_prod.startswith("dernier:"):
        chemin_prod = chemin_prod[len("dernier:"):]
    else:
        if "<date_compact>" in chemin_prod:
            chemin_prod = chemin_prod.replace("<date_compact>", datetime.now(timezone.utc).strftime('%Y%m%d'))
        elif "<date>" in chemin_prod:
            chemin_prod = chemin_prod.replace("<date>", datetime.now(timezone.utc).strftime('%Y-%m-%d'))

    if any(c in chemin_prod for c in "*?["):
        candidats = sorted(BASE_DIR.glob(chemin_prod))
        return candidats[-1] if candidats else None
    return BASE_DIR / chemin_prod


def evaluer_age_organe(organe_def: dict) -> float:
    """Retourne l'âge en secondes du dernier battement / produit."""
    mode = organe_def.get("mode", "produit")
    chemin_cible = resoudre_chemin_produit(organe_def)

    if not chemin_cible or not chemin_cible.exists():
        return float('inf')

    try:
        if mode == "pouls_direct":
            data = charger_json_securise(chemin_cible, {})
            ts_str = data.get("dernier_battement")
            if not ts_str:
                return float('inf')
            dt = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        else:
            # Pour un produit brut, on utilise l'mtime du fichier
            mtime = chemin_cible.stat().st_mtime
            dt = datetime.fromtimestamp(mtime, tz=timezone.utc)
            
        maintenant = datetime.now(timezone.utc)
        age = (maintenant - dt).total_seconds()
        return max(0.0, age)
    except Exception:
        return float('inf')

def crier(organe_nom: str, message: str, gravite: str = "CRITIQUE"):
    """Déclenche les 3 cris avec protection anti-tempête 1h.

    Le cri est aussi inscrit dans CRIS_ACTIFS : l'état VIVANT des cris est ensuite
    écrit dans thermo/cris.json (liste des cris ACTIFS à cet instant, auto-effacée).
    """
    now_ts = time.time()
    etats = charger_json_securise(ETAT_CHIEN, {})

    dernier_cri = etats.get(organe_nom, 0)
    if now_ts - dernier_cri < 3600:
        # Anti-tempête respecté : le cri reste ACTIF (il est déjà dans CRIS_ACTIFS
        # grâce à la fusion avec le cycle précédent) mais la voix ne repart pas.
        CRIS_ACTIFS.setdefault(organe_nom, {"message": message, "gravite": gravite,
                                            "voix": "anti-tempête (voix il y a < 1 h)",
                                            # Le cri DURE : on date son début au premier cri
                                            # réellement prononcé (état anti-tempête), pas au
                                            # moment où ce fichier a été créé.
                                            "depuis_estime": dernier_cri})
        return

    etats[organe_nom] = now_ts
    ecriture_atomique(ETAT_CHIEN, json.dumps(etats, indent=2))

    # 1. Log dédié des alertes (append-only) — ne pollue plus MEMOIRE_COLLAB.
    #    Sorti du mémo le 18/09 (il le saturait : 101 lignes de bruit machine).
    ligne_memo = f"| {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}Z | CHIEN | {gravite} | {organe_nom} : {message} |\n"
    try:
        ALERTES_LOG.parent.mkdir(parents=True, exist_ok=True)
        with open(ALERTES_LOG, "a", encoding="utf-8") as f:
            f.write(ligne_memo)
    except Exception:
        pass

    # 2. Alerte vocale existante (nohup détaché, killall say avant).
    #    On TRACE le résultat : un cri dont la voix n'a pas pu être lancée est un
    #    FAUX CRI (l'humain lit « alerté » alors qu'il n'a rien entendu) — R14.
    voix = "non tentée (script absent)"
    if ALERTE_VOCALE_SCRIPT.exists():
        msg_voix = f"Alerte organe {organe_nom}. {message}"
        try:
            subprocess.Popen(
                ["python3", str(ALERTE_VOCALE_SCRIPT), msg_voix],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )
            voix = "lancée"
        except Exception as e:
            voix = "ÉCHEC DE LANCEMENT (%s)" % str(e)[:60]
    CRIS_ACTIFS[organe_nom] = {"message": message, "gravite": gravite, "voix": voix,
                              "depuis_estime": now_ts}

def _ts_iso(valeur):
    """Horodatage (ISO ou epoch) -> timestamp. None si illisible."""
    if valeur is None:
        return None
    if isinstance(valeur, (int, float)):
        return float(valeur)
    try:
        return datetime.fromisoformat(str(valeur).replace("Z", "+00:00")).timestamp()
    except Exception:
        try:
            return float(valeur)
        except Exception:
            return None


def _champ(donnees, chemin):
    """Lit un champ, chemin pointé accepté (« derniere.ts_emission »)."""
    d = donnees
    for part in str(chemin or "").split("."):
        if not isinstance(d, dict):
            return None
        d = d.get(part)
    return d


def _condition_remplie(donnees, cond):
    """`exiger_si` : la décision n'est exigée QUE si la condition est vraie.
    Exemple : le verdicteur-micro ne note que s'il y a eu au moins une alerte —
    sans cette clause on crierait « il ne décide pas » alors qu'il n'y a rien
    à décider (faux positif, exactement ce qu'on veut éviter)."""
    if not cond:
        return True
    val = _champ(donnees, cond.get("champ"))
    if "min" in cond:
        try:
            return float(val) >= float(cond["min"])
        except (TypeError, ValueError):
            return False
    if cond.get("non_null"):
        return val is not None
    return True


def mesurer_aveuglement(decl, etats):
    """Depuis quand cet organe ne peut plus décider ?

    mode « nul » (défaut) : la décision (champ_decision) est restée nulle.
      - jsonl : la date du DERNIER point où elle sortait est DANS le fichier → mesure
        exacte (queue seulement : ces JSONL pèsent des dizaines de Mo) ; si la queue
        n'en contient aucune, on rend une borne basse (au moins aussi ancien).
      - json  : le produit est RÉÉCRIT à chaque cycle, « depuis quand » n'est pas dans
        le fichier → c'est le chien qui le retient (état persistant, ETAT_AVEUGLE).
    mode « age » : la décision existe mais SON horodatage est vieux (produit réécrit
      et frais : c'est tout le piège de cette famille).

    Retourne None si le produit est absent/illisible : ce n'est PAS un aveuglement
    (c'est « hors délai / non surveillé », déjà traité plus haut).
    """
    cle = decl.get("cle") or decl.get("organe")
    produit = BASE_DIR / str(decl.get("produit", ""))
    if not produit.exists():
        return None
    champ = decl.get("champ_decision")

    points = []
    if decl.get("type") == "jsonl":
        try:
            with open(produit, "rb") as f:
                f.seek(0, os.SEEK_END)
                fin = f.tell()
                f.seek(max(0, fin - 4 * 1024 * 1024))
                bloc = f.read()
        except OSError:
            return None
        for ligne in bloc.split(b"\n"):
            if not ligne.strip():
                continue
            try:
                d = json.loads(ligne)
            except Exception:
                continue
            if isinstance(d, dict):
                points.append(d)
    else:
        d = charger_json_securise(produit, {})
        if not isinstance(d, dict):
            return None
        points.append(d)
    if not points:
        return None

    dernier = points[-1]
    maintenant = time.time()

    if decl.get("mode") == "age":
        ts = _ts_iso(_champ(dernier, champ))
        if ts is None:
            return None
        return {"age_sec": max(0.0, maintenant - ts), "exact": True}

    if not _condition_remplie(dernier, decl.get("exiger_si")):
        etats.pop(cle, None)   # rien à décider : le chrono repart de zéro
        return None
    if decl.get("type") == "jsonl":
        decision = premier = None
        for d in points:
            ts = _ts_iso(d.get("ts") or d.get("ts_iso") or d.get("date"))
            if ts is None:
                continue
            if premier is None:
                premier = ts
            if _champ(d, champ) is not None:
                decision = ts
        if decision is not None:
            return {"age_sec": max(0.0, maintenant - decision), "exact": True}
        if premier is not None:
            return {"age_sec": max(0.0, maintenant - premier), "exact": False}
        return None

    if _champ(dernier, champ) is not None:
        etats.pop(cle, None)   # il décide : sain
        return {"age_sec": 0.0, "exact": True}
    debut = etats.get(cle)
    if not debut:
        debut = maintenant
        etats[cle] = debut
    return {"age_sec": max(0.0, maintenant - debut), "exact": False}


def ecrire_cris_vivants():
    """Écrit l'état VIVANT des cris : thermo/cris.json (auto-effacé).

    Seuls les cris ACTIFS à cet instant y figurent. « depuis » et « nb_cris » sont
    repris du cycle précédent pour la même clé → un cri qui dure se VOIT durer, et
    quand la cause disparaît il disparaît du fichier (aucun cri fantôme à nettoyer
    à la main, aucune ligne de log à interpréter).
    """
    ancien = charger_json_securise(CRIS_JSON, {}) or {}
    anciens = {c.get("organe"): c for c in (ancien.get("cris") or []) if isinstance(c, dict)}
    maintenant = datetime.now(timezone.utc)
    cris = []
    for cle, info in CRIS_ACTIFS.items():
        av = anciens.get(cle) or {}
        voix = info.get("voix", "")
        depuis = av.get("depuis")
        if not depuis:
            deb = info.get("depuis_estime")
            depuis = (datetime.fromtimestamp(deb, tz=timezone.utc).isoformat(timespec="seconds")
                      if deb else maintenant.isoformat(timespec="seconds"))
        cris.append({
            "organe": cle,
            "gravite": info.get("gravite", "CRITIQUE"),
            "message": info.get("message", ""),
            "depuis": depuis,
            # Un cri vu avec une voix déjà prononcée vaut au moins 1 (sinon on afficherait
            # « 0 cri » pour un cri bien réel, seulement parce que la voix est en attente
            # d'anti-tempête — le genre de détail qui fait douter d'une alarme).
            "nb_cris": (int(av.get("nb_cris") or 0) + 1 if voix == "lancée"
                        else max(int(av.get("nb_cris") or 0), 1 if info.get("depuis_estime") else 0)),
            "voix": voix,
            "voix_le": maintenant.isoformat(timespec="seconds") if voix == "lancée" else av.get("voix_le"),
        })
    rang = {"CRITIQUE": 0, "MAJEUR": 1}
    cris.sort(key=lambda c: (rang.get(c["gravite"], 2), c["depuis"]))
    try:
        ecriture_atomique(CRIS_JSON, json.dumps({
            "ts": maintenant.isoformat(timespec="seconds"),
            "nb": len(cris),
            "nb_critique": len([c for c in cris if c["gravite"] == "CRITIQUE"]),
            "note": ("CRIS ACTIFS à l'instant du cycle : ce fichier s'auto-efface quand la cause "
                     "disparaît. Un cri sans voix tracée serait un faux cri."),
            "cris": cris,
        }, indent=2, ensure_ascii=False))
    except Exception:
        pass
    print("CRIS VIVANTS : %d actif(s)" % len(cris))
    for c in cris[:5]:
        print("   %s %s — %s (depuis %s, %d cri(s), voix %s)"
              % (c["gravite"], c["organe"], c["message"][:90], c["depuis"], c["nb_cris"], c["voix"]))


def main():
    if verifier_kill_switch():
        print("Chien de garde en pause : Kill-switch ou Maintenance active.")
        sys.exit(0)

    # Pouls du chien lui-même (il survit à sa propre surveillance) : écrit AVANT tout le reste,
    # ainsi même un crash en cours de cycle laisse un battement daté.
    try:
        POULS_DIR.mkdir(parents=True, exist_ok=True)
        ecriture_atomique(POULS_DIR / "chien-de-garde.json", json.dumps({
            "organe": "chien_de_garde",
            "dernier_battement": datetime.now(timezone.utc).isoformat(),
            "ok": True
        }, indent=2))
    except Exception:
        pass

    registre = charger_json_securise(REGISTRE_PATH)
    if not registre or "organes" not in registre:
        print("CRITIQUE: Registre des organes absent ou corrompu (Fail-fast).", file=sys.stderr)
        crier("chien_de_garde", "REGISTRE SOURD OU CORROMPU")
        sys.exit(1)

    organes = registre.get("organes", [])
    vivants = []
    vieillissants = []
    non_surveilles = []
    sans_produit = []      # chargé, aucun produit déclaré, mais sortie 0 → sur son code
    alertes_declarees = [] # sortie non nulle VOULUE (canal d'alerte déclaré)
    echecs_sortie = []     # sortie non nulle NON déclarée → vrai échec

    # Dernière sortie connue de chaque label launchd (lu une fois, pas 99 fois)
    code_sortie = {}
    try:
        out = subprocess.check_output(["launchctl", "list"], text=True,
                                      stderr=subprocess.DEVNULL)
        for ligne in out.splitlines():
            parts = ligne.split("\t")
            if len(parts) >= 3:
                code_sortie[parts[2].strip()] = (parts[0].strip(), parts[1].strip())
    except Exception:
        pass
    contrat = charger_json_securise(CONTRAT_SORTIE_PATH, {}) or {}
    if isinstance(contrat, dict):
        contrat = contrat.get("contrat", contrat)
    grisaille = []
    dormants = []   # organes VERSIONNÉS mais NON installés : veille assumée, pas une panne (19/09)
    maintenant_str = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

    for org in organes:
        nom = org.get("organe")
        if org.get("zone_grise", False):
            grisaille.append(org)
            continue
        # Organe « dormant » = présent dans le repo mais PAS chargé par launchd.
        # Alerter dessus serait un FAUX POSITIF (ex. croisements-indices, geopol — orphelins).
        if org.get("dormant", False):
            dormants.append({"organe": nom, "pourquoi": org.get("commentaire_dormant", "non installé")})
            continue

        freq = org.get("frequence_attendue_sec", 300)
        tolerance = org.get("tolerance_mult", 2.0)
        seuil = freq * tolerance
        age = evaluer_age_organe(org)

        # âge infini (produit/pouls introuvable ou illisible) -> None (JSON null)
        age_sec = None if age == float('inf') else round(age, 1)
        info = {
            "organe": nom,
            "age_sec": age_sec,
            "seuil_sec": seuil,
            "criticite": org.get("criticite", "MINEUR")
        }

        if age <= seuil:
            vivants.append(info)
        elif age == float('inf') and org.get("criticite") != "CRITIQUE":
            # 4e seau : organe MINEUR sans produit câblé. On ne le laisse plus
            # « non surveillé » (personne ne regarde jamais) : on lit sa SORTIE launchd.
            label = str(org.get("plist") or "").replace(".plist", "").strip()
            entree = code_sortie.get(label)
            if not entree:
                non_surveilles.append(info)
                continue
            pid, code = entree
            info["code_sortie"] = code
            declare = (contrat.get(label) or {}).get(str(code)) if isinstance(contrat, dict) else None
            if declare:
                info["sens"] = declare
                alertes_declarees.append(info)
            elif pid != "-":
                # Job EN VOL : le code affiché est celui de l'instance PRÉCÉDENTE
                # (ex. -9 = tué par un redémarrage launchd). Même règle que la page vol
                # (leçon 18/09) : un job qui tourne n'est pas un échec. Crier ici
                # produirait exactement le faux positif qu'on cherche à supprimer.
                info["sens"] = f"en vol (code de l'instance précédente : {code})"
                sans_produit.append(info)
            elif str(code) not in ("0", "-"):
                echecs_sortie.append(info)
                crier(nom, f"Sortie launchd non nulle et NON déclarée : exit {code} "
                           f"(organe arrêté, aucun produit câblé pour juger plus loin — "
                           f"déclarer le code dans contrat_sortie.json s'il est voulu)")
            else:
                sans_produit.append(info)
        else:
            vieillissants.append(info)
            if org.get("criticite") == "CRITIQUE":
                age_aff = "infini (produit/pouls introuvable ou illisible)" if age == float('inf') else f"{round(age)}s"
                crier(nom, f"Age réel {age_aff} dépasse le seuil {seuil}s")

    # ── 🙈 SENS ÉTEINTS : organes VIVANTS mais AVEUGLES ───────────────────────
    # On ne juge QUE ce qui est déclaré (sens_declares.json). Un organe frais dont
    # la décision ne sort plus est VIVANT au sens du plist et du fichier — et il est
    # inutile. C'est la classe de panne qui a laissé le short BTC muet 5 h le 20/09.
    aveugles = []
    etats_aveugles = charger_json_securise(ETAT_AVEUGLE, {})
    declarations = charger_json_securise(SENS_PATH, [])
    if isinstance(declarations, dict):
        declarations = declarations.get("sens", [])
    for decl in declarations or []:
        if not isinstance(decl, dict) or not decl.get("produit"):
            continue
        nom_sens = decl.get("organe") or decl.get("cle") or "?"
        mesure = mesurer_aveuglement(decl, etats_aveugles)
        if not mesure:
            continue
        fenetre = float(decl.get("fenetre_min", 45)) * 60
        if mesure["age_sec"] <= fenetre:
            continue
        age_min = mesure["age_sec"] / 60.0
        info = {
            "organe": nom_sens,
            "champ_decision": decl.get("champ_decision"),
            "aveugle_min": round(age_min, 1),
            "fenetre_min": decl.get("fenetre_min", 45),
            "mesure_exacte": mesure["exact"],
            "criticite": decl.get("criticite", "MINEUR"),
            "pourquoi": decl.get("pourquoi", "")
        }
        aveugles.append(info)
        borne = "" if mesure["exact"] else "au moins "
        crier(f"{nom_sens}-aveugle",
              f"VIVANT MAIS AVEUGLE — la décision ({decl.get('champ_decision')}) ne sort plus "
              f"depuis {borne}{age_min:.0f} min (fenêtre tolérée {info['fenetre_min']} min). "
              f"Le process tourne et le produit est frais, mais il ne peut plus décider : "
              f"{decl.get('pourquoi', '')}")
    try:
        ecriture_atomique(ETAT_AVEUGLE, json.dumps(etats_aveugles, indent=2))
    except Exception:
        pass

    # ── 📋 REVUE DES ORGANES : écarts STRUCTURELS non déclarés ────────────────
    # La revue (scripts/revue_organes.py, toutes les 3 h) compare ce que le registre
    # DÉCLARE avec ce que le disque PROUVE : cadence déclarée ≠ déclencheur réel,
    # produit déclaré que plus rien ne résout, contenu figé, produit absent. Un seul
    # cri pour toute la classe (pas 30 alarmes) : la revue n'est pas une panne,
    # c'est une déclaration à faire. Chaque ligne se ferme en la déclarant dans
    # strategie/revue_declares.json (raison + date) — le cri s'auto-efface alors.
    revue = charger_json_securise(REVUE_JSON, {}) or {}
    a_trancher = revue.get("a_trancher") or []
    if a_trancher:
        noms = ", ".join(str(x.get("organe")) for x in a_trancher[:3])
        crier("revue-organes",
              f"REVUE : {len(a_trancher)} organe(s) à trancher ({noms}{'…' if len(a_trancher) > 3 else ''}) — "
              f"voir thermo/REVUE_ORGANES.md. Champ "
              f"« cadence déclarée ≠ déclencheur réel », « produit déclaré non résolu » "
              f"ou « contenu figé ». Se ferme en DÉCLARANT la ligne (raison + date) "
              f"dans strategie/revue_declares.json.",
              gravite="MAJEUR")

    # Écriture du rapport JSON et Markdown du Chien
    rapport_data = {
        "generated_at": maintenant_str,
        "vivants": vivants,
        "vieillissants": vieillissants,
        "aveugles": aveugles,
        "non_surveilles": [i.get("organe") for i in non_surveilles],
        "sans_produit": [i.get("organe") for i in sans_produit],
        "alertes_declarees": [i.get("organe") for i in alertes_declarees],
        "echecs_sortie": echecs_sortie,
        "grisaille": [o.get("organe") for o in grisaille],
        "dormants": [d.get("organe") for d in dormants],
        "cris": len(CRIS_ACTIFS),
        "cris_critiques": len([c for c in CRIS_ACTIFS.values() if c.get("gravite") == "CRITIQUE"]),
        "statut": "alerte" if (vieillissants or aveugles or echecs_sortie) else "sain"
    }
    ecriture_atomique(RAPPORT_JSON, json.dumps(rapport_data, indent=2))
    ecrire_cris_vivants()

    # Génération du rapport Markdown
    md_content = f"""# 🐕 RAPPORT DU CHIEN DE GARDE
*Généré le : {maintenant_str}*

## 🟢 Vivant / À l'heure ({len(vivants)})
"""
    for v in vivants:
        md_content += f"- **{v['organe']}** : âge {v['age_sec']}s (seuil {v['seuil_sec']}s)\n"

    md_content += f"\n## 🟠 Vieillissants / Hors délai ({len(vieillissants)})\n"
    for v in vieillissants:
        age_aff = "infini (produit introuvable)" if v["age_sec"] is None else f"{v['age_sec']}s"
        md_content += f"- **{v['organe']}** : âge {age_aff} (seuil {v['seuil_sec']}s) [Criticité: {v['criticite']}]\n"

    md_content += f"\n## 🙈 Vivants mais AVEUGLES (process OK, produit frais, décision muette) ({len(aveugles)})\n"
    for a in aveugles:
        borne = "" if a["mesure_exacte"] else "≥ "
        md_content += (f"- **{a['organe']}** [{a['criticite']}] : `{a['champ_decision']}` nul depuis "
                       f"{borne}{a['aveugle_min']:.0f} min (fenêtre {a['fenetre_min']} min) — {a['pourquoi']}\n")
    if not aveugles:
        md_content += "- (aucun : tous les sens déclarés produisent une décision)\n"

    md_content += f"\n## 🌫️ Grisaille (Non chargés / Audit) ({len(grisaille)})\n"
    for g in grisaille:
        md_content += f"- **{g.get('organe')}** (plist: {g.get('plist', 'inconnu')})\n"

    md_content += f"\n## 😴 Dormants assumés (versionnés mais NON installés — pas une panne) ({len(dormants)})\n"
    for d in dormants:
        md_content += f"- **{d['organe']}** : {d['pourquoi']}\n"

    md_content += f"\n## ⚪ Sans produit déclaré — jugés sur leur sortie launchd, exit 0 ({len(sans_produit)})\n"
    for v in sans_produit:
        md_content += f"- {v['organe']} (exit 0)\n"

    md_content += f"\n## 🟡 Alertes déclarées (sortie non nulle VOULUE — canal d'alerte) ({len(alertes_declarees)})\n"
    for v in alertes_declarees:
        md_content += f"- **{v['organe']}** : exit {v.get('code_sortie')} — {v.get('sens')}\n"

    md_content += f"\n## 🔴 Échecs de sortie (non nuls NON déclarés) ({len(echecs_sortie)})\n"
    for v in echecs_sortie:
        md_content += f"- **{v['organe']}** : exit {v.get('code_sortie')} (aucun produit câblé)\n"
    if not echecs_sortie:
        md_content += "- (aucun)\n"

    md_content += f"\n## ⚪ Non surveillés (label launchd absent — à compléter) ({len(non_surveilles)})\n"
    for v in non_surveilles:
        md_content += f"- {v['organe']}\n"

    md_content += f"\n## 🛡️ Santé du Chien\n- Statut : ACTIF\n- Registre : OK\n"
    ecriture_atomique(RAPPORT_MD, md_content)

if __name__ == "__main__":
    main()
