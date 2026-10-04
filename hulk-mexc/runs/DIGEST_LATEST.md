# Hulk DIGEST — 2026-10-04T15:02:09Z

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
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 8.46 | 0.79 | 0.04 | 3153811.12 | 6.95 | skipped_fast |
| ETHUSDT | IDLE | 0.3 | 0.55 | 0.35 | 0.01 | 102131906.46 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.28 | 0.52 | 0.27 | 0.01 | 15979006.49 | 2.0 | skipped_fast |
| BTCUSDT | IDLE | 0.21 | 0.39 | 0.18 | 0.01 | 308654536.76 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.35 | 7.02 | 3.24 | 0.09 | 1001364.83 | 15.48 | skipped_fast |
| EDELUSDT | IDLE | 2.05 | 8.11 | 2.67 | 0.16 | 517134.53 | 2.06 | skipped_fast |
| CHIPUSDT | IDLE | 3.01 | 5.95 | 2.54 | 0.05 | 60030.96 | 13.04 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 12.28 | 1.76 | -0.02 | 51893.23 | 65.77 | skipped_fast |
| CCUSDT | IDLE | 1.59 | 3.16 | 0.2 | 0.03 | 327237.69 | 5.56 | skipped_fast |
| MNSRYUSDT | IDLE | 3.5 | 6.42 | 3.88 | 0.0 | 46842.23 | 11.59 | skipped_fast |
| PYTHUSDT | IDLE | 0.96 | 1.79 | 0.88 | -0.0 | 316428.66 | 2.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.21 | 2.27 | 1.03 | -0.01 | 235720.53 | 27.73 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 2.85 | 2.4 | -0.02 | 83649.28 | 10.12 | skipped_fast |
| REDUSDT | IDLE | 1.53 | 2.84 | 1.5 | -0.02 | 66274.48 | 12.69 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.51 | 0.18 | 0.0 | 439755.02 | 6.83 | skipped_fast |
| BIOUSDT | IDLE | 0.64 | 1.18 | 0.68 | -0.03 | 67851.02 | 6.53 | skipped_fast |
| RWAINCUSDT | IDLE | 0.44 | 0.83 | 0.35 | 0.06 | 5622.24 | 31.43 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 1.75 | 1.35 | -0.01 | 137388.03 | 31.63 | skipped_fast |
| RWAUSDT | IDLE | 0.2 | 0.37 | 0.22 | -0.0 | 55100.41 | 14.61 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.04 | 1706.42 | 23.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
