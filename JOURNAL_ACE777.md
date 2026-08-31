
## 30/08 22:50 — FIX : ETH sans seed (tableau à 0)
- Diagnostic : ETH (banc de preuve, ajouté 27/08) n'avait JAMAIS eu de SEED_START → colonne bag du début = 0 au cockpit, ligne classée "observe" → son +0,37$ du 28-30/08 (BUY 2449 → SELL 2495, trailing) invisible dans le score.
- Cause : le label "banc_de_preuve" de universe_profils.json n'est pas lu par le moteur (seul PAPER_OBSERVE_PAIRS bloque) → ETH était tradable sans seed. Décision Christophe : ETH TRADABLE + seed 10$ comme les 19 autres.
- Action : seed injecté (état : pos ETH 10$ @ 2497.44 seed:true, cash 19.96→9.96) + ligne SEED_START ajoutée au CSV. Redémarrage moteur via watchdog launchd (--resume, positions tenues). Vérifié : 14 pos + ETH, trades 34.

## 31/08 — FIX JUSTESSE : ZONE MORTE FUNDING + ANTI-FUITE (GO Christophe)
Christophe a creusé le score de justesse de Cortana qui descendait (50.0%). Audit complet :
- **Cause racine** : le funding est collé à sa valeur neutre (0.0001 = 0.01%/8h) sur TOUTE la base (7 693 points, 88% exactement à 0.000100, jamais > 0.0001). Vérifié à la source Binance : il bouge réellement (0.000059→0.000100) mais dans une bande minuscule = AUCUNE information directionnelle. Ce n'est pas une panne, c'est un indice muet.
- **Le bug était dans la notation** : on notait des NEUTRE sur un indice sans signal → MISS systématique quand BTC bouge >0.3% (8 NEUTRE depuis le 16/08 → 7 MISS). Le funding tirait le score global vers le bas injustement.
- **FIX implémenté (score_justesse.py v2)** :
  1. ZONE MORTE : funding < 0.0002 (0.02%) = signal inexistant → analyse NON NOTÉE (ni HIT ni MISS). Décidée par la DONNÉE, pas par l'analyste → pas d'échappatoire possible (même un LONG affirmé n'est pas noté).
  2. ANTI-FUITE : compteur de NEUTRE émis quand le signal EXISTE. Si >60% des avis → alarme « évitement » dans justesse_cockpit.json + affichage cockpit.
  3. NEUTRE reste noté quand le signal existe (HIT si plat, MISS si ça bouge).
- **Résultat** : score global 50.0% (59/118) → **54.5% (48/88)**. Funding retiré du score (toute la base en zone morte). Compteur anti-fuite : 37/145 = 25.5% → pas d'alarme (Cortana n'esquive pas actuellement).
- **Tests** : 14 tests hermétiques tous verts (dont 5 nouveaux : zone morte, exclusion du score, anti-fuite, hors-funding non affecté).
- **Cockpit** : carte JUSTESSE affiche désormais le taux NEUTRE-avec-signal + alarme rouge si fuite + règle zone morte.
- **Prompt Cortana** (cortana_analyse.py) : consigne gravée — zone morte = non noté (décidé par la donnée), pas de refuge, compteur anti-fuite actif.
- **Leçon (encore)**: quand un score descend, creuser l'INDICE pas seulement la chaîne. Un indice collé à sa valeur neutre depuis des semaines aurait dû être détecté avant. C'est Christophe qui l'a trouvé.

