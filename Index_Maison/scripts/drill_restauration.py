#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle (ACE777) : DRILL DE RESTAURATION — « si le Mac mourait ce soir, ACE777 reviendrait-il ? »

POURQUOI (leçon du 19/09/2026) : des organes étaient INSTALLÉS mais non VERSIONNÉS,
et personne ne testait jamais la restauration. Une sauvegarde jamais testée n'est pas
une sauvegarde : c'est une hypothèse. Ce script transforme l'hypothèse en PREUVE datée.

CE QU'IL FAIT (100 % LECTURE SEULE sur le système vivant) :
  1. SOURCE   — le repo git contient-il tout ? (écarts HEAD↔disque, fichiers non suivis)
  2. AGENTS   — chaque agent launchd installé est-il reconstructible depuis le repo ?
  3. RECONSTRUIRE — dans un dossier NEUF (/tmp), on « rebâtit » les agents depuis le repo
                    et on valide chaque plist (plutil -lint). Rien n'est installé.
  4. ORGANES  — chaque chemin que l'agent invoque (script, WatchPath, dossier de travail)
                existe-t-il ENCORE ? dedans / hors du repo (à sauvegarder autrement) / absent ?
  5. SCELLÉS  — les md5 du registre (veilleuse) correspondent-ils au repo ?
  6. VERDICT  — READY (restaurable) ou TROU (avec la liste exacte de ce qui manque).

