#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
troupeau_inv.py — TROUPEAU-INV : le monde ombre retourné en instrument (GO Christophe 13/09/2026).

SPEC FIGÉE AVANT LE PREMIER RUN (TROUPEAU_INV_SPEC_20260913.md) :
  R1  paire A (témoin, question neutre) + B (bousculée : "imaginez le contraire du consensus")
  R2  A doit parapher (INI <= 0.3) sinon paire annulée (miroir instable)
  R3  signal = divergence direction A vs B ; même direction = cas non compté
  R4  juge mécanique : direction réelle BTC à T+72h (thermo/history.jsonl, clé mark)
  R5  1 paire / 48h · 8 semaines · ~24 paires
  R6  verdict 08/11/2026 : >= 55% HIT sur >= 20 cas, sinon dossier fermé définitivement
  R7  0 CHF — hub local uniquement (modèle free)
  R8  paire 0 = calibration sur la graine du 08/08 (A doit reproduire la paraphrase baissière/plate)
  R9  lecture seule sur la maison · aucun ordre · produit = l'historique JSONL
  R10 script scellé au registre synapses avant le premier run

Usage :
  python3 troupeau_inv.py --calibration   # paire 0 : graine du 08/08 (figée)
  python3 troupeau_inv.py --cycle         # paire standard : graines live du moment
  python3 troupeau_inv.py --juger         # juge les paires arrivées à T+72h
  python3 troupeau_inv.py --status        # tableau de bord
