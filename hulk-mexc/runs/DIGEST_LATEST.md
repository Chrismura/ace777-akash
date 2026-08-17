# Hulk DIGEST — 2026-08-17T03:10:02Z

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
| XRPUSDT | IDLE | 0.83 | 1.62 | 0.31 | -0.0 | 7896327.19 | 1.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.53 | 26.44 | 19.54 | 0.04 | 42843.57 | 34.44 | skipped_fast |
| CHIPUSDT | IDLE | 1.51 | 7.11 | 0.92 | 0.07 | 293606.62 | 6.87 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 1.94 | 0.8 | -0.03 | 292962.03 | 9.4 | skipped_fast |
| WUSDT | IDLE | 0.99 | 1.77 | 1.39 | 0.01 | 187694.99 | 10.56 | skipped_fast |
| EDELUSDT | IDLE | 1.91 | 3.58 | 1.54 | 0.04 | 55519.22 | 51.88 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 2.62 | 1.57 | -0.01 | 54134.57 | 14.87 | skipped_fast |
| PYTHUSDT | IDLE | 0.93 | 1.83 | 0.23 | -0.01 | 151190.36 | 5.15 | skipped_fast |
| ZBCNUSDT | IDLE | 0.8 | 1.48 | 0.76 | -0.01 | 193598.3 | 19.13 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 1.67 | 0.41 | -0.01 | 62830.45 | 4.12 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 1.83 | 1.37 | -0.03 | 61181.42 | 27.94 | skipped_fast |
| TELUSDT | IDLE | 1.65 | 3.28 | 0.07 | 0.01 | 90354.0 | 33.86 | skipped_fast |
| QNTUSDT | IDLE | 1.25 | 2.28 | 1.46 | -0.03 | 33250.01 | 7.11 | skipped_fast |
| RWAINCUSDT | IDLE | 0.68 | 1.31 | 0.34 | 0.01 | 2867.76 | 96.45 | skipped_fast |
| HBARUSDT | IDLE | 0.64 | 1.26 | 0.14 | -0.0 | 88759.44 | 1.54 | skipped_fast |
| QAITUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 2142.08 | 61.3 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.88 | 0.09 | 0.01 | 50194.77 | 17.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.62 | 1.16 | 0.49 | 0.01 | 401.06 | 22.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
