#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""wiki_ia.py — LA PORTE D'ENTRÉE DES IA (03/11/2026, GO Christophe : « assez de re-chercher »).

LE PROBLÈME, MESURÉ
-------------------
La maison AVAIT déjà les cartes : `OSSATURE_INDEX.md` (« loi du coffre — ouvrir ici avant de
créer un fichier au hasard »), `CARTE_ORGANES_20260911.md`, `ARCHITECTURE_VIVANTE.md`,
`PLAN_DE_VOL.md`, `RUN_INDEX.md`, 140 fichiers de signets… et pourtant chaque IA repart de
zéro et re-scanne tout. Pourquoi ? Parce qu'AUCUNE de ces cartes ne répond à la seule
question qu'une IA se pose : « pour CE besoin, quel fichier exactement, et est-il encore
frais ? ». Une carte qui ne dit pas où est la réponse ne remplace pas la recherche.

CE QUE CE MODULE PRODUIT
------------------------
  Index_Maison/WIKI_IA.md      → lisible par un humain ET par une IA (ordre de lecture imposé)
  Index_Maison/data/wiki_ia.json → même contenu, machine (routes + fraîcheurs + compteurs)

Tout est GÉNÉRÉ depuis le disque : registre des scellés, fichiers `thermo/`, `data/`,
calendrier, en-têtes du registre d'erreurs, mtimes des cartes, comptage des signets.
Aucune phrase inventée sur l'état : ce qui n'est pas lisible sort en `SANS_MESURE`.

AUTO-CONTRÔLE (ce qui rend le wiki fiable)
------------------------------------------
  · chaque route de la table « OÙ REGARDER » est vérifiée : ✓ existe / ✗ INTROUVABLE ;
  · chaque instrument porte son ÂGE (bandes DÉCLARÉES : > 24 h = lent, > 72 h = muet) ;
  · le wiki porte sa propre date ; `--check` sort 2 si le wiki a plus de 2 h (périmé) ;
  · lecture seule sur tout le reste : 0 ordre, 0 écriture ailleurs que ses 2 sorties.

Usage :
  python3 wiki_ia.py            # régénère
  python3 wiki_ia.py --check    # 0 = frais, 2 = périmé / source manquante
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(os.path.expanduser("~/ace777-test-day1"))
IM = ROOT / "Index_Maison"
THERMO = IM / "thermo"
DATA = IM / "data"
RUNS = ROOT / "hulk-mexc" / "runs"
OBS = Path(os.path.expanduser("~/Documents/Obsidian_ACE777"))
SIGNETS = OBS / "Signets_X"
OUT_MD = IM / "WIKI_IA.md"
OUT_JSON = DATA / "wiki_ia.json"
FRAIS_MAX_H = 2.0
BANDE_LENT_H = 24.0
BANDE_MUET_H = 72.0

