# Hulk DIGEST — 2026-08-20T02:21:29Z

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
| XRPUSDT | IDLE | 1.2 | 3.85 | 2.23 | 0.11 | 44150923.81 | 1.8 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 22.95 | 13.19 | 0.08 | 54900.35 | 192.38 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 4.08 | 3.38 | 0.1 | 367179.58 | 7.09 | skipped_fast |
| WUSDT | IDLE | 1.42 | 3.19 | 2.04 | 0.07 | 263613.43 | 15.13 | skipped_fast |
| PYTHUSDT | IDLE | 0.8 | 2.49 | 0.21 | 0.12 | 312827.84 | 4.68 | skipped_fast |
| CHIPUSDT | IDLE | 1.12 | 3.54 | 1.57 | 0.08 | 197201.63 | 3.55 | skipped_fast |
| REDUSDT | IDLE | 1.4 | 6.6 | 0.38 | 0.12 | 102044.94 | 11.95 | skipped_fast |
| BIOUSDT | IDLE | 1.08 | 5.22 | 1.39 | 0.15 | 162818.25 | 10.57 | skipped_fast |
| ZBCNUSDT | IDLE | 0.86 | 3.64 | 2.38 | 0.15 | 217334.02 | 24.5 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.97 | 0.75 | 0.05 | 357330.22 | 1.4 | skipped_fast |
| KITEUSDT | IDLE | 0.79 | 1.49 | 1.08 | 0.05 | 58225.07 | 13.49 | skipped_fast |
| RWAINCUSDT | IDLE | 0.81 | 2.35 | 1.01 | 0.05 | 17075.85 | 16.96 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 4.98 | 0.33 | 0.21 | 83354.1 | 77.65 | skipped_fast |
| QAITUSDT | IDLE | 0.74 | 2.03 | 0.5 | 0.02 | 10637.2 | 61.42 | skipped_fast |
| TELUSDT | IDLE | 0.78 | 3.71 | 0.91 | 0.13 | 188308.61 | 67.42 | skipped_fast |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
