# Hulk DIGEST — 2026-08-19T18:17:46Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 3.29 | 6.37 | 1.38 | 0.06 | 25415827.66 | 1.89 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.01 | 17.91 | 7.4 | 0.02 | 126148.1 | 15.73 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.69 | 9.56 | 0.05 | 0.09 | 275901.6 | 9.13 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 15.26 | 4.15 | 0.15 | 127941.76 | 10.57 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.75 | 13.04 | 1.43 | 0.11 | 70940.47 | 36.25 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 19.8 | 7.85 | 0.09 | 166363.38 | 70.49 | skipped_fast |
| PYTHUSDT | IDLE | 2.96 | 5.74 | 1.23 | 0.04 | 249245.99 | 2.5 | skipped_fast |
| RIZEUSDT | IDLE | 4.2 | 8.15 | 2.73 | -0.05 | 35842.03 | 51.27 | skipped_fast |
| ZBCNUSDT | IDLE | 3.02 | 6.95 | 1.21 | 0.08 | 197532.24 | 19.09 | skipped_fast |
| WUSDT | IDLE | 2.76 | 5.32 | 1.27 | 0.04 | 164484.37 | 11.84 | skipped_fast |
| CHIPUSDT | IDLE | 2.29 | 7.24 | 3.32 | 0.03 | 159282.21 | 7.17 | skipped_fast |
| QAITUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.21 | 9.16 | 0.0 | 0.05 | 11445.62 | 62.16 | skipped_fast |
| KITEUSDT | IDLE | 2.72 | 5.16 | 1.92 | 0.03 | 57527.68 | 15.85 | skipped_fast |
| FLUIDUSDT | IDLE | 3.4 | 7.57 | 2.77 | 0.02 | 2336.32 | 21.13 | skipped_fast |
| HBARUSDT | IDLE | 2.23 | 4.2 | 1.77 | 0.05 | 247431.73 | 1.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.0 | 5.91 | 2.9 | 0.04 | 17123.25 | 45.77 | skipped_fast |
| QNTUSDT | IDLE | 1.95 | 3.67 | 1.52 | 0.03 | 38047.12 | 8.69 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.49 | 0.78 | -0.0 | 53562.66 | 17.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
