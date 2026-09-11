# Hulk DIGEST — 2026-09-11T13:20:17Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 2.15 | 4.17 | 0.83 | 0.01 | 41468027.38 | 2.94 | skipped_fast |
| ETHUSDT | IDLE | 1.65 | 3.23 | 0.52 | 0.04 | 471730204.96 | 0.56 | skipped_fast |
| BTCUSDT | IDLE | 1.38 | 2.69 | 0.52 | 0.01 | 507394138.9 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.71 | 5.13 | 1.95 | -0.03 | 436872.8 | 9.21 | skipped_fast |
| PYTHUSDT | IDLE | 2.43 | 4.84 | 0.11 | 0.02 | 367731.59 | 1.91 | skipped_fast |
| RIZEUSDT | IDLE | 1.2 | 24.77 | 6.46 | 0.17 | 113972.71 | 59.06 | skipped_fast |
| WUSDT | IDLE | 2.01 | 3.91 | 0.75 | 0.0 | 126706.68 | 1.05 | skipped_fast |
| CHIPUSDT | IDLE | 1.84 | 5.71 | 2.01 | -0.02 | 131178.8 | 17.27 | skipped_fast |
| BIOUSDT | IDLE | 2.01 | 3.9 | 0.83 | 0.0 | 77781.84 | 3.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.67 | 3.3 | 0.25 | 0.02 | 168842.73 | 14.57 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 3.5 | 1.77 | 0.01 | 59210.67 | 11.98 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 3.52 | 1.41 | -0.01 | 59525.83 | 20.66 | skipped_fast |
| QNTUSDT | IDLE | 2.85 | 5.19 | 3.37 | -0.0 | 40943.8 | 1.54 | skipped_fast |
| RWAINCUSDT | IDLE | 1.98 | 3.55 | 2.72 | 0.01 | 5005.39 | 33.63 | skipped_fast |
| EDELUSDT | IDLE | 0.6 | 2.87 | 0.74 | -0.05 | 196101.95 | 18.73 | skipped_fast |
| HBARUSDT | IDLE | 1.68 | 3.26 | 0.63 | 0.0 | 183109.68 | 1.33 | skipped_fast |
| TELUSDT | IDLE | 1.69 | 3.22 | 1.08 | -0.01 | 97353.78 | 40.22 | skipped_fast |
| FLUIDUSDT | IDLE | 1.36 | 2.37 | 2.31 | -0.01 | 1290.24 | 21.57 | skipped_fast |
| RWAUSDT | IDLE | 0.69 | 1.3 | 0.53 | 0.01 | 49595.46 | 22.7 | skipped_fast |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
