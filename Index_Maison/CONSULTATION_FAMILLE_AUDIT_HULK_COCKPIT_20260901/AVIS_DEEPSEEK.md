# AVIS DEEPSEEK (task deepseek.analyse · Google Gemini · 2026-09-01T07:20Z)

### 1. FAITS
- **Runtime Hulk :** Mode *paper* sur MEXC, 20 paires configurées, 15 positions actives, 0 bags (selon l'état runtime), cash par paire = 114.08 USDT, PnL réalisé = -6.2422 USDT, 40 trades exécutés.
- **Flux de données & Logs :** ~18,772 lignes CSV dont 18,697 `SKIP` (volume sec, spread, murs, cooldown). `aspiration_src=fichier`, `aspiration_live.json` frais, `observer_murs` périodique.
- **Cockpit & Santé :** Santé cockpit 15/15 OK (après correction contrat CSV/JSON). SAPI poussière = 0.502, alerte = false, persistance = false, pipeline health = 0.9. Confusion sémantique relevée : l'état indique 0 bags, mais le cockpit en affiche 15 via un champ historique/portfolio.
- **Paramètres Clés :** NOTIONAL = 20 USDT, seed = 150 (répartis sur 17 max), compound ON (50% PnL, cap x3), tier B (x0.25), spread achat max = 100 bps, cooldown stop = 4h, `REENTRY_MAX` = 1, `BAG_PAIRS` = `CCUSDT, EDELUSDT`. Profil EDEL impose `IMPULSE`. Score toutes les 10 boucles (~3 min), prix toutes les 20s, cache book 45s.
- **Contradictions documentées :** Sonde d'aspiration *observation-only* vs filtre murs dans `maybe_enter` ; `BAG_PAIRS` inclut EDEL malgré un ancien schéma restreignant à CC ; commentaires contradictoires dans les defaults (QNT/FLUID/RWA/MNSRY).

---

### 2. DIAGNOSTIC
Le système Hulk *paper* tourne et produit des métriques, mais souffre d'une **asymétrie critique entre l'intention théorique et l'exécution réelle** :
1. **Filtre de bruit excessif (99.6% de SKIP) :** Avec 18,697 `SKIP` pour 40 trades, le moteur est soit mal calibré pour la liquidité actuelle des 20 paires, soit englué dans des gardes contradictoires (murs/cooldown/spread). Cela détruit l'opportunité statistique.
2. **Divergence Sémantique et État (Cockpit vs Runtime) :** La contradiction entre le runtime (0 bags) et le cockpit (15 bags) prouve que le dashboard lit des structures de données obsolètes ou mal mappées de la famille ACE777. Un opérateur ne peut piloter un risque réel avec un affichage ambigu.
3. **Performance nette négative en régime neutre/haussier :** Un PnL réalisé de -6.22 USDT pour 40 trades en *paper* avec des frais/spreads non absorbés indique une espérance mathématique ($E$) négative ou nulle avant même de basculer en live.
4. **Fallback réseau risqué :** Le fallback inline sur JSON satellite stale augmente la surface d'attaque en latence et en appels API au lieu de couper proprement les nouvelles entrées (fail-safe manquant).

---

### 3. ANGLES MORTS
- **Impact réel du Slippage et de la Profondeur (Order Book) :** Le cache book à 45s et le prix toutes les 20s sont inadaptés à des paires illiquides (mentionnées dans le profil EDEL). Le PnL *paper* simule-t-il des fills impossibles en réel ? Aucune preuve dans le code/logs fournis.
- **Exposition cachée des Bag Pairs :** `BAG_PAIRS` inclut EDEL (sans stop technique, DCA bag, crash bag -20% vend 90%). Si EDEL décroche, la logique de "bag" absorbe du capital sans borne stricte de perte globale par paire.
- **Gestion du SAPI et Poussières :** SAPI à 0.502 sans persistance ni alerte active laisse présager un risque de blocage d'ordres ou de poussières non nettoyées en fin de cycle live.

---

### 4. AMÉLIORATIONS PROPOSÉES (P0 / P1 / P2)
*En tant que critique, je ne me contente pas de valider : je pose l'architecture corrective obligatoire.*

- **[P0 - Critique] Unification du Contrat d'État (Runtime vs Cockpit) :** 
  * *Proposition :* Supprimer le champ `bags` obsolète dans le calcul du cockpit. Forcer le cockpit à lire *uniquement* l'état atomique courant du JSON de session Hulk. Interdire tout affichage de sous-systèmes ACE/Vortex non actifs dans le même namespace.
- **[P1 - Haute] Refactoring du Fail-Safe Aspiration :** 
  * *Proposition :* Remplacer le fallback inline par un **stop-new-entries strict** en cas de stale data du satellite (> 60s). Le système doit refuser d'entrer en position plutôt que de multiplier les requêtes réseau risquées.
- **[P2 - Moyenne] Nettoyage de la matrice de filtrage (SKIP) :** 
  * *Proposition :* Dissocier dans les logs CSV les *skips de données* (panne/latence) des *skips de stratégie* (filtre murs/spread). Abaisser le cache book à 15s sur les paires `IMPULSE` et purger les paires illiquides identifiées dans les commentaires contradictoires des defaults.

---

### 5. PRIORITÉS AVANT TOUT PASSAGE LIVE
1. **P0 :** Prouver par un script de test unitaire que l'espérance mathématique par trade ($E = (WinRate \times WinAvg) - (LossRate \times LossAvg)$) est strictement supérieure aux frais MEXC (Taker/Maker + Spread moyen constaté).
2. **P0 :** Corriger la divergence d'affichage des bags (Runtime 0 vs Cockpit 15).
3. **P1 :** Implémenter la persistance des alertes SAPI et un coupe-circuit automatique si le pipeline health descend sous 0.8.
4. **Interdiction formelle d'activer Kelly ou Cortana** tant que le PnL réalisé en paper sur 500 trades minimum n'est pas strictement positif et statistiquement stable ($p-value < 0.05$).

---

### 6. AVIS STRICT
- **Paper Actuel :** **GO-AVEC-RÉSERVES** (Le système tourne mais produit un PnL négatif et des incohérences d'affichage cockpit).
- **Passage Live :** **NON** (Absence de preuve d'espérance positive, gestion des bags risquée sur EDEL
