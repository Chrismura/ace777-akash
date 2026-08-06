# Protocole liens — ne pas rater l’essence

**Problème :** Christophe envoie un lien → Cursor / Punk croient « avoir lu » → en fait X/403, thread tronqué, images floues, article paywall. **On rate l’essence** alors que l’humain croit que c’est digéré.

**Règle d’or :** un lien seul = **lecture partielle** jusqu’à preuve du contraire.

---

## 1 — Ce que l’IA doit toujours dire
Après un lien, **1 ligne honnête** :
- `LU_COMPLET` — texte + images clés accessibles  
- `LU_PARTIEL` — profil / titre / extrait seulement (préciser quoi)  
- `BLOQUÉ` — 403 / login / média illisible  

Si `LU_PARTIEL` ou `BLOQUÉ` → **demander le collage** avant de classer en GARDÉ / REFUS définitif (sauf REFUS évident packaging).

---

## 2 — Ce que Christophe peut faire (le plus fiable)
Quand le sujet compte (Index / sniff) :

1. **Coller le texte** du post / article (ou le passage clé) dans le chat  
2. **Joindre les images** du thread (schéma, courbe fees…) — Cursor sait les *voir*  
3. Ou une seule commande Punk :
```bash
cd ~/ace777-test-day1/veille-punk
./bin/suivi --offline "@compte
colle ici tout le texte du post
…
"
```
4. Option : sauver dans `veille-punk/inbox/NOTE.md` puis dire « lis inbox »

**Minimum vital :** titre + 2–3 paragraphes essence + schéma si y en a un.

---

## 3 — Ce que l’IA peut tenter (dans l’ordre)
1. Fetch direct URL  
2. Miroir lecteur (`r.jina.ai/https://…`) si 403  
3. Si image seule (pbs.twimg…) → télécharger + lire  
4. Si encore trou → **stop** + demander collage (`LU_PARTIEL`)

Ne **pas** inventer le reste du thread. Ne **pas** classer S9/S12 sur un titre seul.

---

## 4 — Mot magique
| Mot | Effet |
|-----|--------|
| `LIS CA` + collage texte/images | Priorité lecture complète → éval |
| `LIEN SEUL` | OK pour triage soft ; pas de doctrine lourde |
| `COMPLETE #14` | Complète une éval déjà ouverte avec le texte collé |

---

## 5 — Coutume agora
- Vérité Index = ce qui est **dans la note**, pas « on a ouvert le lien ».  
- Si doute → `LU_PARTIEL` + Attention « à coller ».  

Voir aussi [[BRIEF_IA_SNIFF]] · [[COUTUMES_AGORA]].
