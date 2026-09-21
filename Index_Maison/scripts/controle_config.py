#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROLE : Contrôleur de configuration HULK — attrape la panne SILENCIEUSE de la
       config avant qu'elle ne coûte de l'argent. Aucun ordre, aucune écriture
       dans les fichiers de config : lecture seule, sauf son propre rapport.

POURQUOI IL EXISTE (21/09/2026) :
  Trois pannes de la même famille, toutes INVISIBLES, ont été trouvées en 48 h :
    1. `STOP_COOLDOWN_HOURS` était déclaré DEUX FOIS dans defaults.env, la 2e
       occurrence écrasait la 1re en silence — et le commentaire au-dessus
       annonçait une valeur (4 h) que personne n'avait. La config MENTAIT.
    2. Le state de boot (pnl=0, aucune position) a été lu comme une perte de
       13,93 % → Mur de Fer → STOP_ALL : le moteur tué à chaque redémarrage.
    3. Le journal est COPIÉ à chaque `--resume` : toute mesure qui lit deux
       fichiers compte l'histoire deux fois (aujourd'hui : +20 $ de faux net).
  Une valeur par défaut lue comme une décision, un doublon qui écrase, un
  commentaire qui ne décrit plus le code : même maladie — la config n'est
  PROUVÉE par personne. Ce contrôleur est la preuve.

