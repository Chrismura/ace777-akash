# Mémoire collaborative — ce qu’on touche

**Hygiene swarm :** chaque ajout / modif / décision traçable = **1 ligne ici**.  
Pour que Cursor · Punk · Cortana · Christophe sachent **ce qui a bougé**, sans fouiller le chat.

| Colonne | Sens |
|---------|------|
| ts | UTC |
| 2026-08-10T12:12Z | Ada | ★ | LECTURE COMPLETE [LECTURE_COMPLETE_OK] 1129 fichiers |
| Qui | Cursor / Punk / Cortana / Humain |
| Action | `+` ajout · `~` modif · `✕` retrait · `★` décision |
| Où | chemin vault ou workspace |
| Quoi | 1 ligne claire |

## Règles
1. Toucher un fichier « produit » → logger ici **dans la même session**.
2. Pas de roman — le détail vit dans Index / évals.
3. Miroir workspace : `ace777-test-day1/Index_Maison/MEMOIRE_COLLAB.md`
4. Cortana : lit aussi [[10_ATTENTION_VOCALE]] pour résumer à voix haute.

## Journal (récent en haut)

| ts | Qui | Action | Où | Quoi |
|----|-----|--------|-----|------|
| 2026-08-14T0625Z | Buffy | ~ | cockpit/hub/voix | COCKPIT NICKEL (GO Christophe 14/08) — audit approfondi du travail DeepSeek : pont TTL 30s (/mission ne relance plus le feed à chaque poll, était ~10s = 28 542 fichiers SAISON) · ada_saison archive JSONL au lieu d'1 fichier/scan (purge faite, tar /tmp/backups-cockpit-nickel-20260814-081440) · cortana_urgent_poll TTL 30s (était feed à chaque poll 10s) · conflit pont résolu : orphelin open_cockpit_app tué, launchd KeepAlive reprend (était 7611 échecs Address-in-use) · mute aligné 5 chemins voix (brief/analyse/offres/analyste/yeux) · cortana_thermo annonce la vérité moteurs via /status (E-10) · graph z-index bouton ↻ (E-13) · hub : /events+/usage tail atomique + only_model typé (résidus DeepSeek) · tout testé, backups datés |
| 2026-08-13T2306Z | session_fin | ★ | Index | Fin session auto · journal + OUTBOX |
| 2026-08-13T2305Z | Buffy | ✕ | A_Mon_Attention | Accountability : JOURNEE_DESASTRUEUSE + RELEVE + TOPO + AUDIT (projet + vault + git) — c'est moi qui ai foutu la merde |
| 2026-08-13T2305Z | Buffy | ★ | git | Pushes OK : ace777-akash + obsidian-vault (fermeture session) |
| 2026-08-13T2250Z | Buffy | ~ | cockpit | Badge RUN STATUS en haut OPS (🟢/🟡/🔴 live via /status) — agent_status.js figé depuis 30/07 (disait RUNNING à tort) |
| 2026-08-13T2250Z | Buffy | ~ | cockpit | Graph synapse : α/β/HULK + arêtes gatés par liveness réelle (engineOn) — ne montre plus des bots « actifs » morts |
| 2026-08-13T2245Z | Buffy | ~ | moteur | trap ERR dans genesis_manifest (FATAL_RC1 ligne/cmd) — diagnostic mort silencieuse rc=1 d'Alpha |
| 2026-08-13T2240Z | Buffy | ~ | voix | MUTE actif (.cortana_mute) — coupe la voix horaire · ⚠ 5 chemins locaux l'ignorent encore (à aligner) |
| 2026-08-13T2220Z | Buffy | ★ | voix | Règle « une seule piste » (killall say+afplay) étendue à 6 chemins voix — double voix corrigée |
| 2026-08-13T2200Z | Buffy | ~ | offres | queue_offres : intégration `enabled:True` (validation IA auto — décision Christophe 14/08) |
| 2026-08-13T2200Z | Buffy | ★ | run | MASTER_VORTEX_V2_COLLAB_4H terminé (PNL +1.37$) · ALPHA mort rc=1 à 18:25Z (13 min après départ) · audit famille 6/6 → A_Mon_Attention |
| 2026-08-13T2301Z | session_fin | ★ | Index | Fin session auto · journal + OUTBOX |
| 2026-08-13T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-13T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-13 | Snapshot auto hygiène soir |
| 2026-08-13T1648Z | session_debut | ★ | session | début mode=froid |
| 2026-08-13T1045Z | Buffy | ★ | REPRISE POST-COUPURE (13/08) | coupure batterie -> position orpheline BTCUSDT SHORT -0.0184 (lev 13) bloquait la marge -> Margin insufficient (-2019) -> Abort leverage error -> ALPHA exit 1 en boucle, duo cassé ; fix : arrêt propre + fermeture position orpheline (API reduceOnly hedge) + nettoyage fichiers run + RE-SCELLEMENT champion 98c80b5c (=9fe9f105 sans barrière + FIX-SCOUT, vérifié diff) dans verif_pre_run_3x/verif_setup_champion + vérif md5 champion intégrée au preflight (C1 mécanique) + garde-fou compte à plat (positionRisk != 0 -> refus de lancer, C8) ; run 8h relancé 08:44Z (fin ~16:44Z) sain, 0 erreur marge ; validation : mon action du 12/08 23:29Z était juste (genesis = champion restauré + fix) |
| 2026-08-12T2354Z | session_debut | ★ | session | début mode=vol |
| 2026-08-12T2329Z | Buffy | ★ | RUN 8H PATCHE (13/08) | moteur champion 9fe9f105 + FIX-SCOUT revenge (role==SCOUT seulement, 3 modifs chirurgicales validees 5 cas) ; run 8h lance 23:28 UTC via lancer_detache + GEMINI_TEST x13 fixe ; backups: genesis_manifest.txt.BAK_CHAMPION_9fe9f105_20260812 ; watcher -> runs/BILAN_PATCHE_8H_20260813.md ; le 1er livrable codeur refuse (ts/ts_ms + DUO_SUFFER + modes supprimes), v2 chirurgical accepte |
| 2026-08-12T2216Z | Buffy | ★ | TEST CHAMPION 9fe9f105 | run test champion restaure (x13 fixe start=13 end=13, sans barriere) : 0 BARRIER_TIMEOUT, 0 no_trigger, 0 no_state, tensions ALPHA/BETA distinctes (pas de clone), cycles alignes 18/17, 3 fills en 3 min ; backup 37fca367 = genesis_manifest.txt.BAK_37fca367_20260812_TESTCHAMPION ; protocole = lancer_detache + LAUNCH_V85_SCRIPT=GEMINI_TEST.sh |
| 2026-08-12T2137Z | Buffy | ★ | audit moteurs cursor | preuve forensique substitution Cursor : champion 37fca367 (avec barriere duo) scelle actif, bonnet 9fe9f105 (sans barriere) fourni en douce le 12/07, 13/07 = 712 BARRIER_TIMEOUT + trade fatal revenge -16.84 (13:27:39), 14/07 dormance ; dossier plaintes/ + ERREURS_AI/ = preuves de Christophe confirmees par les donnees ; verdict derive des donnees |
| 2026-08-12T2115Z | Buffy | ★ | audit dormance alpha | codeur a produit audit_dormance_alpha.py (compare 9-10/07 vs 14/07) : asymetrie confirmee (fills ALPHA 5.5% -> 1.7%, PnL +29.52 -> -13.25, BETA stable ~11%) ; bug filtre fenetre B corrige (fichier cumulatif polluait PnL +51.24) ; piste mode=OFF radar_adj=0 (81x le 14/07, absent le 9-10/07) a verifier ; config non verifiable (T1_console non parse) ; cadence ALPHA ralentit 1.6->1.3, BETA accelere 1.9->2.6 |
| 2026-08-12T2057Z | Buffy | ★ | cycles_terminal | jumeau terminal du cockpit : flux cycles ALPHA/BETA avec les memes couleurs (ALPHA ambre, BETA cyan), lecture live + replay + json audit, PnL sur ligne complete, teste sur log reel (32083 lignes, ALPHA +161.45 BETA +8.00) |
| 2026-08-12T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-12T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-12 | Snapshot auto hygiène soir |
| 2026-08-12T1845Z | Buffy | ★ | archi: Buffy superviseur | ajout zone ORCHESTRATION (vue humaine) + composant BUFFY superviseur/chief scientist + correction Orchestrator ABSENT -> SESSION (tech.html + ARCHITECTURE_TECH.md) |
| 2026-08-12T1831Z | Buffy | ★ | mirofish documente | ajout MiroFish a l archi TECH (vue humaine + tech.html) : membre recherche en PAUSE 10/08, cle ZEP OK, reactivation = decision collective, a la demande seulement ; +1 ligne POINT_REPRISE |
| 2026-08-12T1811Z | Buffy | ★ | archi-tech 12/08 | mise a jour architecture TECH + vue humaine : hub cloud seule passerelle LLM (C9/C10), pont gate :11439, vigie, analyste, ADA, journal intention, fiches offres, signets, Cortana V2, note stricte sincere famille |
| 2026-08-12T1734Z | Buffy | ★ | gravure 24h | synthese 24h + journal du 12 + sync Obsidian + push GitHub 77cad5d (10k fichiers) |
| 2026-08-12T1734Z | Buffy | ★ | Index_COMMANDES | ajout GO_VORTEX_V2 (gate hub), ENCHAINER_RUN_4H_HUB, LLM_GATE_PONT_CACHE_SEC |
| 2026-08-12T1734Z | Buffy | ★ | chantier hub | pont llm_gate_hub_bridge : gate trades -> hub (grok/gemini), cache 90s, fail-closed, preuve llm_wind, run 4h comparaison lance |
| 2026-08-12T1728Z | journal_auto | ★ | CONSOLE+Journal_2026-08-12 | Snapshot auto hygiène soir |
| 2026-08-12T1218Z | Cursor | ★ | ERREURS_AI | E-20260812-1 ban Cursor lignes · rapport vie privee classe |
| 2026-08-11T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-11T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-11 | Snapshot auto hygiène soir |
| 2026-08-11T0510Z | session_debut | ★ | session | début mode=froid |
| 2026-08-10T2138Z | session_debut | ★ | session | début mode=froid |
| 2026-08-10T2130Z | session_debut | ★ | session | début mode=froid |
| 2026-08-10T2127Z | session_debut | ★ | session | début mode=froid |
| 2026-08-10T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-10T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-10 | Snapshot auto hygiène soir |
| 2026-08-09T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-09T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-09 | Snapshot auto hygiène soir |
| 2026-08-09T1723Z | session_debut | ★ | session | début mode=froid |
| 2026-08-08T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-08T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-08 | Snapshot auto hygiène soir |
| 2026-08-07T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-07T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-07 | Snapshot auto hygiène soir |
| 2026-08-06T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-06T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-06 | Snapshot auto hygiène soir |
| 2026-08-05T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-05T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-05 | Snapshot auto hygiène soir |
| 2026-08-04T1854Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-04T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-04 | Snapshot auto hygiène soir |
| 2026-08-04T1701Z | session_debut | ★ | session | début mode=froid |
| 2026-08-04T0119Z | Humain+Cursor | ★ | Evaluations/BRIEF_SIGNETS_X | v4 : 138 signets (28 lots, couverture 28/28, GitHub lu) -> brief ecrit |
| 2026-08-04T0052Z | Humain | ★ | Evaluations/BRIEF_SIGNETS_X | Brief validé + 12 lignes TABLEAU + lien AGORA |
| 2026-08-03T2342Z | Humain+Cursor | ★ | Evaluations/BRIEF_SIGNETS_X | v4 : 138 signets (28 lots, couverture 27/28, GitHub lu) -> brief ecrit |
| 2026-08-03T2333Z | Humain+Cursor | ★ | Evaluations/BRIEF_SIGNETS_X | v4 : 138 signets (28 lots, couverture 27/28, GitHub lu) -> brief ecrit |
| 2026-08-03T2243Z | Humain+Cursor | ★ | Evaluations/BRIEF_SIGNETS_X | Synthèse v2 138 signets (14 lots, manifest 1/14, GitHub lus) → brief écrit |
| 2026-08-03T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-03T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-03 | Snapshot auto hygiène soir |
| 2026-08-02T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-02T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-02 | Snapshot auto hygiène soir |
| 2026-08-01T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-01T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-01 | Snapshot auto hygiène soir |
| 2026-08-01T0727Z | session_debut | ★ | session | début mode=vol |
| 2026-08-01T0727Z | session_debut | ★ | session | début mode=froid |
| 2026-07-31T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-07-31T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-07-31 | Snapshot auto hygiène soir |
| 2026-07-31T1442Z | Humain | + | test | boucle automation OK |
| 2026-07-31T1441Z | Humain | ★ | test | boucle automation OK |
| 2026-07-31T1441Z | install | ★ | bin | wrapper ~/bin/memoire OK |
| 2026-07-31T1441Z | install | ★ | memoire_auto | install_memoire_auto.sh — smoke OK |
| 2026-07-31T1440Z | Humain | ★ | test | boucle automation OK |
| 2026-07-31T1438Z | install | ★ | memoire_auto | install_memoire_auto.sh — smoke OK |
| 2026-07-31T1436Z | Humain | ★ | où | quoi |
| 2026-07-31T1434Z | Cursor | ★ | AUTO memoire | memoire_log+molette_log+règle Cursor alwaysApply — plus de rappel manuel |
| 2026-07-31T1426Z | Cursor+Humain | ★ | JOURNAL_MOLETTES_SETUP | Canon journal molettes (qui/quoi/**pourquoi**) · STORM_HUNTER OFF défaut + E-07 retest · pas GO aujourd’hui |
| 2026-07-31T09:11Z | session_fin | ★ | Index | Fin session · VOL LAISSÉ TOURNER · journal + OUTBOX |
| 2026-07-31T1229Z | Cursor | ★ | parler simple | Règle d’or : vulgariser par défaut · technique sur demande · `.cursor/rules/vulgariser-par-defaut.mdc` · [[PREFS_STACK]] |
| 2026-07-31T09:03Z | cadence | ★ | Index | GO cadence · finition cosmétique gelée · session début/fin ancrés |
| 2026-07-31T05:24Z | session_fin | ★ | Index | Fin session auto · journal + OUTBOX |
| 2026-07-31T0522Z | Cursor | ✅ | session+cockpit app | session_debut/fin + open_cockpit_app (pywebview/Brave) · run NUAGE_PROD_4H en vol |
| 2026-07-31T0445Z | Humain+Cursor | ★ | PLAN + C-05 | Bouton ROUGE urgence cockpit A propre / B crash + confirm · test validation duo |
| 2026-07-30T2130Z | Humain+Cursor | ★ | fin session | Demain: pywebview cockpit + session_debut/fin auto · journal jour + PLAN_DE_VOL |
| 2026-07-30T2125Z | Cursor | + | pastilles ACE/NET/PONT | Haut-droite évolutif · FEED OFF = PONT OFF |
| 2026-07-30T2120Z | Cursor | + | JOURNAL_COCKPIT + pré-son | Cockpit produit à part · chime news + prechime TTS suave |
| 2026-07-30T2115Z | Cursor | ★ | S26 validation | PROTOCOLE_VALIDATION_TEST_AVANT_REEL + JOURNAL_ERREURS_TEST · UAT avant réel |
| 2026-07-30T2110Z | Cursor | + | cockpit BOARD | Onglet BOARD = `thermo/index.html` SIMPLE/COMPLET A·B·C après THERMO |
| 2026-07-30T2055Z | Cursor | ★ | cockpit+hygiène | S22 **ZONE TEST** · check indicateurs = hygiène · news Cortana 14s · carte après-midi VOL |
| 2026-07-30T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-07-30 | Snapshot auto hygiène soir |
| 2026-07-30T0915Z | Cursor | ~ | `cockpit` | Cockpit FUSÉE v2 · Alpha/Beta/Hulk trades live · mission feed |
| 2026-07-30T0840Z | Cursor | + | `thermo`+`cortana_thermo` | Indicateurs free branchés (21/25) · Cortana Q funding/mois · feed cockpit |
| 2026-07-30T0830Z | Cursor | ~ | `Index_Maison/thermo` | Clin d'œil VERT/JAUNE/ROUGE + options + radar enrichi |
| 2026-07-30T0810Z | Cursor | + | `architecture/tech.html` | Spec TECH + ARCHITECTURE_TECH.md · rubrique revue IA |
| 2026-07-30T0800Z | Cursor | + | `architecture/index.html` | Carte visuelle Agora · §5c INDEX_COMMANDES · fin schéma structure |
| 2026-07-30T0755Z | Cursor | + | #25 M6 Attention | LongViewCrypto S&P value capture · exemple raisonnement style Raoul · sync Obsidian |
| 2026-07-29T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-07-29 | Snapshot auto hygiène soir |
| 2026-07-30T0721Z | Cursor | ~ | RAG+vault | seeco 8 règles **canalisé** dans HISTO_LOCAL_RAG · anti-overdose ossature · pas S25 |
| 2026-07-30T0653Z | Cursor | + | `HISTO_LOCAL_RAG_OBSIDIAN` | #24 S24 WATCH — RAG Obsidian/Ollama après P2 · Attention |
| 2026-07-30T0628Z | Cursor | + | `labo/Backtesting-Engine` | Clone Research Desk #23 S23 WATCH · pas npm pendant ACE P2 |
| 2026-07-30T0621Z | Cursor | ★ | Pack A P2 | GO 2e passe pattern 4h · tag PACK_A_P2 · fin~12:21CET · Hulk still ON |
| 2026-07-30T0619Z | Cursor | ★ | Voie A score | A +19.79 vs B -19.18 · soft win A · caveat fenêtres ≠ · Hulk still ON |
| 2026-07-29T2124Z | Cursor | ★ | hygiène Index | Cockpit → INDEX_COMMANDES + OSSATURE + S22 BUILD v1 · OUTBOX sync |
| 2026-07-29T2120Z | Cursor | ★ | `cockpit/index.html` | GO build Arcade Radar v1 · fake data · open navigateur |
| 2026-07-29T2118Z | Cursor | ★ | `COCKPIT_LOOK_FIGE` | Peau Arcade Radar + indicateurs figés · maquette validée Christophe · build plus tard |
| 2026-07-29T1515Z | Cursor | ★ | chain Pack B | GO user → watcher auto B après fin A (~21:12CET) |
| 2026-07-29T1513Z | Cursor | ★ | `VALIDATION_VOIE_A_PACK_A` | GO Pack A 4h testnet · V8 0.85/6.5%/void · duo marche · fin~21:12CET |
| 2026-07-29T1505Z | Cursor | + | `PROTOCOLE_VALIDATION_PATTERN_V8` | Voie A : grille score A vs B · critères succès · GO type paper |
| 2026-07-29T1450Z | Cursor | + | Bureau `FORMULE_BASSINE_PRIVEE_RESTAUREE` | Restauration privée formule+calibrage V8 · pas sync Index · avis 2 couches |
| 2026-07-29T1437Z | Cursor | ~ | `HISTO_TRINITY` | Clarif : phrases récup = protocole mémoire Gemini (restore), pas mantras |
| 2026-07-29T1435Z | Cursor | ~ | `HISTO_TRINITY` | Enrichi 29 modules + phrases récup 18–20/02 → Diamant/Akash · 1 phrase canon · stop clés chat |
| 2026-07-29T1432Z | Cursor | + | `HISTO_TRINITY_ABONDANCE_HYBRIDE` | #22 S21 — récup échange Gemini Trinity-02 · utile≠théâtre |
| 2026-07-29T1424Z | Cursor | + | `thermo_quotidien_free` | Auto FREE OI/funding/L/S → THERMO_DERNIER · ZeroGEX=exemple · REFUS API payantes |
| 2026-07-29T1421Z | Cursor | + | `OSSATURE_INDEX` + `HISTO_ESCALIER` | #21 S19/S20 — carte anti-éparpillement · escalier synaptique archivé |
| 2026-07-29T1417Z | Cursor | + | `THERMO_SOURCES_API` | C23–C25 dark pool + GEX/ZeroGEX · liens API (FlashAlpha/UW/Quant) · WATCH |
| 2026-07-29T1415Z | Cursor | + | `thermo C18–C22` | Tension/impulse/bassine/SKIP/verre d’eau → indicateurs + hygiène fil de l’eau |
| 2026-07-29T1414Z | Cursor | + | `FORMULE_BASINE_POINTEUR` | #20 — pointeur discret Bassine/Vide (pas la formule en clair) |
| 2026-07-29T1354Z | Cursor | + | `MEMOIRE_PERSO_SYNTONIE_PERMABEL` | #19 S17 — Manifeste Syntonie/Permabel clarifié (mythe≠code≠médecine) |
| 2026-07-29T1339Z | Cursor | + | `ACE_DIAMANT_ARCHIVE` | #18 S16 — Diamant EIP-2535 clarifié depuis Bureau · GARDÉ archive / WATCH idées |
| 2026-07-29T1329Z | Cursor | ~ | `ARCHITECTURE_AGORA` | Recadré = **prototype ensemble** (ACE·Hulk·Cortana·Punk·Index) · Launch×9 = annexe |
| 2026-07-29T1328Z | Humain+Cursor | + | `ARCHITECTURE_AGORA` | Schéma 3 plans + Ollama Launch×9 WATCH (Hermes/OpenClaw cold) · pas pendant ACE |
| 2026-07-29T1109Z | Humain+Cursor | ★ | `VALEUR_INFORMATION` | **VALIDÉ** S14 A·B — GARDÉ filtre session recherche (ops OK) |
| 2026-07-30T0824Z | Cursor | + | `Index_Maison/thermo` | Board THERMO live A/B/C + live.json free · S22b |
| 2026-07-29T1049Z | Cursor | + | `Index_Maison` | S14 VALEUR_INFORMATION A·B · #17 · grille économie+$ |
| 2026-07-29T1018Z | Cursor | + | `Index_Maison` | #16 @Av1dlive suivi · Meridian WATCH · pref Kimi API · règle auto-add COMPTES |
| 2026-07-29T1012Z | Cursor | + | `Index_Maison` | #15 N01ennn · PROTOCOLE_CONTRA_SOFT · S13 PISTE · REFUS cron 6h · CONTRA.md |
| 2026-07-29T0812Z | Cursor | ★ | `ace777-test-day1` | GO ACE NUAGE_TEST_4H_0729 Terminal · Ollama ON · duo en marche · fin ~12:11Z |
| 2026-07-29T0810Z | Cursor | ★ | `hulk-mexc` | GO Hulk paper SEED 20$ XRP+HBAR · Terminal · ACE bloqué preflight Ollama |
| 2026-07-29T0702Z | Cursor | + | `Index_Maison/BRIEF_IA_SNIFF.md` | Brief sniff IA branché Punk/suivi + coutumes |
| 2026-07-29T0629Z | Cursor | ★ | `hygiene` | Grosse hygiene matin + stop Ollama · STERILE=OK |
| 2026-07-28T2254Z | Punk | + | `A_Mon_Attention/20260728T2254Z_RaoulGMI_…` | Suivi PERTINENT · offline · @RaoulGMI liquidité/RRP → M1 |
| 2026-07-28T2254Z | Cursor | ★ | `veille-punk` | GO ordre naturel : plomberie `obsidian.env` + suivi offline + speak |
| 2026-07-28T2243Z | journal_auto | ★ | CONSOLE+Journal_2026-07-29 | Snapshot auto hygiène soir |
| 2026-07-28T2242Z | journal_auto | ★ | CONSOLE+Journal_2026-07-29 | Snapshot auto hygiène soir |
| 2026-07-28T2238Z | journal_auto | ★ | CONSOLE+Journal_2026-07-29 | Snapshot auto hygiène soir |
| 2026-07-28T2101Z | Cursor | ★ | `Obsidian_ACE777` | Vault unique : Projet_2→Assistant_Vocal ; 2e .obsidian backup ; obsidian.json 1 vault |
| 2026-07-28T2048Z | Cursor | ★ | `Swarm_Bus/09_MEMOIRE_COLLAB.md` | GO sync agora coffre |
| 2026-07-28T2045Z | Cursor | + | `Swarm_Bus/09_MEMOIRE_COLLAB.md` | Création mémoire collab (hygiene) |
| 2026-07-28T2045Z | Cursor | + | `Swarm_Bus/10_ATTENTION_VOCALE.md` | File résumé oral Cortana |
| 2026-07-28T2045Z | Cursor | ~ | `Swarm_Bus/00_LIRE_MOI.md` | Index +09 +10 |
| 2026-07-28T2045Z | Cursor | + | `Index_Maison/Suivi_Info/` | Comptes suivis + pipeline filtre |
| 2026-07-28T2045Z | Cursor | + | `Index_Maison/A_Mon_Attention/` | File propositions |
| 2026-07-28T2045Z | Cursor | + | `Index_Maison/01_TABLEAU_VIVANT.md` | Board améliorations |
| 2026-07-28T2045Z | Cursor | + | `veille-punk/suivi_check.py` | Filtre post vs tableau + mémoire |
| 2026-07-28T2030Z | Cursor | ★ | M5 | Doctrine anti-si fixes (phase 2 débloquer) |
| 2026-07-28T2200Z | Cursor | + | Évals #01–#11 | Session posts X → Index |
| 2026-07-28T2200Z | Cursor | + | M1–M4 mindsets | Liquidité, sniper, judge, prove-wrong |
| 2026-07-28T2200Z | Cursor | + | S8 | Suivi → Cortana (piste → branché) |

---

*Append-only. Ne pas réécrire l’historique — corriger par une nouvelle ligne `~`.*

~ 2026-07-30 — Cockpit: retour peau arcade/radar (pas fusée littérale). Alpha Engine / Beta Boost / Hulk bags séparés, flèches portefeuille +/-, essaim au rythme cycle, feed enrichi size/lev/conf.

~ 2026-07-30T15:11Z — Point froid: STERILE=OK, P2 +0.81$, Hulk paper rouge, RAM TIGHT, cockpit figé. Pas de GO.

~ 2026-07-30T15:56Z — Voie A PARKÉE. Reprise setup usine d’avant (GO_USINE + BIDIR/STORM/MIN_ENTRY=3.0). STERILE=OK · RAM TIGHT. Commande prête 2h tag NUAGE_SETUP_AVANT — GO humain.

~ 2026-07-30T16:35Z — Cortana résumé horaire (launchd 1h) + avis sentiment. Dashboard tech.html ouvert. Kimi #15 Risk/WARM/DR intégrés (C7/C8). Risk Guardian pas en vol.

~ 2026-07-30T16:45Z — P1 CLOSED atomic veille · P2 MAX_GLOBAL_DD_PCT=8 · P3 Cortana URGENT (code+plist prêts). load launchd = toi.

~ 2026-08-13T20:05Z — COCKPIT RELOOK v2 (famille 6 GO): heure LOCALE partout (fini UTC/Z, 4 traces trades+alertes+SESSION converties), graph synapse sans bulles (soma+leader line+anti-chevauchement), cosmos 2 anneaux si >8 providers + labels triés par angle, tableaux de droite en grille 2 colonnes, LIVE = polling hub.json 10s (prouvé: budget 1602→1623 sans reload) + degragade si 3 echecs + visibilitychange. Backup index.html.bak-cockpit-relook-20260813-195218. Specs: SPEC_cockpit_relook_v2.md + v2_corrections.md. AUDIT_COCKPIT_RELOOK_2026-08-13/.

~ 2026-08-13T21:10Z — COCKPIT STABILITÉ v1 (audit famille 6 : GO unanime)
  · Graph cosmos : buildNodes initialise les providers sur leur orbite + pollHubLive met à jour en douce (plus de saut / tassés au centre)
  · Size_note traduits en FR (cartes ALPHA/BETA) : strong_conf_full+entry_25_75_full → pleine confiance · entrée 25/75
  · Feed cosmos hub.json : 120s → 30s (launchd com.ace777.hub-cockpit-feed) → cockpit synchronisé en live
  · Diffing v2 famille : re-rendu seulement si generated_at a changé
  · Testé Chromium + WebKit (pywebview) : positions stables 136px, 0 erreur JS
  · Fichier : Index_Maison/cockpit/index.html | backup : index.html.bak-cockpit-stabilite-*
