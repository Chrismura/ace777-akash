#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""veilleuse_chantiers.py — VEILLEUSE DES CHANTIERS SNIFFER/COULEUR (19/08).

Pour ne rien oublier (demande Christophe) : la couleur régime est EN TEST
(observation), les chantiers S-01..S-05 sont ouverts. Cette veilleuse vérifie
chaque jour (launchd) :
  1. Le TEST tourne : dernier enregistrement de regime_couleur.jsonl < 72h,
     sinon rappel « les plists couleur sont morts ».
  2. Le TEST accumule : si une couleur atteint ≥ 5 échantillons notés -> rappel
     « S-05 prêt à valider ».
  3. Les chantiers ne sont pas oubliés : rappel max 1×/semaine pour relire
     CHANTIERS_A_FAIRE.md § sniffer/couleur.
Écrit un rappel dans OUTBOX_OBSIDIAN/A_Mon_Attention/ si besoin.
Lecture seule. Stdlib uniquement.
"""
import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent
IM = RACINE / "Index_Maison"
REGIME_HIST = IM / "thermo" / "regime_couleur.jsonl"
JUSTESSE = IM / "scripts" / "regime_justesse.json"
CHANTIERS = IM / "CHANTIERS_A_FAIRE.md"
ATTENTION_DIR = IM / "OUTBOX_OBSIDIAN" / "A_Mon_Attention"
RAPPEL_PATH = ATTENTION_DIR / "RAPPEL_CHANTIERS_SNIFFER.md"

MAX_AGE_TEST_H = 72          # le test doit tourner (dernier enregistrement < 72h)
MIN_SAMPLES_VALIDATION = 5   # seuil de validation S-05 par couleur (échantillons)
SEUIL_TX_VALIDATION = 60.0   # (fix 23/08) : une couleur n'est « prête à valider »
                             # que si son taux de réussite est >= 60 % (sinon on injecterait
                             # un signal pire que pile-ou-face dans la chaîne)
RAPPEL_SEMAINE_J = 7         # rappel « relire les chantiers » max 1×/semaine


def maintenant():
    return datetime.now(timezone.utc)


def dernier_ts_jsonl():
    """Timestamp (unix) du dernier enregistrement couleur."""
    if not REGIME_HIST.exists():
        return None
    try:
        last = None
        with open(REGIME_HIST, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                    ts = r.get("ts_unix")
                    if ts:
                        last = ts
                except Exception:
                    continue
        return last
    except Exception:
        return None


def echantillons_par_couleur():
    """Échantillons notés par couleur (depuis regime_justesse.json)."""
    if not JUSTESSE.exists():
        return {}
    try:
        j = json.loads(JUSTESSE.read_text(encoding="utf-8"))
        out = {}
        for c, s in j.get("par_couleur", {}).items():
            out[c] = {"n": s.get("n", 0), "taux": s.get("taux_pct")}
        return out
    except Exception:
        return {}


def date_du_rappel():
    """Date du dernier rappel écrit (si fichier existe)."""
    if not RAPPEL_PATH.exists():
        return None
    try:
        txt = RAPPEL_PATH.read_text(encoding="utf-8")
        for line in txt.splitlines():
            if line.startswith("> jour : "):
                return line.replace("> jour : ", "").strip()
    except Exception:
        pass
    return None


def ecrire_rappel(lignes):
    """Écrit le rappel du jour (remplace l'ancien, garde l'historique de date)."""
    ATTENTION_DIR.mkdir(parents=True, exist_ok=True)
    jour = maintenant().strftime("%Y-%m-%d")
    contenu = ("# ⏰ RAPPEL — CHANTIERS SNIFFER / COULEUR\n\n"
               "> jour : %s\n\n" % jour + "\n".join(lignes) + "\n\n"
               "_Écrit par veilleuse_chantiers.py — ne rien oublier._\n")
    RAPPEL_PATH.write_text(contenu, encoding="utf-8")
    return jour


def main():
    rappels = []
    now = maintenant()

    # 1) Le TEST tourne ?
    last = dernier_ts_jsonl()
    if last is None:
        rappels.append("- 🟥 La couleur régime n'a **jamais** été enregistrée : les plists "
                       "`couleur-regime` (8h05/15h55) sont-elles chargées ?")
    else:
        age_h = (now - datetime.fromtimestamp(last, timezone.utc)).total_seconds() / 3600.0
        if age_h > MAX_AGE_TEST_H:
            rappels.append("- 🟥 Le test couleur régime **ne tourne plus** (%dh de silence) : "
                           "vérifier `launchctl list | grep couleur-regime`." % int(age_h))

    # 2) Le TEST accumule ? (fix 23/08 : la validation exige un TAUX >= 60 %,
    #    pas seulement des échantillons — sinon on validerait ORANGE à 27,6 %)
    for c, s in echantillons_par_couleur().items():
        taux = s.get("taux")
        if s["n"] >= MIN_SAMPLES_VALIDATION and taux is not None and taux >= SEUIL_TX_VALIDATION:
            rappels.append("- 🟢 Couleur **%s** : %d échantillons notés (%s%%) → **S-05 prêt à "
                           "valider** (famille → juge → GO)."
                           % (c, s["n"], taux))
        elif s["n"] >= MIN_SAMPLES_VALIDATION and taux is not None and taux < SEUIL_TX_VALIDATION:
            rappels.append("- 🔴 Couleur **%s** : %d échantillons notés mais taux **%s%% < %s%%** → "
                           "PAS fiable, à ramollir / ré-évaluer — ne PAS injecter en l'état."
                           % (c, s["n"], taux, SEUIL_TX_VALIDATION))
        elif s["n"] > 0:
            rappels.append("- 🟡 Couleur **%s** : %d échantillons notés (min %d) — le test avance."
                           % (c, s["n"], MIN_SAMPLES_VALIDATION))

    # 3) Chantiers pas oubliés (max 1×/semaine)
    derniere = date_du_rappel()
    if not derniere or (now - datetime.strptime(derniere, "%Y-%m-%d").replace(tzinfo=timezone.utc)).days >= RAPPEL_SEMAINE_J:
        rappels.append("- 📋 Relire `CHANTIERS_A_FAIRE.md` § Sniffer/Couleur (S-01 enquête blocs "
                       "fantômes · S-02 scores lisibles · S-03 bulles d'info · S-04 pédagogie).")

    if not rappels:
        print("[veilleuse-chantiers] Rien à signaler — test couleur OK, chantiers suivis.")
        return 0

    jour = ecrire_rappel(rappels)
    print("[veilleuse-chantiers] Rappel écrit (%s) :" % jour)
    for r in rappels:
        print("  " + r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
