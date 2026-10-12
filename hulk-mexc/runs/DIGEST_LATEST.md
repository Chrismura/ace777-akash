# Hulk DIGEST — 2026-10-12T10:52:02Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.19 | 14.73 | 1.12 | 0.17 | 1720254.77 | 14.57 | skipped_fast |
| WUSDT | IDLE | 0.82 | 15.49 | 10.97 | 0.64 | 14446408.69 | 16.26 | skipped_fast |
| XRPUSDT | IDLE | 0.82 | 1.48 | 1.07 | 0.01 | 24007697.12 | 2.13 | skipped_fast |
| BTCUSDT | IDLE | 0.68 | 1.22 | 0.92 | 0.01 | 240294431.77 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.17 | 0.82 | 0.02 | 254933281.78 | 0.04 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 25.76 | 12.98 | 0.13 | 165988.11 | 17.47 | skipped_fast |
| QNTUSDT | IDLE | 2.14 | 3.88 | 2.61 | -0.02 | 822695.29 | 0.42 | skipped_fast |
| CHIPUSDT | IDLE | 2.49 | 7.86 | 2.72 | -0.04 | 196294.32 | 15.32 | skipped_fast |
| KITEUSDT | IDLE | 2.31 | 4.44 | 1.2 | 0.05 | 63410.83 | 9.14 | skipped_fast |
| CCUSDT | IDLE | 0.89 | 1.61 | 1.18 | 0.05 | 389872.4 | 10.35 | skipped_fast |
| EDELUSDT | IDLE | 1.33 | 2.5 | 1.05 | -0.03 | 240132.1 | 7.95 | skipped_fast |
| HBARUSDT | IDLE | 1.51 | 2.74 | 1.83 | 0.03 | 479335.08 | 3.21 | skipped_fast |
| ZBCNUSDT | IDLE | 0.93 | 1.91 | 0.48 | 0.06 | 277420.08 | 14.52 | skipped_fast |
| BIOUSDT | IDLE | 1.49 | 2.69 | 1.96 | 0.01 | 101960.76 | 3.39 | skipped_fast |
| RIZEUSDT | IDLE | 1.25 | 7.57 | 4.47 | 0.12 | 51300.61 | 56.23 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 3.49 | 0.9 | 0.02 | 184411.73 | 28.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.7 | 1.99 | 1.35 | -0.01 | 18701.76 | 20.24 | skipped_fast |
| MNSRYUSDT | IDLE | 0.85 | 1.48 | 1.43 | 0.0 | 38208.29 | 23.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 2.76 | 0.47 | 0.02 | 61757.22 | 21.25 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.54 | 0.38 | 0.03 | 52699.53 | 7.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
