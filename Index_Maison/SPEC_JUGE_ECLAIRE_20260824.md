# SPEC — JUGE ÉCLAIRÉ (architecture rapide + efficace du verrou IA des trades)

**Orchestrateur :** Buffy — **Date :** 24 août 2026 (après-midi). **Statut :** GO Christophe.

## Contexte (validé par Christophe, 24/08)

**Constats du jour (boucle du forfait)** : 3 plists launchd zombies (`run72h`, `run-vortex-96h`,
`run-setupA-4h`, désactivées + renommées `.OFF-20260824`) ont réveillé 6 moteurs en parallèle
→ le verrou IA des trades (`vortex_supervisor_v2_llm.rb` → pont `llm_gate_hub_bridge.py` → hub
`supervise.decision`) a été martelé : **4 426 requêtes en 4 h, ~78 vrais hits hub dont ~55 en
échec** (groq 429 → chute sur nara, 120-493 s → timeouts → re-tape). Budget cloud éclaté
(758/624). Hulk seul préservé.

**Deux défauts de fond révélés (validés par Christophe comme « pas normal »)**
1. **Le juge est AVEUGLE** : le prompt envoyé au hub est `{"swarm_cohesion":0.5,"mode":"CHOP"}`
   (~30 car. — aucune donnée de marché). Le modèle répond à l'aveugle. Les indicateurs existent
   pourtant (`thermo/live.json`, `data/bloc_privatise.json`… « le juge = la porte que Cortana a
   les yeux ouverts »).
2. **Le chemin est fragile** : appels à CHAQUE cycle (~15-20 s), routage groq→nara (nara = 2-5 min
   quand groq est 429), pas de verrou anti-doublon entre moteurs.

**Principes actés par Christophe**
- « Fraîcheur et essentiel » : on ne nourrit le juge qu'avec des indicateurs FRAIS (âge mesuré,
  sinon marqués STALE/ignorés — jamais de vieux data présentés comme bons).
- Le juge doit rester un **verrou de sécurité terrain rapide** (< 1 s) ; Cortana reste l'analyste
  au-dessus (déjà branchée sur les même fichiers).
- Zéro IA locale, tout passe par le hub (directive 12/08 conservée).

## RÈGLES ABSOLUES

1. **Python 3.9** (système), **stdlib uniquement**. AUCUNE dépendance externe.
2. **INTERDIT** `str | None` dans les annotations à l'exécution (`typing.Optional` ou rien).
3. **NE PAS TOUCHER AU MOTEUR** (genesis, alpha/beta, CSV sources, scellés). Seuls sont modifiés :
   le **superviseur juge** (`scripts/vortex_supervisor_v2_llm.rb` — c'est lui qu'on rend
   événementiel) et le **pont** (`Index_Maison/scripts/llm_gate_hub_bridge.py`), déjà adaptés le
   12/08 dans le même esprit.
4. **Ne jamais casser la chaîne** : tout défaut d'indicateur → ligne `[ERR]` dans le pavé, jamais
   de crash du pont ni du hub. Un fichier manquant/vieux ne bloque jamais un trade : le moteur
   garde son fallback règles (fail-closed) quand le hub répond 503.
5. **UTF-8 partout**, fichiers produits uniquement dans `Index_Maison/scripts/` + `runs/`.
6. Le **cache du pont reste haché sur le prompt REÇU du moteur** (le pavé est généré au moment de
   la consultation réelle) — sans ça les 2 700 hits cache/jour seraient perdus.
7. Fraîcheur : **TTL par indicateur** (voir table). Tout fichier plus vieux que son TTL est marqué
   `[STALE xx m]` dans le pavé et son contenu n'est PAS injecté (le modèle sait qu'il ne doit pas
   en tenir compte). Jamais de « vieux = bon ».

## MODIFICATION 1 — PAVÉ D'INDICATEURS (le juge voit le marché)

`Index_Maison/scripts/juge_indicateurs.py` (nouveau module pur, sans I/O réseau) :

- Fonction `pave(racine, now=None) -> str` : lit les fichiers de la table, vérifie l'âge
  (mtime vs now), extrait les valeurs clés via des extracteurs tolérants, assemble **6-10 lignes**
  compactes, **≤ ~1 500 car.**, tout en try/except non fatal.
- Table des indicateurs (chemin relatif à `Index_Maison/`, TTL) :

| Fichier | Contenu clé | TTL |
|---|---|---|
| `thermo/live.json` | ts, mark, oi, funding + régime/couleur + onchain (injecté par pont_onchain) | 10 min |
| `data/bloc_privatise.json` | taux_fantome %, n_snapshots, nb_tx_cachees, taux_non_fiable | 15 min |
| `thermo/sante_index.json` | statut global + compteurs par circuit | 30 min |
| `strategie/ada_gardienne_live.json` | zone (VERT/ROUGE…), voilure %, alerte, pnl_alpha | 10 min |
| `strategie/alarme.json` | alerte active ? (déclencheur, ts) | 5 min |
| `thermo/regime_couleur.json` | régime/couleur (source secondaire) | 5 min |

