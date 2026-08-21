# Hulk DIGEST — 2026-08-21T21:01:43Z

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
| PYTHUSDT | IDLE | 1.21 | 4.51 | 1.58 | 0.09 | 5575079.71 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.18 | 3.73 | 2.82 | 0.1 | 128234227.69 | 2.18 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 8.19 | 5.95 | 0.08 | 480268.18 | 51.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 4.62 | 3.55 | 0.08 | 514415.39 | 6.18 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.28 | 0.1 | 641698.94 | 8.28 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.04 | 1.51 | 0.06 | 809396.42 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.83 | 0.86 | 0.07 | 368214.03 | 10.49 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 5.2 | 2.7 | 0.01 | 187783.8 | 3.16 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.72 | 0.17 | 152949.67 | 26.19 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 4.12 | 2.97 | -0.05 | 82438.4 | 22.7 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.46 | 0.01 | 56230.07 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.04 | 10901.49 | 32.14 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.0 | 2.24 | 0.11 | 61230.91 | 10.22 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.37 | 0.01 | 181186.84 | 32.19 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.68 | 0.03 | 60168.13 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 175.02 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.08 | 0.74 | 0.03 | 53804.37 | 24.93 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
