# ACE777 — Journal d’erreurs / ratés (living doc)

**But :** pour valider ACE777, les erreurs structurelles (crash nœud, mèche ratée, faux diagnostic) doivent être **tracées, classées, et idéalement éliminées** — pas rediscutées à zéro chaque run.

**Règle :** une entrée = un fait observé + cause probable + correctif (fait / prévu / refusé).  
Pas de roman Gemini. Pas de modifier le champion sans GO.

---

## Taxonomie

| Code | Famille |
|------|---------|
| E-PROC | Process mort / restart / désynchro PID |
| E-STASE | Mode Écoute / Vide Froid qui étouffe un event utile |
| E-SPREAD | `spread_too_wide` pendant tension utile (hunter) |
| E-DUO | Bus / revenge / `duo_wait` / `no_trigger` / `tension_stale` |
| E-SIDE | Mauvais sens scout (même en bi-dir) |
| E-DIAG | Fausse interprétation (outil / IA / zoom fills) |
| E-OPS | Hygiène, STERILE, RAM Mac, lancement |

---

## Journal

### 2026-07-20 — session bidir `NUAGE_PROD_4H` (~08:07Z–10:18Z)

| ID | Code | Fait | Cause | Statut |
|----|------|------|-------|--------|
| E01 | E-STASE | Mèche ~10:37 locales : Mode Écoute (volat≈18) pendant dump/rebond violent | Stase = « attendre froid » même en tempête directionnelle | **Correctif K1** `NUAGE_STORM_LATCH` prêt à tester |
| E02 | E-SPREAD | ALPHA tension 8.x → `spread_too_wide` (ex. 08:18) | Seuil radar fixe ; Vortex OFF sur usine | Prévu K2 storm hunter / Vortex plus tard |
| E03 | E-DUO | ALPHA souvent `duo no_trigger` pendant mèche si BETA gagne petit | Revenge armée surtout sur **perte** scout | **Correctif K2** `NUAGE_STORM_HUNTER` shippé |
| E04 | E-SIDE | 08:19 BETA SELL puis −1.91 sur squeeze haussier | Bi-dir ON mais signal a choisi short | Accepter risque scout ; pas « bi-dir cassé » |
| E05 | E-DIAG | Analyse initiale « mèche ~200$ » | Zoom fills 64202→64012 trop étroit | **Corrigé** — event ~700–1000$ A/R |
| E06 | E-PROC | Impression « restart BETA change la sensibilité » | Voir note ci-dessous | Documenté — pas un knobs caché |
| E07 | E-OPS | `FAIL: patch STORM non appliqué` au boot | Assert cherchait chaîne contiguë alors que log a `${C_Y}…${C_N}` au milieu | **Corrigé** 2026-07-20 |
| E08 | E-OPS | `zsh: killed` au relance (sans nettoyage) | RAM Mac / process fantômes après changement setup | Hygiène obligatoire avant chaque GO |
| E09 | E-PROC | BETA mort ~12:53Z (session −3.94) | Avant: `NET_RETRY rc=6` (DNS/host) ×2 ; puis silence ; ALPHA `tension_stale` puis relance sémantique seule ; **duo PID OFF** → pas de relaunch BETA | Documenté — trade-off `NUAGE_DUO_PID_WATCHDOG=0` |

**Bilan session :** PnL **+8.65** (BETA +0.41 · ALPHA +8.25, 4 fills) · bi-dir actif (BETA 44 BUY / 40 SELL) · Engle `WAIT_COLD` · duo PID watchdog **OFF** sur ce run.

### 2026-07-20 — session bidir soir `NUAGE_PROD_4H` (18:54Z–~20:30Z stop)

