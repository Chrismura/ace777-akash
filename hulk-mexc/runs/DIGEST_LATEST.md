# Hulk DIGEST — 2026-08-28T14:06:22Z

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
| XRPUSDT | IDLE | 1.54 | 2.77 | 2.05 | -0.03 | 49893828.29 | 7.13 | skipped_fast |
| PYTHUSDT | IDLE | 1.92 | 3.77 | 3.59 | -0.05 | 1211529.4 | 14.9 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.36 | 12.74 | 1.32 | 0.15 | 977127.68 | 13.39 | skipped_fast |
| QAITUSDT | IDLE | 2.44 | 32.58 | 21.1 | -0.2 | 64293.45 | 46.67 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 2.51 | 2.18 | -0.05 | 405302.81 | 11.7 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 4.26 | 2.47 | -0.0 | 242654.64 | 36.73 | skipped_fast |
| WUSDT | IDLE | 1.47 | 2.56 | 2.48 | -0.04 | 197334.17 | 1.08 | skipped_fast |
| RIZEUSDT | IDLE | 1.42 | 7.12 | 1.35 | -0.09 | 103202.68 | 56.88 | skipped_fast |
| REDUSDT | IDLE | 1.48 | 2.74 | 1.42 | -0.03 | 73383.99 | 20.66 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 2.15 | 2.1 | -0.02 | 74578.32 | 12.01 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.63 | 1.57 | -0.04 | 83700.26 | 10.64 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.84 | 1.6 | -0.03 | 308518.94 | 6.5 | skipped_fast |
| RWAINCUSDT | IDLE | 1.25 | 4.22 | 1.07 | 0.01 | 19055.28 | 102.51 | skipped_fast |
| EDELUSDT | IDLE | 0.53 | 2.43 | 1.53 | -0.07 | 55951.03 | 43.08 | skipped_fast |
| QNTUSDT | IDLE | 1.61 | 2.82 | 2.66 | -0.01 | 47223.46 | 6.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.62 | 2.93 | 2.01 | -0.03 | 4507.19 | 0.75 | skipped_fast |
| TELUSDT | IDLE | 1.33 | 2.91 | 2.82 | -0.02 | 133539.79 | 49.93 | skipped_fast |
| RWAUSDT | IDLE | 1.19 | 2.11 | 1.82 | -0.01 | 53335.69 | 25.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
