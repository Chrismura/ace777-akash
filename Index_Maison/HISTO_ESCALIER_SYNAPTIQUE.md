# Historique — Escalier synaptique (28 fév. 2026)

**Statut :** 🟢 GARDÉ **archive ops** · 🔴 **pas** de relance sans GO + Mac froid + tag neuf  
**Source :** commande « ESCALIER SYNAPTIQUE » vérifiée 2026-02-28 18:40 UTC (Gemini/Cursor époque)  
**Valeur :** A2 (léçon params) · B1 si on compare fills vs stack actuelle

---

## Ce que c’était

Run **4h** timer Ruby + `caffeinate` + clone futures V2, log dédié, molettes « escalier » (seuils bas, soft anomaly, trail serré).

### Intent (lecture)

| Idée | Traduction technique |
|------|----------------------|
| Escalier / synapse | Enchaîner cycles avec **soft hold** + anomaly soft |
| Momentum bas (0.60) | Plus permissif que V8.3 (0.85) / fortress (0.96) |
| Radar ON · Trend OFF | Filtre direction carnet, pas MA |
| Soft neutral 40s · min hold anomaly 3 | Éviter chop / sorties précoces |
| Min profit 10 bps · SL 5 · trail 2 | Scalping serré |
| Leverage 5 · Buy 250 | BETA-like size |

### Différence vs stack actuelle (NUAGE / V8.6)

| | Escalier fév. | Agora juil. |
|--|---------------|-------------|
| Entrée | `ACE777_STRICT_CLONE…` direct | `GO_USINE_NUAGE.sh` + duo BETA/ALPHA |
| Impulse / tension V8 | Non (stack plus vieille) | Resonance + Tension + storm |
| Timer | `ruby sleep` + `STOP` | wait-timer NUAGE + STOP_ALPHA/BETA |
| Tag / log | `ACE777_ESCALIER_4H.csv` | `NUAGE_TEST_*` |

**Léçon :** l’escalier = **piste de soft-hold / anomaly** à comparer en paper — pas à coller à l’aveugle sur le champion NUAGE.

---

## Commande (archive — ne pas coller pendant un vol)

> Stockée pour mémoire. Relance = **GO explicite** + stérilité + nouveau tag CSV.

```bash
cd /Users/christophe/ace777-test-day1 && rm -f STOP && (ruby -e 'sleep 14400; File.write("STOP","")' &) && caffeinate -is bash -c 'LOG_FILE="runs/ACE777_SYNCHRO_REEL_7H/ACE777_ESCALIER_4H.csv" ENABLE_ORDERS=TRUE CYCLES=999999 LEVERAGE=5 BUY_USDT=250 MOMENTUM_THRESHOLD=0.60 POLL_SEC=0.10 TREND_FILTER=FALSE RADAR_GATE=TRUE ANOMALY_SOFT_MODE=TRUE SOFT_NEUTRAL_HOLD_SEC=40 MIN_HOLD_FOR_ANOMALY=3 MIN_PROFIT_BPS=10 STOP_LOSS_BPS=5 TRAIL_GIVEBACK_BPS=2 bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh'
```

---

## Board

| Item | Statut |
|------|--------|
| Archive escalier | 🟢 GARDÉ histo |
| Relance telle quelle | 🔴 REFUS sans GO + revue |
| Idée soft anomaly / min hold | 🔵 WATCH à tester via molettes modernes si GO |

Liens : [[OSSATURE_INDEX]] · [[ARCHITECTURE_AGORA]] · [[MEMOIRE_PERSO_SYNTONIE_PERMABEL]]
