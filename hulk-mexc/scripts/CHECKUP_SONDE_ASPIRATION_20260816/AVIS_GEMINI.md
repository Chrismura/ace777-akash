# AVIS GEMINI (provider NVIDIA build.nvidia.com (100+ modeles))

**1. VERDICT : GO AVEC RÉSERVES**

Le code est propre, fail-open correctement placé (2e lecture échoue → lecture simple, jamais de blocage), normalisation temporelle GROK intégrée, seuil 500$ JUGE respecté. Les réserves portent sur les angles morts ci-dessous.

---

**2. ANGLES MORTS**

- **BUG — `_drop` non protégé contre m2 > m1** : si le mur AUGMENTE entre les 2 lectures (reconstruction), `drop` devient négatif → `max_drop` peut être négatif → `aspiration_side = "NONE"` (correct) MAIS `drop_bid_pct_per_s` négatif est loggé et pourrait fausser la calibration CSV. Ajouter `max(0, ...)`.

- **BUG — `notional_drop_ok` vérifie le mur de RÉFÉRENCE, pas le mur qui FOND** : si `aspiration_side = "BUY"` (mur ask fond), on vérifie `ref_wall = d1["wall_ask_usdt"]`. OK. MAIS si le mur bid fond et que le mur ask est énorme, `aspiration_side = "SELL"` → on vérifie le mur bid. Correct. Par contre, si les DEUX murs fondent, on prend le plus gros drop — mais on ne vérifie le notional QUE sur le côté choisi. Le côté non-choisi peut être < 500$ et pourtant contribuer au signal. Mineur mais à noter.

- **SPOOF — seuil 15%/s arbitraire** : `drop_now >= 15.0` est un chiffre sorti de nulle part. En mode observation 48h, c'est acceptable, mais il faut le logger systématiquement pour calibrer CE seuil aussi, pas seulement le seuil d'aspiration.

- **RATE-LIMIT — `ASPIRATION_PROBE_EVERY=3` cycles** : si le cycle moteur est ~1s, ça fait un probe toutes les 3s × 5 paires = 1.67 requêtes/s en plus du moteur. MEXC limite ~20 req/s par IP. OK mais à surveiller si le moteur accélère.

- **CSV — pas de flush explicite** : `csv.writer(f).writerow(...)` sans `f.flush()`. Si le process crash, les dernières lignes sont perdues. Ajouter `f.flush()` après chaque write.

---

**3. AMÉLIORATION CONCRÈTE GO-SIZED**

**Ajouter `max(0, ...)` dans `_drop` et logger le `drop_negatif` séparément** :

```python
def _drop(m1, m2):
    if m1 <= 0: return 0.0
    return max(0.0, (m1 - m2) / m1 * 100.0)  # jamais négatif
```

Et dans le retour, ajouter un champ `drop_negatif` pour la calibration :

```python
"drop_negatif": round(min(0.0, (d1["wall_bid_usdt"] - d2["wall_bid_usdt"]) / d1["wall_bid_usdt"] * 100.0), 2) if d1["wall_bid_usdt"] > 0 else 0.0
```

Ça permet de distinguer « mur qui fond » de « mur qui se reconstruit » dans le CSV — crucial pour le spoof.

---

**4. CLAUSE PERMANENTE — PROPOSITION AUTRE CHOSE**

**Approche différente : au lieu de mesurer le DROP du mur, mesurer la VITESSE DE CONSOMMATION relative au volume total côté opposé.**

Le drop %/s est biaisé : un mur de 500$ qui fond à 50%/s est moins significatif qu'un mur de 50 000$ qui fond à 5%/s (le premier est probablement du spoof, le second est une vraie aspiration institutionnelle).

**Nouvelle métrique : `aspiration_ratio = (drop_pct_per_s / 100) * (wall_usdt / total_volume_opposite)`**

- Si le mur qui fond représente 10% du volume total côté opposé → signal fort.
- Si le mur qui fond est minuscule par rapport au volume total → bruit.

Ça nécessite de lire le volume total côté opposé (somme des 20 niveaux), ce qui est déjà dans `_one()`. Coût : quasi nul. Gain : le seuil devient un ratio sans dimension, calibré une fois pour toutes, indépendant de la taille de la paire.

**En clair : remplace `drop_pct_per_s >= 15.0` par `aspiration_ratio >= 0.05` (5% du volume total consommé par seconde)** — plus robuste, moins de faux positifs spoof, et ça marche sur toutes les paires sans recalibrage.

---

**RÉSUMÉ EXÉCUTIF** : GO avec 2 corrections immédiates (max(0,...) + flush CSV), 1 métrique à ajouter (aspiration_ratio) pour la calibration 48h, et le seuil spoof 15%/s doit être calibré sur les données réelles — pas sorti du chapeau.
