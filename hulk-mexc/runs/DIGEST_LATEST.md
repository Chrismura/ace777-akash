# Hulk DIGEST — 2026-09-12T03:22:12Z

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
| XRPUSDT | IDLE | 0.66 | 1.44 | 0.15 | 0.02 | 52958528.32 | 1.47 | n/a |
| ETHUSDT | IDLE | 0.32 | 0.7 | 0.42 | 0.03 | 642671989.51 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.27 | 0.52 | 0.13 | 0.01 | 571562531.42 | 0.05 | no_map |
| CCUSDT | IDLE | 1.99 | 3.79 | 1.22 | 0.01 | 425012.18 | 7.07 | no_map |
| PYTHUSDT | IDLE | 1.66 | 3.43 | 0.12 | 0.02 | 408814.3 | 1.93 | tvl≈114,190,097 |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.98 | 5.56 | 5.21 | -0.01 | 15073.58 | 5.6 | no_map |
| CHIPUSDT | IDLE | 1.85 | 5.4 | 2.12 | 0.01 | 121290.92 | 18.94 | no_map |
| WUSDT | IDLE | 1.61 | 3.4 | 0.07 | 0.03 | 197779.11 | 14.25 | tvl≈1,484,500,810 |
| EDELUSDT | IDLE | 1.73 | 4.8 | 2.42 | 0.05 | 165703.05 | 35.27 | no_map |
| ZBCNUSDT | IDLE | 1.42 | 2.64 | 1.36 | -0.0 | 193002.12 | 16.24 | n/a |
| REDUSDT | IDLE | 1.67 | 4.58 | 0.72 | 0.08 | 64162.74 | 7.64 | tvl≈2,295,785 |
| BIOUSDT | IDLE | 1.57 | 3.11 | 0.23 | 0.03 | 81965.04 | 7.85 | n/a |
| KITEUSDT | IDLE | 0.73 | 1.34 | 0.86 | -0.01 | 59039.82 | 12.02 | no_map |
| TELUSDT | IDLE | 1.5 | 3.13 | 2.8 | -0.02 | 101472.52 | 5.89 | no_map |
| HBARUSDT | IDLE | 0.56 | 1.08 | 0.31 | -0.01 | 258750.36 | 1.34 | empty_tvl |
| RIZEUSDT | IDLE | 0.05 | 3.37 | 1.1 | 0.68 | 206373.13 | 105.76 | no_map |
| QNTUSDT | IDLE | 1.12 | 2.21 | 0.2 | -0.0 | 46167.19 | 6.25 | n/a |
| FLUIDUSDT | IDLE | 1.14 | 2.27 | 0.0 | 0.02 | 1933.19 | 20.32 | tvl≈2,662,999,168 |
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
