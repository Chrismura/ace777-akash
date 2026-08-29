# SPEC v2 — HULK : REMPLACER LA COUPE 100% (SELL FULL) PAR DES SORTIES EN CASCADE — 29/08/2026

**Statut :** VALIDÉE SOUS CONDITION par la famille (trio + juge) et Cortana · v2 = intégration
des 3 verrous obligatoires du juge · **Fichier cible :** `hulk-mexc/scripts/paper_diprip.py`
**Auteur :** Buffy (assistante) — aucune modification de code à ce jour (lecture seule).

---

## CONTEXTE COMPLET (fondamental — tout est vrai)

- **Portefeuille** : paper HULK MEXC, 15 small-caps, 22/07 → 29/08/2026, dip&rip + DCA.
  786 BUY, 378 SELL_PARTIAL, 166 SELL full, 1336 trades exécutés.
- **Signal amplitude** (move24 = range haut-bas 24h) : patron « dormance→pic », 54-78 % du
  temps sous la moyenne, pics 2-5×. L'amplitude prédit le MOUVEMENT pas la direction
  (le prix monte 70-100 % du temps après un pic).
- **Croisement sorties** (données réelles) :
  - SELL_PARTIAL : **+83,96 $** (moy +0,22), gagnant même en amplitude forte (+0,19).
  - SELL full : **−153,24 $** (moy −0,92), pire en amplitude forte (−1,57 $),
    pire régimes COOLING (61) / IMPULSE (42). fearGreed identique (~68) → biais mécanique.
- **Audit code** : `sell_trade(qty=None)` = vente 100 % déclenchée par stop en % du prix
  (`stop = max(4%, cadence × 0.70)`), sans vérifier l'invalidation ni le régime.
  3 déclencheurs : lignes 1894 / 1918 (stop avant 2×) et 1940 (trailing giveback).
- **Avis IA (29/08, contexte complet)** :
  - Cortana : LONG, confiance moyenne — « stopper l'hémorragie des ventes totales »,
    pattern « faux signal de coupe par volatilité », mais règle à nuancer
    (ne pas rendre le bot immobile).
  - Famille : SOUS CONDITION — validé sur le fond à 100 %, 3 verrous exigés (ci-dessous).

---

## LES 3 VERROUS OBLIGATOIRES DU JUGE (v2 — à intégrer AVANT de coder)

### VERROU 1 — Dust Sweeper / taille de lot (micro-poussières)
**Problème** : la cascade partielle (qty × 0.5) peut laisser des résidus sous la taille
minimale de lot MEXC (`min_qty` / `min_notional`) → « poussières » qui sédimentent,
bloquent les ordres suivants et faussent le compound (signalé par Cortana ET DeepSeek).
**Exigence** :
- Avant toute vente partielle, vérifier `qty_restante ≥ min_qty` ET
  `valeur_restante ≥ min_notional` (1 $) de la paire (profil `_profils()`).
- Si la position résiduelle passe sous le seuil → **liquidation forcée complète** de ce
  résidu (event `DUST_SWEEP`) au lieu de le laisser traîner.
- Traçage : les `DUST_SWEEP` apparaissent dans le CSV (reason `dust_sweep_<min>`).

### VERROU 2 — Disponibilité temps réel des indicateurs
**Problème** : la garde doit pouvoir lire ses indicateurs au moment EXACT où les lignes
1894/1918/1940 se déclenchent — sinon elle ne s'applique pas (blocage par manque de données).
**État vérifié (audit 29/08)** : `sc` contient DÉJÀ, à chaque tick :
- `move24_pct` (ligne 456) — l'amplitude, le signal principal ✓
- `vol_spike` (lignes 336 / `sniff_volume`) — proxy volume/activité ✓
- `dd6_pct`, `dd15_pct`, `dd24_pct`, `range15_pct`, `move6_pct` — structure du creux ✓
**Le VWAP 1H n'existe PAS encore dans le moteur** → la confirmation d'invalidation de la
v2 utilise les indicateurs disponibles (`vol_spike` + `dd15_pct`) au lieu du VWAP.
**Exigence** :
- La garde lit `sc["move24_pct"]` et `sc["vol_spike"]` au moment du stop (déjà passés
  dans `manage_open` via `sc`).
