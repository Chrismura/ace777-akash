# Hulk DIGEST — 2026-10-21T01:30:22Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.71 | 1.36 | 0.45 | 0.03 | 24289984.86 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.23 | 0.47 | 0.03 | 170231338.26 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.84 | 0.29 | 0.02 | 327382518.28 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.2 | 3.77 | 1.61 | 0.1 | 1187778.32 | 5.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 13.17 | 11.64 | -0.07 | 80583.28 | 5.56 | skipped_fast |
| WUSDT | IDLE | 1.52 | 2.76 | 1.84 | 0.03 | 652988.62 | 18.69 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 2.98 | 0.73 | 0.02 | 810925.04 | 2.54 | skipped_fast |
| CHIPUSDT | IDLE | 0.91 | 2.9 | 2.35 | 0.07 | 445529.04 | 13.52 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.76 | 1.03 | 0.01 | 369830.01 | 8.54 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 12.76 | 10.01 | 0.07 | 17191.27 | 29.34 | skipped_fast |
| RIZEUSDT | IDLE | 1.74 | 6.76 | 5.87 | 0.04 | 75363.18 | 28.76 | skipped_fast |
| EDELUSDT | IDLE | 0.42 | 3.64 | 0.75 | 0.34 | 364567.39 | 16.69 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 2.6 | 0.33 | 0.04 | 192820.86 | 15.76 | skipped_fast |
| BIOUSDT | IDLE | 1.01 | 1.84 | 1.24 | 0.05 | 60924.97 | 4.07 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 1.97 | 0.25 | 0.04 | 58190.57 | 18.3 | skipped_fast |
| KITEUSDT | IDLE | 0.73 | 1.33 | 0.87 | 0.0 | 73384.2 | 9.04 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.47 | 0.59 | 0.02 | 349014.62 | 3.57 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.41 | 0.09 | -0.0 | 39786.74 | 7.12 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.63 | 0.16 | 0.0 | 52819.81 | 31.3 | skipped_fast |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
