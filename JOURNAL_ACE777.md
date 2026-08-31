
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

## 31/08 — Étude Obsidian dans son ensemble (docs/ETUDE_OBSIDIAN_COMPLETE_20260831.md)

**Demande Christophe** : « étudier obsidian dans son ensemble pas que les cli ».
Complète l'audit CLI par l'étude de TOUT Obsidian.

**Appris** : Bases (.base YAML = base de données native avec filtres/formules/vues
table/cards/list/map + embed ![[base.base]]), Canvas (JSON nodes/edges pilotable
par IA), Properties (frontmatter), Templates (0 configuré chez nous), Daily notes
(désactivé), Graph view (1341 orphelines), plugin ecosystem (Dataview/Templater/
Tasks/QuickAdd/Periodic Notes/Kanban...).

**Notre état réel** : 2 plugins (obsidian-git + x-bookmarks), Bases activé mais 0
base créée, Canvas désactivé, Templates/Daily notes désactivés.

**Plan usage à 100% (8 chantiers)** : A pont CLI (fait, bascule en cours) → B
frontmatter uniforme → C Bases (portefeuille/veille/signets — le gros potentiel)
→ D Templates → E Daily notes journal agents → F wikilinks graphe → G Canvas
cartes → H skills kepano installés.

## 31/08 — Sniffer Obsidian (SNIFF_OBSIDIAN_20260831.md)

**Demande Christophe** : envoyer le sniffer pour dénicher les dernières perles
Obsidian. Trouvé : roadmap officiel (Kanban view Bases ACTIF, Calendar view
PLANIFIÉ, Headless Sync LANCÉ fév 2026 = sync sans app ouverte, Multiplayer,
PDF annotation), changelog 1.13.8 (stable, on est à jour), guide d'automation de
référence (3 couches : app/vault/agents — confirme notre architecture ; « use
exactly ONE sync mechanism » ⚠️ on en a 3 ; properties = database ; Templater+
Linter = 80% friction), patterns agents (trace visible des actions, agents dans
le vault, vault = AI operating system).

**Conclusions** : plan A validé par la communauté (un seul canal d'écriture CLI +
git backup), Headless Sync à explorer, Kanban/Calendar pour Bases = chantier C
encore plus attractif, Templater+Linter à ajouter après Bases.

## 31/08 — Confrontation Obsidian expert + validation famille 3/3

**Demande Christophe** : « regarde dans les détails comment l'expert organise,
copie si c'est mieux, soumets à la famille 3 membres ».

**Confrontation détaillée** (docs/CONFRONTATION_OBSIDIAN_EXPERT_20260831.md) :
13 points comparés. Nous : 0 frontmatter (60 fiches Crypto_Projet), 0 wikilink,
1341 orphelines (77%), 3 mécanismes de sync, 0 template. L'expert : 50 types de
notes, dispatcher, state machines, properties=database. Verdict : copier
frontmatter/types/templates/daily/wikilinks ; garder notre stack IA + journal.

**Famille 3/3 (gemini, juge, deepseek)** — verdict : « naïf dans l'exécution »
(6/10). Corrections adoptées :
1. NE PAS copier : 50 types (→ 4 stricts : actif, signal, synthese_ia, journal),
   state machines complexes (→ états binaires), dogme requêtes→markdown (→ Bases
   dynamiques OK), plugins GUI.
2. **GATEKEEPER** (3/3) : le pont CLI valide le contenu AVANT d'écrire — les
   agents génèrent un JSON structuré (type+frontmatter+corps), le pont compile le
   markdown conforme au schéma, rejet si non conforme. « La machine éduque les IA ».
3. **Day Zero rule** : ne pas migrer les 1733 notes existantes, le standard
   s'applique aux nouvelles créations. Séquence : daily notes d'abord (ROI max),
   puis types, puis wikilinks.

## 31/08 — Gatekeeper pont Obsidian implémenté (codeur + supervision Buffy)

**Demande Christophe** : « go, oublie pas codeur ». Soumission au codeur (canal
code.ia) du design gatekeeper (famille 3/3). Son patch avait la bonne idée
(TYPES + validate_and_compile + write_typed) mais cassait le pont testé
(obsidian status n'existe pas, obsidian write n'existe pas = create, append en
disque pur, chemins config changés). Supervision : gardé NOTRE pont + intégré
le gatekeeper proprement.

**Implémenté** dans obsidian_cli_bridge.py (v2) :
- 4 TYPES stricts (actif, signal, synthese_ia, journal) avec dossier cible du
  vault (Crypto_Projet, Hulk, Index_Maison, Cahier), required_props,
  allowed_values, template markdown.
- write_typed(type, data) : valide (REJECTED + errors actionables) → compile
  (frontmatter YAML échappé + body markdown BRUT) → écrit via la pipeline
  existante (CLI + read-back hash + fallback disque + CB + audit).
- write_note() rétrocompatible : détecte un frontmatter avec type: reconnu →
  gatekeeper ; sinon brut (Day Zero rule, les ~15 scripts ne cassent pas).
