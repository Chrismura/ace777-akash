# Hulk DIGEST — 2026-09-26T04:50:41Z

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
| XRPUSDT | IDLE | 1.07 | 1.91 | 1.59 | 0.01 | 109965165.94 | 1.93 | skipped_fast |
| ETHUSDT | IDLE | 0.29 | 0.54 | 0.24 | 0.0 | 300632464.49 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.41 | 0.17 | -0.0 | 650519976.67 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.26 | 3.33 | 1.56 | 0.08 | 1200370.13 | 4.06 | skipped_fast |
| CCUSDT | IDLE | 1.2 | 5.0 | 2.81 | 0.14 | 912326.28 | 12.14 | skipped_fast |
| HBARUSDT | IDLE | 1.33 | 2.35 | 2.05 | 0.02 | 897151.69 | 1.06 | skipped_fast |
| QNTUSDT | IDLE | 2.29 | 7.46 | 5.77 | 0.02 | 552680.4 | 6.06 | skipped_fast |
| WUSDT | IDLE | 1.45 | 2.68 | 1.84 | 0.05 | 454970.01 | 9.77 | skipped_fast |
| ZBCNUSDT | IDLE | 1.89 | 4.21 | 3.43 | 0.03 | 226484.4 | 22.8 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 4.96 | 3.66 | 0.05 | 148741.66 | 16.33 | skipped_fast |
| KITEUSDT | IDLE | 2.0 | 5.63 | 1.75 | 0.09 | 78700.16 | 9.46 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 3.38 | 2.38 | 0.02 | 85674.36 | 16.92 | skipped_fast |
| BIOUSDT | IDLE | 1.11 | 2.93 | 2.25 | 0.05 | 113578.12 | 3.07 | skipped_fast |
| EDELUSDT | IDLE | 0.76 | 1.5 | 0.17 | 0.01 | 168366.61 | 6.75 | skipped_fast |
| RIZEUSDT | IDLE | 0.2 | 2.64 | 0.85 | -0.18 | 78152.56 | 41.47 | skipped_fast |
| TELUSDT | IDLE | 0.71 | 1.23 | 1.21 | 0.01 | 112768.99 | 6.13 | skipped_fast |
| RWAINCUSDT | IDLE | 0.25 | 0.71 | 0.71 | -0.1 | 12751.69 | 60.88 | skipped_fast |
| FLUIDUSDT | IDLE | 1.05 | 1.83 | 1.79 | 0.0 | 3437.87 | 21.77 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.04 | 0.44 | -0.01 | 52906.32 | 7.38 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.91 | 0.48 | 0.01 | 41088.35 | 39.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