- Format attendu (modèle) :
  ```
  [taux_fantome] 2.15% (16 snapshots, fiable) — privatisé 140/6508 tx
  [zone] VERT · voilure 91% · alerte OFF · pnl_alpha +2.01
  [marche] mark=77525.9 oi=107000 funding=0.0001
  [sante] 9/9 OK (…)
  [STALE 4h] regime_couleur (non injecté)
  ```
- Cas testables : fichier frais OK / STALE / absent / JSON corrompu / champ manquant.

## MODIFICATION 2 — PONT : INJECTION DU PAVÉ (cache préservé)

Dans `llm_gate_hub_bridge.py` `do_POST` :
- L'ordre actuel est conservé : `cache_fraiche(prompt)` d'abord (clé = prompt du moteur) → si
  cache → réponse ; sinon → construire le pavé (`juge_indicateurs.pave(<..>)`), l'insérer
  **avant le prompt reçu** dans le `user` envoyé au hub, puis `call_hub`.
- Ajouter `MAX_PAVE_CAR = 1500` (coupé), configurable par env `LLM_GATE_PONT_PAVE_MAX_CAR`.
- Log une ligne par consultation réelle : `JUGE ECLAIRE paves=5 stale=1 (12 ms)`.
- Le fusible cooldown (24/08) reste tel quel : si hub KO → 503 immédiat sans retape.
- Perf : construction du pavé mesurée et notée (doit rester < 150 ms ; ~1 ms attendu).

## MODIFICATION 3 — SUPERVISEUR : APPELS SUR ÉVÉNEMENT + VERROU ANTI-DOUBLON

`scripts/vortex_supervisor_v2_llm.rb` (le superviseur juge, PAS le moteur) :
- **Verrou fichier** (`runs/vortex_llm.lock`, flock, TTL 30 s) : si le verrou est tenu par un
  autre superviseur → PAS d'appel hub : le superviseur **relit la décision déjà écrite** dans
  `runs/vortex_control.json` et la réémet telle quelle (le moteur lit toujours un état frais).
  C'est l'application du principe du verrou famille 13/08 au juge : 2 copies peuvent tourner sans
  jamais doubler les appels cloud.
- **Appel sur événement** : ne consulter le hub QUE si (a) pas de décision, ou (b) la précédente
  a plus de `VORTEX_LLM_MAX_AGE_S` (30 s), ou (c) l'état a changé de façon nette :
  `|chop_score - prev| >= 0.06` OU `|tension - prev| >= 0.5` OU changement de mode. Sinon :
  pas d'appel, on réécrit la même décision (le moteur la relit à 0 ms).
- Toutes les valeurs par env, défauts ci-dessus. Le format écrit de `vortex_control.json`
  (structure stricte v2) est INCHANGÉ.
- Emergency override (LLM > budget) inchangé : si le hub tarde, fallback règles.

## MODIFICATION 4 — ROUTAGE : gemini D'ABORD (le chemin rapide)

`~/prise-ia/routing.json`, tâche `supervise.decision` :
- `provider: gemini` (flash, mesuré 0,6-0,9 s), `fallback: groq` (~2 s), `secondary: nara`
  (dernier filet). Note datée (24/08).
- Effet : en nominal, décision en < 1 s ; nara n'est plus jamais le chemin du trade.

## TESTS À FOURNIR (hermétiques, tout en /tmp)

`python3 Index_Maison/scripts/juge_indicateurs.py --test` + un test pont :
- T1 : pavé frais → les 5 indicateurs présents, pas de STALE.
- T2 : fichier vieilli (mtime - TTL - 60 s) → `[STALE n m]` + contenu non injecté.
- T3 : fichier absent → ligne `[absent]`, pas de crash.
- T4 : JSON corrompu → ligne `[err]`, pas de crash.
- T5 : `now` figé → déterminisme (même sortie pour même état).
- T6 : longueur pavé ≤ 1500 car. sur données réelles.
- T7 : pont avec fake hub → le pavé apparaît dans la requête ; cache : 2e requête même prompt →
  réponse sans nouveau pavé (cache OK).
- T8 : 2 superviseurs simultanés (simulés) → 1 seul appel hub.

## CONTRAT DE SORTIE

Code complet + tests, commentaires en français, non fatal, prêt à déployer (kickstart du pont,
reload du superviseur via le lanceur). Rien d'autre dans la chaîne ne bouge : le moteur ne voit
aucune différence (toujours `vortex_control.json` + le pont qui émule Ollama).

## FICHIERS CONCERNÉS
- **Nouveau** : `Index_Maison/scripts/juge_indicateurs.py` (+ son test intégré)
- `Index_Maison/scripts/llm_gate_hub_bridge.py` (injection pavé, log)
- `scripts/vortex_supervisor_v2_llm.rb` (éventuel + verrou) — limité au superviseur, PAS au moteur
- `~/prise-ia/routing.json` (supervise.decision → gemini/groq/nara)
- `Index_Maison/SPEC_JUGE_ECLAIRE_20260824.md` (ce document)