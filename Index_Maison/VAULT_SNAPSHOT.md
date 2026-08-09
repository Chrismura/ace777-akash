# VAULT SNAPSHOT — 2026-08-09T08:43Z

> Notes modifiees < 24h (extraits). Jamais un remplacement du vault — vue recente seulement.

## PROTOCOLE_PROMPTING.md
# Protocole Prompting — 10 techniques (canon)

> Source : « Prompt Engineering — 10 Techniques Internes OpenAI Anthropic Google (2026-08) ».  
> Créé par **Buffy** (chef d'orchestre) le **05/08/2026** — ordre exécuté par Christophe.  
> **But :** standardiser les prompts pour nourrir **Qwen locale**, guider les agents (Cursor/Punk/Cortana) et cadrer les décisions GO.

---


## MEMOIRE_COLLAB.md
| 2026-08-09T08:38Z | Ada | ★ | systeme | FIX DEFINITIF TIMEOUT HUB : patience (retry x3 plafonne 600s) avant fallback, erreurs deterministes 401/402 -> fallback immediat. Preuve : audit 147.5s reste sur DeepSeek V4 (avant: bascule a 120s). Traces kind=timeout. Backup .bak-timeout |
| 2026-08-09T08:00Z | Ada | = | session | CLOTURE PROPRE (arret demande Christophe). Etat stable : hub 8 providers (inferx + ultra-550b + qwen3-coder ajoutes aujourd'hui), MiroFish OK (ZEP presente), superviseur action=none, autopilote OK. Audit gelee. |
| 2026-08-09T07:44Z | Ada | + | systeme | INFERX ACTIVE (cle ix_ OK) : DeepSeek V4 Flash + Qwen3-Coder-Next (code) gratuits jusqu'au 12/08 — HUB = 8 PROVIDERS ACTIFS (qwen-local, gemini, gpt-oss, nvidia, juge, ultra-550b, inferx, inferx-coder) |
| 2026-08-09T07:38Z | Ada | + | systeme | HUB 6 PROVIDERS ACTIFS : + nemotron-3-ultra-550b:free (gratuit, 550B, test OK) via cle OpenRouter existante — tache ultra.analyse + fallback analyse.profonde. InferX prepare (cle gratuite avant 12/08), groq/mistral/cf en attente de cles |
| 2026-08-09T06:49Z | Ada | ★ | systeme | SLOT MISSION = MEILLEURE IA PAR MESURE : bench A/B 09/08 -> DeepSeek V4 (NVIDIA) provider, fallback Gemini (Grok retire, payant). Bench: Evaluations/BENCH_MISSION_2026-08-09.md |
| 2026-08-09T06:46Z | Ada | ★ | systeme | GROK MIS DE COTE (payant 402, GO Christophe) : grok.enabled=false, mission -> nvidia — hub = 5 providers |
| 2026-08-09T06:46Z | Ada | + | systeme | HYGIENE : RAM 813 Mo (OK), grosse_hygiene EXIT=0, disque 13%, /tmp purge — OSS20 flaky upstream (429/content=None) -> fallback Gemini OK |
| 2026-08-09T06:39Z | Ada | + | systeme | CHECK COMPLET : doc PROD_QWEN_REVEIL fixe, hygiene_mac_ram repare (rg->grep), IDEES realigne, Qwen observation OK, hub teste (Qwen/Gemini/NIM/Juge OK, OSS20 429 upstream, Grok 402) |

## JOURNAL_COCKPIT.md
# Journal Cockpit — horloge & évolution

**Rôle :** le cockpit est un **produit à part** (lecture / Cortana / BOARD).  
S’il ne tourne pas comme une horloge → c’est un **problème ops**, pas un détail UI.  
**Ne pas mélanger** avec le juge trading (fills CSV) ni avec [[JOURNAL_ERREURS_TEST]] (sauf P0 partagé).

| Canon | Fichier |
|-------|---------|

## Bookmark_2083762211718394276.md
---
auteur: "@unknown"
date: Sun Aug 02 03:50:00 +0000 2026
url_source: "https://twitter.com/cyrilXBT/status/2083762211718394276"
tweet_id: "2083762211718394276"
likes: 852
retweets: 156
vues: 156729

## Bookmark_2083915748401991797.md
---
auteur: "@unknown"
date: Sun Aug 02 14:00:06 +0000 2026
url_source: "https://twitter.com/elune0x/status/2083915748401991797"
tweet_id: "2083915748401991797"
likes: 106
retweets: 18
vues: 13297

## Bookmark_gippp_loop_to_graph.md
---
auteur: "@gippp69 (Gipp)"
date: Mon Aug 03 11:49:00 +0000 2026
url_source: "https://x.com/gippp69 (article X, lien exact a completer)"
tweet_id: "inconnu (colle depuis bookmarks)"
vues: 88800
tags:
  - signet/x

## Bookmark_2083485399721320739.md
---
auteur: "@unknown"
date: Sat Aug 01 09:30:03 +0000 2026
url_source: "https://twitter.com/hb_stocks/status/2083485399721320739"
tweet_id: "2083485399721320739"
likes: 70
retweets: 4
vues: 5302

## Bookmark_2083826089701540095.md
---
auteur: "@unknown"
date: Sun Aug 02 08:03:50 +0000 2026
url_source: "https://twitter.com/GitTrend0x/status/2083826089701540095"
tweet_id: "2083826089701540095"
likes: 115
retweets: 27
vues: 14663

## Bookmark_2083352921396199612.md
---
auteur: "@unknown"
date: Sat Aug 01 00:43:37 +0000 2026
url_source: "https://twitter.com/0x_Punisher/status/2083352921396199612"
tweet_id: "2083352921396199612"
likes: 33
retweets: 3
vues: 5137

## Bookmark_2083674944982900767.md
---
auteur: "@unknown"
date: Sat Aug 01 22:03:14 +0000 2026
url_source: "https://twitter.com/andreysuperior/status/2083674944982900767"
tweet_id: "2083674944982900767"
likes: 89
retweets: 13
vues: 6736

## Bookmark_2083468508403540175.md
---
auteur: "@unknown"
date: Sat Aug 01 08:22:56 +0000 2026
url_source: "https://twitter.com/RoundtableSpace/status/2083468508403540175"
tweet_id: "2083468508403540175"
likes: 212
retweets: 21
vues: 72720

## Bookmark_2083265738769359069.md
---
auteur: "@unknown"
date: Fri Jul 31 18:57:11 +0000 2026
url_source: "https://twitter.com/0x_hexer/status/2083265738769359069"
tweet_id: "2083265738769359069"
likes: 33
retweets: 7
vues: 1773

## Bookmark_2083681333482496467.md
---
auteur: "@unknown"
date: Sat Aug 01 22:28:37 +0000 2026
url_source: "https://twitter.com/Granite0x/status/2083681333482496467"
tweet_id: "2083681333482496467"
likes: 114
retweets: 6
vues: 17277

## Bookmark_2083857225429217541.md
---
auteur: "@unknown"
date: Sun Aug 02 10:07:33 +0000 2026
url_source: "https://twitter.com/danikkk_wqs/status/2083857225429217541"
tweet_id: "2083857225429217541"
likes: 13
retweets: 3
vues: 1248

## Bookmark_2083299822480810096.md
---
auteur: "@unknown"
date: Fri Jul 31 21:12:38 +0000 2026
url_source: "https://twitter.com/ami10iv/status/2083299822480810096"
tweet_id: "2083299822480810096"
likes: 108
retweets: 12
vues: 11594