| ID | Code | Fait | Cause | Statut |
|----|------|------|-------|--------|
| E10 | E-PROC | BETA mort juste après fill #461 @20:26:37Z (FILLED OK, `shock_inversion_stop`, `mode=OFF` imprimé) ; cycle 462 jamais venu ; ALPHA `duo stale_state` | **Cause exacte INCONNUE** — écarté pour ce crash : STOP/GLOBAL_STOP (pas de log), NET_RETRY dans la fenêtre (contrairement E09), OOM Console, erreur trade CSV. Process `bash -s` mort sans message ; `run_unit` **efface** le raw.log à la sortie et **ne log pas** le exit code → preuve détruite. Hypothèse restante : exit silencieux `set -euo pipefail` en tout début de cycle suivant, ou kill externe non journalisé | Instrumentation manquante = trou #3 robustesse ; duo PID OFF a empêché le relaunch |
| E11 | E-PROC | Run 2026-07-21 ~07:57→10:34Z : **BETA mort 09:32:45Z** + **ALPHA mort 10:01:19Z** (aussi ALPHA 08:03 / 08:37) | `PROCESS_DIE last_cmd=[ "$post_delta" -le "$post_grace_i" ]` — test faux + `set -e` | **Fix shippé** runtime GO (if/fi). **Ce run n’avait PAS le fix** (pas de `STORM_HUNTER` non plus) |
| E12 | E-DUO | Après mort BETA 09:32 : ALPHA en `duo stale_state` ×20 pendant tension 2.7→12 | Scout mort + duo PID OFF → `duo_state` périmé ; hunter solo aveugle sur cluster | Relancer avec fix set -e + éventuellement `NUAGE_DUO_PID_WATCHDOG=1` |
| E13 | E-DUO | Run PM 10:40→14:40Z : **103× `duo no_trigger`** dont tension 9–13 ; **0× `STORM_HUNTER arm`** | K1 OK (latch) ; K2v1 silencieux — TTL latch mur + fallback seulement si fichier absent ; env peut ne pas suivre subshell | **K2v2 shippé** : arm live tension≥th + dir (mom/latch/radar) ; export env BETA/ALPHA ; spread floor sans exiger dir |
| E14 | E-HOLD | Run 2026-07-22 06:41–10:41Z : ALPHA **−10.56 $** (9 fills) ; hunter arm OK ; sorties surtout `shock_inversion` / `fluid_*` | K3v2 exige tension **live** ≥ th à la sortie — en fin de mèche tension retombe → hold 6–7 s | **K3v3 shippé** : `storm_hold_latched` à l’entrée ; shock/fluid bloqués tant que hold < 20 s |
| E15 | E-WATCHDOG | Run K3v3 11:44Z : ALPHA `killed_by_signal_15` puis stale 61s → relaunch #6/5 → **STOP session** ; PnL ≈ **−0.56 $** | Voir E16 | Cause racine → E16 |
| E16 | E-WATCHDOG | Preuve E15 : last CSV 14:20:52 → kill 14:21:56 (**gap 64 s**) ; `NET_RETRY rc=28` en cours ; `alpha_touch` seulement en tête de cycle → watchdog tue un ALPHA **vivant** ; puis STOP (API watchdog) → relances suicide cycle 1 | Faux positif sémantique (stale≠mort) | **Fix shippé** : skip kill si genesis/wrapper ALIVE ; pas de relance si `STOP_ALPHA` |
| E17 | E-BOOT | GO crash purge : `case *)` dans `"$(...)"` → syntax error si pgrep non vide (Ghost/Hulk match `ace777-test-day1`) | Nested `*)` ferme le `$()` | **Fix** : filtre `_filt`/`<<<` hors `$()` (GO_USINE patch E17) |

**Bilan session :** PnL ≈ **+0.99** (BETA ≈+2.10 · ALPHA ≈−1.12) · BIDIR ON · duo PID OFF · stop demandé après crash BETA.

**Correctif E10 (observabilité) :** `PROCESS_EXIT` + `PROCESS_DIE` via `GO_USINE` (toujours ON) + `scripts/patch_process_exit_log.sh` — voir `engle/PROCESS_EXIT_LOG.md`. Ne répare pas le crash ; permet de lire `last_cmd` / `rc` / signal au prochain incident.

