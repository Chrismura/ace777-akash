# Hulk DIGEST — 2026-08-30T16:21:15Z

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
| ETHUSDT | IDLE | 1.25 | 2.48 | 0.2 | 0.03 | 178743115.37 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.8 | 1.57 | 0.23 | 0.01 | 18462111.4 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.44 | 0.23 | 0.01 | 263053985.0 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 8.01 | 5.96 | -0.03 | 549950.7 | 2.5 | skipped_fast |
| PYTHUSDT | IDLE | 3.14 | 5.93 | 2.37 | 0.02 | 405022.25 | 4.08 | skipped_fast |
| ZBCNUSDT | IDLE | 2.82 | 4.96 | 4.54 | -0.04 | 169488.65 | 31.86 | skipped_fast |
| EDELUSDT | IDLE | 2.09 | 5.99 | 3.88 | 0.07 | 72389.88 | 25.2 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.63 | 0.28 | 0.04 | 217105.97 | 12.57 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.62 | 0.89 | 0.02 | 260530.27 | 8.43 | skipped_fast |
| REDUSDT | IDLE | 1.08 | 2.14 | 0.14 | 0.02 | 60141.14 | 11.7 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 1.58 | 0.25 | -0.0 | 73701.45 | 10.89 | skipped_fast |
| TELUSDT | IDLE | 1.93 | 3.85 | 0.0 | -0.01 | 82023.26 | 5.79 | skipped_fast |
| KITEUSDT | IDLE | 0.63 | 1.21 | 0.38 | -0.04 | 61164.74 | 18.69 | skipped_fast |
| RIZEUSDT | IDLE | 0.69 | 2.45 | 0.65 | -0.05 | 45975.98 | 58.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 3.01 | 0.0 | 0.0 | 1671.88 | 127.74 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.13 | 0.4 | -0.0 | 126445.0 | 1.33 | skipped_fast |
| MNSRYUSDT | IDLE | 0.74 | 1.41 | 0.48 | 0.02 | 33131.26 | 21.33 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.14 | 0.19 | 0.01 | 38361.89 | 6.44 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.82 | 0.08 | 0.01 | 53001.48 | 24.4 | skipped_fast |
| FLUIDUSDT | IDLE | 0.41 | 0.83 | 0.0 | 0.02 | 2467.03 | 21.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
