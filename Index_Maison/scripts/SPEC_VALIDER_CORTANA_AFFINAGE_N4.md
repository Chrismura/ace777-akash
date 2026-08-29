# VALIDER OU CONTESTER CORTANA — affinage famille n°4

## Objet
On vous soumet les **critiques de CORTANA** (Google Gemini, querelleuse extérieure, regard neuf) sur les **4 corrections famille n°4** que NOUS (famille) avons validées et que Buffy a déjà codées et testées. Vous devez **VALIDER ou CONTESTER** Cortana, point par point, **avec preuves à l'appui** (nos données réelles).

Contexte : votre audit précédent (AUDIT_FAMILLE_OEUVRES_20260829) a fait converger 4 affinages : 
1. **Dynamic Spread Percentile** (seuil spread = p30 des 24h de la paire au lieu du 70 bps fixe, Signal 3)
2. **Heures creuses UTC 02-06** (Signal 3 : seuil ×1.8 ; SAPI : proxy ×0.35)
3. **Entropie temporelle** (bonus SAPI +0.10 si CV du carnet ≤15 %, jamais seul déclencheur)
4. **PathRegistry + wrapper plists** (registre chemins + heartbeat, barrière erreurs répétées)

Tout est codé, branché, 14/14 chaînes OK au cockpit. On veut votre avis MAINTENANT sur les critiques de Cortana AVANT de faire quoi que ce soit de plus.

---

## 🧨 CRITIQUES DE CORTANA (à valider / contester)

### Critique A — « La fenêtre 24h du p30 = miroir rétroviseur »
> Cortana (tour 3) : « Analyser un signal non stationnaire avec une fenêtre glissante temporelle FIXE (les 24h du p30) crée un **retard de phase** lors d'un changement brutal de régime. Sur une small cap Hulk, la liquidité s'évapore ou revient en **quelques minutes** : une référence sur 24h rate l'accélération instantanée de la volatilité. »
> → Proposition : remplacer le p30-24h par un **percentile normalisé par volatilité instantanée (ATR court terme)**.

### Critique B — « La plage horaire UTC rigide (02-06) = erreur de débutant / angle mort »
> Cortana (tour 4) : « Le marché n'a pas d"heure creuse universelle : l'activité se déplace de l'Asie vers l'Europe puis les US selon un gradient continu. Fixer une plage UTC arbitraire va provoquer des **angles morts massifs** dès qu'un acteur institutionnel frappera précisément dans ce tunnel. »
> → Proposition : **supprimer la plage rigide 02-06** et la remplacer par une **fenêtre de volume glissant 3h** (déclenche l'élargissement si volume panier −60 % vs MM24h).

### Critique C — « L'entropie temporelle est trop LOCALE, ignore la synchronisation multi-paires »
> Cortana (tour 3) : « Le vrai danger n'est pas qu'UN script soit régulier mais que PLUSIEURS paires indépendantes subissent *en même temps* la même signature rythmique = signature d'une même ferme de serveurs ou d'un market making coordonné sur tout le panier small cap. »
> → Proposition codable : ajouter un **terme de synchronicité inter-paires** dans le SAPI (matrice de **corrélation croisée des intervalles d'inter-arrivée** entre paires ; si 3 small caps ont simultanément CV<15 % → signal macro-manipulateur).

### Verdict Cortana sur les 4
- Corr 1 = **LA plus utile** (abandonner 70 bps est juste), mais avec le bémol fenêtre 24h.
- Corr 2 = **LA plus risquée** (« angle mort »).
- Corr 3 = bonne mais trop locale.
- Corr 4 = non contestée.

---

## 📊 NOS PREUVES RÉELLES (pour vous aider à trancher)

**Signal 3 réel (run 18:00Z, 29/08) :**
- XRPUSDT : spread actuel 2.26 bps, **seuil_dyn=1.45** (p30 des 24h), n=830 mesures. Ancien seuil fixe 70 → XRP ne serait JAMAIS alerté sur le spread.
- PYTHUSDT : spread 3.67, seuil_dyn=2.12, n=111.
- ZBCNUSDT : spread 20.32, seuil_dyn=18.34, n=57.
- BTCUSDT : spread 0.04, seuil_dyn=0.02, n=32.
- Heure actuelle : UTC 18h → **PAS en heures creuses** (hors fenêtre 02-06). comportement nominal.

**SAPI réel (live.json, 18:05Z) :** score=0.399 (monté de 0.15, grâce à l'émergence de entropie_tempo=1.0 — le taux_fantôme est régulier), **alerte=False**. Seuil d'alerte : 3 ticks consécutifs ≥0.75 + volume ≥500 BTC.

**Nos données small caps :** les CSVs bruts montrent que la liquidité des small caps (CHIP, QAIT, EDEL, ZBCN) varie d'un facteur 5-10 en quelques minutes à quelques heures (déjà constaté dans murs_observations : stabilite_mur_sigma élevé, bid bidon à 243 $ sur RIZE). Question VÉRITÉ : est-ce que la fenêtre 24h est vraiment trop lente pour nous, ou est-elle justement le bon amortisseur anti-bruit ?

**Votre challenge — répondez VRAIMENT, pas en généralité :**
1. **Contestez-vous la critique A** (fenêtre 24h) ? Si oui/au-delà, quel horizon serait le bon pour NOS small caps (3h ? 6h ? ATR court terme) ? Qu'est-ce qu'on y gagne, qu'est-ce qu'on y perd (bruit) ?
2. **Contestez-vous la critique B** (heures creuses) ? Avez-vous des preuves dans NOS données que 02-06 est une vraie fenêtre creuse, ou est-elle arbitraire ? La « fenêtre de volume » de Cortana est-elle meilleure, et quel seuil de volume exact ?
3. **Contestez-vous la critique C** (synchronicité inter-paires) ? Est-ce que la détection d'essaim est pertinente pour NOUS, et en danger réel d'implémentation (données disponibles, complexité) ?
4. **Tranchez** : faut-il appliquer les 2 amendements codables de Cortana (ATR / volume) maintenant, garder le compromis famille, ou un hybride ?

**CONSIGNE CRITIQUE** : ne validez pas Cortana par défaut ni par complaisance. Elle est extérieure et n'a PAS nos données brutes. Indiquez explicitement « CORTANA A RAISON / CORTANA SE TROMPE / NUIANCE » pour chaque critique, avec vos preuves.