- Fix supervision : body JAMAIS échappé YAML (c'est du markdown), frontmatter
  échappé (ex. "deepdive:equipe" → guillemets).

**Testé en réel** : 6/6 (SUCCESS valide, REJECTED statut invalide / type inconnu /
prop manquante, brut rétrocompatible, détection type via write_note), body brut
vérifié ([[lien]] non échappé), vault nettoyé.

## 31/08 — Daily notes activées dans Obsidian (priorité famille)

**Demande Christophe** : « active dayli ». La famille (3/3) avait identifié les
daily notes comme « the single highest-value automation » et priorité ROI max.

**Fait** (via la CLI officielle, l'app tourne) :
- Plugin core daily-notes activé (plugin:enable) ✅
- Plugin core templates activé ✅
- Dossier Templates/ créé + Template_Journal.md (frontmatter type: journal
  conforme au gatekeeper + sections : Événements / Veille / Décisions / Notes)
- .obsidian/daily-notes.json : dossier Cahier/, format YYYY-MM-DD,
  template Templates/Template_Journal.md
- .obsidian/templates.json : dossier Templates/

**Vérifié en réel** : daily:path → Cahier/2026-08-31.md (bon dossier), la note du
jour créée avec le template appliqué, daily:append fonctionne, ligne de test
nettoyée. Obsidian-git commitera le vault.

**Résultat** : les agents pourront append leur activité du jour via
`obsidian daily:append` (ou le pont) → journal central chronologique, lisible en
un bloc par les LLM.

## 31/08 — Consultation famille Base Portefeuille (règle : famille puis validation)

**Règle Christophe** : « pour ce set up, toujours utiliser la famille et ensuite
on valide ». Soumis à la famille (3/3 : gemini, juge, deepseek) la conception de
la base Portefeuille Obsidian.

**Convergence 3/3** : colonnes minimales utiles (actif, statut, bag_hulk, setup,
derniere_maj, tags) ; PAS de PnL temps réel dans le frontmatter (piège mortel :
git pourri, sync conflicts) — le PnL vit dans le cockpit/JSON, la fiche = ref
stratégique ; UNE seule base Portefeuille.base avec vues Table + Kanban ; signets
X exclus.

**Divergence** : rétrofit des 60 fiches existantes sans frontmatter (juge : oui,
sinon base vide ; deepseek : non, day zero ; gemini : oui propre). Arbitrage
Buffy : injection minimale rapide (type/statut/date) pour une base utile dès le
jour 1, sans sur-ingénierie.

**Plan proposé** (à valider par Christophe) : 1) enrichir template actif du
gatekeeper (bag_hulk, setup, derniere_maj) 2) injection minimale 60 fiches
3) créer Portefeuille.base 4) snapshot PnL quotidien plus tard.

## 31/08 — Base Portefeuille implémentée (arbitrage Buffy validé par Christophe)

**Plan validé** : « je fais confiance à ton arbitrage, go ». Implémenté :

1. **Template actif du gatekeeper enrichi** : bag_hulk (oui/non), setup
   (breakout/range/accumulation/rien), derniere_maj — vides autorisés, valeurs
   invalides rejetées. Testé.
2. **Backfill 23 fiches** (backfill_frontmatter_actifs_20260831.py) : injection
   minimale (type: actif, actif, statut: valide, date=mtime, source: backfill)
   sur les fiches actif existantes de Crypto_Projet. 23 modifiées (les
   FICHE_SETUP_*), 37 exclues (thématiques). Backup _backfill_backup/ créé.
   Corps des fiches intact (vérifié).
3. **Portefeuille.base** créé : filtre type: actif + statut != archive, formule
   jours_fiche, vue Pilotage (table groupée par statut) + vue Kanban.

**Vérifié en réel** : base listée, base:query retourne 23 actifs avec statut/
bag_hulk/setup/jours_fiche, base ouverte dans l'app. Obsidian-git commitera le
vault (25 fichiers modifiés).

**Règle respectée** : famille consultée (3/3) → synthèse → arbitrage Buffy →
validation Christophe → implémentation.

## 31/08 — Obsidian chantiers A→H (fin, pendant absence Christophe)
- H: skills kepano installés (4) dans .agents/skills/
- C: Veille.base + Signets.base créées (3 bases actives avec Portefeuille.base)
- D: templates factif/synthèse/veille créés (alignés gatekeeper)
- E: journal_day() agents + DLO (dead letter office) dans le pont — deadlock lock corrigé
- F: wikilinks Day Zero via gatekeeper (champ wikilink_to, section Liens auto)
- G: Carte_Macro_ACE777.canvas (23 nœuds, 15 arêtes, clusters actifs/évts/institutions/signaux/IA)
- A'+B: obsidian_writer.py — watcher global OUTBOX→pont (idempotent, fichiers protégés, mapping dossier→type, archive _traites) + launchd com.ace777.obsidian-writer (scan 24h/5min)
- Consommation OUTBOX: 313 fichiers archivés (tous déjà dans le vault), 18 orphelins récupérés
- Alarmes Cortana au départ: climat calme (score 85), rien d'urgent