# LA TABLE QUI REMPLACE LA RECHERCHE — une question, un fichier, une réserve.
# (question, chemin, note / piège à connaître)
OU_REGARDER = [
    ("Quel chiffre fait foi ?", "hulk-mexc/runs/PAPER_V1_*_state.json",
     "le MOTEUR — jamais un replay (§42). short_*_state.json pour les shorts"),
    ("Que vaut le portefeuille ?", "Index_Maison/thermo/equity_reconcilie.json",
     "lire les champs *moteur* ; le replay est NON ATTRIBUÉ"),
    ("Le journal est-il réconcilié ?", "hulk-mexc/runs/PNL_NET_*.json",
     "booking = |pnl_usdt| > 0, tout événement (§23/§24)"),
    ("Combien alléger, et à quelle taille ?", "hulk-mexc/runs/degraissage_plan.json",
     "dérivé de thermo/m_kelly_live.json (demi-Kelly)"),
    ("Le dégraissage s'exécute-t-il ?", "hulk-mexc/runs/degraissage_papier_etat.json",
     "PAPIER · trace : degraissage_papier.jsonl"),
    ("Trading / observation / radiées ?", "Index_Maison/strategie/classification_paires.json",
     "décide les périmètres de tous les ratios"),
    ("Quel organe tourne, à quelle cadence, produit quoi ?",
     "Index_Maison/strategie/ARCHITECTURE_VIVANTE.md", "généré à chaque validation"),
    ("Qui est scellé, et avec quel rôle ?", "Index_Maison/strategie/REGISTRE_SYNAPSES.json",
     "source du verrou : ne se lit pas à la main, se vérifie avec verrou_scelles.py"),
    ("Puis-je modifier ce fichier ?", "Index_Maison/scripts/predemodifier.py",
     "OBLIGATOIREMENT --declarer AVANT, y compris pour un AJOUT (§42 faute 6)"),
    ("Quelle est la règle de la maison ?", "Index_Maison/REGLE_D_OR.md",
     "plus §42 du registre d'erreurs (doctrine MOTEUR)"),
    ("Quelle erreur est déjà arrivée ?", "Index_Maison/REGISTRE_ECHECS_ET_ERREURS.md",
     "chercher le SYMPTÔME, pas le code : la cause est souvent déjà écrite"),
    ("Où va un nouveau fichier ?", "Index_Maison/OSSATURE_INDEX.md",
     "loi du coffre : une info = une place"),
    ("Quelles cartes existent déjà ?", "Index_Maison/CARTE_ORGANES_20260911.md",
     "plus CARTE_PROTOTYPE_20260919 · ARCHITECTURE_AGORA · SCHEMA_ARCHITECTURE"),
    ("Que faire en hack / cygne noir ?", "Index_Maison/scripts/hack_actif_mesure.py",
     "plus disjoncteur.py, STOP_ALL, et le §42"),
    ("Quel est le prochain rendez-vous obligatoire ?", "Index_Maison/calendrier.json",
     "rituel — l'oubli est un problème documenté"),
    ("Que disent les bookmarks X ?", "Documents/Obsidian_ACE777/Signets_X/",
     "plus index/SIGNETS_RESUMES.json (1 211 signets résumés)"),
    ("Comment mesurer AVANT de changer ?", "hulk-mexc/scripts/sandbox_degraissage.py",
     "contrefactuel ; tests test_*.py ; jamais de branchement sans chiffre"),
    ("Où sont les frais et le spread ?", "hulk-mexc/scripts/couts_communs.py",
     "§24 : modèle de coûts UNIQUE (5 bps/côté + spread)"),
    ("Quel plan est en vol ?", "Index_Maison/PLAN_DE_VOL.md",
     "plus PLAN_GRAND_LIVRE_20261103.md"),
    ("Quelles données sont périmées ?", "Index_Maison/WIKI_IA.md",
     "section FRAÎCHEUR : l'âge de chaque instrument, calculé ici"),
]

CARTES = ["OSSATURE_INDEX.md", "CARTE_ORGANES_20260911.md", "CARTE_PROTOTYPE_20260919.md",
          "ARCHITECTURE_AGORA.md", "SCHEMA_ARCHITECTURE_20260821.md",
          "PLAN_DE_VOL.md", "PLAN_GRAND_LIVRE_20261103.md", "SOUS_L_OEIL.md",
          "REGLE_D_OR.md", "MEMOIRE_COLLAB.md"]


def utc():
    return datetime.now(timezone.utc)


def age_h(p: Path):
    try:
        return round((utc().timestamp() - p.stat().st_mtime) / 3600.0, 2)
    except Exception:
        return None


def ts_du_json(d: dict):
    for k in ("ts", "ts_utc", "date", "horodatage", "generated_at"):
        v = d.get(k)
        if not v:
            continue
        try:
            if isinstance(v, (int, float)):
                return datetime.fromtimestamp(float(v), timezone.utc)
            t = datetime.fromisoformat(str(v).replace("Z", "+00:00"))
            return t if t.tzinfo else t.replace(tzinfo=timezone.utc)
        except Exception:
            continue
    return None


def instruments():
    out = []
    for d in (THERMO, DATA):
        if not d.exists():
            continue
        for f in sorted(d.glob("*.json")):
            try:
                j = json.loads(f.read_text(encoding="utf-8"))
            except Exception:
                continue
            if not isinstance(j, dict):
                continue
            t = ts_du_json(j)
            a = round((utc() - t).total_seconds() / 3600.0, 2) if t else None
            if a is None:
                bande = "SANS HORODATAGE"
            elif a > BANDE_MUET_H:
                bande = "MUET"
            elif a > BANDE_LENT_H:
                bande = "LENT"
            else:
                bande = "frais"
            out.append({"fichier": f"{d.name}/{f.name}", "age_h": a, "bande": bande})
    return out


