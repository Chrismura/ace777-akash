# Hulk DIGEST — 2026-09-28T03:16:21Z

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
| QNTUSDT | IDLE | 2.12 | 68.44 | 31.05 | 0.51 | 14759812.33 | 8.18 | skipped_fast |
| WUSDT | IDLE | 2.33 | 8.93 | 7.97 | 0.06 | 5344675.14 | 14.29 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 3.33 | 2.29 | 0.01 | 2002181.83 | 2.41 | skipped_fast |
| XRPUSDT | IDLE | 1.52 | 2.69 | 2.29 | -0.02 | 48035046.5 | 1.33 | skipped_fast |
| ETHUSDT | IDLE | 1.15 | 2.04 | 1.77 | -0.02 | 248633182.24 | 0.15 | skipped_fast |
| BTCUSDT | IDLE | 1.09 | 1.9 | 1.85 | -0.01 | 482259104.33 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.14 | 7.73 | 1.16 | 0.06 | 725266.66 | 10.47 | skipped_fast |
| HBARUSDT | IDLE | 2.4 | 4.38 | 2.84 | 0.01 | 919706.78 | 2.1 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 7.74 | 6.5 | -0.07 | 109905.49 | 9.01 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 6.05 | 5.46 | -0.03 | 89220.66 | 3.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.7 | 3.05 | 2.33 | -0.02 | 247974.17 | 9.82 | skipped_fast |
| REDUSDT | IDLE | 2.21 | 3.86 | 3.69 | -0.03 | 66540.3 | 14.54 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 4.35 | 3.89 | -0.06 | 94853.38 | 15.42 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 7.71 | 4.25 | -0.12 | 157987.93 | 52.14 | skipped_fast |
| RIZEUSDT | IDLE | 1.41 | 13.55 | 6.71 | -0.22 | 65416.61 | 70.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.69 | 6.69 | 3.65 | 0.22 | 31261.1 | 36.01 | skipped_fast |
| FLUIDUSDT | IDLE | 2.36 | 4.13 | 3.97 | 0.01 | 3567.99 | 21.98 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.24 | 1.76 | 0.02 | 174790.87 | 16.3 | skipped_fast |
| MNSRYUSDT | IDLE | 1.1 | 1.98 | 1.5 | -0.0 | 39673.48 | 59.04 | skipped_fast |
| RWAUSDT | IDLE | 0.68 | 1.22 | 0.99 | 0.0 | 59282.42 | 35.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
