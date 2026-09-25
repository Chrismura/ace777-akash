# Hulk DIGEST — 2026-09-25T15:44:57Z

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
| XRPUSDT | IDLE | 2.88 | 5.5 | 3.71 | 0.04 | 116546368.0 | 2.55 | skipped_fast |
| ETHUSDT | IDLE | 1.51 | 2.63 | 2.54 | -0.0 | 381518428.91 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.39 | 2.46 | 2.08 | -0.01 | 751252252.04 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.36 | 6.36 | 2.04 | 0.06 | 1266312.72 | 1.37 | skipped_fast |
| CCUSDT | IDLE | 2.12 | 7.29 | 2.31 | 0.11 | 781119.97 | 9.69 | skipped_fast |
| HBARUSDT | IDLE | 2.5 | 4.39 | 4.04 | 0.01 | 976365.08 | 2.15 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.59 | 10.33 | 5.81 | 0.05 | 114424.46 | 9.34 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.64 | 8.93 | 1.43 | 0.07 | 196708.32 | 26.32 | skipped_fast |
| WUSDT | IDLE | 2.17 | 3.97 | 2.42 | 0.01 | 362904.6 | 7.58 | skipped_fast |
| QNTUSDT | IDLE | 1.3 | 8.52 | 6.04 | 0.16 | 577437.45 | 6.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 6.19 | 4.08 | 0.08 | 170778.65 | 20.73 | skipped_fast |
| KITEUSDT | IDLE | 2.47 | 4.62 | 2.19 | -0.02 | 73497.73 | 11.5 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 16.89 | 11.6 | 0.56 | 132003.08 | 50.76 | skipped_fast |
| REDUSDT | IDLE | 1.81 | 3.84 | 1.75 | 0.06 | 135737.22 | 12.9 | skipped_fast |
| EDELUSDT | IDLE | 0.49 | 5.36 | 1.39 | 0.1 | 216541.99 | 20.05 | skipped_fast |
| TELUSDT | IDLE | 1.73 | 3.11 | 2.31 | -0.0 | 121287.04 | 36.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.99 | 3.47 | 3.36 | 0.02 | 3184.11 | 21.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.02 | 3.53 | 2.22 | 0.0 | 22509.71 | 96.42 | skipped_fast |
| MNSRYUSDT | IDLE | 1.28 | 2.42 | 1.0 | 0.01 | 42177.13 | 12.78 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.1 | 1.02 | -0.0 | 58060.59 | 7.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
