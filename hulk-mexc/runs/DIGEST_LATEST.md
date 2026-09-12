# Hulk DIGEST — 2026-09-12T15:36:52Z

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
| ETHUSDT | IDLE | 0.33 | 0.61 | 0.32 | -0.03 | 340991527.29 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.34 | 0.62 | 0.34 | -0.02 | 26283007.28 | 1.46 | skipped_fast |
| BTCUSDT | IDLE | 0.16 | 0.31 | 0.11 | -0.02 | 421865268.48 | 0.0 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 6.86 | 6.0 | -0.03 | 225278.17 | 19.14 | skipped_fast |
| PYTHUSDT | IDLE | 1.78 | 4.28 | 0.47 | 0.02 | 386923.67 | 1.82 | skipped_fast |
| RIZEUSDT | IDLE | 1.65 | 57.62 | 26.18 | 0.78 | 147484.78 | 598.85 | skipped_fast |
| CHIPUSDT | IDLE | 3.02 | 7.97 | 1.88 | 0.01 | 80957.88 | 19.96 | skipped_fast |
| RWAINCUSDT | IDLE | 2.8 | 5.17 | 4.86 | -0.0 | 11829.09 | 33.22 | skipped_fast |
| EDELUSDT | IDLE | 1.59 | 4.25 | 1.19 | 0.07 | 164910.21 | 17.17 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.67 | 1.54 | -0.02 | 254440.73 | 7.15 | skipped_fast |
| WUSDT | IDLE | 0.89 | 1.75 | 0.14 | -0.01 | 124444.7 | 15.2 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.57 | 0.85 | -0.01 | 72713.53 | 3.89 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.72 | 1.07 | 0.01 | 62163.71 | 18.69 | skipped_fast |
| KITEUSDT | IDLE | 0.71 | 1.32 | 0.71 | -0.03 | 60542.75 | 12.2 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 2.05 | 1.07 | -0.08 | 90140.42 | 29.95 | skipped_fast |
| HBARUSDT | IDLE | 0.35 | 0.69 | 0.11 | -0.02 | 201220.24 | 1.34 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 1.85 | 1.46 | 0.01 | 54537.77 | 29.56 | skipped_fast |
| QNTUSDT | IDLE | 0.46 | 0.84 | 0.59 | -0.02 | 41052.57 | 7.76 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.0 | 1327.32 | 22.06 | skipped_fast |
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
