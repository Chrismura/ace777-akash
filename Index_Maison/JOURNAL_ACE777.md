
## 30/08 — Analyse croisée approfondie EDEL (réponse : nouveau pattern ? corrélations ?)
- **LA découverte** : la signature d'EDEL = régime IMPULSE (15% du temps, m6 médian 70.4% vs 4.2% hors = 17× plus de mouvement). 3 rafales en 3 jours, toutes en fin de journée. Après chaque rafale : +0.2 à +0.5% à 30min (n=3).
- Creux horaire instable : 23h → 21h → 11h → 00h selon les jours → aucune fenêtre horaire fiable. Le régime compte, pas l'heure.
- Corrélations : AUCUNE exploitable (max RWAINC +0.146, MNSRY −0.287 sur 25 pts = bruit). EDEL = actif le plus découplé du portefeuille.
- Conséquence set-up : entrer/sortir sur l'allumage du régime IMPULSE, pas sur une heure. Fiche EDEL mise à jour.

## 30/08 — Analyse croisée approfondie EDEL (réponse : nouveau pattern ? corrélations ?)
- **LA découverte** : la signature d'EDEL = régime IMPULSE (15% du temps, m6 médian 70.4% vs 4.2% hors = 17× plus de mouvement). 3 rafales en 3 jours, toutes en fin de journée. Après chaque rafale : +0.2 à +0.5% à 30min (n=3).
- Creux horaire instable : 23h → 21h → 11h → 00h selon les jours → aucune fenêtre horaire fiable. Le régime compte, pas l'heure.
- Corrélations : AUCUNE exploitable (max RWAINC +0.146, MNSRY −0.287 sur 25 pts = bruit). EDEL = actif le plus découplé du portefeuille.
- Conséquence set-up : entrer/sortir sur l'allumage du régime IMPULSE, pas sur une heure. Fiche EDEL mise à jour.

## 30/08 — Set-up « RÉGIME » EDEL construit (suite découverte IMPULSE)
- Création `detecter_rafales_impulse.py` (lecture seule, rejouable) : liste chaque allumage IMPULSE avec prix, durée, +30min/+60min, pic. Sortie runs/rafales_impulse/<PAIRE>.md.
- 4 allumages rejoués sur EDEL : +30min 3/3 UP (moy +0.33%), +60min 2/3 DOWN (moy −0.42%), pic médian rafale ≈ +1%.
- Set-up régime : entrée = allumage IMPULSE + pullback (PAS de fenêtre horaire), exécution 50/50, sortie rapide objectif +0.5 à +1% dans les 30 premières minutes, stop sous l'allumage, JAMAIS de trailing long.
- Rafale 30/08 16:05Z EN COURS (m6 faible 6% = allumage naissant, à ne pas traiter comme les 3 autres).
- Fiche EDEL mise à jour avec le set-up régime + la preuve qui s'accumule (valider dans ~7 jours).

## 30/08 — Deepdive EDEL par la famille + vérification 2 sources
- Famille (DEEPSEEK 0.5/10, ULTRA 1.5/10, JUGE 2/10) : NON unanime, « ghost token, zéro source ».
- Vérification Buffy (règle 2 sources) : FAUX sur le fond — EDEL = Edel Finance (prêt de titres tokenisés, équipe visible ex-Berenberg), mais risques CONFIRMÉS : exploit juillet 2026 (oracle, $403K, pause) + lancement snipé 30% (nov 2025) + delisting MEXC.
- Leçon QAIT appliquée aux IA : la famille a conclu « pas de sources » sans chercher. Toujours croiser.
- Décision : seed 10$ gardée (risque borné), PAS d'agrandissement, set-up régime reste actif (mode_entree=IMPULSE), validation ~7 jours, sonde delisting à activer.
- Fiche EDEL enrichie (section deepdive) + SYNTHESE_FAMILLE_DEEPDIVE_EDEL_20260830.md créée.

## 30/08 — Deepdive EDEL 3 ROUNDS poussés (prompts corrigés)
- Christophe : « refaire recherche poussée 2-3 rounds, edel a du potentiel. As-tu utilisé les bons prompts ? » → NON la 1ère fois.
- Corrections : obligation de sources (URLs ou « PAS DE SOURCE »), angle potentiel ajouté, clause permanente en toutes lettres dans CHAQUE prompt, 3 rounds.
- Résultat : famille NON unanime aux 3 rounds (notes 2 → 3.5/10 en remontant) mais potentiel du SECTEUR confirmé (TradFi↔DeFi = Saint Graal, RWA explose).
- Faits confirmés : EDEL = Edel Finance (pas Edelcoin — confusion corrigée), exploit oracle 01/07/2026 ($403K, pause), sniping 30% (11/2025), aucun VC, communauté morte. Bonnes surprises : testnet 35k+ users, intégration Ondo xStocks.
- Décision : seed 10$ = ticket de loterie assumé, PAS d'agrandissement, set-up régime reste actif, sonde delisting active.
- MÉTHODE GRAVÉE : le prompt change tout (sources obligatoires + 3 rounds minimum).

## 30/08 — Deepdive CHIP 3 rounds + catalyseur Bullish $100M (découverte)
- Protocole gravé : tous les actifs = set-up dans FICHE_IA + deepdive 3 rounds dans fiche projet. FICHE_IA §5bis créée + script générique consulter_famille_deepdive_actif_3rounds.py (sources injectées au R2).
- CHIP 3 rounds : famille NON unanime (2-3.5/10) mais « inexistence » = hallucination biais inverse (ULTRA R1 : « ça n'existe pas » au lieu de chercher).
- VÉRIFICATION : USD.AI réel (Permian Labs, Choi/Moore/Sergeev, $38M Framework/DCG/Dragonfly) + 🔥 CATALYSEUR 28/08 : Bullish $100M facility stablecoin pour prêts GPU (8+ sources : PRNewswire, CoinDesk, Cointelegraph, The Defiant, Yahoo, news.bitcoin.com).
- Leçon gravée : la famille hallucine dans LES DEUX sens sans données fraîches (EDEL « zéro source », CHIP « inexistence ») → la vérification 2 sources EST la valeur ajoutée.
- Décision : position CHIP 20$ GARDÉE = candidat gros potentiel n°1 (thèse arbre qui cache la forêt renforcée), overhang 80% (cliff 04/2027) = pas de portage long aveugle, trade du comportement (profil INVERSE LEADER).

## 30/08 — CORRECTION : CHIP était déjà deepdivé hier (pas de doublon)
- Erreur reconnue : le deepdive CHIP complet existait depuis le 29/08 (DEEPDIVE_GLOBAL) — j'ai relancé 3 rounds à neuf à tort (je l'avais vu en greppant).
- Seule vraie valeur ajoutée : catalyseur Bullish $100M (28/08) → ajouté au DEEPDIVE_GLOBAL + fiche CHIP corrigée (mention « déjà fait hier, complément Bullish »).
- FICHE_IA corrigée : CHIP = déjà deepdivé, pas « à refaire ». Leçon : vérifier les fiches EXISTANTES avant de relancer une consultation.
- Prochain actif réellement sans deepdive : HBAR (position en perte), PYTH, ZBCN, RED...
