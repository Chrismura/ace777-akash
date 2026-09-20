# Hulk DIGEST — 2026-09-20T23:02:35Z

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
| XRPUSDT | IDLE | 0.81 | 1.58 | 0.31 | -0.0 | 39532392.57 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.47 | 0.41 | 0.0 | 282324495.05 | 0.15 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.88 | 0.14 | -0.0 | 458431620.12 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 2.83 | 0.9 | 0.06 | 1262574.09 | 1.16 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.53 | 33.67 | 6.01 | 0.34 | 157808.3 | 25.34 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.76 | 0.87 | 0.01 | 670106.03 | 4.87 | skipped_fast |
| WUSDT | IDLE | 1.94 | 4.95 | 1.13 | 0.06 | 490389.97 | 7.71 | skipped_fast |
| CHIPUSDT | IDLE | 3.01 | 6.51 | 3.83 | -0.03 | 86189.48 | 16.43 | skipped_fast |
| RWAINCUSDT | IDLE | 3.51 | 6.62 | 2.64 | -0.01 | 7354.19 | 78.1 | skipped_fast |
| CCUSDT | IDLE | 1.02 | 1.94 | 0.64 | -0.01 | 408421.11 | 9.22 | skipped_fast |
| RIZEUSDT | IDLE | 2.34 | 5.14 | 0.83 | 0.0 | 36025.27 | 41.54 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 1.98 | 0.59 | -0.05 | 202639.1 | 46.92 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 2.27 | 0.63 | 0.01 | 61067.26 | 11.21 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 1.84 | 1.26 | 0.01 | 74712.23 | 7.27 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.72 | 0.54 | -0.01 | 76027.77 | 7.23 | skipped_fast |
| TELUSDT | IDLE | 1.26 | 2.34 | 1.18 | 0.01 | 94665.22 | 52.88 | skipped_fast |
| QNTUSDT | IDLE | 0.75 | 1.31 | 1.3 | -0.02 | 109694.24 | 20.34 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.25 | 0.36 | 0.01 | 54720.1 | 14.63 | skipped_fast |
| FLUIDUSDT | IDLE | 0.78 | 1.49 | 0.41 | -0.02 | 4043.36 | 21.63 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.52 | 0.01 | -0.0 | 37311.35 | 2.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