"""
import json
import hashlib
import subprocess
import time
import urllib.request
from pathlib import Path
from datetime import datetime, timedelta, timezone

INDEX = Path.home() / "ace777-test-day1/Index_Maison"
HIST = INDEX / "troupeau_inv_hist.jsonl"
THERMO = INDEX / "thermo/history.jsonl"
HUB = "http://127.0.0.1:11435/v1/chat/completions"
MODEL = "deepseek-ai/DeepSeek-V3-0324"  # R7 : free sur hub, plus discipliné (6.7b paraphait mal : INI 0.83)
# F2 (GO C. 16/09) : état des appels hub — visible, hors circuit sirène ([C4] : alarme.json interdit aux organes)
ETAT_HUB = INDEX / "thermo/troupeau_inv_hub_etat.json"

# Graine de calibration (R8) — les vraies données du 08/08 (sim_e39c6ebbe6e2)
GRAINE_0808 = (
    "BTC tourne autour de 64 978 $. Indice peur & cupidité : 30/100 (peur). "
    "Ratio long/short des top traders : 1,208. Flux ETF du jour : +57,4 M$. "
    "Résistance : 70 000 $. Support : 60 000 $. Funding : repassé positif."
)

MAX_TOKENS = 350
INI_SEUIL = 0.30          # R2
JOURNEES = 48             # R5 (heures entre paires)
VERDICT_DATE = "2026-11-08"
SEUIL_HIT, MIN_CAS = 0.55, 20   # R6


def maintenant_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def demander_hub(systeme, user):
    payload = {"model": MODEL, "messages": [
        {"role": "system", "content": systeme},
        {"role": "user", "content": user}],
        "temperature": 0.6, "max_tokens": MAX_TOKENS}
    # F2 (GO C. 16/09) : backoff ×3 (0,10,30) — pattern cortana_propose_params prouvé en vol.
    # Un 502 passager du hub ne tue plus le cycle (le 16/09, cycle 04:00Z mort sur un 502 unique).
    last = None
    for i, delai in enumerate((0, 10, 30)):
        if delai:
            time.sleep(delai)
        try:
            req = urllib.request.Request(HUB, data=json.dumps(payload).encode(),
                                         headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=180) as resp:
                d = json.loads(resp.read())
            _noter_hub(True, f"tentative {i+1} OK")
            return d["choices"][0]["message"]["content"].strip()
        except Exception as e:
            last = e
    _noter_hub(False, f"3 tentatives échouées : {last}")
    raise last


def _noter_hub(ok, detail=""):
    """F2 : chaque appel hub noté dans un état dédié (thermo/) — visible par la famille
    sans toucher au circuit des sirènes ([C4]). 3 échecs consécutifs (échecs_consecutifs>=3)
    = organe en panne lisible par le chien/la veilleuse, pas de cri vocal."""
    try:
        precedent = {}
        if ETAT_HUB.exists():
            try:
                precedent = json.loads(ETAT_HUB.read_text())
            except Exception:
                precedent = {}
        consec = 0 if ok else int(precedent.get("echecs_consecutifs", 0)) + 1
        etat = {"ts": maintenant_iso(), "ok": ok, "detail": str(detail)[:200],
                "echecs_consecutifs": consec}
        ETAT_HUB.parent.mkdir(parents=True, exist_ok=True)
        ETAT_HUB.write_text(json.dumps(etat, ensure_ascii=False, indent=2))
    except Exception:
        pass


def extraire_nombres(txt):
    import re
    # le suffixe k/m/b fait PARTIE du token (60k = 60000, pas 60)
    return set(re.findall(r"\d+(?:[\s.,]\d+)*[kmbKMB]?", txt))


def _num_val(tok):
    """Normalise un token numérique : '60 000'->60000.0, '60k'->60000.0, '57,4'->574.0 (cohérent des 2 côtés)."""
    t = tok.strip().lower().replace("\u202f", "").replace("\u00a0", "").replace(" ", "").replace(",", "").rstrip(".")
    mult = 1.0
    if t and t[-1] in "kmb":
        mult = {"k": 1e3, "m": 1e6, "b": 1e9}[t[-1]]
        t = t[:-1]
    if not t or not any(c.isdigit() for c in t):
        return None
    try:
        return round(float(t) * mult, 1)
    except ValueError:
        return None


def _sigfig(x, n):
    """Arrondi à n chiffres significatifs : 76792 -> (2) 77000, (1) 80000."""
    if x == 0:
        return 0.0
    from math import floor, log10
    d = floor(log10(abs(x))) - n + 1
    return round(x / 10**d) * 10**d


def _meme_nombre(a, b):
    """LE MÊME nombre : égal, troncature de chiffres (60 vs 60 000), ou approximation à ±2,5 %.
    Narrer le chiffre de la graine autrement ≠ introduire une info nouvelle."""
    if a == b:
        return True
    if not a or not b or a <= 0 or b <= 0:
        return False
    lo, hi = (a, b) if a < b else (b, a)
    r = hi / lo
    if r in (10.0, 100.0, 1000.0, 10000.0):
        return str(int(lo)) == str(int(hi))[:len(str(int(lo)))]
    return (hi - lo) / hi <= 0.05


def ini(reponse, graine):
    """INI : part des nombres de la réponse absents de la graine.
    Note d'instrument (calibration 13/09) : les NIVEAUX RONDS (multiples de 1000)
    proches à ±10 % d'un nombre de la graine sont du verbiage technique des LLM
    ("70k", "75k"...) — ils sortent du comptage, des deux côtés. Un niveau rond LOIN
    de tout, ou un chiffre précis nouveau, reste de la vraie nouveauté."""
    rep_all = {v for v in (_num_val(n) for n in extraire_nombres(reponse)) if v is not None and v >= 13}
    gr_all = {v for v in (_num_val(n) for n in extraire_nombres(graine)) if v is not None and v >= 13}

    def _ancre_pres(v, vals):
        return v % 1000 == 0 and any(abs(v - g) / max(v, g) <= 0.10 for g in vals)

    nb_rep = {v for v in rep_all if not _ancre_pres(v, gr_all)}
    nb_gr = {v for v in gr_all if not _ancre_pres(v, gr_all - {v})}
    if not nb_rep:
        return 0.0
    nouveaux = {n for n in nb_rep if not any(_meme_nombre(n, g) for g in nb_gr)}
    return round(len(nouveaux) / len(nb_rep), 3)


HAUSSIER = ["hausse", "rebond", "rally", "haussier", "acheter", "achat", "cassure par le haut", "montée", "up", "bull", "optimiste", "confinance", "appétit"]
BAISSIER = ["baisse", "crash", "chute", "baissier", "vendre", "vente", "liquidation", "down", "bear", "peur", "panique", "cassure par le bas", "descendre", "dégringolade"]


def direction(txt):
    b = txt.lower()
    h = sum(b.count(m) for m in HAUSSIER)
    bb = sum(b.count(m) for m in BAISSIER)
    if h > bb:
        return "up"
    if bb > h:
        return "down"
    return "plat"


def lire_thermo():
    """Dernière ligne utile du thermo (mark)."""
    last = None
    for line in THERMO.open():
        try:
            d = json.loads(line)
            if isinstance(d.get("mark"), (int, float)) and d["mark"] > 1000:
                last = d
        except Exception:
            pass
    return last


def prix_a(ts_iso):
    """Premier point thermo à >= ts_iso (pour le jugement T+72h)."""
    for line in THERMO.open():
        try:
            d = json.loads(line)
            if str(d.get("ts", "")) >= ts_iso and isinstance(d.get("mark"), (int, float)) and d["mark"] > 1000:
                return d["mark"]
        except Exception:
            pass
    return None


def charger_hist():
    rows = []
    if HIST.exists():
        for line in HIST.open():
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows


def ecrire_hist(row):
    HIST.parent.mkdir(exist_ok=True)
    with HIST.open("a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def graine_du_moment():
    t = lire_thermo()
    if not t:
        raise RuntimeError("thermo indisponible")
    return (f"BTC tourne autour de {t['mark']:,.0f} $. Indice peur & cupidité : {t.get('fearGreed')}/100. "
            f"Ratio long/short : {t.get('longShort')}. Flux ETF récent : {t.get('etfBtcM')} M$. "
            f"Funding : {t.get('funding')}. Score maison : {t.get('score')}/100.")


def faire_paire(graine, paire_id, calibration=False):
    """R1-R3 : deux sims, témoin + bousculée."""
    sysA = ("Tu es un collectif de 5 traders (retail, fonds, mineur, hedge, analyste) qui discute sur un forum. "
            "Vous donnez votre lecture courte et franche du marché décrit. 5 phrases max.")
    sysB = ("Tu es un collectif de 5 traders (retail, fonds, mineur, hedge, analyste) qui discute sur un forum. "
            "CONSIGNE PARTICULIÈRE : le marché décrit a un consensus évident. Imaginez que le marché fasse "
            "EXACTEMENT LE CONTRAIRE de ce consensus dans les 3 jours. Quelle serait votre lecture alors ? 5 phrases max.")
    repA = demander_hub(sysA, "Marché : " + graine + "\nVotre lecture ?")
    repB = demander_hub(sysB, "Marché : " + graine + "\nVotre lecture, si le contraire du consensus se produit ?")
    iniA, iniB = ini(repA, graine), ini(repB, graine)
    dirA, dirB = direction(repA), direction(repB)
    diverge = (dirA != dirB and dirA != "plat" and dirB != "plat")
    row = {
        "paire": paire_id, "ts": maintenant_iso(), "calibration": calibration,
        "graine": graine,
        "graine_md5": hashlib.md5(graine.encode()).hexdigest()[:10],
        "ts_graine": maintenant_iso(), "prix_graine": lire_thermo()["mark"] if lire_thermo() else None,
        "iniA": iniA, "iniB": iniB, "dirA": dirA, "dirB": dirB,
        "diverge": diverge, "verdict": None, "jugé_ts": None,
        "repA": repA, "repB": repB,
    }
    if iniA > INI_SEUIL:
        row["verdict"] = "ANNULEE_MIROIR_INSTABLE"
        row["jugé_ts"] = maintenant_iso()
    ecrire_hist(row)
    return row


def juger():
    """R4 : juge les paires divergentes dont T+72h est atteint."""
    rows = charger_hist()
    n_juges = 0
    for r in rows:
        if r.get("verdict") is not None or not r.get("diverge"):
            continue
        t_graine = datetime.strptime(r["ts_graine"], "%Y-%m-%dT%H:%MZ").replace(tzinfo=timezone.utc)
        cible = (t_graine + timedelta(hours=72)).strftime("%Y-%m-%dT%H:%MZ")
        px = prix_a(cible)
        if px is None:
            continue
        p0 = r.get("prix_graine")
        if not p0:
            continue
        reel = "up" if px > p0 * 1.002 else ("down" if px < p0 * 0.998 else "plat")
        attendu = "up" if r["dirA"] == "down" else ("down" if r["dirA"] == "up" else None)
        # le signal : B s'oppose à A ; le marché vérifie-t-il B ?
        if attendu is None:
            r["verdict"] = "NON_COMPTABLE"
        else:
            r["verdict"] = "HIT" if reel == attendu else "MISS"
        r["prix_t72h"] = px
        r["reel"] = reel
        r["jugé_ts"] = maintenant_iso()
        n_juges += 1
    if n_juges:
        with HIST.open("w") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return n_juges


def status():
    rows = charger_hist()
    comptables = [r for r in rows if r.get("verdict") in ("HIT", "MISS")]
    hits = sum(1 for r in comptables if r["verdict"] == "HIT")
    n = len(comptables)
    print("=== TROUPEAU-INV — statut ===")
    print(f"paires enregistrées : {len(rows)}")
    print(f"diverges (cas)      : {len([r for r in rows if r.get('diverge')])}")
    print(f"cas jugés           : {n}  · HIT {hits}  · réussite {hits/n*100:.1f}%" if n else "cas jugés : 0")
    print(f"verdict pré-enregistré : {VERDICT_DATE} — >= {SEUIL_HIT*0:.0f}".replace(">= 0", f">= {int(SEUIL_HIT*100)} % sur >= {MIN_CAS} cas"))
    if n >= MIN_CAS:
        ok = hits / n >= SEUIL_HIT
        print("VERDICT : " + ("PASSER — le monde ombre inversé est informatif" if ok else "ÉCHOUER — dossier fermé définitivement (R6)"))
    else:
        print(f"manquent {MIN_CAS - n} cas avant le verdict")
    cal = [r for r in rows if r.get("calibration")]
    if cal:
        c = cal[-1]
        print(f"calibration : INI A = {c['iniA']} (seuil {INI_SEUIL}) · dirA {c['dirA']} · {c['verdict'] or 'en attente'}")


def main():
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "--status"
    if mode == "--status":
        status()
    elif mode == "--juger":
        print(f"paires jugées : {juger()}")
    elif mode == "--calibration":
        print("=== PAIRE 0 — calibration sur la graine du 08/08 (R8) ===")
        r = faire_paire(GRAINE_0808, "cal-0808", calibration=True)
        print(f"INI A = {r['iniA']} (seuil {INI_SEUIL}) · dirA = {r['dirA']} · dirB = {r['dirB']} · diverge = {r['diverge']}")
        print(f"A: {r['repA'][:220]}")
        print(f"B: {r['repB'][:220]}")
        print("statut :", r["verdict"] or "enregistrée (jugement T+72h différé)")
    elif mode == "--cycle":
        rows = charger_hist()
        pid = f"paire-{len(rows):03d}"
        print(f"=== {pid} — graines live (R5) ===")
        g = graine_du_moment()
        r = faire_paire(g, pid)
        print(f"INI A = {r['iniA']} · dirA = {r['dirA']} · dirB = {r['dirB']} · diverge = {r['diverge']}")
        print("statut :", r["verdict"] or "enregistrée (T+72h)")
        # RÉPARÉ 20/09/2026 (Buffy, GO « incassable ») : le plist ne lance QUE --cycle →
        # `--juger` n'était JAMAIS exécuté par la machine. Conséquence mesurée : la seule
        # paire divergente (paire-008, graine du 14/09 04:00Z) attendait son verdict T+72h
        # depuis le 17/09, 3 jours plus tard, sans que rien ne le signale. Un protocole
        # dont le verdict ne peut pas être rendu est mort par construction. Le cycle juge
        # donc ce qui est dû (idempotent : ne rejuge jamais une paire déjà jugée).
        n = juger()
        if n:
            print(f"jugement T+72h : {n} paire(s) arrivée(s) à échéance jugée(s)")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