## 31/08 — AUDIT INDICES + FIX RAPPELS VOCAUX + COCKPIT ONGLET (GO Christophe)
1. **AUDIT muet-silence autres indices** : funding = SEUL indice muet (97% sur une valeur, déjà corrigé). Les autres sont sains (oi, longShort, score, chg24, takerRatio, topTraderLS, liq, etfBtcM varient). fearGreed se répète car métrique journalière (62 aujourd'hui) = NORMAL, pas un bug.
2. **POUSSIÈRE à 50 SANS VOIX** : diagnostiqué — l'alerte poussiere_cpfp a bien sonné (journal 08:22Z, score 50 + CPFP), mais le fichier **STOP_ALERTE global (créé 10:31) a coupé la boucle vocale**. Score actuel redescendu à 10 (< seuil 45) → plus de déclenchement. veille_signal est bien planifiée (launchd). NON un bug de déclenchement : c'est le STOP_ALERTE.
3. **FIX RAPPELS VOCAUX (alerte_vocale.py)** : la boucle répétait le même message toutes les 30s SANS différencier. Désormais : lecture initiale = l'alarme ; chaque répétition = précédée de "Rappels. " → on sait que c'est la MÊME alerte qui se répète, pas un nouvel événement.
4. **FIX COCKPIT ONGLET (index.html)** : le reload auto (quand la version du cockpit change) ramenait toujours au 1er onglet (OPS) et en haut. Désormais on sauvegarde onglet actif + scrollY avant reload, et on les restaure au chargement. Vérifié syntaxe JS (node).

## 31/08 — AUDIT CPFP/POUSSIÈRE : 2 BUGS STRUCTURELS CORRIGÉS (GO Christophe)
Christophe a trouvé le CPFP « bizarre » (hier et aujourd'hui : score poussière qui oscille 50/35/10, alarmes qui partent pour rien). Audit à la source (detecter_cpfp.py → pont_onchain.py → veille_signal.py) :
- **BUG 1 — le score poussière affiché = bruit sur 10 tx** : carte3.score = ratio de poussière dans l'échantillon /mempool/recent (10 transactions) × 50. En frais bas, l'échantillon tombe souvent 9-10/10 poussière → score 50 → ALARME. Puis l'échantillon change → score 15. Le VRAI signal (cumul 48h ≥ 1000, carte3.declenche = 1109 aujourd'hui) n'était PAS utilisé par l'alerte.
- **BUG 2 — « signature CPFP » toujours vraie** : veille_signal testait `z >= 3.0` sur le score NORMALISÉ 0-100 (71.8 pour z réel 3.59) → condition vraie quasi en permanence → faux URGENT (poussiere_cpfp) même sans CPFP confirmé (carte2).
- **FIX** :
  1. pont_onchain.py expose `cpfpDustDeclenche` (cumul), `cpfpCarte2` (signature CPFP par frais), `cpfpZReel` (z réel = score/20) — les vraies données.
  2. veille_signal.py : le déclencheur poussière = SEUL le cumul 48h (cpfpDustDeclenche). Le ratio 10-tx n'est plus qu'affichage. sig_cpfp (URGENT) = carte2 ou signal confirmé — plus jamais le z normalisé.
- **Tests** : 5 cas simulés tous OK (cumul+CPFP→URGENT ; cumul seul→WATCH ; bruit 50/50 sans cumul→AUCUNE alerte ; champ manquant→AUCUNE). Pipeline réelle rejouée : aujourd'hui = WATCH (cumul 1109, pas de carte2) — avant le fix c'était un faux URGENT.
- **Verdict Christophe confirmé** : hier et aujourd'hui c'était le MÊME artefact — un échantillon de 10 tx qui criait 50/50. Le vrai cumul (1109 ≥ 1000) est déclenché mais c'est un WATCH sans CPFP, pas un URGENT.

## 31/08 — FIX ADA : seuil liquidations CALIBRÉ (GO Christophe)
ADA criait « FEUX DE L'ORAGE : liquidations massives » alors que zone VERT (voilure 86%). Audit :
- **Donnée réelle** : liq24h = 53,6 M$ (accumulation du petit crash du 30/08, 2,5M→53,5M dans la journée) — mais PAS massif : percentile 87, max historique 141 M$, médiane 7j 35,8 M$.
- **Bug** : seuil STATIQUE 50 M$ dans ada_gardienne.py (déclencheur + normalisation pression storm qui sature à 100% dès 50 M$). Sonnait sur un jour normal (28/08 : 54,7 M$).
- **FIX** : seuil RELATIF = max(médiane 7j × 1,5, plancher 80 M$), via médiane_liq_7j() (thermo/history.jsonl). Pression storm normalisée sur la même référence.
- **Résultat** : 53,6 M$ → plus de sirène (au-dessus de la moyenne, pas massif). Vrai pic 141 M$ → sirène. Simulé avec données réelles : SIRÈNE=False, déclencheurs=[]. 19/19 tests hermétiques verts (dont 2 nouveaux : 53M→non, 141M→oui).
- **Balayage autres seuils fixes de la maison** : les restants sont sains — sat/vB et tailles BTC = unités absolues physiques (légitimes), z=3σ = statistique (relatif par construction), funding déjà relatif (3×moy30). Les 3 vrais bugs du jour (funding, CPFP, liquidations) étaient des seuils absolus appliqués à des échelles qui dépendent du régime de marché.

## 31/08 — Phase 3 moteur léger : satellite aspiration + 2 bugs corrigés

**Contexte** : GO Christophe « observe et si c bon, go phase 3 ». Observation ~10 min : Phases 1+2 validées (CPU 0-4%, RSS stable, 0 erreur réseau, 16 positions tenues).

**Phase 3 implémentée** :
- `scripts/satellite_aspiration.py` : satellite autonome (pattern short_btc validé) qui sonde l'aspiration/murs des 5 paires actives + BTC, écrit `runs/aspiration_live.json` en atomique. Launchd `com.ace777.satellite-aspiration` (StartInterval 20s).
- Bascule réversible `ASPIRATION_SRC=fichier|inline` dans `hulk-mexc/config/defaults.env` + fallback inline si fichier absent/stale (>45s).
- Le cœur lit le fichier au lieu de sonder le carnet → 0 appel depth dans le cœur.

**Bug pré-existant corrigé** (découvert pendant la validation) : `regime referenced before assignment` dans `maybe_enter` — utilisé dans les logs des chemins de retour CB (stale) avant son assignation → NameError sur ces chemins → paire non évaluée. Assignation en tête + `sc.get`. Absent des logs depuis le fix.

**Bug introduit par la bascule corrigé** : CB BTC TTL=10s mais satellite écrit toutes les ~29s (StartInterval 20s + ~9s d'exécution mesurée) → circuit ouvert en boucle (faux positif, Hulk ne traderait plus). TTL aligné sur la fenêtre de fraîcheur réelle du fichier (45s), même principe que le fix GEX 27/08.

**Validé en réel** : 16 positions reprises (resume), cb:CLOSED, 0 stale, 0 regime, CPU 3.4%, RSS 19MB, contexte frais.

**Commit** : à venir

## 31/08 — Pont CLI Obsidian : installé + validé famille 3/3 + implémenté

**Contexte** : signet X du jour (@KanikaBK) sur la CLI officielle Obsidian (v1.12+).
Vérifié réel : binaire obsidian-cli v1.13.7 présent, activé dans Settings > General >
Advanced par Christophe, testé create/append/read/tags sur le vault ACE777.

**Consultation famille (gemini, juge) + codeur — 3/3 avis** : plan validé (8/10) avec
4 corrections : queue séquentielle (Obsidian mono-thread), timeout 3s + read-back hash
(ne pas faire confiance à exit code 0), fail-open absolu (disque = socle, CLI = couche
notification), circuit breaker 3 échecs/15 min + audit jsonl. Rejeté : obsidian search
pour valider (lent), plugin REST API (tiers), URI scheme.

**Implémenté** : `Index_Maison/scripts/obsidian_cli_bridge.py` — pont séquentiel
(verrou global), timeout 3s, create+read-back hash, append, fallback écriture directe
dans le vault, circuit breaker, audit `.ace777_bridge_audit.jsonl`.

**Testé en réel** : SUCCESS_CLI (create+read-back OK), fallback disque (app morte →
SUCCESS_FALLBACK), concurrence 5 écritures sans crash, audit complet. Vault nettoyé.

**Suite** : additif, rien n'est basculé — on laisse le pont tourner en parallèle avant
de remplacer les écritures OUTBOX_OBSIDIAN des synthèses.

## 31/08 — Audit usage Obsidian + étude CLI à 100% (docs/AUDIT_OBSIDIAN_CLI_20260831.md)

**Demande Christophe** : « analyse comment on utilise obsidian, étudie comment
l'utiliser à 100%, va sur github faire une formation, trouve des améliorations ».

**Audit** : vault 1733 notes/117MB, 2 plugins (obsidian-git OK, x-bookmarks),
1341 notes orphelines, daily notes non activé, 0 base. Point faible = synchro
manuelle OUTBOX→vault (~15 scripts, 323 fichiers en attente, liste de cp fragile
= source des bugs « Obsidian ne bouge pas »).

**Formation trouvée** : kepano/obsidian-skills (GitHub, 19.1k★, CEO Obsidian) —
5 skills officiels (markdown, bases, canvas, cli, defuddle). CLI testée en réel :
search/read/create/append/property:set/tags/eval (JS dans l'app !)/bases/orphans/
recents/commands/plugin:install/diff — tout fonctionne.

**Améliorations identifiées** : A) remplacer la synchro manuelle par le pont CLI
(priorité 1, déjà lancé), B) frontmatter uniforme sur les fiches, C) Bases Obsidian
(portefeuille/veille en base de données), D) daily notes agents, E) hygiène graphe
(wikilinks), F) skills officiels pour nos IA, G) cockpit→Obsidian.
