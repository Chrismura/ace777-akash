#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
derive_memoire.py — Chantier 2 : Dérive mémoire (4 indicateurs @0xWast3)
Surveille la santé de la mémoire d'ACE777 (analyses Cortana & justesse).
Lecture seule. Stdlib uniquement. Fail-safe.
Sortie : Index_Maison/thermo/DERIVE_MEMOIRE.md + strategie/derive_memoire.json
Exit : 0 sain · 1 instable(s) · 2 critique(s)
"""

import os
import sys
import json
import glob
from datetime import datetime, timezone

# Chemins relatifs par rapport à la racine du projet (ace777-test-day1)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ANALYSES_DIR = os.path.join(BASE_DIR, "Index_Maison", "thermo", "analyses")
JUSTESSE_PATH = os.path.join(BASE_DIR, "Index_Maison", "scripts", "justesse_v2.json")
RAPPORT_MD_PATH = os.path.join(BASE_DIR, "Index_Maison", "thermo", "DERIVE_MEMOIRE.md")
RAPPORT_JSON_PATH = os.path.join(BASE_DIR, "Index_Maison", "strategie", "derive_memoire.json")


def charger_analyses():
    """Charge toutes les lignes des fichiers .jsonl dans analyses/"""
    analyses_par_indice = {}
    if not os.path.exists(ANALYSES_DIR):
        return analyses_par_indice

    pattern = os.path.join(ANALYSES_DIR, "*.jsonl")
    for filepath in glob.glob(pattern):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        obj = json.loads(line)
                        indice = obj.get("indice")
                        if not indice:
                            continue
                        if indice not in analyses_par_indice:
                            analyses_par_indice[indice] = []
                        analyses_par_indice[indice].append(obj)
                    except json.JSONDecodeError:
                        continue
        except Exception:
            continue

    # Tri de chaque liste d'analyses par timestamp (ts)
    for indice in analyses_par_indice:
        analyses_par_indice[indice].sort(key=lambda x: x.get("ts", ""))

    return analyses_par_indice


def charger_justesse():
    """Charge justesse_v2.json"""
    if not os.path.exists(JUSTESSE_PATH):
        return {}
    try:
        with open(JUSTESSE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def extraire_avis(texte_analyse):
    """Extrait l'avis strict (LONG, SHORT, NEUTRE) et la confiance (faible, moyenne, haute) d'un texte d'analyse"""
    avis = "NEUTRE"
    confiance = "moyenne"

    if not isinstance(texte_analyse, str):
        return avis, confiance

    lignes = texte_analyse.split("\n")
    for ligne in lignes:
        ligne_upper = ligne.upper()
        if "AVIS STRICT" in ligne_upper:
            if "LONG" in ligne_upper:
                avis = "LONG"
            elif "SHORT" in ligne_upper:
                avis = "SHORT"
            elif "NEUTRE" in ligne_upper:
                avis = "NEUTRE"
        if "CONFIANCE" in ligne_upper:
            if "FAIBLE" in ligne_upper:
                confiance = "faible"
            elif "HAUTE" in ligne_upper:
                confiance = "haute"
            elif "MOYENNE" in ligne_upper:
                confiance = "moyenne"

    return avis, confiance


def extraire_hit(texte_analyse):
    """Détecte si l'analyse mentionne un statut HIT/MISS (le scoreur l'écrit parfois dans le texte)."""
    if not isinstance(texte_analyse, str):
        return None
    up = texte_analyse.upper()
    if "HIT" in up:
        return True
    if "MISS" in up:
        return False
    return None