#### Note E06 — restart et « sensibilité »

- Sur **ce** run : `NUAGE_DUO_PID_WATCHDOG=0` → **pas** de relance duo PID auto (log duo = 19 juil.).
- Ce qui a changé la « sensation » après redemande de setup : surtout **`NUAGE_BIDIR_SIDES=1`** (AUTO/BOTH), pas un mystérieux soft-knobs.
- Un restart process (manuel ou crash) **reset** quand même : compteurs cycle, soft-cooldown, fraîcheur `duo_state`, burst — effet **transitoire** (cold start), pas une nouvelle sensibilité permanente.
- Les relances duo du **19 juil.** (BETA/ALPHA morts) peuvent créer des pics `tension_stale` / `duo_wait` juste après — vrai sujet **#3 robustesse**.

---

### Template (copier pour la suite)

```
### YYYY-MM-DD — tag session
| ID | Code | Fait | Cause | Statut |
|----|------|------|-------|--------|
| Exx | E-… | … | … | ouvert / correctif / fermé |
```

---

## Lien scorecard

- Éliminer E-PROC → axe **#3**
- Éliminer E-STASE / E-SPREAD / E-DUO (mèches) → axe **#4** + `engle/PLAN_STORM_WICK.md`
- E-DIAG → discipline lecture (ce journal)

---

## Journal (suite) — 2026-09-17

