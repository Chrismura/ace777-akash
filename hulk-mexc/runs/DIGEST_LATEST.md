# Hulk DIGEST — 2026-10-08T13:15:20Z

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
| WUSDT | IDLE | 0.83 | 6.75 | 2.64 | 0.19 | 4361375.61 | 15.29 | skipped_fast |
| QNTUSDT | IDLE | 1.9 | 4.43 | 1.08 | -0.01 | 2545840.52 | 2.49 | skipped_fast |
| XRPUSDT | IDLE | 1.14 | 2.1 | 1.18 | -0.03 | 39603328.24 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 1.11 | 2.04 | 1.26 | -0.01 | 391231046.34 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.77 | 1.42 | 0.77 | -0.01 | 508991471.57 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.59 | 3.41 | 2.13 | 0.06 | 689700.91 | 5.31 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 3.57 | 2.59 | 0.0 | 474949.03 | 5.09 | skipped_fast |
| ZBCNUSDT | IDLE | 2.82 | 5.28 | 3.29 | -0.05 | 291129.84 | 24.28 | skipped_fast |
| CHIPUSDT | IDLE | 2.18 | 7.57 | 5.96 | 0.01 | 171245.13 | 16.27 | skipped_fast |
| HBARUSDT | IDLE | 2.09 | 3.79 | 2.61 | 0.0 | 534806.22 | 6.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.74 | 16.06 | 7.42 | 0.02 | 56619.7 | 54.87 | skipped_fast |
| REDUSDT | IDLE | 2.29 | 4.11 | 3.12 | -0.01 | 57807.84 | 8.69 | skipped_fast |
| BIOUSDT | IDLE | 2.1 | 4.11 | 3.11 | 0.02 | 68064.21 | 6.92 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.75 | 9.77 | 5.86 | -0.07 | 180197.18 | 37.54 | skipped_fast |
| EDELUSDT | IDLE | 0.64 | 4.83 | 2.01 | -0.13 | 308253.75 | 31.43 | skipped_fast |
| KITEUSDT | IDLE | 0.92 | 1.74 | 0.7 | 0.02 | 63205.09 | 8.1 | skipped_fast |
| FLUIDUSDT | IDLE | 1.45 | 4.11 | 3.63 | 0.04 | 20061.31 | 21.43 | skipped_fast |
| RWAINCUSDT | IDLE | 0.28 | 1.41 | 0.15 | -0.11 | 45435.83 | 54.82 | skipped_fast |
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