def main():
    main_ts = datetime.now(timezone.utc).isoformat()
    analyses_dict = charger_analyses()
    justesse_data = charger_justesse()
    par_indice_justesse = justesse_data.get("par_indice", {})

    now_dt = datetime.now(timezone.utc)
    resultats_indices = {}

    global_instables = 0
    global_critiques = 0
    max_exit_code = 0

    indices_tous = sorted(list(set(list(analyses_dict.keys()) + list(par_indice_justesse.keys()))))

    if not indices_tous:
        # Aucun indice trouvé, on écrit un rapport vide et exit 0
        ecrire_rapport({}, 0, 0, main_ts)
        ecrire_json({}, 0, 0, main_ts)
        sys.exit(0)

    for indice in indices_tous:
        list_analyses = analyses_dict.get(indice, [])
        n_analyses = len(list_analyses)

        # ----------------------------------------------------
        # I1. Fréquence de référence
        # ----------------------------------------------------
        analyses_14j = 0
        jours_analyses = set()
        for an in list_analyses:
            ts_str = an.get("ts", "")
            try:
                dt = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                delta_jours = (now_dt - dt).days
                if 0 <= delta_jours <= 14:
                    analyses_14j += 1
                    jours_analyses.add(dt.date())
            except Exception:
                pass

        i1_statut = "STABLE"
        if n_analyses == 0:
            i1_statut = "FROID"
        else:
            dernier_ts = list_analyses[-1].get("ts", "")
            age_jours = 999
            try:
                dt_der = datetime.fromisoformat(dernier_ts.replace("Z", "+00:00"))
                age_jours = (now_dt - dt_der).days
            except Exception:
                pass

            if age_jours >= 7:
                i1_statut = "FROID"
            elif n_analyses <= 2 and analyses_14j <= 2:
                i1_statut = "SOUS-UTILISE"

        # ----------------------------------------------------
        # I2. Taux de contradiction (Flip-flop)
        # ----------------------------------------------------
        contradictions = 0
        paires_valides = 0
        avis_precedent = None

        for an in list_analyses:
            texte = an.get("analyse", "")
            avis_actuel, _ = extraire_avis(texte)
            if avis_precedent is not None:
                paires_valides += 1
                # Contradiction = LONG <-> SHORT (retournement strict)
                if (avis_precedent == "LONG" and avis_actuel == "SHORT") or \
                   (avis_precedent == "SHORT" and avis_actuel == "LONG"):
                    contradictions += 1
            avis_precedent = avis_actuel

        taux_contradiction = (contradictions / paires_valides) if paires_valides > 0 else 0.0
        i2_statut = "STABLE"
        if taux_contradiction > 0.5 and paires_valides >= 2:
            i2_statut = "INSTABLE"

        # ----------------------------------------------------
        # I3. Vitesse de décroissance (Âge)
        # ----------------------------------------------------
        age_derniere_analyse = 999
        if list_analyses:
            dernier_ts = list_analyses[-1].get("ts", "")
            try:
                dt_der = datetime.fromisoformat(dernier_ts.replace("Z", "+00:00"))
                age_derniere_analyse = (now_dt - dt_der).days
            except Exception:
                pass

        i3_statut = "STABLE"
        if age_derniere_analyse > 14:
            i3_statut = "CRITIQUE"
        elif age_derniere_analyse > 7:
            i3_statut = "PÉRIMÉ"

        # ----------------------------------------------------
        # I4. Dispersion de confiance (Calibration)
        # ----------------------------------------------------
        # Comparaison justesse sur haute vs faible confiance
        # Donnée 1 : statut HIT/MISS par indice depuis justesse_v2 (par_indice)
        justesse_info = par_indice_justesse.get(indice, {})
        pct_indice = justesse_info.get("pct")
        if pct_indice is None:
            # pas de pct par indice dans la v2 — on utilise hit/n si présents
            hit_n = justesse_info.get("hit")
            n_n = justesse_info.get("n")
            if isinstance(hit_n, (int, float)) and isinstance(n_n, (int, float)) and n_n:
                pct_indice = hit_n / n_n * 100.0
        # Donnée 2 : extraction des HIT/MISS dans les textes d'analyse (si le scoreur l'a écrit)
        hits_texte = misses_texte = 0
        for an in list_analyses:
            h = extraire_hit(an.get("analyse", ""))
            if h is True:
                hits_texte += 1
            elif h is False:
                misses_texte += 1

        # Calibration : écart entre justesse de l'indice et 50% (pile-ou-face), borné [-1, 1]
        if pct_indice is not None:
            # calibration = (pct - 50) / 50 → positif = meilleur que pile-ou-face
            score_calibration = (pct_indice - 50.0) / 50.0
        elif hits_texte + misses_texte > 0:
            pct_texte = hits_texte / (hits_texte + misses_texte) * 100.0
            score_calibration = (pct_texte - 50.0) / 50.0
        else:
            score_calibration = 0.0  # inconnu → neutre

        i4_statut = "STABLE"
        # Confiance déconnectée : justesse de l'indice <= 40% (nettement sous pile-ou-face)
        if pct_indice is not None and pct_indice <= 40:
            i4_statut = "CRITIQUE"
        elif pct_indice is not None and pct_indice < 50:
            i4_statut = "INSTABLE"

        # ----------------------------------------------------
        # Synthèse du statut de l'indice (le pire des 4)
        # ----------------------------------------------------
        pire_statut = "STABLE"
        for s in [i1_statut, i2_statut, i3_statut, i4_statut]:
            if s == "CRITIQUE":
                pire_statut = "CRITIQUE"
            elif s == "INSTABLE" and pire_statut != "CRITIQUE":
                pire_statut = "INSTABLE"
            elif s == "PÉRIMÉ" and pire_statut not in ["CRITIQUE", "INSTABLE"]:
                pire_statut = "PÉRIMÉ"
            elif s in ["FROID", "SOUS-UTILISE"] and pire_statut not in ["CRITIQUE", "INSTABLE", "PÉRIMÉ"]:
                pire_statut = s

        if pire_statut in ["INSTABLE", "PÉRIMÉ"]:
            global_instables += 1
            if max_exit_code < 1:
                max_exit_code = 1
        elif pire_statut == "CRITIQUE":
            global_critiques += 1
            max_exit_code = 2

        resultats_indices[indice] = {
            "n_analyses": n_analyses,
            "i1_frequence": i1_statut,
            "i2_contradiction": f"{taux_contradiction*100:.1f}% ({i2_statut})",
            "i3_age_jours": age_derniere_analyse,
            "i3_statut": i3_statut,
            "i4_calibration": f"{score_calibration*100:+.1f} ({i4_statut})",
            "statut": pire_statut
        }

    ecrire_rapport(resultats_indices, global_instables, global_critiques, main_ts)
    ecrire_json(resultats_indices, global_instables, global_critiques, main_ts)

    sys.exit(max_exit_code)


