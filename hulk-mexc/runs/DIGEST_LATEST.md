# Hulk DIGEST — 2026-09-05T11:24:50Z

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
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 57.48 | 33.0 | -0.04 | 220819.45 | 18.67 | skipped_fast |
| XRPUSDT | IDLE | 0.49 | 0.89 | 0.58 | -0.03 | 37793599.88 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.22 | 0.4 | 0.29 | -0.03 | 362282524.09 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.14 | 0.25 | 0.16 | -0.02 | 496459495.53 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.92 | 6.84 | 6.06 | -0.02 | 452353.22 | 1.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.94 | 25.72 | 17.92 | -0.16 | 155921.36 | 97.17 | skipped_fast |
| PYTHUSDT | IDLE | 0.9 | 1.7 | 0.63 | -0.02 | 427395.71 | 1.85 | skipped_fast |
| CCUSDT | IDLE | 0.53 | 0.99 | 0.44 | -0.02 | 330401.28 | 10.14 | skipped_fast |
| WUSDT | IDLE | 0.76 | 1.4 | 0.82 | 0.01 | 205435.17 | 14.13 | skipped_fast |
| REDUSDT | IDLE | 1.26 | 2.32 | 2.02 | 0.04 | 65405.33 | 10.32 | skipped_fast |
| ZBCNUSDT | IDLE | 0.65 | 1.42 | 0.2 | -0.04 | 198474.28 | 5.82 | skipped_fast |
| KITEUSDT | IDLE | 1.14 | 2.11 | 1.09 | -0.03 | 63384.25 | 9.88 | skipped_fast |
| BIOUSDT | IDLE | 0.79 | 1.39 | 1.27 | -0.01 | 84908.36 | 7.32 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 1.6 | 0.62 | 0.02 | 288020.82 | 1.25 | skipped_fast |
| RWAUSDT | IDLE | 1.71 | 3.38 | 0.28 | 0.01 | 52890.41 | 28.57 | skipped_fast |
| RWAINCUSDT | IDLE | 0.86 | 1.52 | 1.33 | -0.01 | 5271.81 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 0.96 | 1.72 | 1.28 | -0.04 | 73272.11 | 35.48 | skipped_fast |
| FLUIDUSDT | IDLE | 0.96 | 1.92 | 0.0 | -0.01 | 1031.33 | 22.51 | skipped_fast |
| QNTUSDT | IDLE | 0.48 | 0.91 | 0.4 | -0.04 | 45002.86 | 4.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.31 | 0.3 | -0.01 | 36354.4 | 30.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
