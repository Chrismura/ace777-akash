# Wyckoff SHADOW — simulation replay

> Tag: `MASTER_BASE_V8_5_IMPACT_4H00` | Filtre: `2026-07-08T05:41:00Z` | Mode: **lecture seule** (pas appliqué au live)
> Généré: `2026-07-08T16:38:24Z`

## Résultat global

| Métrique | Sans Wyckoff (réel) | Avec Wyckoff shadow |
|----------|---------------------|---------------------|
| Trades FILLED | 118 | 73 exécutés, 45 filtrés |
| PnL net | **17.1100 USDT** | **1.2500 USDT** |
| Delta | — | **-15.8600 USDT** |

- Pertes évitées (trades filtrés perdants): **5.3420 USDT**
- Gains manqués (trades filtrés gagnants): **21.2020 USDT**

## Détail des trades FILLED

| TS | Unité | Side | PnL | Wyckoff | Phase | Raisons |
|----|-------|------|-----|---------|-------|---------|
| 2026-07-08T05:43:04Z | BETA | SELL | -0.0799 | BOOST | unknown | upthrust_short |
| 2026-07-08T05:44:25Z | ALPHA | BUY | -0.8508 | ALLOW | unknown |  |
| 2026-07-08T05:46:34Z | ALPHA | BUY | -0.0383 | ALLOW | unknown |  |
| 2026-07-08T05:47:14Z | ALPHA | BUY | 0.3928 | ALLOW | unknown |  |
| 2026-07-08T05:47:49Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T05:47:49Z | ALPHA | BUY | 0.0000 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T05:48:49Z | BETA | SELL | 0.2256 | ALLOW | markdown |  |
| 2026-07-08T05:49:53Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T05:51:02Z | BETA | SELL | 0.0602 | ALLOW | markdown |  |
| 2026-07-08T05:55:04Z | BETA | SELL | -0.0009 | ALLOW | markdown |  |
| 2026-07-08T05:55:45Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T05:55:45Z | ALPHA | BUY | 0.0000 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T05:56:59Z | BETA | SELL | -0.0207 | ALLOW | accumulation |  |
| 2026-07-08T05:57:50Z | ALPHA | BUY | 0.2874 | ALLOW | accumulation |  |
| 2026-07-08T06:02:07Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T06:03:53Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T06:04:11Z | BETA | SELL | 0.1043 | ALLOW | markdown |  |
| 2026-07-08T06:04:44Z | BETA | SELL | -0.0009 | ALLOW | markdown |  |
| 2026-07-08T06:05:09Z | ALPHA | BUY | -0.9580 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T06:09:09Z | ALPHA | BUY | 0.0000 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T06:10:13Z | ALPHA | BUY | 0.4503 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T06:11:59Z | ALPHA | BUY | 0.0000 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T06:14:09Z | ALPHA | BUY | -0.0288 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T06:17:46Z | ALPHA | BUY | -0.6993 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T06:18:58Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T06:18:59Z | ALPHA | BUY | 0.0000 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T06:23:06Z | BETA | SELL | -0.2546 | ALLOW | markdown |  |
| 2026-07-08T06:23:24Z | BETA | SELL | -0.1415 | ALLOW | markdown |  |
| 2026-07-08T06:24:17Z | BETA | SELL | -0.3975 | ALLOW | markdown |  |
| 2026-07-08T06:24:47Z | ALPHA | BUY | 0.0671 | ALLOW | accumulation |  |
| 2026-07-08T06:24:50Z | BETA | SELL | -0.0038 | ALLOW | accumulation |  |
| 2026-07-08T06:25:09Z | BETA | SELL | 0.0052 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T06:25:29Z | BETA | SELL | -0.0127 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T06:25:47Z | BETA | SELL | -0.0583 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T06:29:19Z | ALPHA | BUY | -0.4215 | ALLOW | markup |  |
| 2026-07-08T06:31:14Z | BETA | SELL | -0.0000 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T06:31:49Z | BETA | SELL | -0.1081 | ALLOW | accumulation |  |
| 2026-07-08T06:33:13Z | ALPHA | BUY | -1.9120 | ALLOW | markup |  |
| 2026-07-08T06:34:17Z | BETA | SELL | 0.0569 | ALLOW | accumulation |  |
| 2026-07-08T06:37:15Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T06:37:49Z | BETA | SELL | 0.0837 | ALLOW | markdown |  |
| 2026-07-08T06:45:02Z | BETA | SELL | -0.0263 | ALLOW | markdown |  |
| 2026-07-08T06:46:25Z | BETA | SELL | 0.0306 | ALLOW | markdown |  |
| 2026-07-08T06:48:35Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T06:52:03Z | BETA | SELL | -0.0000 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T06:57:40Z | BETA | SELL | -0.0000 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T07:08:39Z | BETA | SELL | -0.0094 | ALLOW | markdown |  |
| 2026-07-08T07:09:04Z | ALPHA | BUY | 0.0000 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T07:10:50Z | ALPHA | BUY | 1.4083 | ALLOW | accumulation |  |
| 2026-07-08T07:13:17Z | ALPHA | BUY | 0.0000 | ALLOW | markup |  |
| 2026-07-08T07:21:57Z | ALPHA | BUY | 0.0191 | ALLOW | markup |  |
| 2026-07-08T07:23:17Z | ALPHA | BUY | 0.3346 | ALLOW | markup |  |
| 2026-07-08T07:25:20Z | ALPHA | BUY | 1.0516 | ALLOW | markup |  |
| 2026-07-08T07:25:54Z | ALPHA | BUY | 0.0191 | ALLOW | markup |  |
| 2026-07-08T07:33:53Z | ALPHA | BUY | 0.2316 | ALLOW | markup |  |
| 2026-07-08T07:38:33Z | ALPHA | BUY | 0.0000 | ALLOW | markup |  |
| 2026-07-08T07:38:46Z | BETA | SELL | -0.0000 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T07:42:12Z | BETA | SELL | -0.0959 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T07:43:24Z | ALPHA | BUY | 0.6979 | ALLOW | markup |  |
| 2026-07-08T07:45:13Z | ALPHA | BUY | -0.8029 | ALLOW | markup |  |
| 2026-07-08T07:45:36Z | BETA | SELL | 0.1269 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T07:46:21Z | BETA | SELL | -0.0005 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T07:49:16Z | ALPHA | BUY | -0.0573 | ALLOW | markup |  |
| 2026-07-08T07:49:39Z | BETA | SELL | -0.0616 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T07:50:35Z | ALPHA | BUY | -0.2290 | ALLOW | markup |  |
| 2026-07-08T07:54:12Z | ALPHA | BUY | 0.4532 | ALLOW | markup |  |
| 2026-07-08T07:56:59Z | BETA | SELL | 0.0085 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T08:03:31Z | BETA | SELL | -0.0038 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T08:03:49Z | ALPHA | BUY | 0.0000 | ALLOW | markup |  |
| 2026-07-08T08:04:22Z | ALPHA | BUY | -0.3244 | ALLOW | markup |  |
| 2026-07-08T08:06:32Z | BETA | SELL | -0.0216 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T08:10:50Z | ALPHA | BUY | -0.0096 | ALLOW | markup |  |
| 2026-07-08T08:11:56Z | ALPHA | BUY | 1.2128 | ALLOW | markup |  |
| 2026-07-08T08:12:23Z | ALPHA | BUY | 0.0048 | ALLOW | markup |  |
| 2026-07-08T08:18:05Z | ALPHA | BUY | -0.8604 | ALLOW | markup |  |
| 2026-07-08T08:18:14Z | BETA | SELL | 0.0940 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T08:29:42Z | BETA | SELL | 0.0104 | ALLOW | markdown |  |
| 2026-07-08T08:32:43Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T08:34:51Z | BETA | SELL | -0.1558 | ALLOW | markdown |  |
| 2026-07-08T08:35:35Z | ALPHA | BUY | 0.0000 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T08:36:16Z | ALPHA | BUY | -1.7581 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T08:36:58Z | ALPHA | BUY | 0.0000 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T08:36:59Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T08:38:54Z | BETA | SELL | 0.1738 | ALLOW | markdown |  |
| 2026-07-08T08:45:44Z | BETA | SELL | 1.2776 | ALLOW | markdown |  |
| 2026-07-08T08:46:18Z | BETA | SELL | -0.1568 | ALLOW | markdown |  |
| 2026-07-08T08:46:46Z | BETA | SELL | -0.0274 | ALLOW | markdown |  |
| 2026-07-08T08:47:57Z | ALPHA | BUY | 0.3370 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T08:49:38Z | BETA | SELL | 0.4997 | ALLOW | markdown |  |
| 2026-07-08T08:49:43Z | ALPHA | BUY | 0.0000 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T08:51:22Z | BETA | SELL | 0.0010 | ALLOW | markdown |  |
| 2026-07-08T08:53:25Z | BETA | SELL | -0.0712 | ALLOW | markdown |  |
| 2026-07-08T08:54:34Z | ALPHA | BUY | 1.1761 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T08:55:37Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T08:56:25Z | BETA | SELL | -0.0238 | ALLOW | markdown |  |
| 2026-07-08T08:56:40Z | ALPHA | BUY | 0.3904 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T08:57:46Z | ALPHA | BUY | 0.0000 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:00:11Z | ALPHA | BUY | 1.4876 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:01:29Z | ALPHA | BUY | 0.5591 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:02:11Z | ALPHA | BUY | 0.0145 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:07:09Z | BETA | SELL | 0.7972 | ALLOW | markdown |  |
| 2026-07-08T09:07:31Z | BETA | SELL | -0.4679 | ALLOW | markdown |  |
| 2026-07-08T09:08:47Z | ALPHA | BUY | -1.4755 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:09:04Z | BETA | SELL | 0.0043 | ALLOW | markdown |  |
| 2026-07-08T09:12:44Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T09:21:40Z | BETA | SELL | 0.0788 | ALLOW | markdown |  |
| 2026-07-08T09:28:23Z | BETA | SELL | -0.2312 | ALLOW | markdown |  |
| 2026-07-08T09:29:46Z | ALPHA | BUY | -0.0291 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:30:26Z | ALPHA | BUY | 0.7438 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:30:43Z | ALPHA | BUY | 1.8402 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:32:34Z | ALPHA | BUY | 0.4637 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:33:40Z | ALPHA | BUY | 0.0000 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:34:19Z | ALPHA | BUY | 2.0624 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:34:33Z | BETA | SELL | -0.0000 | ALLOW | markdown |  |
| 2026-07-08T09:34:40Z | ALPHA | BUY | 11.4423 | SKIP | markdown | phase_markdown_block_long |
| 2026-07-08T09:35:28Z | BETA | SELL | -0.1388 | SKIP | markup | phase_markup_block_short |
| 2026-07-08T09:35:47Z | ALPHA | BUY | 0.0000 | ALLOW | markup |  |
| 2026-07-08T09:40:33Z | ALPHA | BUY | -0.6506 | ALLOW | accumulation |  |

## Lecture

**Verdict simulation : négatif** — Wyckoff shadow aurait **réduit** le PnL (-15.86 USDT). Trop filtrant sur ce timeframe.

_Règles shadow : effort/résultat, spring/upthrust, filtre phase markup/markdown, chop sélectif._
