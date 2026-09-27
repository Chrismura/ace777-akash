# Hulk DIGEST — 2026-09-27T18:11:26Z

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
| WUSDT | IDLE | 1.82 | 11.52 | 3.62 | 0.16 | 4281085.69 | 16.42 | skipped_fast |
| PYTHUSDT | IDLE | 1.51 | 5.56 | 1.75 | 0.11 | 2284618.17 | 4.67 | skipped_fast |
| QNTUSDT | IDLE | 1.43 | 22.14 | 4.03 | 0.49 | 6209999.86 | 10.37 | skipped_fast |
| XRPUSDT | IDLE | 0.97 | 1.83 | 0.72 | -0.01 | 43936310.07 | 1.31 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.22 | 0.89 | 0.0 | 192788013.58 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.53 | 0.95 | 0.67 | 0.01 | 444452599.97 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 42.2 | 24.22 | 0.03 | 24968.01 | 4.57 | skipped_fast |
| CCUSDT | IDLE | 1.85 | 3.68 | 0.07 | 0.01 | 559499.71 | 7.31 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 8.08 | 6.2 | -0.12 | 129999.85 | 47.84 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 4.7 | 0.81 | 0.06 | 173410.26 | 10.48 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.64 | 0.15 | 0.0 | 669956.32 | 1.06 | skipped_fast |
| CHIPUSDT | IDLE | 1.76 | 3.29 | 1.56 | -0.05 | 100839.23 | 18.99 | skipped_fast |
| ZBCNUSDT | IDLE | 0.92 | 1.69 | 1.03 | -0.01 | 203522.7 | 10.93 | skipped_fast |
| BIOUSDT | IDLE | 1.21 | 2.35 | 0.53 | -0.03 | 89505.21 | 6.32 | skipped_fast |
| TELUSDT | IDLE | 1.46 | 6.22 | 1.27 | 0.16 | 160222.3 | 5.34 | skipped_fast |
| REDUSDT | IDLE | 0.83 | 1.65 | 0.12 | 0.0 | 64040.06 | 12.89 | skipped_fast |
| RIZEUSDT | IDLE | 0.51 | 1.94 | 0.72 | -0.04 | 45954.58 | 64.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.12 | 0.0 | 0.03 | 1601.23 | 20.74 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 1.0 | 0.42 | 0.01 | 56554.94 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.24 | 0.46 | 0.13 | 0.01 | 39495.61 | 37.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
