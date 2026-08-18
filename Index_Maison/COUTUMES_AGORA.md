# Coutumes de l’Agora

**Pour :** Christophe · Cursor · Gemini · Kimi · Punk · Cortana · tout nouvel arrivant.  
**Où :** ce fichier vit dans le coffre. Le chat n’est **pas** la loi.

## 1. Vérité = coffre, pas le chat
- Toute décision / ajout / retrait utile → note dans le vault + **1 ligne** dans `Swarm_Bus/09_MEMOIRE_COLLAB`.
- Si le chat disparaît, l’agora reste.

## 2. Un seul vault léger
- Coffre actif : notes **markdown**.  
- **Jamais** dans le vault : `target/`, Cargo build, `.env`, runs bruts, backups Go.  
- Code vocal : hors vault (`~/Assistant_Vocal_HORS_VAULT/`, `crypto-voice-assistant-core`).

## 3. Champion ACE intouchable
- md5 champion **jamais modifié** sans **GO humain** explicite.  
- Pas de `GO_USINE_NUAGE` sans GO.  
- Fills / CSV = juge trading, pas le récit IA.

## 4. Qui fait quoi
| Qui | Rôle |
|-----|------|
| Humain | GO, validation, risque |
| Cursor / Gemini / Kimi | Code, plans, écriture coffre |
| Punk | Veille / bullshit check → notes |
| Cortana | Lit digests / attention vocale — pas le hot path |

**Consulter la famille (avis / validation) = `python3 Index_Maison/scripts/consulter_famille.py`.**
Prompts + tasks canoniques dans `identity/prompts/famille.json`. **Ne JAMAIS improviser** :
GEMINI→`gemini.analyse`, DEEPSEEK→`deepseek.analyse`, JUGE→`juge.tranche` (le JUGE tranche APRÈS avoir lu les deux autres). Respecter la CLAUSE PERMANENTE (proposer est attendu) + le format de sortie.

**Trace auto (ne plus redemander) :** toute intervention non triviale → `python3 Index_Maison/scripts/memoire_log.py …`  
Molette / setup → `molette_log.py` (avec **pourquoi**). Règle Cursor `memoire-auto.mdc`. Toi aussi : même commande.

## 5. Ce qui est auto vs manuel
| Auto (si branché) | Manuel (GO humain) |
|-------------------|--------------------|
| Punk `check` / `suivi` → note + ligne mémoire | Lancer ACE / Hulk / Ollama |
| Scripts rapatriement **une phase** | Dire `GO B` / `GO C` / … |
| **Journal du jour + refresh [[CONSOLE_GENERALE]]** (cible hygiène) | Dire GO pour brancher le script soir |
| | Brancher plugins Obsidian |

**Rien n’est « magique 24/7 »** tant qu’on n’a pas dit GO et branché le daemon. Par défaut : **humain déclenche**.

### 5b. Hygiène quotidienne (coutume)
1. Fin de session (ou `GO journal`) : snapshot ACE / Hulk / veille → **Cahier/Journal_DATE** + maj **CONSOLE_GENERALE**.  
2. Une ligne dans **09_MEMOIRE_COLLAB**.  
3. Objectif : que ce soit **automatique** (script), mais d’abord la coutume humaine.  
4. **Cockpit (zone test)** : avant / pendant lecture run → `cockpit_hygiene_check.sh` (thermo + feed + pont Cortana). Voir [[COCKPIT_LOOK_FIGE]] · [[2026-07-30_cockpit_zone_test]].  
5. **Test avant réel** : portes hygiène → outils → run → go-no-go · anomalies dans [[JOURNAL_ERREURS_TEST]] · [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]]. **Jamais** de promote réel sans GO.  
6. **Début / fin de session** : bientôt 1 commande ([[PROTOCOLE_SESSION_DEBUT_FIN]]) — journal + OUTBOX + checks, **sans** GO trading auto.  
Voir [[AUTO_PROCESSUS]] · [[PLAN_DE_VOL]].

## 6. Hygiène Obsidian (Mac Air 8 Go)
- Graph View : **OK** si vault léger (< ~100 Mo notes). Si crash → couper Graph.  
- Après gros changement : 2–3 min stables sur `AGORA` avant la suite.  
- Vault idéalement **&lt; 100 Mo** de notes.

## 7. Index / améliorations
- Board : `Index_Maison/01_TABLEAU_VIVANT`.  
- Comptes X : `Index_Maison/Suivi_Info/COMPTES`.  
- **Brief sniff IA** : `Index_Maison/BRIEF_IA_SNIFF` (+ éval #12) — sujets à prioriser en veille (anti-overfit, frais, kill-switch, liquidité).  
- **Liens** : `Index_Maison/PROTOCOLE_LIENS` — lien seul = lecture partielle ; coller texte/images si l’essence compte.  
- **CONTRA soft** : `Index_Maison/PROTOCOLE_CONTRA_SOFT` — déroulement chat → prototype ; claim/assumption + Pass 2 manuel ; mot `GO contra`. **Pas** de cron LLM.  
- **Valeur info** : `Index_Maison/VALEUR_INFORMATION` — **A** économie (temps/RAM) · **B** $ ; scorer avant d’investir.  
- Phase 2 plus tard : scores soft, **anti-si fixes** (M5).

## 8. Nouvel arrivant (IA ou humain)
1. Lire `AGORA` + **ce fichier**.  
2. Lire `09_MEMOIRE_COLLAB` (dernières lignes).  
3. Lire `BRIEF_IA_SNIFF` si tu fais de la veille / recherche.  
3b. Lire `PREFS_STACK` (ex. Kimi = pref API agents).  
3c. **Consulter la famille** = `scripts/consulter_famille.py` (jamais improviser les prompts).  
4. Ne rien lancer qui chauffe le Mac sans demander.  
5. Écrire ce qu’on touche.  
5b. Compte X validé → **auto** `COMPTES` + éval + mémoire (pas reporter).

## 9. Stacking functions (esprit permaculture)
Une action est **meilleure** si elle sert **plusieurs** buts d’un coup (hygiène + réalisme + Index + RAM…).  
Les IA du swarm : à chaque job non trivial → livrer + **vérifier** si une petite amélioration stacke + **proposer** en 1–3 lignes (sans diluer, sans GO trading implicite).  
Exemple : démarrer Hulk paper **et** seed 20$ tokens → on teste aussi la vente baissière.

---

*Coutume &gt; prompt improvisé.*

## 🔗 Connexions

- [[MEMOIRE_COLLAB]] — MEMOIRE_COLLAB
- [[INDEX_COMMANDES]] — INDEX_COMMANDES
- [[01_TABLEAU_VIVANT]] — 01_TABLEAU_VIVANT
- [[14_AUDIT_TROIS_JAMBES_SWARM]] — 14_AUDIT_TROIS_JAMBES_SWARM
- [[09_MEMOIRE_COLLAB]] — 09_MEMOIRE_COLLAB


Lien carte : [[OSSATURE]] — séparé mais relié.
