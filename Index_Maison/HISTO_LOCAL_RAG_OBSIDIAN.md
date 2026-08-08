# Pointeur — Local RAG Obsidian + Ollama

**Statut :** 🔵 WATCH · **après** Pack A P2 / Mac froid  
**Source :** [@ridark_eth](https://x.com/ridark_eth/status/2082433601384096219) (« Claude + Obsidian + Nvidia = $5k Local RAG ») + guide `OLLAMA_ORIGINS`  
**Valeur :** A2 (mémoire notes) · B0

## Idée
RAG local = Obsidian cherche dans le vault par **sens** (embeddings) via Ollama — notes restent sur le Mac.

## Chez Christophe (Mac Air 8 Go)
- **Utile :** fix Origins + plugin léger (ex. Smart Connections) + embed petit modèle  
- **Pas :** build Nvidia 5k$ · indexer tout pendant ACE  
- Scope v1 : vault `Obsidian_ACE777` / Index froids, par paquets  

## Fix Mac (si plugin n’indexe pas)

```bash
launchctl setenv OLLAMA_ORIGINS "app://obsidian.md,*"
```
Puis quitter/relancer Ollama (barre de menu).  
**Pas pendant** un run ACE qui dépend d’Ollama.

## Même famille — « vault qui s’écrit » (seeco / 8 règles)

Source : https://x.com/seeconvm/status/2077355292128379331  

Esprit utile : 1 inlet · raw sacré · liens > notes isolées · synthèse hebdo · contexte session.  
**Chez nous déjà :** Index / Attention / OUTBOX / `MEMOIRE_COLLAB` / ossature.

**Anti-overdose (jugement Cursor) :**  
- **Pas** de 2ᵉ cerveau parallèle ni auto-écriture libre dans le vault.  
- Si un jour GO : 1 fichier règles vault qui **pointe** [[OSSATURE_INDEX]] (éditer canons, pas créer des dumps).  
- RAG (Origins + plugin) = v1 possible ; « vault auto » = **plus tard / optionnel**, seulement si ça reste fluide.

## Quand
Après fin Pack A P2 + Mac froid · GO explicite « RAG Obsidian » (pas « vault auto » d’office).

## Liens
[[INDEX_COMMANDES]] · [[PREFS_STACK]] · [[HISTO_RESEARCH_DESK]] · Ollama déjà installé
