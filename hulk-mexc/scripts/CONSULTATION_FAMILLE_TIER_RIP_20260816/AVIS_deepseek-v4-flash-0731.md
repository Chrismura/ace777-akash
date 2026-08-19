# AVIS deepseek-ai/deepseek-v4-flash-0731 (provider NVIDIA build.nvidia.com (100+ modeles), 102.3s)

**AVIS CONSULTATION FAMILLE — 16/08/2026**

---

### RÉPONSES AUX 4 QUESTIONS

1. **TIER_B_POSITION_MULT=0.25** : Raisonnable en attendant mieux. 0.1 serait plus prudent vu les stops gapés (RIZE −12.25%). Watch-only strict = trop restrictif (vous ratez les spikes). **0.25 avec stop gapé assumé** est un compromis acceptable.

2. **RIP_SELL_FRAC=0.50 au 1er franchissement** : Oui, vente unique à 50%. Les paliers (30% + 30%) complexifient le code pour un gain marginal. Le problème actuel est le *give-back total* (RED +32.8% non vendu) — une vente franche à 50% règle ça.

3. **Rip sur tier B** : **Oui, mais avec prudence**. Les tier B spikent fort (c'est leur nature), mais l'illiquidité rend la sortie risquée. Appliquez le rip aux tier B **uniquement si le spread est < 100 bps au moment de la vente** (sinon, attendez le 2× ou le stop). Ajoutez cette condition dans le code.

4. **REENTRY_MAX=1 + cooldown 4h** : Bons. EDEL acheté 3× sur une chute = erreur classique. 1 seule re-entry max, même après 4h, est la bonne discipline.

---

### VERDICT : **GO-AVEC-RÉSERVE**

**Réserve** : Le bloc 3 (rip) doit inclure une condition de spread max pour les tier B (sinon vous vendez à un prix théorique jamais exécutable).

---

### CONFIANCE : **78%**

---

### HYPOTHÈSES

1. Les 15 paires PAPER_PAIRS en dur sont un reliquat de test, pas un choix délibéré.
2. Le spread MEXC est stable pendant la session (pas de variation brutale entre le check et l'exécution).
3. Le `rip_pct` calculé au buy() est pertinent pour la durée de vie de la position (pas de re-calibration nécessaire).

---

### CE QUI CHANGERAIT L'AVIS

- **Preuve que les tier B ont un taux de réussite > 30%** sur 20+ trades (avec stop gapé inclus) → passer à 0.5.
- **Découverte que le spread MEXC varie > 50% pendant la session** → le bloc 3 devient inutile, il faut un ordre limite.
- **Un backtest montrant que les re-entries à +4h sur des paires en chute sont rentables** → REENTRY_MAX=2.

---

### AMÉLIORATIONS PROPOSÉES

1. **Ajouter un check spread dans le bloc 3** : `if self.spread(pair) < 100: vendre rip, sinon attendre`.
2. **Log systématique du spread au moment du buy()** — pour corréler spread et performance future.
3. **Après 2 semaines de ce fix, faire un A/B test** : tier B avec mult 0.25 vs watch-only, pour décider si on garde ou on supprime.

---

### SYNTHÈSE (5 lignes)

Diagnostic : le système trade des paires illiquides (tier B) à pleine taille, avec des stops gapés, et ne vend jamais les gains (give-back). Ordre d'actions : (1) implémenter les 4 blocs avec la réserve spread sur le rip, (2) purger PAPER_PAIRS des tier B non extra, (3) surveiller 2 semaines, (4) si les tier B restent négatifs même à 0.25, les passer en watch-only.
