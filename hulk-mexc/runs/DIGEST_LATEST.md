# Hulk DIGEST — 2026-09-28T06:19:07Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.97 | 9.65 | 7.62 | -0.02 | 5013295.31 | 10.4 | skipped_fast |
| PYTHUSDT | IDLE | 2.5 | 6.54 | 3.61 | -0.04 | 1964949.04 | 4.89 | skipped_fast |
| XRPUSDT | IDLE | 1.89 | 3.43 | 2.33 | -0.02 | 51589335.85 | 2.02 | skipped_fast |
| QNTUSDT | IDLE | 0.44 | 14.54 | 3.24 | 0.51 | 16045530.31 | 12.67 | skipped_fast |
| BTCUSDT | IDLE | 1.03 | 1.87 | 1.22 | -0.02 | 564814000.67 | 0.05 | skipped_fast |
| ETHUSDT | IDLE | 0.9 | 1.64 | 1.07 | -0.02 | 274828127.22 | 0.23 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.93 | 9.05 | 5.73 | 0.01 | 826253.41 | 8.76 | skipped_fast |
| HBARUSDT | IDLE | 2.4 | 4.67 | 0.87 | 0.04 | 1200442.36 | 1.02 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.54 | 6.66 | 5.42 | -0.05 | 98544.77 | 6.63 | skipped_fast |
| KITEUSDT | IDLE | 2.97 | 6.18 | 4.76 | -0.04 | 107906.89 | 9.74 | skipped_fast |
| RIZEUSDT | IDLE | 2.23 | 13.55 | 6.0 | -0.15 | 59299.11 | 18.14 | skipped_fast |
| REDUSDT | IDLE | 2.23 | 4.67 | 4.03 | -0.05 | 66045.3 | 6.74 | skipped_fast |
| ZBCNUSDT | IDLE | 1.34 | 2.44 | 1.59 | -0.03 | 242890.55 | 7.36 | skipped_fast |
| EDELUSDT | IDLE | 1.23 | 6.77 | 2.78 | -0.12 | 176021.93 | 27.77 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 4.42 | 3.04 | -0.08 | 87166.6 | 15.57 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 5.45 | 5.17 | -0.03 | 3554.0 | 47.12 | skipped_fast |
| RWAINCUSDT | IDLE | 0.56 | 5.61 | 2.25 | 0.21 | 31610.4 | 23.85 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 2.69 | 2.46 | 0.05 | 172270.75 | 54.95 | skipped_fast |
| RWAUSDT | IDLE | 0.79 | 1.44 | 0.92 | -0.01 | 59972.43 | 28.65 | skipped_fast |
| MNSRYUSDT | IDLE | 1.1 | 2.01 | 1.29 | -0.01 | 38715.63 | 55.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
