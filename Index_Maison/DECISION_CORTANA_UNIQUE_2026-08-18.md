# DÉCISION — UNE seule Cortana (18/08/2026)

**Décision** : chief scientist (Buffy) — simplifier, léger, réactif.
**Constat Christophe** : « je ne sais pas qui c'est, j'entends juste une voix » — deux
voix différentes, une bonne (contexte) une mauvaise (aucun contexte).

---

## Le constat (vérifié dans le code)

| | **Cortana cockpit (bridge)** | **Cortana Rust vocale** |
|---|---|---|
| Chemin | `cortana_cockpit_bridge.py` (:17777) | `~/crypto-voice-assistant-core/` |
| Accès Christophe | ✅ **LE chat en haut du cockpit** (son seul accès direct) | ❌ la voix ne marche pas sur le cockpit bureau |
| Voix | **Vivienne** (edge-tts — la bonne, léger accent) | Amélie (say — moins bonne) |
| Contexte ACE/Hulk | ✅ injecté (18/08) | ❌ aucun |
| Passe par le hub | ✅ (budget, routage, C9) | ❌ LLM direct (violerait C9) |
| Rôle réel | analyse, brief, famille, yeux | prototype vocale séparé |

## La décision

1. **LA Cortana = le chat cockpit (bridge :17777)** — canal unique, contexte branché,
   voix Vivienne, hub officiel. C'est celle que Christophe utilise.
2. **L'app Rust vocale passe en VEILLE** — comme MiroFish : hors-circuit, gardée
   (rien ne se supprime), réactivation = décision + GO.
3. **Pas de fusion** : deux stacks différents (Python vs Rust) — fusionner = risque
   pour zéro gain (l'app Rust n'est pas utilisée).
4. **Schéma mis à jour** : `architecture/ARCHITECTURE_TECH.md` (tableau composants +
   changelog 18/08).

## Réversibilité

- Réactiver l'app Rust : relancer `~/crypto-voice-assistant-core/launch_cortana.sh`
  (aucun fichier supprimé, aucune plist retirée).
- La note + le schéma se mettent à jour par simple édition.

## Pour Christophe, en clair

Quand tu écris dans le chat en haut du cockpit → tu parles à **LA** Cortana : la bonne,
avec le contexte, avec Vivienne. Il n'y en a qu'une. L'autre (la voix qui ne marche pas
sur ton bureau) est rangée en veille — elle ne gênera plus.