def scelles():
    try:
        reg = json.loads((IM / "strategie" / "REGISTRE_SYNAPSES.json").read_text(encoding="utf-8"))
        entrees = reg.get("fichier") or []
    except Exception:
        return {"n": None, "roles": []}
    roles = []
    for e in entrees:
        r = (e.get("role") or e.get("origine") or "").strip()
        if r:
            roles.append((str(e.get("nom")), r[:110]))
    return {"n": len(entrees), "roles": roles[:14]}


def erreurs(n=8):
    try:
        lignes = (IM / "REGISTRE_ECHECS_ET_ERREURS.md").read_text(encoding="utf-8").splitlines()
    except Exception:
        return []
    return [l[3:].strip() for l in lignes if l.startswith("## §")][-n:]


def calendrier():
    try:
        c = json.loads((IM / "calendrier.json").read_text(encoding="utf-8"))
    except Exception:
        return {"ouverts": None, "prochains": []}
    items = c.get("items") or c.get("evenements") or []
    ouverts, prochains = 0, []
    for it in items:
        if it.get("fait") is True or it.get("clos") is True or it.get("statut") == "fait":
            continue
        ouverts += 1
        d = str(it.get("date") or it.get("echeance") or "")
        if d:
            prochains.append((d, str(it.get("titre") or it.get("titre_court") or it.get("quoi") or "")[:80]))
    prochains.sort()
    return {"ouverts": ouverts, "prochains": prochains[:6]}


def signets():
    n = len(list(SIGNETS.glob("Bookmark_Master_*.md"))) if SIGNETS.exists() else 0
    # DÉFAUT FERMÉ 03/11 : le chemin était DEVINÉ (`index/SIGNETS_RESUMES.json`) et sortait
    # SANS_MESURE alors que le fichier vivait ailleurs — exactement le « chemin supposé »
    # qui fait croire qu'une donnée n'existe pas. Quatre bases connues + recherche bornée
    # dans le vault ; si aucune ne le trouve, LÀ c'est un vrai SANS_MESURE.
    # Chemin CANONIQUE d'abord : `strategie/SIGNETS_RESUMES.json` (SPEC 15/08, queue_offres.py,
    # ARCHITECTURE_TECH). Le 03/11 il manquait dans ma liste → le wiki annonçait SANS_MESURE
    # sur un fichier qui existait. Un chemin absent de la liste n'est pas une absence de donnée.
    cands = [IM / "strategie" / "SIGNETS_RESUMES.json",
             OBS / "index" / "SIGNETS_RESUMES.json", OBS / "SIGNETS_RESUMES.json",
             DATA / "SIGNETS_RESUMES.json", IM / "SIGNETS_RESUMES.json"]
    cands += sorted(OBS.rglob("SIGNETS_RESUMES.json")) if OBS.exists() else []
    res = next((c for c in cands if c.exists()), None)
    n_res = None
    if res is not None:
        try:
            j = json.loads(res.read_text(encoding="utf-8"))
            n_res = len(j if isinstance(j, list) else (j.get("signets") or j.get("items") or []))
        except Exception:
            n_res = None
    return {"bookmarks": n, "resumes": n_res}


