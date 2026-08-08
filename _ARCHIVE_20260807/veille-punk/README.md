# ◆ VEILLE PUNK — IA de recherche (gratuite)

Terminal coloré **+** IA locale **Punk** (Ollama `qwen2.5:3b`).

## Lancer
```bash
/Users/christophe/ace777-test-day1/veille-punk/launch.sh
```

## Check
```bash
check "https://x.com/..."
check "texte du tweet"
```

Chaque `check` :
1. Analyse (avec `CONTEXTE_PUNK.md`)
2. Sauve `out/CHECK_*.md`
3. Écrit Obsidian `Swarm_Bus/Punk/` + bus `07_PUNK_VEILLE.md`
4. Enrichit le log dans `CONTEXTE_PUNK.md` (mémoire pour les prochains checks)