def ecrire_rapport(resultats, n_instables, n_critiques, ts):
    """Écrit le rapport Markdown DERIVE_MEMOIRE.md"""
    os.makedirs(os.path.dirname(RAPPORT_MD_PATH), exist_ok=True)

    saine = "OUI" if (n_instables == 0 and n_critiques == 0) else "NON (Attention requise)"

    lignes_md = [
        f"# Rapport — Dérive Mémoire (Santé ACE777)",
        f"",
        f"- **Date** : `{ts}`",
        f"- **Indices Instables** : `{n_instables}`",
        f"- **Indices Critiques** : `{n_critiques}`",
        f"- **Mémoire Globale Saine** : **{saine}**",
        f"",
        f"## Tableau par Indice",
        f"",
        f"| Indice | N Analyses | I1 Fréquence | I2 Contradiction | I3 Âge (J) | I4 Calibration | Statut |",
        f"|---|---|---|---|---|---|---|"
    ]

    for ind, r in sorted(resultats.items()):
        lignes_md.append(
            f"| `{ind}` | {r['n_analyses']} | {r['i1_frequence']} | {r['i2_contradiction']} | {r['i3_age_jours']}j ({r['i3_statut']}) | {r['i4_calibration']} | **{r['statut']}** |"
        )

    lignes_md.extend([
        f"",
        f"## Alertes & Synthèse",
        f"1. **Stabilité globale** : {'La mémoire ne présente aucune dérive critique.' if n_instables == 0 and n_critiques == 0 else 'Des dérives ont été détectées sur certains indices nécessitant une revue de Cortana.'}",
        f"2. **Indicateurs clés** : I1 (Fréquence), I2 (Flip-flop / Contradiction), I3 (Péremption temporelle), I4 (Calibration de la confiance).",
        f"3. **Discipline** : Ce rapport est généré automatiquement par `derive_memoire.py` (Chantier 2 @0xWast3).",
        f""
    ])

    try:
        with open(RAPPORT_MD_PATH, "w", encoding="utf-8") as f:
            f.write("\n".join(lignes_md))
    except Exception:
        pass


def ecrire_json(resultats, n_instables, n_critiques, ts):
    """Écrit le fichier JSON de traçabilité"""
    os.makedirs(os.path.dirname(RAPPORT_JSON_PATH), exist_ok=True)
    payload = {
        "ts": ts,
        "global": {
            "indices_instables": n_instables,
            "indices_critiques": n_critiques,
            "note": "Saine" if (n_instables == 0 and n_critiques == 0) else "Attention requise"
        },
        "par_indice": resultats
    }
    try:
        with open(RAPPORT_JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


if __name__ == "__main__":
    sys.exit(main())
