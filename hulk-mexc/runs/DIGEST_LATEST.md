# Hulk DIGEST — 2026-08-31T03:15:22Z

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
| XRPUSDT | IDLE | 2.83 | 5.09 | 3.76 | -0.03 | 34424979.54 | 2.22 | skipped_fast |
| ETHUSDT | IDLE | 2.32 | 4.21 | 2.93 | -0.02 | 384148684.78 | 0.46 | skipped_fast |
| BTCUSDT | IDLE | 1.28 | 2.34 | 1.44 | -0.01 | 395313864.12 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.08 | 7.25 | 4.45 | -0.02 | 532358.94 | 2.14 | skipped_fast |
| CHIPUSDT | IDLE | 2.07 | 6.38 | 3.56 | -0.04 | 515936.83 | 2.6 | skipped_fast |
| WUSDT | IDLE | 3.18 | 6.33 | 0.98 | 0.02 | 236986.41 | 11.75 | skipped_fast |
| BIOUSDT | IDLE | 3.36 | 6.22 | 3.55 | -0.05 | 88210.74 | 3.8 | skipped_fast |
| EDELUSDT | IDLE | 3.04 | 6.32 | 4.5 | 0.04 | 86940.61 | 16.81 | skipped_fast |
| KITEUSDT | IDLE | 2.66 | 7.34 | 4.01 | -0.07 | 91096.34 | 12.52 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 4.26 | 1.35 | -0.02 | 211905.93 | 10.2 | skipped_fast |
| REDUSDT | IDLE | 2.36 | 4.49 | 1.54 | -0.0 | 62312.92 | 10.11 | skipped_fast |
| RIZEUSDT | IDLE | 2.47 | 4.59 | 2.35 | -0.01 | 37566.62 | 60.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.07 | 2.78 | 0.53 | -0.04 | 223979.46 | 18.11 | skipped_fast |
| FLUIDUSDT | IDLE | 3.12 | 5.58 | 4.43 | -0.02 | 3849.88 | 21.72 | skipped_fast |
| HBARUSDT | IDLE | 1.77 | 3.18 | 2.44 | -0.02 | 213608.55 | 1.36 | skipped_fast |
| TELUSDT | IDLE | 1.71 | 3.05 | 2.5 | -0.01 | 82632.34 | 47.62 | skipped_fast |
| RWAINCUSDT | IDLE | 1.14 | 1.98 | 1.94 | 0.0 | 2191.44 | 90.34 | skipped_fast |
| QNTUSDT | IDLE | 1.39 | 2.59 | 1.23 | -0.02 | 40671.62 | 6.63 | skipped_fast |
| MNSRYUSDT | IDLE | 0.91 | 1.64 | 1.22 | -0.01 | 31049.35 | 31.14 | skipped_fast |
| RWAUSDT | IDLE | 0.77 | 1.39 | 1.05 | 0.01 | 52315.2 | 40.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
