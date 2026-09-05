# AVIS GEMINI (task gemini.analyse · Google Gemini · 2026-09-01T07:20Z)

### 1. FAITS
- **Runtime Hulk :** Mode *paper* sur MEXC, 20 paires configurées, 15 positions actives, 0 *bags* enregistrés, cash par paire 114.08 USDT, PnL réalisé -6.2422 USDT, 40 trades exécutés.
- **Volumétrie & Logs :** ~18 777 lignes CSV dont 18 697 en `SKIP` (volume sec, spread, murs/cooldown). Watchdog et fichiers d'état actifs.
- **Flux de données :** `aspiration_src=fichier`, satellite `aspiration_live.json` frais, `observer_murs` périodique.
- **Santé & Infrastructures :** Cockpit 15/15 OK (après correction contrat CSV/JSON). SAPI poussière actuel 0.502, alerte `false`, persistance `false`, pipeline health 0.9 nominal.
- **Paramètres Clés :** `NOTIONAL` 20 USDT, seed 150 (répartis sur 17 max), *compound* ON (50% PnL, cap x3), tier B x0.25, spread achat max 100 bps, cooldown stop 4h, `REENTRY_MAX` 1, `BAG_PAIRS` (CCUSDT, EDELUSDT), *bag* sans stop technique avec DCA, crash bag -20% (vend 90%), *rip scale-out* (25% + 25%), runner 50%, `SELL_FULL` guard 12%, Cortana en mode `ADVISORY`.
- **Régimes & Cycles :** WATCH/COOLING/IMPULSE/IMPULSE_WAIT. Score toutes les 10 boucles (~3 min), prix toutes les 20s, cache book 45s. Profil EDEL impose `IMPULSE`. Seuils historiques, présence de paires illiquides.
- **Anomalies & Contradictions :** 
  - PnL réalisé négatif (-6.24 USDT) sur 40 trades, performance proche de l'équilibre vs HOLD mais dépendante du marquage live.
  - Sémantique floue entre le state runtime (15 positions, 0 bags) et le cockpit (15 bags).
  - Contradictions documentées dans le code (sonde d'aspiration *observation-only* vs filtre murs dans `maybe_enter` ; `BAG_PAIRS` incluant EDEL vs ancien schéma CC seul ; commentaires contradictoires sur QNT/FLUID/RWA/MNSRY).
  - Fallback inline en cas de JSON satellite *stale* risquant d'amplifier les appels réseau au lieu de geler les entrées.
  - Le cockpit mélange des états de sous-systèmes ACE/Vortex historiques avec le runtime Hulk actuel.

---

### 2. DIAGNOSTIC
Le système Hulk *paper* est fonctionnel d'un point de vue purement technique (infrastructure, boucles, persistance des états), mais souffre d'une **dette documentaire et sémantique critique** ainsi que d'une **anémie des flux de décision** (taux de `SKIP` de 99.6%). 

Le ratio de filtration extrême (18 697 `SKIP` pour 40 trades) couplé à un PnL réalisé négatif suggère que la logique de filtrage (murs, spread, volume sec) rejette la majorité des opportunités viables tout en laissant passer des exécutions sous-optimales sur des paires illiquides (ex: profil EDEL forçant `IMPULSE`). La confusion sémantique entre "positions" et "bags" dans le cockpit masque le risque réel d'enlisement sur les paires désignées `BAG_PAIRS`. Enfin, le fallback réseau sur satellite *stale* est une faille de conception défensive : en cas de coupure ou de latence, le système devrait fail-safe (bloquer les nouvelles prises de risque) plutôt que de multiplier les requêtes.

---

### 3. ANGLES MORTS
- **L'illusion du taux de SKIP :** Un taux de SKIP de 99.6% ne prouve pas la robustesse du filtre ; il peut masquer une configuration de seuils obsolète par rapport à la liquidité réelle actuelle des paires MEXC.
- **La bombe à retardement EDEL :** `BAG_PAIRS` inclut EDEL alors que son profil impose `IMPULSE` et que l'historique contredit son statut, créant un risque de *bagging* non maîtrisé sur une valeur potentiellement illiquide.
- **La pollution visuelle et décisionnelle du Cockpit :** L'affichage d'états ACE/Vortex historiques dans le même cockpit que le runtime Hulk induit un risque de confusion cognitive pour l'opérateur en situation de crise.
- **L'absence de traçabilité fine du blocage :** Impossible de distinguer précisément dans les 18 697 `SKIP` la part imputable à une panne de données de celle imputable à une règle de risque stricte.

---

### 4. AMÉLIORATIONS (PROPULSIONS ACE777)
En tant qu'auditeur en chef, je ne me contente pas de valider. Voici ce qui DOIT être implémenté pour dépasser le stade actuel :

1. **Architecture de Sécurité du Satellite (Remplacement du Fallback Inline) :**
   * *Proposition :* Interdire tout fallback réseau en cas de JSON satellite *stale* (> 90s). À la place, basculer instantanément le moteur en mode `READ-ONLY / NO-NEW-ENTRIES` pour stopper net l'hémorragie d'appels et figer l'exposition.
2. **Clarification Sémantique & Nettoyage du Code Mort :**
   * *Proposition :* Unifier la nomenclature entre le runtime (`state.json`) et le cockpit via un DTO unique et strict. Supprimer purement et simplement les commentaires contradictoires (QNT/FLUID/RWA/MNSRY) et purger la configuration des paires dont la liquidité moyenne sur 7 jours est inférieure au seuil critique de `NOTIONAL * 50`.
3. **Refonte de la Supervision Cockpit (Isolation Hulk) :**
   * *Proposition :* Créer un namespace étanche dans le cockpit dédié exclusivement à Hulk runtime, masquant totalement les vieux sous-systèmes ACE/Vortex archivés pour garantir un diagnostic forensique immédiat sans bruit de fond historique.

---

### 5. PRIORITÉS
- **P0 :** Corriger le comportement du fallback satellite (interdire l'augmentation des appels réseau sur *stale*) et résoudre la contradiction sémantique positions/bags entre le runtime et le cockpit.
- **P1 :** Nettoyer la configuration des paires illiquides et purger les contradictions documentaires dans le code (`BAG_PAIRS` vs profils).
- **P2 :** Isoler proprement les métriques Hulk dans le cockpit en masquant l'historique ACE/V
