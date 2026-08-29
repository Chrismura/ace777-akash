# Famille vs Cortana — validation croisée de l'affinage n°4 (29/08)

- Conseil réuni : GEMINI, DEEPSEEK, ULTRA, INFERX, GROK (makers en parallèle) puis **JUGE** (tranche après lecture).
- Question : les 3 critiques de Cortana sur nos 4 corrections famille. Valider/contester, avec preuves (nos données réelles).
- Verdict global : **GO avec réserves (6/6)** — code actuel 14/14 validé, mais la famille AGRÉE une partie des critiques de Cortana et propose un **hybride**.

---

## 🧭 LE GRAND CONVERGENT (majeur : les 6 convergent sur l'architecture)

> **Personne ne rejette tout Cortana, personne ne l'accepte en bloc.** Mais il y a UN consensus quasi-unanime et très net : **« ne pas jeter la 24h ni l'UTC, ni accepter l'ATR pur ni la matrice lourde — faire un HYBRIDE ».**

| Critique Cortana | Verdict famille | Consensus clé |
|---|---|---|
| **A. Fenêtre 24h = miroir rétroviseur** | **Cortana A PARTIELLEMENT raison** (la 24h lisse trop sur small caps dont la liquidité s'évapore en minutes) **MAIS son remède (ATR pur) est une bombe à faux positifs** | Ne PAS remplacer par ATR pur. **HYBRIDE : garder p30_24h (amortisseur) + courte fenêtre (4h/EMA)** |
| **B. UTC 02-06 rigide = angle mort** | **DIVERGENT** · JUGE/DEEPSEEK/GROK : Cortana a raison, remplacer par **volume glissant 3h** · INFERX/ULTRA : **tort**, 02-06 est empiriquement vrai chez nous, garder + gardien dynamique | Soit volume-glissant 3h (juuge-majorité), soit garder 02-06 + gardien. À trancher |
| **C. Entropie trop locale → synchronicité inter-paires** | **Cortana SE TROMPE sur la complexité** : matrice de corrélation croisée = latence + deadlock + SPoF, inutile à notre stade | 6/6 : **REJETER la matrice lourde**, mais adopter un **compteur d'essaim LÉGER** |
| **D. PathRegistry + wrapper** | non contestée | garder |

---

## 📋 SYNTHÈSE PIÈCE PAR PIÈCE

### Critique A — p30-24h
- **Cortana partiellement raison** : nos small caps (ZBCN spread 20.32 vs seuil 18.34 ; murs à 243 $) ont une liquidité qui s'évapore en minutes. La 24h crée un angle mort transitoire de 15-30 min.
- **MAIS** : l'ATR court terme pur « s'emballe au premier spoofing » → transformerait le Signal 3 en machine à faux positifs (le bruit de carnet des bots). Preuve famille : on a DÉJÀ eu cet écueil.
- **Amendement hybride retenu** (GEMINI/DEEPSEEK/GROK/INFERX/JUGE convergent) :
  - `Seuil = 0.7 × p30_24h + 0.3 × p30_4h` (DEEPSEEK) — réagit < 60 min sans lâcher l'amortisseur.
  - ou `max(p30_24h, ATR_30m × k)` (GEMINI) / fenêtre 4h + ATR 15m (GROK).

### Critique B — heures creuses UTC 02-06
- **Le point de désaccord famille-famille** :
  - **JUGE, DEEPSEEK, GROK** → **Cortana a raison** : remplacer par **volume glissant 3h**, déclenche si volume panier chute (GROK corrige le seuil à **−50 %** vs le −60 % de Cortana jugé trop strict).
  - **INFERX** → **Cortana se trompe** : « nos logs montrent une chute structurelle de volume ×4-6 entre 01:30-06:00, la plage est empiriquement exacte, pas arbitraire ; la fenêtre de volume déclenche des faux signaux les jours fériés/lundis calmes ». → garder 02-06 + **gardien dynamique** (si volume 1h −80 % hors plage, basculer en mode creux).
  - **ULTRA** → donner raison à la critique mais juger la solution de Cortana « un cauchemar de robustesse en tempête » (boucle de rétroaction au pire moment) → garder 02-06 en attendant un indicateur non-récursif.

### Critique C — synchronicité inter-paires
- **6/6 rejettent la matrice de corrélation croisée** (latence, deadlock, coût CPU, décorrélation naturelle small caps).
- **6/6 convergent sur un « compteur d'essaim léger »** facilement codable :
  - si **≥ 2-3 paires** affichent un **CV ≤ 15 % en même temps** dans une fenêtre de **60 s** → majoration du SAPI de **+0.20 à +0.25** (au lieu du +0.10 local).
  - GROK préfère une variante « volume panier : si les 14 paires s'effondrent de 40 %, doubler le bonus ».

### Critique D — PathRegistry
- Non contesté. INFERX ajoute un détail : le wrapper doit écrire un `heartbeat.lock` daté pour tuer les zombies en heure creuse.

---

## 🎯 DÉCISION À PRENDRE (Buffy n'a rien appliqué en plus — le code actuel 14/14 est validé)

**Recommandation JUGE (85 % de confiance)** :
1. ✅ **GARDER** le code actuel (14/14 OK) — rien à défaire.
2. ✅ **Amender la Corr 1** : p30 hybride **4h/24h** (observable en <60 min sans bruit).
3. ✅ **Amender la Corr 2** : remplacer UTC 02-06 par **volume glissant 3h (−50 %)** — le JUGE tranche DANS le sens de Cortana sur ce point.
4. ✅ **Amender la Corr 3** : **compteur d'essaim léger** (≥ 3 paires CV≤15 % en 60 s → +0.20 SAPI) — adopter l'idée de fond de Cortana sans la matrice lourde.

**3 choix ouverts pour Christophe** :
- **A : appliquer les 3 amendements JUGE** (hybride 4h/24h + volume-glissant −50 % + compteur d'essaim) — « GO ».
- **B : appliquer seulement le volume-glissant ET garder 02-06 en gardien** (version INFERX, la plus prudente prod).
- **C : ne rien toucher** (compromis famille d'origine, déjà validé et testé).

Verdicts individuels détaillés : `scripts/CONSULTATION_FAMILLE_VALIDER_CORTANA_N4/AVIS_*.md` · transcription Cortana : `VAL_CROISEE_CORTANA_AFFINAGE_N4_20260829.md`.