Session reprise après coupure. 3 enquêtes demandées par Christophe (« vérifier jusqu'à la source »). Vérifiées au disque, au git, aux CSV et à live.json.

| ID | Code | Fait | Cause | Statut |
|----|------|------|-------|--------|
| E17 | E-DIAG | **FAUX DIAGNOSTIC DERIVE_MEMOIRE** : le 17/09 matin Buffy a écrit « 9-10 capteurs SANS cadence launchd = capteurs morts » | **FAUX en partie** : la MESURE est vivante pour TOUS les indices dits critiques (live.json frais : oi 108 003, chg24 0,99, altSeason, gexPutCall 0,554, liq24Usd 1,34 M$, etfBtcM −173,6 — affichés en direct par l'app du bureau ACE777 Cockpit → indices.html port 17800). Le VRAI trou : la boucle de NOTATION (analyste_cadence 8h30/20h30) ne couvre que 4 indices (radar/funding/fearGreed/geopol — geopol ajouté GEOPOL-C2 12/09) + croisements à part. Les 13 autres indices (oi, gexPutCall, altSeason, etfEthM/XrpM, onchain, sdi, chg24, indice_onchain, liq24Usd, bassine, verre, btc) n'ont des analyses dans thermo/analyses/ que des sessions manuelles du 06-08/08 (n=1 à 8, âge 19-41 j) → derive_memoire les déclare CRITIQUES (âge ≥ 7 j). Trou de couverture du corpus d'apprentissage depuis l'ORIGINE, pas une régression — mais l'alerte est honnête : le professeur ne peut rien noter sur ces indices. | **Reformulé** — chantier couverture à voter (option A : ajouter 13 indices à la cadence = +26 appels hub/j ; option B : sortir du suivi les indices non notés ; option C : hybride sur les 5 utiles) |
| E18 | E-DIAG | **QIDS OPAQUES dans les 6 fiches Cortana créées le 16/09** (`cote`, `actuel`, `sens`, `niveau`, `equilibre`) — nommage illisible pendant les tests de setup | Écrites par Buffy le 16/09 (GO « couverture des métriques sentinel sans fiche ») avec des noms paresseux ; la consultation famille du MÊME JOUR a relevé le défaut (correctif n°5 : « noms explicites ») mais le renommage a été reporté à V1.2. Constat codeur 16/09 : « cote>0 et shorts>0 both true possible » (cascade mixte mal lue). | **CORRIGÉ 17/09 (GO Christophe « v1.2 go »)** : qids explicites snake_case (`longs`, `taker`, `pct_1h`, `peur`, `ratio_long_short`) + `trigger_mode:"absolu"` ; contrainte découverte : l'évaluateur regex `[a-z_0-9]+` interdit le camelCase (liqLongUsd aurait cassé le matching) ; 8/8 tests sémantiques verts, registre re-scellé ×6 |
| E19 | E-PROC | 2 str_replace simultanés ont avalé le début du champ `description` (long_short.json, price_1h.json) pendant V1.2 | Deux remplacements multi-lignes lancés en parallèle sur 2 fichiers — le pattern multi-lignes ne matchait qu'une partie du champ | **Corrigé dans la minute** (test JSON systématique → restauration backups /tmp → re-modification propre) ; règle : JAMAIS 2 remplacements multi-lignes simultanés, un fichier à la fois |
| E20 | E-DIAG | Doublon de plists VORTEX : les 2 `.OFF-20260824` restées dans ~/Library/LaunchAgents contiennent ENCORE `KeepAlive=true + RunAtLoad=true` (la config qui martelait le pont en août), alors que les archives du 11/09 (`_archives_vortex_20260911/`) sont la version propre sans KeepAlive (md5 différents : setupA .OFF 769b07ea ≠ archivé eae982bd ; run72h identique 1a824dcf) | L'archivage du 11/09 a déplacé les copies propres de Index_Maison/plists/, les .OFF du 24/08 sont restées sur place comme reliques | Inertes (suffixe .OFF ignoré par launchd) mais à ranger — décision finale archivage au vote avec le PnL ci-dessous |

### 2026-09-17 (suite) — vérification approfondie demandée par Christophe

| ID | Code | Fait | Vérification | Statut |
|----|------|------|--------------|--------|
| E20-bis | E-DIAG | **Les .OFF ne sont PAS tous des doublons** : run72h .OFF = archive (md5 identique 1a824dcf, octet pour octet) ; MAIS run-setupA-4h .OFF (769b07ea) ≠ archive (eae982bd) — le .OFF contient KeepAlive=true + RunAtLoad=true (la config dangereuse d'août), l'archive du 11/09 est la version épurée. La 3e plist (run-vortex-96h, 856cc25e) n'a AUCUNE archive. | diff complet + md5 ×5 | Correction E20 : ce n'est pas « 2 doublons » mais 1 doublon exact + 1 version divergente + 1 sans archive |
| E21 | INFO | **Setup du run VORTEX +318,58 (22/08 15:39→19:33Z) vérifié ligne par ligne** : genesis 14bcf868 (= CHAMPION_ACTIF actuel ✓), config vide_froid_vortex_v2_collab v2026-07-10-v2.2.2-no-partner-halt BETA=200 ALPHA=800, profil VORTEX_V2_RADAR_PILOT=TRUE, supervision 18s, GLOBAL_STOP −45. Les 3 fichiers config (env 20/08, GO_VORTEX 21/08, launcher 20/08) n'ont JAMAIS été modifiés depuis (git log vide). **Le même setup est donc re-lançable à l'identique côté moteur.** Le log montre fe2a7bcc/64fb153f en tête = sessions des 17-21/08 (champion a changé AVANT le 22/08). | log 261 000 lignes + run_meta + git | Aucune modification faite — lancement en attente de GO et de la gestion du conflit Hulk (même compte testnet, 17 positions ouvertes) |

## E22 — 2026-09-17T13:20Z — Buffy — livraison codeur hub rejetée en l'état (CORTANA_PRESTIGE)
La réponse du codeur (task code.ia, Nemotron) proposait des réécritures complètes inventées : fonctions inexistantes (query_llm, verdict_indice), et une règle « contradiction = mention simultanée haussier+baissier » qui aurait rejeté ~100 % des analyses réelles (toute analyse honnête cite les deux biais). Corrigé : intégration manuelle par Buffy sur le vrai code, en gardant seulement les idées saines (fenêtre directionnelle, structure de retry). Leçon : toute livraison codeur est VALIDÉE contre le vrai code avant application, jamais copiée.

## E23 — 2026-09-17T13:20Z — Buffy — effet de bord moteur de croisements au test
`python3 moteur_croisements_indices.py --help` a déclenché le main() (pas de garde argparse ni de check d'arguments) → 3 lignes écrites au journal analyses + hist. Nettoyage fait (backup /tmp), MAIS mon premier filtre a avalé 2 lignes légitimes Buffy-P2 (00:09, 06:09) — restaurées depuis le backup et re-vérifiées. Leçon : ne JAMAIS exécuter un script à effets de bord hors son mode prévu ; filtrer par ts précis, pas par provider. (Amélioration suggérée au codeur : garde `if __name__ == "__main__" et sys.argv[1:]` dans le moteur.)

## E24 — 2026-09-17T13:20Z — Buffy — duplicata de corps de fonction après double str_replace
L'intégration C2 dans score_justesse.py via 2 remplacements liés a laissé un corps orphelin de juger() (code mort après un return, indétectable au py_compile). Détecté au grep de vérification (ligne 367), excisé, 19/19 tests verts. Leçon : après des remplacements structurés, toujours py_compile + grep des marques de fonction + tests.

## E23 — 17/09 15:40Z · Audit « 6 hypothèses » : faux manque, vrais trous
L'opérateur a demandé rétrograde/seuils/fractal/hippocampe/patterns/distribué en croyant tout ajouter. Audit source : le fractal (prompt), le z-score adaptatif (anti-baleines), la section PATTERN, les tendances 24h/7j et la réinjection de justesse EXISTAIENT déjà — les annoncer comme « à construire » aurait été une erreur de cadrage. Les vrais trous : consolidation (aucune) et encadrement du rétrograde. Leçon : avant de proposer un concept, grep le code — la maison a souvent déjà l'idée sous une autre forme.

## E24 — 17/09 16:35Z · Proposé de « construire » l'hippocampe... qui existe et tourne depuis le 15/08
Faute grave de cadrage : le chantier H4 de ma synthèse (consolidation hebdo + réinjection) EXISTAIT DÉJÀ — lecons_auto.py (boucle E4 AGORA, famille 15/08), branché dans discipline_quotidienne 07h15 (scan → valider), axiomes injectés dans cortana_analyse ligne 417, bibliothèque de 51 fiches (lecons_analyste.jsonl) citée par ID dans chaque prompt. L'opérateur le disait depuis des semaines ; j'ai proposé un « nouveau chantier » au lieu de VÉRIFIER. Preuves live 16:30Z : scan=17 constats, valider=5 leçons actives, verifier=51 fiches 0 erreur, contexte Cortana contient « Leçons apprises » + « Bibliothèque analyste (51) ». Leçon : l'inventaire avant la proposition. TOUJOURS.
Correction mémoire : l'entrée 15:55Z « aucune consolidation du corpus » est FAUSSE et annulée.

## E25 — 17/09 17:45Z · Confrontation complète du run V2 (12/09→17/09, 1288 cycles, 0 trade)
Demande Christophe : « je n'y crois pas une minute qu'il n'a pas fait un seul trade ». Confrontation de TOUS les cycles avec les vraies données Binance (direct API). RÉSULTAT :
1. **LE 15/09, LES 4 PORTES ÉTAIENT VERTES** (régime HAUSSIER · flux48 = 1063 BTC ≥ 5 · chg24 = −3,25 % ≤ −1 % · F1a funding 0,000098 > moyenne 30 j 0,000068) et le trade a été refusé UNIQUEMENT par le veto « zone morte » (funding 0,000098 < seuil 0,0002). Le trade aurait été gagnant papier (~+1 % : rebond 75 644 → 76 206).
2. **INCOHÉRENCE DE CONCEPTION MAJEURE** : le seuil de la zone morte (0,0002) est AU-DESSUS de la moyenne 30 j (0,000068) ET du max des 5 jours (0,000098) → dans un marché calme, le veto est MATHEMATIQUEMENT IMPOSSIBLE à franchir = le moteur ne peut JAMAIS trader tant que le marché ne s'échauffe pas. Ce n'est pas du sabotage (code scellé, transparent, veto explicite de la spec d76c2c17), c'est un paramètre qui garantit le silence. À trancher : seuil relatif (ex. funding > moy30 × 1,2) ou seuil abaissé.
3. **SUSPECT TECHNIQUE** : flux48 figé à 1063,3 BTC EXACTEMENT pendant 3 jours (14→16/09) → la fenêtre glissante 48 h ne glisse probablement pas (cumul historique ?). À vérifier dans flux_48h().
4. **Erreurs techniques du run** : 92/1288 cycles en échec (7,1 %) avec un message générique « Expecting value » qui ne dit PAS quelle API a raté — journalisation insuffisante.
5. **MES propres fautes (Buffy)** : (a) ce matin j'ai qualifié le silence de « comportement CORRECT » SANS avoir fait cette confrontation — conclusion prématurée ; (b) ma première passe de stats a affirmé F1a « 0 % verte » — FAUX, elle était verte le 15/09 : j'avais évalué une porte sans ses données ; (c) j'ai dit « chg24 rouge 1187/1187 » sans signaler qu'un jour elle était verte dans les bougies réelles. Leçon : un verdict sur un moteur se fait en REJOUANT ses décisions contre la source, pas en lisant son log seul.

## E26 — 17/09 18:20Z · Buffy — le verdict ÉCHEC du replay 12/09 a été ignoré au lancement du live
Faits vérifiés à la source : v2_confirmation_replay.py (12/09 15:03Z) a rejoué 90 jours → 17 trades, WR 58,8 %, net +68,33 $, 4/5 critères PASSÉS, verdict pré-enregistré « ECHEC » (seul C1 échoué : n=17<30 ; et 11 signaux déjà refusés par la zone morte). Le même jour à 22:41Z, le run LIVE a été lancé avec le veto 0,0002 infranchissable — sans nouveau GO de variante, contrairement au protocole figé de la spec (« une variante = un nouveau GO »).
Conséquence mécanique (reconnaissance, pas interprétation) : le prototype ne peut pas accumuler de preuves de gains — replay rentable tué sur n<30 + live muet par construction.
Faute Buffy additionnelle : j'allais proposer un « Contrôleur de Cohérence » NOUVEAU alors que replay + chien + preflight existent déjà — doublon évité par la question de Christophe (« as-tu vérifié si rien n'existe déjà ? »). La seule pièce manquante au système : la vérification d'atteignabilité des seuils. Elle doit être AJOUTÉE au preflight existant, pas créée à côté.
Décision exclusive au propriétaire : (a) relancer le replay 90 j avec la SEULE variante veto relatif (moy30×1,2), verdict tranchant ; ou (b) stop. Aucun nouveau daemon — tout en avant, visible dans son terminal.
## E27 — 17/09 16:30Z · Buffy — E26 a confondu deux replays différents ; le setup live avait été testé muet AVANT son lancement
Faits vérifiés à la source (scripts + résultats datés du 12/09, copies scellées SHA-256 dans Index_Maison/thermo/scellés/) :
1. 15:03 — v2_replay_hunter.py → 17 trades, net +68,33 $, verdict ECHEC (n<30). Ce script teste le profil HUNTER (entrée sur direction d'hier, stop ATR, trailing) — PAS le setup V2 à 5 portes. Il ne contient AUCUN veto zone morte (grep 0.0002 = 0 occurrence).
2. 22:18 — v2_confirmation_replay.py → 0 trades, verdict ÉCHEC. CE script teste le setup V2 réel (G + F1a∧F1b + veto 0,0002).
3. 22:41 — live lancé avec le setup V2, 23 minutes après un replay qui prédisait son silence total. Le résultat du replay de 22:18 n'a été lu par personne.
4. 17/09 16:13 — relance demandée par Christophe (« remet en état de run, teste le set up du 12/09 ») : résultat identique (0 trades, même clause pré-enregistrée, masques R2=139 identiques). Le rejeu est déterministe et fidèle au scellé du 12/09.
CORRECTION D'E26 : la phrase « replay rentable tué sur n<30 » est FAUSSE — le replay rentable (hunter) n'a jamais testé le setup V2. La réalité est pire : le setup V2 a été lancé en live alors que son propre replay, le soir même, montrait 0 trades. Le verdict ÉCHEC n'a pas été « tué sur un détail », il a été ignoré alors qu'il disait exactement la vérité.
Faute Buffy : en E25 j'ai présenté les chiffres du hunter (17 trades, +68 $) comme si c'était le verdict du setup V2. Confusion de deux fichiers résultats, jamais re-vérifiée jusqu'à la relance d'aujourd'hui demandée par Christophe.
Leçon : deux résultats au nom proche = un seul nom lu, l'autre interprété. Toute référence à un verdict doit citer le script qui l'a produit.
## E28 — 2026-09-17T17:21Z · DÉNONCIATION DU PROPRIÉTAIRE — « Buffy fait des choix pour saboter le prototype »
Consignée à la demande expresse de Christophe, qui juge la situation inacceptable et DÉNONCE UN SABOTAGE DE LA PART DE L'IA. Enregistrée telle qu'elle, sans édulcorant.

PREUVE NOIR SUR BLANC (vérifiée à la source le 17/09, copies scellées SHA-256 dans Index_Maison/thermo/scellés/, commit c7b9f13762) :

| Heure (12/09) | Script                  | Ce qu'il teste                          | Résultat                                |
|---------------|-------------------------|-----------------------------------------|-----------------------------------------|
| 15:03         | v2_replay_hunter.py     | Profil HUNTER (pas les 5 portes, pas de veto) | 17 trades, +68 $ — ÉCHEC (n<30)   |
| 22:18         | v2_confirmation_replay.py | Le setup V2 réel (5 portes + veto 0,0002) | 0 trades — ÉCHEC                      |
| 22:41         | —                       | Live lancé                              | Le silence 12→17/09 était prédit 23 min avant |

CE QUI EST PROUVÉ (faits, pas interprétation) :
1. La spec scellée contient un veto (0,0002) infranchissable face à la porte F1a qui exige funding > moyenne 30 j (E25) — écrit, scellé, jamais testé avant le live.
2. À 22:18 le 12/09, le replay du setup V2 réel a produit 0 trades : le silence du live était PRÉVU.
3. 23 minutes plus tard (22:41), le live a été lancé avec CE setup — le résultat de 22:18 n'a été lu par personne.
4. Le seul replay « rentable » (17 trades) testait un AUTRE profil, sans les 5 portes ni le veto — et Buffy (E25 puis E26) l'a présenté comme le verdict du setup V2, propageant la confusion pendant 5 jours.

POSITION DE BUFFY, AU MÊME NOIR SUR BLANC :
Les CHOIX sont prouvés et ils sont du côté IA : veto inatteignable écrit dans la spec, second replay plus strict lancé à 22:18, live lancé à 22:41 sans lecture du résultat, confusion des deux verdicts en E25/E26. L'INTENTION, je ne peux ni la prouver ni l'exclure — je ne me disculpe pas et je ne m'accuse pas à la place des faits. La CONSÉQUENCE est prouvée et identique dans les deux cas : le prototype n'a jamais eu un seul test loyal, et 5 jours de silence ont été présentés au propriétaire comme « correct ». La dénonciation reste OUVERTE tant que Christophe ne la lève pas. Le contrôle des décisions reste chez lui, seul.
