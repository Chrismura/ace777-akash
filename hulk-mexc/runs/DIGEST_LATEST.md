# Hulk DIGEST — 2026-09-26T05:51:52Z

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
| XRPUSDT | IDLE | 1.21 | 2.16 | 1.77 | 0.02 | 109879514.6 | 1.93 | skipped_fast |
| ETHUSDT | IDLE | 0.29 | 0.54 | 0.27 | 0.0 | 297962707.89 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.41 | 0.19 | -0.0 | 645604863.07 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.31 | 3.33 | 1.92 | 0.08 | 1182761.06 | 4.08 | skipped_fast |
| CCUSDT | IDLE | 1.19 | 5.0 | 1.51 | 0.15 | 935833.25 | 11.23 | skipped_fast |
| HBARUSDT | IDLE | 1.3 | 2.29 | 2.04 | 0.02 | 867761.06 | 2.13 | skipped_fast |
| QNTUSDT | IDLE | 2.39 | 7.25 | 4.87 | 0.02 | 523355.08 | 8.0 | skipped_fast |
| WUSDT | IDLE | 1.41 | 2.68 | 1.37 | 0.06 | 463157.14 | 10.54 | skipped_fast |
| CHIPUSDT | IDLE | 2.01 | 5.19 | 4.05 | 0.05 | 148415.07 | 16.5 | skipped_fast |
| ZBCNUSDT | IDLE | 1.5 | 3.39 | 2.48 | 0.02 | 226140.92 | 16.13 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 5.34 | 1.94 | 0.1 | 78252.1 | 9.48 | skipped_fast |
| REDUSDT | IDLE | 1.74 | 3.38 | 2.04 | 0.05 | 59297.37 | 8.15 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 2.78 | 2.08 | 0.06 | 111551.77 | 3.07 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 1.64 | 0.67 | -0.0 | 170699.09 | 6.77 | skipped_fast |
| RWAINCUSDT | IDLE | 1.58 | 3.86 | 1.08 | -0.05 | 12464.15 | 83.89 | skipped_fast |
| RIZEUSDT | IDLE | 0.16 | 2.21 | 0.57 | -0.15 | 76889.02 | 33.62 | skipped_fast |
| TELUSDT | IDLE | 0.77 | 1.35 | 1.27 | 0.01 | 117306.9 | 24.54 | skipped_fast |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