- Si `move24_pct` ou `vol_spike` est absent/None → **mode dégradé** : pas de coupe 100 %,
  bascule automatique en vente partielle (défaut sûr, jamais pire que l'actuel).
- Assertion au démarrage : log `[SELL_FULL_GUARD] indicateurs OK` ou `mode dégradé`.

### VERROU 3 — Compatibilité `--resume` (ne rien corrompre)
**Problème** : le moteur tourne en `--resume` ; les nouveaux paramètres ne doivent pas
corrompre les fichiers d'état (`*_state.json`) ni les CSV existants.
**Exigence** :
- Nouveaux paramètres = **uniquement** dans `defaults.env` (pas de changement de schéma
  state/CSV). Lecture avec fallback vers les défauts si absent (rétro-compatible).
- Le CSV ajoute une colonne optionnelle `guard` (SELL_FULL / SELL_PARTIAL / DUST_SWEEP /
  CASCADE) — les lignes anciennes sans la colonne restent lisibles.
- Test `--resume` sur un COPY du state courant AVANT tout run réel : vérifier
  `python3 paper_diprip.py --resume` lit l'ancien state sans erreur et sans réécriture
  destructive.

---

## LE FIX (4 blocs + config réversible)

### Bloc 1 — Garde-fou coupe 100 % en forte amplitude
Dans les 2 branches stop (1894/1918) : si `move24 > SELL_FULL_AMPLITUDE_GUARD` (défaut 12 %)
ET pas de confirmation d'invalidation → vente **partielle 50 %** (avec VERROU 1 pour les
résidus) au lieu de `sell_trade(qty=None)`.

### Bloc 2 — Filtre de confirmation d'invalidation (proposition juge, adaptée au moteur)
Coupe 100 % autorisée uniquement si **vraie invalidation** : `vol_spike` en chute
(proxy du delta volume, seuil à étalonner) ET creux structurel (`dd15_pct` > seuil
invalidation) — sinon vente partielle. Mode dégradé si indicateurs absents (VERROU 2).
Le VWAP 1H n'existant pas encore, on n'y dépend pas (voir VERROU 2).

### Bloc 3 — Cascade de sortie par paliers en plus-value
Réutiliser `rip_scaleout` (paliers 25 %) : en plus-value qui se dégrade, vendre par
paliers 30 % / 30 % / reste avec trailing + breakeven. Dust Sweeper à chaque palier.

### Bloc 4 — Traçage rétroactif
Compteur `SELL_FULL_BY_REGIME` (COOLING/IMPULSE/IMPULSE_WAIT/WATCH) + colonne `guard`
dans le CSV pour comparer avant/après déploiement.

### Config (`defaults.env`, réversible)
```bash
# Garde-fou SELL full en forte amplitude (SPEC v2 29/08)
SELL_FULL_AMPLITUDE_GUARD=12
SELL_FULL_REQUIRE_INVALIDATION=1
SELL_PARTIAL_CASCADE=1
# Verrou 1 : poussières
DUST_SWEEP_MIN_NOTIONAL=1.0
# Verrou 3 : mode dégradé si indicateurs absents
SELL_FULL_GUARD_DEGRADED=1
```

---

## LIVRABLES (contrat de sortie)

1. Code appliqué dans `paper_diprip.py` (4 blocs + 3 verrous), réversible.
2. Section PREUVE « meilleure logique » (clause permanente Christophe 14/08) : montrer avec
   les données passées combien −153 $ se seraient réduits avec la règle (simulation).
3. Une amélioration prouvée supplémentaire (UNE, bornée, sans effet de bord).
4. Test `--resume` sur copy d'état AVANT run réel (VERROU 3).
5. Rien d'autre — pas de réécriture, pas de feature.

## PRÉCAUTIONS

- Aucune modification faite à ce jour (lecture seule, 29/08).
- Circuit : SPEC v2 → re-soumission rapide famille (les 3 verrous intégrés) → GO Christophe
  → test → déploiement réversible. Le moteur tourne en `--resume` ; tout changement
  compatible et testable en paper.
