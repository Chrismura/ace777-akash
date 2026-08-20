# Hulk DIGEST — 2026-08-20T08:22:43Z

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
| XRPUSDT | IDLE | 1.33 | 4.34 | 0.52 | 0.12 | 48753917.88 | 1.77 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.63 | 24.94 | 7.78 | 0.26 | 177903.69 | 11.59 | skipped_fast |
| BIOUSDT | IDLE | 1.7 | 11.24 | 1.11 | 0.23 | 207510.08 | 9.59 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 4.29 | 0.01 | 0.15 | 390570.05 | 8.72 | skipped_fast |
| RIZEUSDT | IDLE | 1.89 | 12.34 | 9.04 | 0.11 | 68508.27 | 39.82 | skipped_fast |
| WUSDT | IDLE | 1.48 | 3.33 | 0.43 | 0.08 | 291281.01 | 13.71 | skipped_fast |
| EDELUSDT | IDLE | 1.47 | 11.14 | 9.01 | 0.22 | 101989.33 | 22.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 5.32 | 2.83 | 0.13 | 226693.15 | 3.42 | skipped_fast |
| PYTHUSDT | IDLE | 0.87 | 3.05 | 0.69 | 0.11 | 309544.38 | 4.63 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.22 | 0.28 | 0.07 | 388728.92 | 1.38 | skipped_fast |
| ZBCNUSDT | IDLE | 1.0 | 4.1 | 0.23 | 0.15 | 234368.47 | 19.26 | skipped_fast |
| KITEUSDT | IDLE | 0.77 | 1.51 | 0.14 | 0.06 | 59960.52 | 15.52 | skipped_fast |
| QAITUSDT | IDLE | 1.24 | 3.52 | 1.12 | 0.06 | 10520.97 | 64.48 | skipped_fast |
| RWAINCUSDT | IDLE | 0.67 | 1.88 | 1.23 | 0.05 | 17298.97 | 22.61 | skipped_fast |
| FLUIDUSDT | IDLE | 1.9 | 5.66 | 0.34 | 0.12 | 2868.92 | 21.58 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.71 | 0.05 | 0.06 | 37416.13 | 3.33 | skipped_fast |
| TELUSDT | IDLE | 0.56 | 2.69 | 0.43 | 0.14 | 193853.49 | 36.63 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.78 | 0.26 | 0.02 | 54004.66 | 8.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
