# SPEC — Kelly fractionnaire ¼ en mode OMBRE (sizing Hulk) — 15/08/2026

**Chantier 3** (ordre famille validé : nvidia rang 1, 72% — « la plus value immédiate »).
**Origine** : signets N°43 (@kryneeex — Burry : « c'est la taille de position qui compte ») + N°105 (@CorvusXBT — paradoxe de Saint-Pétersbourg → maximiser le logarithme de la richesse = critère de Kelly).
**Décision de supervision** : **mode OMBRE pur** — on CALCULE et on AFFICHE, on n'applique RIEN. Deux raisons : (1) la justesse Cortana est à 44% (<50%) et le win-rate réel des trades Hulk est 0/3 → Kelly plein donnerait 0 ou négatif (paralysie) ; (2) même philosophie que le contrat ADVISORY — rien n'est appliqué tant que la preuve n'est pas là. Le moteur `paper_diprip.py` n'est PAS modifié.

---

## Fichier à créer : `hulk-mexc/scripts/kelly_ombre.py`

Script Python 3 autonome (stdlib uniquement). Lancé à la demande (ou par la discipline quotidienne — voir plus bas). **Lecture seule : ne touche ni au moteur, ni au CSV, ni au state, ni au genesis.**

### Données d'entrée (lecture seule, fail-open)
1. **Justesse Cortana** : `Index_Maison/scripts/justesse_v2.json` → `pct` (44.0 actuellement).
2. **Trades Hulk réels** : dernier `hulk-mexc/runs/PAPER_V1_*.csv` (le plus récent par mtime ayant des trades clos). Compter les événements de sortie (`SELL`, `SELL_PARTIAL`, `BAG_CRASH`, `BAG_SELL`, `STOP*`…) avec `pnl_usdt != 0`.
   - Attention : ignorer les lignes `BUY`, `SEED`, `SKIP`, `BAG_ARM`, `BAG_DCA` (pas des sorties).

### Calcul (formules exactes)
- `win_rate = nb_wins / n` (n = trades clos, wins = pnl > 0).
- `avg_win = moyenne(pnl des wins)` ; `avg_loss = |moyenne(pnl des pertes)|`.
- `b = avg_win / avg_loss` si `avg_loss > 0` sinon `b = 0`.
- **Kelly plein** : `k = win_rate - (1 - win_rate) / b` si `b > 0`, sinon `k = 0`.
- **Kelly ¼** : `k4 = k * 0.25`.
- **Plancher honnête (règle d'or anti-paralysie)** :
  - si `win_rate < 0.50` OU `k4 <= 0` → `k4 = 0` et `motif = "win_rate < 50% ou Kelly ≤ 0 — pas de sizing adaptatif tant que la preuve n'est pas là"`.
  - si `n < 20` → `k4 = k4 * 0.5` (pénalité petit échantillon) et motif complété.
  - Plafond dur : `k4 ≤ 0.02` (2% du capital par position max, comme proposé par nvidia).

### Sortie
1. **Rapport** : `hulk-mexc/runs/KELLY_OMBRE.md` :
   - `# Kelly ombre — <date>` · `win_rate`, `n`, `avg_win`, `avg_loss`, `b`, `kelly_plein`, `kelly_1_4`, `mise_recommandee` (= k4 × capital, capital = 20$ base_notional lu depuis state ou défaut 20).
   - **AVIS** : 3 lignes max — que ferait-on SI on appliquait (et pourquoi on n'applique pas encore).
   - **Règle** : « mode ombre — rien d'appliqué. On passe à l'application quand : win_rate ≥ 50% sur ≥ 20 trades ET justesse Cortana ≥ 50% (validation humaine). »
2. **JSON** : `hulk-mexc/strategie/kelly_ombre.json` : `{ts, capital, win_rate, n, b, kelly_plein, kelly_1_4, mise_recommandee, motif, applique: false}`.
3. **Exit code** : `0` = calcul fait (même si k4=0) · `1` = données insuffisantes (aucun CSV avec trades clos) — fail-open.

### Hook optionnel dans `discipline_quotidienne.py` (modification MINIMALE, 3 lignes)
- Après la dérive mémoire : `subprocess.run([sys.executable, str(SCRIPTS / "kelly_ombre.py")], check=False, capture_output=True, timeout=30)` (fail-open).
- Le fichier kelly_ombre.py peut vivre dans `hulk-mexc/scripts/` (lancé avec chemin absolu) OU dans `Index_Maison/scripts/` (cohabite avec la discipline). **Décision : `Index_Maison/scripts/kelly_ombre.py`** — il lit les CSVs Hulk en absolu, et la discipline le trouve sans path gymnastique.

### Contraintes
- Stdlib, français, commenté, fail-open sur chaque fichier (try/except, on continue).
- `applique: false` TOUJOURS — ce script ne modifie aucun sizing.
- Réversible : suppression du script (+ 3 lignes discipline) = retour à l'état d'avant.

### Format de sortie attendu du codeur
Le code EXACT de `Index_Maison/scripts/kelly_ombre.py` + le diff EXACT des 3 lignes dans `discipline_quotidienne.py`. Zéro autre modification.
