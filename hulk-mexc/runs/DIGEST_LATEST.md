# Hulk DIGEST — 2026-09-27T16:11:09Z

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
| PYTHUSDT | IDLE | 1.88 | 6.98 | 6.03 | 0.06 | 2146885.49 | 6.03 | skipped_fast |
| WUSDT | IDLE | 1.47 | 9.59 | 1.01 | 0.2 | 3931463.85 | 14.33 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 16.63 | 0.44 | 0.57 | 5969246.06 | 11.53 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 2.43 | 1.62 | -0.02 | 44335113.14 | 0.66 | skipped_fast |
| ETHUSDT | IDLE | 0.71 | 1.28 | 0.87 | 0.0 | 190459346.29 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.51 | 0.92 | 0.67 | 0.01 | 450340388.9 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 42.2 | 18.84 | 0.22 | 23087.08 | 137.22 | skipped_fast |
| CCUSDT | IDLE | 2.58 | 4.61 | 3.63 | -0.04 | 536813.18 | 10.49 | skipped_fast |
| CHIPUSDT | IDLE | 2.95 | 6.08 | 4.64 | -0.09 | 97754.87 | 17.01 | skipped_fast |
| HBARUSDT | IDLE | 1.68 | 3.07 | 1.98 | -0.01 | 678467.87 | 1.07 | skipped_fast |
| EDELUSDT | IDLE | 2.27 | 7.94 | 6.5 | -0.1 | 141063.11 | 47.68 | skipped_fast |
| BIOUSDT | IDLE | 1.65 | 3.05 | 1.65 | -0.04 | 96686.82 | 9.51 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 3.18 | 1.46 | 0.06 | 176097.18 | 8.68 | skipped_fast |
| ZBCNUSDT | IDLE | 0.94 | 1.75 | 0.83 | -0.02 | 214024.81 | 12.77 | skipped_fast |
| REDUSDT | IDLE | 1.17 | 2.2 | 0.9 | 0.01 | 64989.01 | 14.1 | skipped_fast |
| TELUSDT | IDLE | 1.72 | 7.78 | 0.85 | 0.17 | 148223.86 | 42.83 | skipped_fast |
| RIZEUSDT | IDLE | 0.58 | 2.1 | 1.54 | -0.05 | 46342.79 | 62.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.9 | 1.75 | 0.28 | 0.02 | 1536.1 | 21.46 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.85 | 0.28 | 0.01 | 56509.25 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.7 | 0.55 | 0.01 | 39699.48 | 39.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
