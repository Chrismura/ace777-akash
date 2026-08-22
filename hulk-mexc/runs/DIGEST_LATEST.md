# Hulk DIGEST — 2026-08-22T15:42:44Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.4 | 0.04 | 51500023.85 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.39 | 7.64 | 6.19 | 0.02 | 215978339.54 | 2.09 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 5.65 | 3.06 | 0.09 | 793527.09 | 10.32 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.21 | -0.02 | 1156153.91 | 6.54 | skipped_fast |
| CHIPUSDT | IDLE | 0.62 | 3.51 | 2.03 | -0.09 | 605173.65 | 3.39 | skipped_fast |
| WUSDT | IDLE | 0.77 | 3.17 | 1.47 | -0.02 | 553280.19 | 15.98 | skipped_fast |
| KITEUSDT | IDLE | 2.76 | 6.37 | 2.0 | 0.03 | 85386.35 | 13.41 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 3.49 | 1.84 | -0.05 | 320126.74 | 20.05 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.11 | -0.07 | 220977.09 | 6.64 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.52 | 1.9 | -0.04 | 79059.02 | 22.78 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 5.14 | -0.12 | 144047.19 | 12.92 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.32 | 0.03 | 56464.76 | 23.62 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.21 | -0.02 | 185107.85 | 6.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 69.84 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.63 | -0.01 | 140519.27 | 48.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 23.22 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.48 | 0.02 | 57455.95 | 16.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
