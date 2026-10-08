#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COUVERTURE DES CLASSES D'ERREUR — « une erreur connue a-t-elle encore sa garde debout ? »
=========================================================================================
POURQUOI CE FICHIER EXISTE (demande Christophe, 08/10/2026)
----------------------------------------------------------
Mot pour mot : « c'est possible d'avoir une IA qui ameliore et anticipe les erreurs ? je veux
que tout soit clean et coherent, sinon pas de plus-value ni de reel. »
La 6e partie du cycle (la memoire des echecs) EXISTE : le registre `REGISTRE_ECHECS_ET_ERREURS.md`
classe mes erreurs (E1..E26) avec, en colonne, « la garde mecanique (pas une promesse) ».
Le TROU, nomme par le registre lui-meme (§13.1 trou B) : *une garde qui existe mais que personne
n'appelle la ou la conclusion se rend est une promesse.* Personne ne repondait a la question :

    « pour CHAQUE classe d'erreur connue : la garde existe-t-elle, est-elle BRANCHEE,
      et son rapport est-il la ? »

CE QU'IL FAIT (lecture seule, stdlib, 0 €, 0 ordre)
---------------------------------------------------
  1. SOURCE UNIQUE — le denominateur est LU au registre : toutes les classes `Exx` citees dans
     les tableaux. Le compte n'est jamais recopie (lecon des « 24 paires » : un chiffre recopie
     est faux en silence des qu'on ajoute une paire).
  2. CARTE DECLAREE — `strategie/gardes_erreurs.json` dit, pour chaque classe, sa garde et son
     type : `mecanique` | `promesse` | `ouverture`. Une carte, pas une deduction : ce qui n'est
     pas declare est visible.
  3. CONTROLE, classe par classe :
       - classe au registre ABSENTE de la carte .......... TROU (erreur connue sans garde declaree)
       - `mecanique` : organe ABSENT du disque ........... TROU
       - `mecanique` : organe jamais CITE dans une zone de cablage ... TROU (R15 : hors de la
         boucle = n'existe pas)
       - `mecanique` : rapports declares manquants ....... TROU (une sortie evanouie = garde cassee)
       - `promesse` / `ouverture` ........................ comptees et NOMMEES, jamais vertes en silence
  4. VERDICT — `PROPRE` si zero TROU, sinon `TROUS` avec la liste exacte. Les promesses et les
     ouvertures sont publiees a cote : « clean » ne veut pas dire « tout est mecanique », ca veut
     dire « aucune garde declaree n'est manquante ».

CE QU'IL N'INVENTE PAS (R17, R14)
---------------------------------
  - Aucun seuil de fraicheur : la carte peut declarer `ttl_h` par garde (avec sa provenance) ;
    sans `ttl_h`, l'age du rapport est AFFICHE, jamais juge. Un seuil invente serait une erreur E1.
  - Aucune deduction « le fichier existe donc c'est branche » : le branchement est MESURE par
    citation reelle dans les zones de cablage, sinon la garde est une promesse qui s'ignore.

BRANCHEMENT (pour que CE fichier ne soit pas, lui aussi, une promesse)
---------------------------------------------------------------------
Appele EN DIRECT par `scripts/drill_restauration.py` (section 7), la ou le verdict READY/TROU se
rend. Usage :
  python3 scripts/couverture_erreurs.py            # rapport humain + exit 0/1
  python3 scripts/couverture_erreurs.py --json     # sortie machine (drill, cockpit, discipline)
  python3 scripts/couverture_erreurs.py --autotest # prouve que le controle SAIT dire NON
  python3 scripts/couverture_erreurs.py --ia       # OPTIONNEL : le HUB propose des gardes pour les
                                                   # classes sans garde mecanique. PROPOSE, ne decide
                                                   # jamais (strategie/anticipation_propositions.json).
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent          # ace777-test-day1
IM = RACINE / "Index_Maison"
REGISTRE = IM / "REGISTRE_ECHECS_ET_ERREURS.md"
CARTE = IM / "strategie" / "gardes_erreurs.json"
OUT_MD = IM / "thermo" / "COUVERTURE_ERREURS.md"
OUT_JSON = IM / "thermo" / "couverture_erreurs.json"
PROPOSITIONS = IM / "strategie" / "anticipation_propositions.json"
HUB = os.environ.get("HUB_URL", "http://127.0.0.1:11435/v1/chat/completions")
HUB_MODEL = os.environ.get("HUB_MODEL", "deepseek-ai/DeepSeek-V3-0324")

# Zones ou l'on CABLe (invoque, charge, appelle). C'est DE LIBERE plus etroit que le depot :
# citer un garde dans un doc de veille n'est pas le brancher (R15 : ce qui n'est pas dans la
# boucle n'existe pas). Restreindre rend aussi la mesure rapide et stable.
ZONES = ["Index_Maison/scripts", "Index_Maison/plists", "Index_Maison/cockpit",
         "Index_Maison/strategie", "Index_Maison/system", "hulk-mexc",
         # les agents launchd vivent HORS repo : un gardien peut n'etre branche que la.
         # Les oublier produirait un faux « non branche » — pire qu'aucun gardien (R14).
         "~/Library/LaunchAgents"]
# Seuls les types qui INV OQUENT (un doc .md qui cite un garde ne le branche pas, une config
# .json qui le declare non plus — sinon on se donne un faux vert, classe E23).
INCLUDES = ["--include=*.py", "--include=*.sh", "--include=*.plist", "--include=*.command",
            "--include=*.env"]

RE_CLASSE = re.compile(r"\*\*(E\d+)\*\*")

# Un fichier qui PARLE de gardes n'est pas un fichier qui les APPELLE. Sans cette exclusion,
# `REGISTRE_SYNAPSES.json` (qui liste les 164 scelles par leur nom) et `gardes_erreurs.json`
# (qui declare les organes) rendraient TOUT le monde « branche » — un faux vert de la classe
# E23 (un instrument qui juge contre un critere que la machine n'utilise pas).
# « declarer_rescel_* », « resceler.py », « predemodifier.py » : ces outils LISTENT/SCELLENT des
# fichiers, ils n'APPELLENT aucune garde. Les compter comme appelants masquait le vrai etat :
# `chiffrage_stop_serre.py` ne paraissait branche que par un utilitaire de re-scellement.
EXCLUS = ("REGISTRE_SYNAPSES", "PREDECLARATIONS", "gardes_erreurs.json", "predeclaration.json",
          "drill_restauration.json", "couverture_erreurs", "INTEGRITE_BASE", "reparations",
          "declarer_rescel", "resceler.py", "predemodifier.py")


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def lire_classes(txt_registre: str) -> list[str]:
    """Le denominateur, LU au registre : les classes citees dans les lignes de tableau."""
    trouvees: set[str] = set()
    for ligne in txt_registre.splitlines():
        if not ligne.lstrip().startswith("|"):
            continue
        for m in RE_CLASSE.finditer(ligne):
            trouvees.add(m.group(1))
    return sorted(trouvees, key=lambda c: int(c[1:]))


def indexer_citations(noms: list[str], racine: Path = RACINE) -> dict | None:
    """UNE passe grep pour tous les noms : {nom_de_base: [chemins qui le citent]}.

    Rend None si la mesure est impossible (on ne conclut alors PAS « non branche » : un
    branchement non mesurable se declare, il ne s'invente pas — classe E10/E2)."""
    noms = sorted({Path(n).name for n in noms if n})
    if not noms:
        return {}
    zones = [str((Path(z).expanduser() if z.startswith(("~", "/")) else racine / z))
             for z in ZONES]
    zones = [z for z in zones if Path(z).exists()]
    if not zones:
        zones = [str(racine)]
    cmd = ["grep", "-rH", "-o", "-F", "--exclude-dir=.git"] + INCLUDES
    for n in noms:
        cmd += ["-e", n]
    cmd += zones
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except Exception:
        return None
    if p.returncode not in (0, 1):
        return None
    idx: dict[str, list[str]] = {n: [] for n in noms}
    for ligne in p.stdout.splitlines():
        if ":" not in ligne:
            continue
        chemin, _, nom = ligne.rpartition(":")
        nom = nom.strip()
        chemin = os.path.normpath(chemin.strip())
        if nom not in idx:
            continue
        base = os.path.basename(chemin)
        if ("/thermo/" in chemin or ".bak" in base
                or any(base.startswith(x) for x in EXCLUS)):
            continue                       # rapport/registre/sauvegarde : parle, n'appelle pas
        idx[nom].append(chemin)
    return idx


def _cites(organe: str, idx: dict | None) -> int | None:
    """Nombre de fichiers AUTRES que l'organe lui-meme qui citent son nom (None = non mesurable)."""
    if idx is None:
        return None
    base = Path(organe).name
    cible = os.path.normpath(organe)
    return sum(1 for c in idx.get(base, []) if c != cible and not c.endswith(cible))


def controler(classes: list[str], carte: dict, racine: Path = RACINE,
              idx: dict | None = "__auto__") -> dict:
    """Classe par classe : garde declaree ? existe ? branchee ? rapport la ?
    Logique pure et injectable (l'autotest l'appelle avec des donnees factices)."""
    declares = (carte or {}).get("classes") or {}
    if idx == "__auto__":
        idx = indexer_citations([(d or {}).get("organe") or "" for d in declares.values()], racine)
    trous, meca, prom, ouv = [], [], [], []
    for c in classes:
        d = declares.get(c)
        if not isinstance(d, dict):
            trous.append({"classe": c, "raison": "classe au registre SANS garde declaree (gardes_erreurs.json)"})
            continue
        typ = d.get("type") or "?"
        if typ == "promesse":
            prom.append({"classe": c, "garde": d.get("garde", "—"), "note": d.get("note", "")})
            continue
        if typ == "ouverture":
            ouv.append({"classe": c, "note": d.get("note", "")})
            continue
        if typ != "mecanique":
            trous.append({"classe": c, "raison": f"type inconnu « {typ} » (attendu mecanique|promesse|ouverture)"})
            continue
        organe = d.get("organe") or ""
        p = (racine / organe) if organe else None
        raisons: list[str] = []
        cites: int | None = None
        if not organe:
            raisons.append("aucun organe declare")
        elif not p.exists():
            raisons.append(f"organe ABSENT du disque : {organe}")
        else:
            cites = _cites(organe, idx)
            if cites == 0:
                raisons.append(f"organe JAMAIS cite dans une zone de cablage -> non branche (R15) : {organe}")
            elif cites is None:
                raisons.append(f"branchement NON MESURABLE (grep indisponible) : {organe} — declare, pas invente")
        ages: dict[str, float] = {}
        for rap in (d.get("rapports") or []):
            rp = racine / rap
            if not rp.exists():
                raisons.append(f"rapport declare MANQUANT : {rap}")
            else:
                ages[rap] = round((time.time() - rp.stat().st_mtime) / 3600.0, 1)
                ttl = d.get("ttl_h")
                if isinstance(ttl, (int, float)) and ages[rap] > ttl:
                    raisons.append(f"rapport GELE : {rap} ({ages[rap]} h > ttl declare {ttl} h)")
        meca.append({"classe": c, "garde": d.get("garde", ""), "organe": organe, "cites": cites,
                     "ages_h": ages, "provenance": d.get("provenance", ""),
                     "ok": not raisons, "raisons": raisons})
        if raisons:
            trous.append({"classe": c, "raison": " ; ".join(raisons)})
    return {"trous": trous, "mecaniques": meca, "promesses": prom, "ouvertures": ouv}


def rapport(classes: list[str], res: dict) -> tuple[str, dict]:
    propre = not res["trous"]
    verdict = "PROPRE" if propre else "TROUS"
    j = {"ts": utc(), "verdict": verdict, "classes_registre": classes, "n_classes": len(classes),
         "n_mecaniques": len(res["mecaniques"]), "n_promesses": len(res["promesses"]),
         "n_ouvertures": len(res["ouvertures"]), "n_trous": len(res["trous"]),
         "trous": res["trous"], "mecaniques": res["mecaniques"],
         "promesses": res["promesses"], "ouvertures": res["ouvertures"]}
    L = [f"# Couverture des classes d'erreur — {j['ts']}", "",
         f"**Verdict : {'✅' if propre else '🔴'} {verdict}** · {len(classes)} classes au registre · "
         f"{len(res['mecaniques'])} gardes mecaniques · {len(res['promesses'])} promesses declarees · "
         f"{len(res['ouvertures'])} ouverture(s).", "",
         "> Le denominateur est **lu au registre** (`REGISTRE_ECHECS_ET_ERREURS.md`), jamais recopie :",
         "> une classe ajoutee au registre sans garde declaree devient un TROU immediatement — c'est",
         "> l'anticipation : le controle crie **avant** que la nouvelle classe morde.", ""]
    if res["trous"]:
        L += ["## 🔴 TROUS (garde declaree manquante, absente ou non branchee)", ""]
        for t in res["trous"]:
            L.append(f"- **{t['classe']}** — {t['raison']}")
        L.append("")
    L += ["## Gardes MECANIQUES (existe · branchee · rapport)", "",
          "| Classe | Garde (organe) | Citée par | Âge rapport (h) | État |", "|---|---|---|---|---|"]
    for m in res["mecaniques"]:
        cites = "non mesurable" if m["cites"] is None else m["cites"]
        ages = ", ".join(str(v) for v in m["ages_h"].values()) or "—"
        L.append(f"| {m['classe']} | `{Path(m['organe']).name or '—'}` | {cites} | {ages} | "
                 f"{'✅' if m['ok'] else '🔴 ' + ' ; '.join(m['raisons'])} |")
    L += ["", "## Promesses déclarées et ouvertures (jamais vertes en silence)", "",
          "| Classe | Type | Note |", "|---|---|---|"]
    for o in res["ouvertures"]:
        L.append(f"| {o['classe']} | ouverture | {o['note']} |")
    for p in res["promesses"]:
        L.append(f"| {p['classe']} | promesse | {p['note']} |")
    L += ["", "---",
          "*Généré par `scripts/couverture_erreurs.py` (lecture seule). Carte : "
          "`strategie/gardes_erreurs.json`. Canon des classes : `REGISTRE_ECHECS_ET_ERREURS.md`. "
          "Appelé EN DIRECT par `drill_restauration.py` (§7).*", ""]
    return "\n".join(L), j


def demander_pistes(res: dict, propositions: Path = PROPOSITIONS) -> str:
    """OPTIONNEL (--ia) : soumet les classes SANS garde mecanique au HUB. PROPOSE, ne decide pas."""
    import urllib.request
    sans = ([f"{t['classe']} (trou : {t['raison']})" for t in res["trous"]]
            + [f"{o['classe']} (ouverture : {o['note'][:200]})" for o in res["ouvertures"]]
            + [f"{p['classe']} (promesse : {p['note'][:200]})" for p in res["promesses"]])
    if not sans:
        return "aucune classe sans garde mecanique — rien a proposer"
    prompt = (
        "Tu es expert en fiabilite de systemes de trading automatises. Voici des CLASSES D'ERREUR "
        "connues d'un moteur paper, qui n'ont PAS de garde mecanique (seulement une regle ecrite). "
        "Pour chacune, propose UNE garde DETERMINISTE verifiable par machine (un controle qui "
        "retourne vrai/faux a partir de fichiers, sans jugement humain). Reponds en JSON strict : "
        '[{"classe":"E11","garde_proposee":"...","mesure":"ce qui est lu","echec_si":"condition"}] '
        "Aucun commentaire hors JSON.\n\nCLASSES SANS GARDE MECANIQUE :\n- " + "\n- ".join(sans))
    corps = json.dumps({"model": HUB_MODEL, "messages": [{"role": "user", "content": prompt}],
                        "temperature": 0.2}).encode()
    try:
        req = urllib.request.Request(HUB, data=corps, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.loads(r.read().decode())
        txt = (d.get("choices") or [{}])[0].get("message", {}).get("content", "")
        servis = d.get("model") or "?"
    except Exception as e:
        return f"HUB injoignable ({e}) — rien propose (declare, non bloquant)"
    propositions.parent.mkdir(parents=True, exist_ok=True)
    propositions.write_text(json.dumps(
        {"ts": utc(), "modele_demande": HUB_MODEL, "modele_servi": servis,
         "statut": "PROPOSITION — ne decide pas (l'automation propose, l'humain approuve)",
         "classes_sans_garde": [s.split(" ")[0] for s in sans], "brut": txt},
        ensure_ascii=False, indent=2), encoding="utf-8")
    return f"propositions ecrites : {propositions.name} (servi par {servis}) — PROPOSE, ne decide pas"


def autotest() -> int:
    """Prouve que le controle SAIT dire NON (sans ca, un gardien vert ne prouve rien — lecon E23)."""
    cas = []
    sain = {"classes": {"E1": {"type": "promesse", "note": "regle ecrite"}}}
    # 1) classe au registre absente de la carte DOIT etre un trou
    r = controler(["E1", "E99"], sain, idx={})
    cas.append(("classe au registre sans declaration -> TROU", any(t["classe"] == "E99" for t in r["trous"])))
    # 2) garde mecanique dont l'organe est ABSENT du disque DOIT etre un trou
    r = controler(["E1"], {"classes": {"E1": {"type": "mecanique",
                                              "organe": "Index_Maison/scripts/nexiste_pas_xyz.py"}}}, idx={})
    cas.append(("organe mecanique absent du disque -> TROU", bool(r["trous"])))
    # 3) garde mecanique presente mais JAMAIS citee DOIT etre signalee non branchee
    import tempfile
    with tempfile.NamedTemporaryFile(suffix="_couverture_autotest.py", delete=False) as tf:
        tmp = tf.name
    try:
        r = controler(["E1"], {"classes": {"E1": {"type": "mecanique", "organe": tmp}}}, idx={})
        non_branche = any("non branche" in t.get("raison", "") for t in r["trous"])
    finally:
        try:
            os.remove(tmp)
        except Exception:
            pass
    cas.append(("organe jamais cite -> signale non branche", non_branche))
    # 3bis) organe CITE ailleurs -> AUCUN trou (pas de faux positif)
    r = controler(["E1"], {"classes": {"E1": {"type": "mecanique",
                                              "organe": "Index_Maison/scripts/critique_erreurs.py"}}},
                  idx={"critique_erreurs.py": ["Index_Maison/scripts/discipline_quotidienne.py"]})
    cas.append(("organe cite ailleurs -> pas de trou", not r["trous"]))
    # 4) rapport declare manquant DOIT etre un trou
    r = controler(["E1"], {"classes": {"E1": {"type": "mecanique",
                                              "organe": "Index_Maison/scripts/critique_erreurs.py",
                                              "rapports": ["Index_Maison/thermo/nexiste_pas_xyz.json"]}}},
                  idx={"critique_erreurs.py": ["x"]})
    cas.append(("rapport declare manquant -> TROU", bool(r["trous"])))
    # 5) une promesse declaree NE DOIT PAS produire de trou
    r = controler(["E1"], sain, idx={})
    cas.append(("promesse declaree -> aucun trou (pas de faux positif)", not r["trous"]))
    # 6) le registre REEL doit rendre un nombre plausible de classes (le denominateur est lu)
    try:
        cas.append(("registre reel lu (>= 20 classes)",
                    len(lire_classes(REGISTRE.read_text(encoding="utf-8"))) >= 20))
    except Exception:
        cas.append(("registre reel lisible", False))
    for nom, ok in cas:
        print(f"  {'[OK ]' if ok else '[KO ]'} {nom}")
    bon = all(ok for _, ok in cas)
    print(f"  -> {'GARDIEN FIABLE' if bon else 'GARDIEN CASSÉ'} ({sum(1 for _, o in cas if o)}/{len(cas)})")
    return 0 if bon else 3


def main() -> int:
    args = sys.argv[1:]
    if "--autotest" in args:
        return autotest()
    try:
        txt = REGISTRE.read_text(encoding="utf-8")
    except Exception as e:
        print(f"❌ registre illisible : {e}")
        return 2
    classes = lire_classes(txt)
    try:
        carte = json.loads(CARTE.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"❌ carte des gardes illisible ({CARTE}) : {e}")
        return 2
    res = controler(classes, carte)
    md, j = rapport(classes, res)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(md, encoding="utf-8")
    OUT_JSON.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding="utf-8")

    if "--json" in args:
        print(json.dumps(j, ensure_ascii=False))
    else:
        print(f"COUVERTURE ERREURS — {j['verdict']} · {j['n_classes']} classes · "
              f"{j['n_mecaniques']} mecaniques · {j['n_promesses']} promesses · "
              f"{j['n_ouvertures']} ouverture(s) · {j['n_trous']} trou(s)")
        for t in res["trous"]:
            print(f"  🔴 {t['classe']} : {t['raison']}")
        for o in res["ouvertures"]:
            print(f"  ⚠️  {o['classe']} : ouverture declaree (remede identifie, en attente de GO)")
        for p in res["promesses"]:
            print(f"  ·  {p['classe']} : promesse declaree (aucune garde mecanique)")
        print(f"  rapport : {OUT_MD}")
    if "--ia" in args:
        print("  IA : " + demander_pistes(res))
    return 0 if not res["trous"] else 1


if __name__ == "__main__":
    sys.exit(main())
