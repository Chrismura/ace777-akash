# Hulk DIGEST — 2026-10-12T01:31:06Z

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
| WUSDT | IDLE | 2.0 | 17.91 | 5.31 | 0.26 | 5035041.98 | 18.11 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.37 | 0.44 | 0.01 | 199458406.52 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.58 | 1.07 | 0.64 | 0.0 | 16958809.85 | 2.14 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.88 | 0.34 | 0.01 | 161061583.03 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.18 | 3.94 | 2.75 | -0.0 | 898533.05 | 5.13 | skipped_fast |
| QNTUSDT | IDLE | 1.35 | 2.48 | 1.45 | 0.0 | 732481.59 | 1.25 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 3.19 | 1.46 | 0.06 | 368361.17 | 0.8 | skipped_fast |
| EDELUSDT | IDLE | 1.51 | 2.86 | 1.08 | -0.02 | 350551.25 | 18.61 | skipped_fast |
| CHIPUSDT | IDLE | 1.46 | 4.84 | 4.4 | -0.05 | 250763.2 | 10.49 | skipped_fast |
| BIOUSDT | IDLE | 1.44 | 2.54 | 2.28 | 0.02 | 96468.79 | 6.75 | skipped_fast |
| ZBCNUSDT | IDLE | 0.95 | 1.76 | 0.87 | -0.0 | 228071.68 | 37.82 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 2.26 | 1.6 | -0.0 | 62618.41 | 10.24 | skipped_fast |
| REDUSDT | IDLE | 1.04 | 1.81 | 1.78 | -0.01 | 55568.93 | 8.03 | skipped_fast |
| RWAINCUSDT | IDLE | 1.0 | 2.64 | 2.28 | -0.01 | 26785.81 | 4.97 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 1.78 | 0.92 | 0.01 | 284787.53 | 5.33 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 2.48 | 1.96 | -0.02 | 171124.72 | 17.6 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 3.69 | 3.0 | 0.06 | 38094.68 | 58.33 | skipped_fast |
| FLUIDUSDT | IDLE | 0.47 | 3.21 | 3.11 | 0.03 | 67168.62 | 21.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.67 | 1.24 | 0.72 | 0.0 | 33891.58 | 12.29 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.54 | 0.08 | 0.02 | 52557.36 | 23.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
