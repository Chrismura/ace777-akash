# 🧰 ORGANES HORS REPO — comment les ramener sur une machine neuve

> Créé le **19/09/2026** (Buffy). Contexte : le drill de restauration a montré que
> **`~/prise-ia` (le HUB des providers) n'était versionné NULLE PART** — une machine nue
> ne ramenait pas l'IA de la maison. `~/mirofis` est déjà couvert par son git amont.
>
> ⚠️ **Ce dossier est un MIROIR DE SAUVEGARDE, pas une 2ᵉ source de vérité.**
> On ne l'édite JAMAIS à la main : il est régénéré par `scripts/sync_organes_hors_repo.sh`
> (appelé par `git_push_auto.sh`, toutes les 3 h) puis poussé sur GitHub.

## Ce que contient le miroir

| Organe | Chemin vivant | Mode | Détail |
|---|---|---|---|
| **prise-ia** (le HUB) | `~/prise-ia` | **miroir-source** | sources uniquement → `organes_hors_repo/prise-ia/` |
| **mirofis** (front/back) | `~/mirofis` | **git-amont** | déjà versionné sur <https://github.com/666ghj/MiroFish.git> + image Docker |

**Exclu volontairement du miroir** (jamais sur GitHub) : `.env` (clés API), `*.log`,
`*.jsonl*` (historiques), `*.bak*`, `hub.db`, `reports/`, états runtime (`heartbeat.json`,
`observatoire.json`), `node_modules/`.

## Restaurer `~/prise-ia` (le HUB)

```bash
# 1. Récupérer le repo (contient le miroir)
git clone https://github.com/Chrismura/ace777-akash.git ~/ace777-restaure
# 2. Recopier les sources du hub
rsync -a ~/ace777-restaure/Index_Maison/organes_hors_repo/prise-ia/ ~/prise-ia/
# 3. Recréer le .env (NON versionné, volontairement) — clés API des providers :
#    GEMINI · OPENROUTER · NVIDIA_NIM · INFERX · PUTER · MISTRAL · NARA · GROQ · HF · ORCA
#    (providers.json ne contient QUE des noms de variables, jamais les clés)
# 4. Relancer l'agent launchd (le plist est versionné dans Index_Maison/plists/)
cp ~/ace777-restaure/Index_Maison/plists/com.ace777.prise-ia.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ace777.prise-ia.plist
```

> Sans le `.env`, le hub démarre mais n'a aucun provider actif : **c'est la seule pièce
> à récupérer hors git** (les clés gratuites se recréent chez chaque provider).

## Restaurer `~/mirofis`

```bash
git clone https://github.com/666ghj/MiroFish.git ~/mirofis
# ou l'image déjà construite : ghcr.io/666ghj/mirofish
```

## Vérifier que la sauvegarde est fraîche

```bash
cat Index_Maison/thermo/organes_hors_repo.json     # ts = dernière synchro
python3 Index_Maison/scripts/drill_restauration.py # doit dire READY
```