GARANTIES : aucun agent installé/déchargé, aucun fichier vivant modifié. Écrit seulement
un rapport (thermo/DRILL_RESTAURATION.md + .json). Stdlib uniquement.
Exit 0 = READY · 2 = TROU (organe perdu s'il y en a) · 1 = erreur d'exécution.
USAGE : python3 scripts/drill_restauration.py [--sandbox <dir>]
"""

import json
import os
import plistlib
import shutil
import stat
import subprocess
import sys
import tempfile
import time
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent          # ~/ace777-test-day1
IM = RACINE / "Index_Maison"
REPO_PLISTS = IM / "plists"
REGISTRE = IM / "strategie" / "REGISTRE_SYNAPSES.json"
AGENTS = Path.home() / "Library" / "LaunchAgents"
RAPPORT_MD = IM / "thermo" / "DRILL_RESTAURATION.md"
RAPPORT_JSON = IM / "thermo" / "drill_restauration.json"

PREUVE_OK = "✅"
PREUVE_TROU = "🔴"


def run(cmd, cwd=None):
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except Exception as e:  # pragma: no cover
        return 1, "", str(e)


def ecrire_atomique(chemin: Path, contenu: str):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(chemin.parent), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(contenu)
        os.replace(tmp, chemin)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise


# ── 1. SOURCE : le repo contient-il tout ? ────────────────────────────────────
def etape_source():
    r = {"branche": "", "head": "", "head_date": "", "modifies": [], "supprimes": [],
         "non_suivis_nb": 0, "non_suivis_critiques": [], "propre": False}
    code, head, _ = run(["git", "rev-parse", "--short", "HEAD"], cwd=RACINE)
    r["head"] = head if code == 0 else "?"
    code, br, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=RACINE)
    r["branche"] = br if code == 0 else "?"
    code, d, _ = run(["git", "log", "-1", "--format=%cI"], cwd=RACINE)
    r["head_date"] = d if code == 0 else "?"

    # --untracked-files=no : on ne veut que les écarts de fichiers SUIVIS (les logs/thermo non suivis sont du bruit)
    code, out, _ = run(["git", "status", "--porcelain", "--untracked-files=no"], cwd=RACINE)
    for ligne in out.splitlines():
        if len(ligne) < 4:
            continue
        statut, chemin = ligne[:2], ligne[3:].strip()
        if statut.strip() in ("M", "MM", "AM"):
            r["modifies"].append(chemin)
        elif statut.strip() == "D":
            r["supprimes"].append(chemin)
    # Fichiers non suivis qui comptent (scripts / plists / règles) — le reste est bruit de thermo
    code, out, _ = run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=RACINE)
    for ligne in out.splitlines():
        if not ligne.startswith("??"):
            continue
        r["non_suivis_nb"] += 1
        chemin = ligne[3:].strip()
        if (chemin.endswith(".plist") or chemin.startswith("Index_Maison/scripts/")
                or chemin.endswith(".mdc") or "/rules/" in chemin):
            r["non_suivis_critiques"].append(chemin)
    r["propre"] = not (r["modifies"] or r["supprimes"] or r["non_suivis_critiques"])
    return r


# ── 2. AGENTS : chaque agent installé est-il reconstructible ? ────────────────
def etape_agents():
    installes = sorted(p.name for p in AGENTS.glob("com.ace777.*.plist"))
    repo = sorted(p.name for p in REPO_PLISTS.glob("com.ace777.*.plist"))
    set_inst, set_repo = set(installes), set(repo)
    return {
        "installes": len(installes),
        "versionnes": len(repo),
        "hors_repo": sorted(set_inst - set_repo),      # 🔴 perdus à la restauration
        "orphelins": sorted(set_repo - set_inst),      # versionnés sans installé (à revoir)
    }


# ── 3. RECONSTRUIRE : dossier NEUF, on rebâtit depuis le repo ────────────────
def etape_reconstruire(sandbox: Path):
    dest = sandbox / "LaunchAgents"
    dest.mkdir(parents=True, exist_ok=True)
    reconstruits, invalides = [], []
    for src in sorted(REPO_PLISTS.glob("com.ace777.*.plist")):
        dst = dest / src.name
        shutil.copy2(src, dst)
        code, out, err = run(["plutil", "-lint", str(dst)])
        (reconstruits if code == 0 else invalides).append(src.name)
    return {"dossier": str(dest), "reconstruits": len(reconstruits), "invalides": invalides}


# ── 4. ORGANES : les chemins invoqués existent-ils encore ? ──────────────────
def chemins_invoques(plist_path: Path):
    """Extrait les chemins absolus utiles d'un plist, avec leur RÔLE.

    role = « programme »  → c'est l'exécutable lancé (le bit x compte)
           « argument »   → script passé en paramètre (lancé par bash/python, bit x inutile)
           « surveille »  → WatchPaths / cwd (dossier attendu)
           « env »        → valeur d'environnement (PATH & listes ':' ignorés : pas un chemin)
    """
    try:
        with open(plist_path, "rb") as f:
            d = plistlib.load(f)
    except Exception:
        return []
    out = []
    for k in ("ProgramArguments", "Program"):
        v = d.get(k)
        if isinstance(v, list):
            for i, x in enumerate(v):
                if isinstance(x, str) and x.startswith("/"):
                    out.append((x, "programme" if i == 0 else "argument"))
        elif isinstance(v, str) and v.startswith("/"):
            out.append((v, "programme"))
    for k in ("WatchPaths", "QueueDirectories", "WorkingDirectory"):
        v = d.get(k)
        vals = v if isinstance(v, list) else ([v] if isinstance(v, str) else [])
        out += [(x, "surveille") for x in vals if isinstance(x, str)]
    env = d.get("EnvironmentVariables") or {}
    if isinstance(env, dict):
        for cle, val in env.items():
            if cle == "PATH" or not isinstance(val, str) or not val.startswith("/"):
                continue
            if ":" in val:      # liste de chemins (PATH déguisé) → pas un chemin unique
                continue
            out.append((val, "env"))
    # dédoublonnage (chemin, rôle) en gardant l'ordre
    vus, uniq = set(), []
    for c in out:
        if c not in vus:
            vus.add(c)
            uniq.append(c)
    return uniq


def etape_organes():
    """Pour chaque agent versionné : les chemins invoqués survivraient-ils ?"""
    dedans, dehors, absents, non_exec = {}, {}, [], []
    detail_dehors = []
    for p in sorted(REPO_PLISTS.glob("com.ace777.*.plist")):
        for chemin, role in chemins_invoques(p):
            # /bin/bash, /usr/bin/python3… : fournis par le système, on ignore
            if chemin.startswith(("/bin/", "/usr/bin/", "/usr/sbin/", "/sbin/", "/System/")):
                continue
            c = Path(chemin)
            if not c.exists():
                # Un « env » ou un dossier de travail peut être créé à la volée : seuls un
                # programme/argument/surveillé absent est un vrai trou.
                absents.append({"agent": p.name, "chemin": chemin, "role": role})
                continue
            racine_str = str(RACINE)
            if chemin == racine_str or chemin.startswith(racine_str + os.sep):
                dedans[chemin] = dedans.get(chemin, 0) + 1
            else:
                dehors[chemin] = dehors.get(chemin, 0) + 1
                # Outillage installable (Homebrew, Xcode CLT) ≠ organe du projet : on
                # distingue, sinon le rapport crie au loup pour npm/uv/python3.
                outils = chemin.startswith(("/opt/homebrew", "/usr/local", "/opt/local",
                                           "/Library/Developer", "/Applications"))
                detail_dehors.append({"agent": p.name, "chemin": chemin, "role": role,
                                      "outil_systeme": outils})
            # Le bit x ne compte QUE pour l'exécutable lancé lui-même ; un script passé
            # en argument à bash/python n'en a pas besoin (68 faux positifs le 19/09).
            if role == "programme" and c.is_file() and not (c.stat().st_mode & stat.S_IXUSR):
                non_exec.append({"agent": p.name, "chemin": chemin})
    # regroupement des racines hors-repo (ce qu'il faut sauvegarder autrement)
    familles = {}
    for chemin in dehors:
        try:
            rel = Path(chemin).relative_to(Path.home())
        except ValueError:
            rel = Path(*Path(chemin).parts[1:])
        tete = "/".join(rel.parts[:2]) if rel.parts else chemin
        familles[tete] = familles.get(tete, 0) + 1
    organes_hors = [d for d in detail_dehors if not d["outil_systeme"]]
    return {
        "dedans": len(dedans), "dehors": len(dehors),
        "familles_dehors": dict(sorted(familles.items(), key=lambda x: -x[1])),
        "detail_dehors": detail_dehors,
        "organes_hors_repo": organes_hors,
        "absents": absents, "non_executables": non_exec,
    }


# ── 5. SCELLÉS : md5 registre ↔ repo ────────────────────────────────────────
def md5(chemin: Path):
    import hashlib
    h = hashlib.md5()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def etape_scelles():
    if not REGISTRE.exists():
        return {"erreur": "registre absent", "total": 0, "ecarts": [], "manquants": []}
    d = json.loads(REGISTRE.read_text(encoding="utf-8"))
    ecarts, manquants, total = [], [], 0
    for e in d.get("fichier", []):
        if e.get("verif") != "md5" or not e.get("md5"):
            continue
        total += 1
        c = RACINE / e["nom"]
        if not c.exists():
            manquants.append(e["nom"])
            continue
        if md5(c) != e["md5"]:
            ecarts.append(e["nom"])
    return {"total": total, "ecarts": ecarts, "manquants": manquants}


def main():
    sandbox = None
    if "--sandbox" in sys.argv:
        sandbox = Path(sys.argv[sys.argv.index("--sandbox") + 1])
    if not sandbox:
        sandbox = Path(tempfile.mkdtemp(prefix="drill_restauration_"))
    started = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())

    src = etape_source()
    ag = etape_agents()
    rc = etape_reconstruire(sandbox)
    org = etape_organes()
    sc = etape_scelles()

    trous = []
    absents_graves = [a for a in org["absents"] if a["role"] != "env"]
    if ag["hors_repo"]:
        trous.append(f"{len(ag['hors_repo'])} agent(s) installé(s) NON versionné(s) → perdus à la restauration")
    if rc["invalides"]:
        trous.append(f"{len(rc['invalides'])} plist(s) versionné(s) invalide(s) (plutil -lint)")
    if absents_graves:
        trous.append(f"{len(absents_graves)} chemin(s) invoqué(s) par un agent n'existe(nt) plus")
    if org["organes_hors_repo"]:
        noms = sorted({d["chemin"] for d in org["organes_hors_repo"]})
        trous.append(f"{len(noms)} organe(s) du projet vivent HORS git → non restaurables depuis le repo "
                     f"({', '.join(noms[:4])}{'…' if len(noms) > 4 else ''})")
    if src["supprimes"]:
        trous.append(f"{len(src['supprimes'])} fichier(s) SUIVI(s) supprimé(s) sur le disque")
    if sc["ecarts"]:
        trous.append(f"{len(sc['ecarts'])} scellé(s) dont le md5 ne correspond plus")
    if sc["manquants"]:
        trous.append(f"{len(sc['manquants'])} fichier(s) scellé(s) ABSENT(s)")

    verdict = "READY" if not trous else "TROU"
    preuve = PREUVE_OK if verdict == "READY" else PREUVE_TROU

    # ── Rapport lisible (Obsidian / cockpit) ────────────────────────────────
    L = []
    L.append(f"# 🩺 DRILL DE RESTAURATION — {preuve} **{verdict}**")
    L.append("")
    L.append(f"> Testé le **{started}** · mode **lecture seule** (rien installé, rien modifié).")
    L.append(f"> Question posée : *« si le Mac mourait ce soir, ACE777 reviendrait-il ? »*")
    L.append("")
    L.append("## 1. Source — le repo (git) contient-il tout ?")
    L.append(f"- Branche `{src['branche']}` · HEAD `{src['head']}` du {src['head_date']}")
    L.append(f"- Fichiers suivis modifiés sur disque : **{len(src['modifies'])}**")
    L.append(f"- Fichiers suivis **supprimés** (perdus) : **{len(src['supprimes'])}**")
    L.append(f"- Nouveaux fichiers non versionnés : {src['non_suivis_nb']} au total, "
             f"dont **{len(src['non_suivis_critiques'])} sensibles** (scripts/plists/règles)")
    if src["non_suivis_critiques"]:
        for c in src["non_suivis_critiques"][:15]:
            L.append(f"  - `{c}`")
    L.append("")
    L.append("## 2. Agents launchd — reconstructibles ?")
    L.append(f"- Installés : **{ag['installes']}** · versionnés : **{ag['versionnes']}**")
    if ag["hors_repo"]:
        L.append(f"- 🔴 **{len(ag['hors_repo'])} installés ABSENTS du repo** (perdus à la restauration) :")
        for c in ag["hors_repo"]:
            L.append(f"  - `{c}`")
    else:
        L.append("- ✅ **0 agent hors repo** — tous reconstructibles.")
    if ag["orphelins"]:
        L.append(f"- 🟠 Versionnés mais plus installés ({len(ag['orphelins'])}) : "
                 + ", ".join(f"`{x}`" for x in ag["orphelins"]))
    L.append("")
    L.append("## 3. Reconstruction dans un dossier neuf")
    L.append(f"- Dossier : `{rc['dossier']}`")
    L.append(f"- Plists rebâtis + validés (`plutil -lint`) : **{rc['reconstruits']}/{rc['reconstruits'] + len(rc['invalides'])}**")
    for x in rc["invalides"]:
        L.append(f"  - 🔴 invalide : `{x}`")
    L.append("")
    L.append("## 4. Organes invoqués par les agents")
    L.append(f"- Chemins **dans le repo** (reviennent avec git) : **{org['dedans']}**")
    L.append(f"- Chemins **hors repo** (à sauvegarder autrement, git ne les ramène PAS) : **{org['dehors']}**")
    if org["organes_hors_repo"]:
        L.append("")
        L.append("  **Organes du projet hors git** (git ne les ramène PAS → à sauvegarder à part) :")
        L.append("")
        L.append("  | Chemin | agent | rôle |")
        L.append("  |---|---|---|")
        for d in org["organes_hors_repo"][:20]:
            ch = d["chemin"].replace(str(Path.home()), "~", 1)
            L.append(f"  | `{ch}` | `{d['agent'].replace('com.ace777.', '').replace('.plist', '')}` | {d['role']} |")
    outils = [d for d in org["detail_dehors"] if d["outil_systeme"]]
    if outils:
        noms = sorted({d["chemin"] for d in outils})
        L.append("")
        L.append(f"  Outillage système hors repo ({len(noms)}) — réinstallable (Homebrew/Xcode CLT), non bloquant : "
                 + ", ".join(f"`{x}`" for x in noms[:8]))
    if org["absents"]:
        L.append("")
        graves = [a for a in org["absents"] if a["role"] != "env"]
        if graves:
            L.append(f"- 🔴 **{len(graves)} chemin(s) introuvable(s)** :")
            for a in graves[:25]:
                L.append(f"  - `{a['chemin']}` (agent `{a['agent']}`, rôle `{a['role']}`)")
        legers = [a for a in org["absents"] if a["role"] == "env"]
        if legers:
            L.append(f"- 🟠 {len(legers)} valeur(s) d'environnement pointant sur un chemin absent (non bloquant) : "
                     + ", ".join(f"`{a['chemin']}`" for a in legers[:6]))
    else:
        L.append("- ✅ Aucun chemin invoqué introuvable.")
    if org["non_executables"]:
        L.append(f"- ⚠️ {len(org['non_executables'])} script(s) sans bit exécutable :")
        for a in org["non_executables"][:10]:
            L.append(f"  - `{a['chemin']}`")
    L.append("")
    L.append("## 5. Scellés (registre des synapses ↔ repo)")
    L.append(f"- Entrées md5 vérifiées : **{sc['total']}** · écarts : **{len(sc['ecarts'])}** · absents : **{len(sc['manquants'])}**")
    for x in sc["ecarts"]:
        L.append(f"  - ⚠️ md5 différent : `{x}`")
    for x in sc["manquants"]:
        L.append(f"  - 🔴 absent : `{x}`")
    L.append("")
    L.append("## 6. Verdict")
    if verdict == "READY":
        L.append("- ✅ **READY** — le prototype est reconstructible depuis le repo.")
    else:
        L.append(f"- 🔴 **{len(trous)} trou(s) à combler :**")
        for t in trous:
            L.append(f"  - {t}")
    L.append("")
    L.append("---")
    L.append("*Rapport généré par `scripts/drill_restauration.py` (lecture seule). "
             "Relancer après toute modification d'organe : un drill, ça se répète.*")
    rapport = "\n".join(L) + "\n"

    ecrire_atomique(RAPPORT_MD, rapport)
    ecrire_atomique(RAPPORT_JSON, json.dumps({
        "ts": started, "verdict": verdict, "trous": trous,
        "source": src, "agents": ag, "reconstruction": rc, "organes": org, "scelles": sc,
    }, ensure_ascii=False, indent=2))

    print(rapport)
    print(f"[drill] rapport : {RAPPORT_MD}")
    return 0 if verdict == "READY" else 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[drill] ERREUR : {e}", file=sys.stderr)
        sys.exit(1)