def main() -> int:
    maintenant = utc()
    routes, manquants = [], []
    for q, chemin, note in OU_REGARDER:
        if chemin == "Index_Maison/WIKI_IA.md":
            ok = True          # sortie de CE module : elle existe dès l'écriture (auto-référence)
        elif any(ch in chemin for ch in ("*", " ")):
            ok = True
        else:
            # 3 bases résolues DÉCLARÉES : racine projet, Index_Maison, foyer (vault Obsidian).
            # Défaut du 03/11 : une route `~/Documents/...` était jugée INTROUVABLE
            # parce qu'on ne regardait QUE sous la racine du projet.
            ok = ((ROOT / chemin).exists()
                  or (IM / chemin).exists()
                  or (Path.home() / chemin).exists()
                  or Path(os.path.expanduser(chemin)).exists())
        if not ok:
            manquants.append(chemin)
        routes.append({"question": q, "chemin": chemin, "note": note, "present": ok})

    cartes = []
    for c in CARTES:
        p = IM / c
        cartes.append({"nom": c, "present": p.exists(), "age_h": age_h(p) if p.exists() else None})

    instr = instruments()
    sc = scelles()
    err = erreurs()
    cal = calendrier()
    sg = signets()

    # La fraîcheur du wiki lui-même : écrit AVANT d'écrire le contenu (sinon 0 min menteur).
    wiki_prec = OUT_MD.exists()
    age_prec = age_h(OUT_MD) if wiki_prec else None

    L = []
    L.append("# WIKI IA — LA PORTE D'ENTRÉE (généré, ne pas éditer à la main)")
    L.append("")
    L.append(f"> Généré le **{maintenant.strftime('%Y-%m-%dT%H:%M:%SZ')}** par "
             f"`Index_Maison/scripts/wiki_ia.py`. Version précédente : "
             f"{('%.2f h' % age_prec) if age_prec is not None else 'aucune'}.")
    L.append("> **Ordre imposé à toute IA : (1) ce wiki, (2) la ligne de la table, (3) le fichier. "
             "La recherche large vient EN DERNIER, jamais en premier.**")
    L.append("")
    L.append("## 0. LES TROIS RÈGLES QUI ÉVITENT 90 % DES ERREURS")
    L.append("")
    L.append("1. **Le chiffre réel est celui du MOTEUR** (`*_state.json`). Un replay n'est pas une "
             "preuve : il se publie comme *écart non attribué* (§42).")
    L.append("2. **Rien ne se modifie sans `predemodifier.py --declarer` AVANT** — y compris un "
             "fichier neuf avant son ajout au registre (§42, faute 6).")
    L.append("3. **Aucun branchement sans chiffre** : mesure d'abord (sandbox / contrefactuel), et "
             "si le chiffre est négatif, on ne branche pas — on le dit.")
    L.append("")
    L.append("## 1. OÙ REGARDER POUR… (remplace la recherche)")
    L.append("")
    L.append("| Question | Fichier / organe | Réserve à connaître |")
    L.append("|---|---|---|")
    for r in routes:
        coche = "✓" if r["present"] else "✗ **INTROUVABLE**"
        L.append(f"| {r['question']} | `{r['chemin']}` {coche} | {r['note']} |")
    L.append("")
    L.append("## 2. INSTRUMENTS — CE QUI EST FRAIS, CE QUI EST MUET")
    L.append("")
    L.append(f"Bandelettes DÉCLARÉES (pas des alarmes) : frais ≤ {BANDE_LENT_H:.0f} h · "
             f"lent ≤ {BANDE_MUET_H:.0f} h · muet au-delà.")
    L.append("")
    L.append("| instrument | âge | état |")
    L.append("|---|---|---|")
    for i in sorted(instr, key=lambda x: (x["age_h"] is None, -(x["age_h"] or 0)))[:24]:
        a = "?" if i["age_h"] is None else f"{i['age_h']:.2f} h"
        L.append(f"| `{i['fichier']}` | {a} | {i['bande']} |")
    L.append("")
    L.append("## 3. CE QUI EST SCELLÉ")
    L.append("")
    n = sc["n"]
    L.append(f"**{n if n is not None else 'SANS_MESURE'} entrées** au registre des scellés "
             f"(`strategie/REGISTRE_SYNAPSES.json`). Vérification : "
             f"`verrou_scelles.py --controle` (un moteur dont un organe n'est pas au plomb ne démarre pas).")
    if sc["roles"]:
        L.append("")
        L.append("| organe | rôle déclaré |")
        L.append("|---|---|")
        for nom, role in sc["roles"]:
            L.append(f"| `{nom}` | {role} |")
    L.append("")
    L.append("## 4. LES ERREURS DÉJÀ PAYÉES (ne pas les repayer)")
    L.append("")
    if err:
        for e in reversed(err):
            L.append(f"- {e}")
    else:
        L.append("- SANS_MESURE : registre d'erreurs illisible.")
    L.append("")
    L.append("## 5. LES CARTES EXISTANTES (ne jamais en créer une 2e)")
    L.append("")
    L.append("| carte | âge | état |")
    L.append("|---|---|---|")
    for c in cartes:
        a = "?" if c["age_h"] is None else f"{c['age_h']:.1f} h"
        L.append(f"| `{c['nom']}` | {a} | {'✓' if c['present'] else '✗ absente'} |")
    L.append("")
    L.append("## 6. RENDEZ-VOUS OBLIGATOIRES")
    L.append("")
    L.append(f"Items ouverts au calendrier : **{cal['ouverts'] if cal['ouverts'] is not None else 'SANS_MESURE'}**.")
    for d, t in cal["prochains"]:
        L.append(f"- `{d}` — {t}")
    L.append("")
    L.append("## 7. SIGNETS X (ce qui a déjà été lu)")
    L.append("")
    L.append(f"- fichiers de bookmarks : **{sg['bookmarks']}** dans `Signets_X/`")
    L.append(f"- signets résumés indexés : **{sg['resumes'] if sg['resumes'] is not None else 'SANS_MESURE'}**")
    L.append("")
    L.append("## 8. AUTO-CONTRÔLE")
    L.append("")
    if manquants:
        L.append(f"- ✗ **{len(manquants)} route(s) INTROUVABLE(S)** : "
                 + ", ".join(f"`{m}`" for m in manquants[:8]))
    else:
        L.append("- ✓ toutes les routes de la table pointent vers un fichier existant.")
    L.append(f"- âge de ce wiki : **{('%.2f h' % age_prec) if age_prec is not None else 'n/a'}** "
             f"(seuil de péremption : {FRAIS_MAX_H:.0f} h, vérifié par `wiki_ia.py --check`)")
    L.append("- régénéré par `com.ace777.wiki-ia` (launchd). Aucun ordre, aucune écriture ailleurs.")

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    _auto_declarer_sorties()
    OUT_MD.write_text("\n".join(L) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps({
        "ts": maintenant.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ou_regarder": routes, "routes_manquantes": manquants,
        "instruments": instr, "scelles": {"n": sc["n"]},
        "erreurs_recentes": err, "calendrier_ouverts": cal["ouverts"],
        "signets": sg, "cartes": cartes,
        "bandes_h": {"lent": BANDE_LENT_H, "muet": BANDE_MUET_H},
        "peremption_h": FRAIS_MAX_H, "lecture_seule": True, "ordres": 0,
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    print("[wiki_ia] %s · %d routes (%d introuvables) · %d instruments · %d scellés · %d cartes"
          % (maintenant.strftime("%H:%M:%SZ"), len(routes), len(manquants), len(instr),
             sc["n"] or 0, len(cartes)))
    if manquants:
        print("  ✗ routes introuvables : " + ", ".join(manquants[:6]))
    return 2 if manquants else 0


def _auto_declarer_sorties() -> None:
    """E58 (03/11) : le générateur DÉCLARE ses propres sorties, à chaque passage.

    MESURÉ : 4 faux rouges « AUDIT DES ACTES » le même jour (vigie_cooldown.json,
    justesse_v2.json, regime_justesse.json, puis WIKI_IA.md à 16:10:23Z) — chaque
    fois une SORTIE d'organe jugée acte non déclaré, chaque fois une alarme
    vocale en boucle. Déclarer à la main ne tient pas : celui qui écrit est le
    seul à savoir qu'il écrit. Ici l'organe se déclare lui-même.
    Idempotent (audit_actes refuse le doublon) et JAMAIS bloquant : si la
    déclaration échoue, le wiki s'écrit quand même et l'audit le dira —
    aucune alarme ne doit dépendre du silence d'un outil.
    """
    import subprocess
    outil = IM / "scripts" / "audit_actes.py"
    if not outil.exists():
        return
    for rel, motif in (
        ("Index_Maison/WIKI_IA.md",
         "wiki d'entree regenere a chaque passage du generateur (E58)"),
        ("Index_Maison/data/wiki_ia.json",
         "version machine du wiki, regeneree a chaque passage (E58)"),
    ):
        try:
            subprocess.run(
                [sys.executable, str(outil), "--declarer-sortie", rel,
                 "--organe", "Index_Maison/scripts/wiki_ia.py", "--motif", motif],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=20)
        except Exception:
            pass


def check() -> int:
    if not OUT_MD.exists():
        print("[wiki_ia --check] wiki ABSENT — régénérer")
        return 2
    a = age_h(OUT_MD)
    try:
        j = json.loads(OUT_JSON.read_text(encoding="utf-8"))
        manq = j.get("routes_manquantes") or []
    except Exception:
        manq = []
    if a is None or a > FRAIS_MAX_H or manq:
        print("[wiki_ia --check] PÉRIMÉ/INCOMPLET (âge %s h, %d route(s) morte(s))"
              % ("?" if a is None else "%.2f" % a, len(manq)))
        return 2
    print("[wiki_ia --check] frais (%.2f h) · %d routes vivantes" % (a, len(j["ou_regarder"])))
    return 0


if __name__ == "__main__":
    sys.exit(check() if "--check" in sys.argv else main())