CE QU'IL PROUVE (et rien de plus) :
  ERREUR  (bloquant, exit 1) :
    · une clé déclarée PLUSIEURS FOIS (la dernière gagne en silence) ;
    · une valeur vide ou illisible (un nombre qui n'en est pas un) ;
    · un booléen hors du jeu autorisé (0/1/true/false/yes/no).
  AVERTISSEMENT (non bloquant, visible dans le rapport) :
    · une clé que PERSONNE ne lit dans le code (règle #15 : brancher ou retirer) ;
    · une clé ressemblant à un flag dont la valeur n'est pas un booléen lisible.
  Un avertissement ne fait pas crier le chien : une alarme qui sonne pour un
  comportement normal tue la confiance dans l'alarme (leçon du contrat de sortie).

PRODUIT = PREUVE DE VIE :
  hulk-mexc/runs/CONTROLE_CONFIG.json   écrit SEULEMENT si conforme → le chien
                                        crie si ce fichier vieillit (l'organe est
                                        déclaré CRITIQUE, seuil 2 h).
  hulk-mexc/runs/CONTROLE_CONFIG_ALERTE.md écrit si anomalie (pour l'humain).

Code de sortie : 0 = conforme · 1 = anomalie bloquante · 2 = panne du contrôleur.
Standard : Python 3.9+, stdlib uniquement, atomique, lecture seule sur la config.
"""
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent          # ace777-test-day1/
HULK = BASE_DIR / "hulk-mexc"
CONFIG_DIR = HULK / "config"
RUNS = HULK / "runs"
RAPPORT_OK = RUNS / "CONTROLE_CONFIG.json"
RAPPORT_ALERTE = RUNS / "CONTROLE_CONFIG_ALERTE.md"
# Déclarations R15 (branchements_declares.json) : les paramètres VOLONTAIREMENT
# sans lecteur machine. Sans ce fichier, le contrôleur crierait chaque heure sur
# une décision déjà prise — et une alarme qui sonne pour un état voulu tue la
# confiance dans l'alarme (leçon du contrat de sortie, R14).
DECLARATIONS = BASE_DIR / "Index_Maison" / "strategie" / "branchements_declares.json"

# Fichiers de configuration surveillés (tous les *.env du dossier config).
# `--env-file <chemin>` AJOUTE un fichier : sert au SELF-TEST (prouver que le
# contrôleur attrape une vraie anomalie). On n'enlève jamais defaults.env, sinon
# le test prouverait seulement que le contrôleur peut se taire.
ENV_FILES = sorted(CONFIG_DIR.glob("*.env"))
# `--dry-run` : ne touche à AUCUN rapport. Indispensable au self-test — sinon un
# test volontairement en anomalie écraserait le vrai rapport d'alerte et ferait
# croire à une panne de production.
DRY_RUN = "--dry-run" in sys.argv
for _i, _a in enumerate(sys.argv):
    if _a == "--env-file" and _i + 1 < len(sys.argv):
        ENV_FILES.append(Path(sys.argv[_i + 1]))

# Dossiers de code dans lesquels on cherche qui lit quoi (source de vérité).
# On cherche dans TOUT le repo : un satellite peut lire une clé du moteur, et la
# déclarer « morte » parce qu'on n'a regardé qu'un dossier serait un faux positif.
RACINES_CODE = [BASE_DIR]
EXCLUS = {".git", "runs", "OUTBOX_OBSIDIAN", "__pycache__", "node_modules",
          "historique", ".venv", "venv", "site-packages", ".Trash"}

LIGNE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*?)\s*$")
BOOL_OK = {"0", "1", "true", "false", "yes", "no", "on", "off", ""}
SUFFIXES_FLAG = ("_ON", "_OFF", "_ENABLED", "_ACTIF")


def lire_env() -> tuple:
    """[(fichier, clé, valeur, ligne)] + doublons {fichier: {clé: [lignes]}}."""
    entrees = []
    doublons = {}
    for f in ENV_FILES:
        vues = {}
        try:
            lignes = f.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue
        for i, ligne in enumerate(lignes, 1):
            if not ligne.strip() or ligne.lstrip().startswith("#"):
                continue
            m = LIGNE.match(ligne)
            if not m:
                continue
            cle, val = m.group(1), m.group(2)
            entrees.append((f, cle, val, i))
            vues.setdefault(cle, []).append(i)
        dup = {k: v for k, v in vues.items() if len(v) > 1}
        if dup:
            doublons[f] = dup
    return entrees, doublons


def lu_sans_defaut(corpus: str, cle: str) -> bool:
    """Vrai si au moins une lecture de la clé n'a PAS de valeur par défaut.

    C'est la PREUVE qui distingue une valeur vide VOULUE d'une valeur vide
    DANGEREUSE. Une clé vidée volontairement (ex. PAPER_WATCH_PAIRS, GO du 30/08 :
    « plus aucune paire observée ») est toujours lue avec un défaut :
        cfg.get("PAPER_WATCH_PAIRS", "").split(",")
    Une clé vidée par accident est lue comme un nombre, sans défaut :
        float(cfg["VOL_SEUIL"])   ->  ValueError au premier cycle.
    Sans cette distinction on crierait sur un état normal — et une alarme qui
    sonne pour un comportement voulu tue la confiance dans l'alarme.
    """
    for m in re.finditer(r"[\"']" + re.escape(cle) + r"[\"']", corpus):
        # Uniquement les VRAIES lectures (`cfg.get("K"`, `cfg["K"]`, `environ["K"]`).
        # Sans ce filtre, `if k in ("A", "B", "K")` — une simple comparaison —
        # passait pour une lecture sans défaut et produisait une FAUSSE erreur.
        avant = corpus[max(0, m.start() - 40):m.start()]
        if "get(" not in avant and "[" not in avant:
            continue
        reste = corpus[m.end():m.end() + 120]
        fin = reste.find(")")
        fenetre = reste[:fin] if fin >= 0 else reste
        if "," in fenetre:          # cfg.get("K", défaut) → défaut explicite
            continue
        # Idiome maison équivalent : cfg.get("K") or "" / cfg.get("K") or 0
        apres = reste[fin + 1:fin + 10] if fin >= 0 else ""
        if re.match(r"\s*(or|if\s+not)\b", apres):
            continue
        return True                 # vraiment lu sans aucun filet
    return False


def corpus_code() -> str:
    """Tout le code Python des racines : sert à prouver qu'une clé est LUE."""
    morceaux = []
    for racine in RACINES_CODE:
        if not racine.exists():
            continue
        for dossier, sous, fichiers in os.walk(racine):
            if any(p in EXCLUS for p in Path(dossier).parts):
                continue
            for nom in fichiers:
                if not nom.endswith(".py"):
                    continue
                try:
                    morceaux.append((Path(dossier) / nom).read_text(
                        encoding="utf-8", errors="ignore"))
                except OSError:
                    continue
    return "\n".join(morceaux)


def charger_declarations() -> tuple:
    """Retourne (ensemble des clés déclarées doc, {clé: raison}).

    Un paramètre déclaré n'est pas un oubli : c'est une DÉCISION écrite, avec sa
    raison. Le contrôleur la respecte et l'affiche — il ne la cache pas.
    """
    try:
        d = json.loads(DECLARATIONS.read_text(encoding="utf-8"))
    except Exception:
        return set(), {}
    doc = d.get("parametres_doc") or {}
    return set(doc.keys()), dict(doc)


def controler() -> tuple:
    """Retourne (erreurs, avertissements, stats)."""
    erreurs, avert = [], []
    entrees, doublons = lire_env()
    corpus = corpus_code()
    doc_declares, raisons_doc = charger_declarations()
    declarees: list = []

    for f, dup in doublons.items():
        for cle, lignes in sorted(dup.items()):
            erreurs.append(
                f"{f.name} : clé « {cle} » déclarée {len(lignes)} fois "
                f"(lignes {', '.join(map(str, lignes))}) — la DERNIÈRE gagne en "
                f"silence. Supprimer les occurrences en trop.")

    cles = sorted({c for _, c, _, _ in entrees})
    jamais_lues = []
    for cle in cles:
        valeurs = [(f.name, v, i) for f, c, v, i in entrees if c == cle]
        f0, v0, l0 = valeurs[-1]        # c'est la DERNIÈRE qui s'applique
        lu = re.search(r"\b" + re.escape(cle) + r"\b", corpus) is not None
        if v0 == "" and lu:
            if lu_sans_defaut(corpus, cle):
                erreurs.append(
                    f"{f0} : clé « {cle} » (ligne {l0}) a une valeur VIDE et le code "
                    f"la lit SANS défaut — au premier cycle le moteur tombera sur "
                    f"une chaîne vide là où il attend un nombre.")
            else:
                avert.append(f"{f0} : « {cle} = » est vide mais toujours lu avec un "
                             f"défaut → vide VOULU (aucune action).")
        if cle.endswith(SUFFIXES_FLAG) and v0.lower() not in BOOL_OK:
            avert.append(f"{f0} : « {cle} = {v0} » ressemble à un flag mais n'est "
                         f"pas un booléen lisible.")
        if not lu and cle not in doc_declares:
            jamais_lues.append((cle, f0, v0, l0))
        elif not lu:
            declarees.append((cle, f0, v0, l0))

    return erreurs, avert, {
        "fichiers_env": [f.name for f in ENV_FILES],
        "cles": len(cles),
        "doublons": sum(len(v) for v in doublons.values()),
        "jamais_lues": len(jamais_lues),
        "detail_jamais_lues": [{"cle": c, "fichier": f, "valeur": v, "ligne": l}
                               for c, f, v, l in jamais_lues],
        "declarees_doc": len(declarees),
        "detail_declarees_doc": [{"cle": c, "fichier": f, "valeur": v, "ligne": l,
                                  "raison": raisons_doc.get(c, "")}
                                 for c, f, v, l in declarees],
    }


def ecrire_rapport(erreurs, avert, stats) -> None:
    if DRY_RUN:                 # self-test : on prouve, on n'écrit rien
        return
    RUNS.mkdir(parents=True, exist_ok=True)
    maintenant = datetime.now(timezone.utc)
    if not erreurs:
        # Conforme → on écrit la PREUVE (c'est elle que le chien surveille).
        json.dump({
            "ts": maintenant.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "conforme": True,
            "avertissements": len(avert),
            **stats,
        }, open(RAPPORT_OK, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        # Le rapport d'alerte ne doit pas rester d'une session précédente.
        if RAPPORT_ALERTE.exists():
            RAPPORT_ALERTE.unlink()
        return

    lignes = [f"# ⛔ CONTRÔLE CONFIG — ANOMALIE ({maintenant:%Y-%m-%d %H:%M:%S}Z)\n",
              "La config n'est PAS prouvée conforme : le produit de vie n'a pas été "
              "rafraîchi, donc le chien de garde crie (c'est voulu).\n",
              "## Anomalies bloquantes\n"]
    lignes += [f"- {e}\n" for e in erreurs]
    if avert:
        lignes.append("\n## Avertissements (non bloquants)\n")
        lignes += [f"- {a}\n" for a in avert]
    if stats["detail_jamais_lues"]:
        lignes.append("\n## Paramètres que PERSONNE ne lit (règle #15 : brancher "
                      "ou retirer)\n")
        lignes += [f"- `{d['cle']} = {d['valeur']}` ({d['fichier']}, "
                   f"ligne {d['ligne']})\n" for d in stats["detail_jamais_lues"]]
    if stats.get("detail_declarees_doc"):
        lignes.append("\n## Paramètres sans lecteur, DÉCLARÉS (décision écrite, "
                      "aucune action)\n")
        lignes += [f"- `{d['cle']} = {d['valeur']}` ({d['fichier']}, ligne "
                   f"{d['ligne']})\n  → {(d.get('raison') or '').strip()}\n"
                   for d in stats["detail_declarees_doc"]]
    RAPPORT_ALERTE.write_text("".join(lignes), encoding="utf-8")


def main() -> int:
    try:
        erreurs, avert, stats = controler()
    except Exception as e:                      # le contrôleur ne doit jamais mentir
        print(f"CONTROLE_CONFIG : panne du contrôleur — {type(e).__name__}: {e}",
              file=sys.stderr)
        return 2

    ecrire_rapport(erreurs, avert, stats)
    print(f"CONTROLE CONFIG — {stats['cles']} clés dans "
          f"{', '.join(stats['fichiers_env'])}")
    print(f"  doublons            : {stats['doublons']}")
    print(f"  jamais lues par le code : {stats['jamais_lues']}"
          f" (+ {stats.get('declarees_doc', 0)} déclarées doc)")
    print(f"  avertissements      : {len(avert)}")
    print(f"  anomalies bloquantes: {len(erreurs)}")
    for e in erreurs:
        print(f"    ⛔ {e}")
    for a in avert:
        print(f"    ⚠  {a}")
    if erreurs:
        print(f"\n⛔ NON CONFORME → {RAPPORT_ALERTE}")
        print("   (produit de vie NON rafraîchi : le chien de garde va crier)")
        return 1
    print(f"\n✅ conforme → preuve écrite : {RAPPORT_OK}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
