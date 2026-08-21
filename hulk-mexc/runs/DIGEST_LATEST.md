# Hulk DIGEST — 2026-08-21T20:17:59Z

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
| PYTHUSDT | IDLE | 1.33 | 4.78 | 3.05 | 0.08 | 5492196.2 | 2.11 | skipped_fast |
| XRPUSDT | IDLE | 1.24 | 4.21 | 2.96 | 0.11 | 129081833.56 | 2.18 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 13.22 | 0.16 | 153444.8 | 21.23 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 10.86 | 6.04 | 0.11 | 477633.57 | 13.56 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 3.91 | 1.52 | 0.08 | 633097.97 | 5.59 | skipped_fast |
| HBARUSDT | IDLE | 1.75 | 3.23 | 2.25 | 0.06 | 796064.87 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.67 | 0.08 | 512692.76 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.12 | 3.92 | 2.1 | 0.06 | 367806.65 | 13.81 | skipped_fast |
| BIOUSDT | IDLE | 2.55 | 5.33 | 3.04 | 0.01 | 190169.63 | 3.16 | skipped_fast |
| EDELUSDT | IDLE | 2.65 | 4.65 | 4.33 | -0.05 | 80210.05 | 11.33 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.54 | 0.02 | 56223.16 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.03 | 11163.46 | 37.5 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.72 | 0.1 | 61242.68 | 11.2 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.0 | 2802.39 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 3.39 | 2.17 | 0.01 | 183762.59 | 27.01 | skipped_fast |
| QNTUSDT | IDLE | 1.42 | 2.65 | 1.31 | 0.04 | 59962.5 | 6.23 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 54447.83 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
