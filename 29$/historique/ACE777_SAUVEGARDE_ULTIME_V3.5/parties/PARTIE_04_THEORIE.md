# [PARTIE 4] — EXPLICATIONS THÉORIQUES DES PHÉNOMÈNES DE MARCHÉ (HORS CONFIG)

**Statut:** ✅ Compilé  
**Réf:** ACE777_SAUVEGARDE_ULTIME_V3.5  

---

## 4.1. Le Principe du Temps de Réponse (Tuning Concept)

L'éclaireur BETA cycle ~8–12 s ; le chasseur ALPHA ~8–15 s avec gate NUAGE **800 ms** sur `duo_state.ts_ms`. Le décalage stroboscopique vise **~2 s** entre publication tension BETA et frappe ALPHA.

**Tension ≠ trigger:** ALPHA lit l'état duo post-trade (RAM), pas la tension V8 instantanée. Un tuning efficace ne synchronise pas les numéros de cycle mais la **fraîcheur RAM** (`age_ms < 800`).

Si BETA freeze (pause pacing) ou meurt (SIGTERM), `duo_state` vieillit → `tension_stale` / `stale_state` → ALPHA dormante. Le watchdog sémantique relance ALPHA mais **ts_ms BETA reste la vérité**.

**Écart de sensibilité:** BETA réagit aux micro-mouvements en scout (levier x5, hold court). ALPHA en hunter x13 a une fenêtre d'entrée plus étroite : elle doit arriver dans les 800 ms post-publication du cadavre scout, sinon le choc s'est dissipé.

---

## 4.2. Le Phénomène de Hachage Microstructurel (Whipsaw ~4$ — 15/07 05:25)

**Observation matin 15/07 ~05:25 UTC:**

```
BETA #189: SELL flat pnl=0.00000000 @ 64651.80 (05:21:11)
BETA #190: SELL perte -0.00760000 @ 64654.80→64655.80 (05:21:33)
ALPHA #94: BUY hunter_revenge perte -0.96480000 @ 64655.80→64651.80 (05:25:14, hold ~7s)
```

Amplitude BTC ~**4 $** — micro-oscillation symétrique.

**Théorie (aucun code):**

1. **Détection adversaire < 10 ms:** les makers HFT testnet/mainnet détectent la signature répétitive (levier × masse × hold 6–7 s × hunter_revenge_1.5x) quasi instantanément.

2. **Transit Surf 400–600 ms:** la ligne fapi (ping preflight ~444 ms typique) ajoute un RTT aller-retour. ALPHA entre **après** que le carnet ait inversé la microstructure locale.

3. **Whipsaw symétrique:** BETA vend sur choc → carnet absorbe → prix remonte légèrement → ALPHA achète au sommet local → prix retombe de ~4$ → sortie `shock_inversion_stop` en perte.

4. **Conséquence systémique:** le coupling logique (revenge valide) peut produire un PnL négatif sur micro-amplitude quand la latence Surf dépasse la fenêtre de cohérence du carnet.

---

## 4.3. Le Concept de Double Standard (Principe de Retournement)

En phase **baissière lourde**, le setup canonique SHORT/LONG peut sous-performer :
- BETA SHORT grattte les rebonds techniques
- ALPHA LONG chasse contre la tendance dominante → drawdowns cumulés

**Concept inverse (non implémenté dans 37fca367):**

| Rôle | Setup canonique | Double standard |
|---|---|---|
| BETA (scout) | SHORT / SELL | **LONG / BUY** |
| ALPHA (hunter) | LONG / BUY | **SHORT / SELL** |

L'inversion adapterait les rôles à la dérive baissière : l'éclaireur achète les squeezes, le chasseur vend les rechutes post-perte scout.

**Statut:** documenté pour recherche future — le champion actuel force `FORCE_ENTRY_SIDE=SELL` (BETA) et `BUY` (ALPHA) dans l'enveloppe NUAGE.
