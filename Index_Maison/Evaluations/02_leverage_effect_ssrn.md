# Éval #2 — Betting on the Leverage Effect (SSRN 6939018)

- **Date :** 2026-07-28
- **Via :** @macro_synergy
- **Lien :** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6939018  
  (PDF SSRN bloqué Cloudflare ici — éval sur abstract / quote du tweet)

## Claim (abstract tweet)

Les actions avec une corrélation **plus négative** entre rendements et innovations de variance (effet de levier plus fort) ont des **rendements futurs plus élevés**.  
Portfolio sorts : primes annuelles ≈ **3,72 %** (corr globale) et **5,76 %** (corr upside).

## Verdict Cursor

| | |
|--|--|
| Science / idée | **Réelle** — leverage effect = stylized fact (Black 1976…) ; paper = variante cross-section « qui a le plus de leverage → premium » |
| Chiffres 3.72 / 5.76 | **À prendre avec pincettes** sans PDF + sample + coûts ; typique equity US academic |
| Thermo maison ? | **Oui, inspiré (signature crash)** |
| Trend maison ? | **Faible** — pas un indicateur de direction moyen terme |
| Utile ACE/Hulk hot ? | **Non** — tri cross-section stocks ≠ dip/rip MEXC / NUAGE |
| Action | Garder l’**intuition** ; ne pas coder le paper |

## Ce qu’on prend

**Signature leverage en live (thermo) :**  
prix ↓ **et** vol ↑ ensemble = régime stress (classique).  
Chez nous : BTC (ou panier) return 1h négatif **+** range/vol qui explose → `CRASH` / frein BUY.  
C’est aligné avec « alts suivent BTC en dump » — le leverage se voit souvent d’abord sur l’index.

## Ce qu’on laisse

- Trier un univers d’actions sur corr(return, Δvariance) pour capturer 3–6 %/an.
- Importer ça dans Hulk comme signal d’entrée long.
- Croire le premium Twitter sans réplication crypto.

## Mapping Index Maison

| Paper | Notre sauce |
|-------|-------------|
| Corr return ↔ vol innovations | Thermo : co-mouvement **return↓ + vol↑** |
| Premium cross-section stocks | Hors scope |
| Upside vs overall corr | Trop fin pour v1 |

## Décision

- **Garder :** règle thermo simple « dump + vol spike ».  
- **Jeter (pour maintenant) :** stratégie equity leverage-correlation sort.  
- Priorité reste : **BTC + panier** avant fancy corr.
