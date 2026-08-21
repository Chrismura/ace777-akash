# Hulk DIGEST — 2026-08-21T02:29:48Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| PYTHUSDT | IDLE | 1.72 | 3.37 | 0.42 | 0.06 | 1684753.3 | 2.21 | skipped_fast |
| XRPUSDT | IDLE | 0.83 | 4.82 | 0.61 | 0.17 | 109076617.92 | 1.54 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.36 | 12.93 | 0.09 | 0.2 | 404702.69 | 5.91 | skipped_fast |
| ZBCNUSDT | IDLE | 2.22 | 7.05 | 0.35 | 0.06 | 301256.98 | 21.47 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 2.48 | 0.47 | 0.01 | 470681.45 | 4.0 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.21 | 0.49 | 0.05 | 456235.71 | 1.34 | skipped_fast |
| EDELUSDT | IDLE | 1.88 | 5.22 | 2.43 | 0.03 | 92174.16 | 21.65 | skipped_fast |
| WUSDT | IDLE | 1.22 | 2.36 | 0.47 | 0.06 | 259200.19 | 15.39 | skipped_fast |
| BIOUSDT | IDLE | 0.82 | 3.48 | 2.74 | 0.09 | 228384.47 | 3.24 | skipped_fast |
| RIZEUSDT | IDLE | 1.68 | 8.99 | 4.71 | -0.05 | 40221.75 | 50.5 | skipped_fast |
| REDUSDT | IDLE | 0.83 | 4.77 | 2.78 | 0.06 | 182554.9 | 23.77 | skipped_fast |
| KITEUSDT | IDLE | 1.48 | 2.92 | 0.26 | 0.03 | 62962.72 | 16.07 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.77 | 1.09 | 0.04 | 8563.06 | 60.42 | skipped_fast |
| QAITUSDT | IDLE | 0.98 | 2.27 | 1.91 | -0.05 | 6229.89 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 0.96 | 4.98 | 2.64 | 0.13 | 195465.46 | 37.89 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.2 | 0.61 | 0.05 | 64894.68 | 6.44 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 2.26 | 0.0 | 0.1 | 1613.36 | 20.64 | skipped_fast |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
