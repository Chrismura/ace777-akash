# SPEC — PRÉCHAUFFAGE DE LA RÉSERVE STORM (garde-fou avant usage)

## Contexte (décision Christophe, 13/08)

> « Prévoir un garde-fou pour qu'on soit sûr un peu à l'avance que la réserve
> tempête soit effectivement fonctionnelle. Un préchauffage du genre : qu'on ne
> bascule pas dessus en tempête et qu'il n'y ait personne. C'est la réserve
> stratégique dans la tempête. »

**Principe** : la réserve storm est la réserve stratégique utilisée en tempête.
On ne doit JAMAIS découvrir au moment critique qu'elle est vide, cassée ou
illisible. Un **préchauffage** (check-list) tourne au check quotidien (au moment du
recalcul du budget) et vérifie que toute la chaîne est fonctionnelle AVANT qu'on en
ait besoin.

## RÈGLES ABSOLUES

1. Python 3.9 stdlib, pas de dépendance externe.
2. `typing.Optional`, jamais `str | None`.
3. Non fatal : le préchauffage ne doit jamais casser quoi que ce soit, il vérifie
   et il ALERTE.
4. **ZÉRO consommation** : le préchauffage ne fait AUCUN appel au hub/providers,
   tout est simulation locale (fichiers, calculs, /tmp).
5. UTF-8, commentaires en français.

---

## CE QUE LE PRÉCHAUFFAGE VÉRIFIE (check-list)

Le script `prechauffage_reserve.py` (dans `~/prise-ia/`) vérifie chaque point et
écrit un rapport avec verdict global.

### C1 — Budget journalier écrit
- Lire `routing.json` :
  - `cloud_daily_budget` existe ET > 0 ;
  - `cloud_daily_reserve` existe ET > 0 ;
  - sinon → POINT KO (la réserve n'a jamais été appliquée : il faut lancer
    `budget_hub.py --apply`).

### C2 — Gratuits lisibles
- Lire `providers.json` :
  - au moins 1 provider actif (enabled ou référencé dans routing) a `free: true` ;
  - sinon → POINT KO (aucun gratuit détecté : en tempête, rien ne tiendrait).

### C3 — Simulation de bascule réserve (en /tmp, zéro consommation)
- Simuler la logique de `hub_prise_ia.py` :
  - budget calme atteint (usage cloud simulé = budget calme) ;
  - mode tempête actif (simulé) ;
  - tâche prioritaire (`signets.juge` par ex.) ;
  - VÉRIFIER que la réserve passe la tâche (aucune coupure) ;
  - VÉRIFIER qu'une tâche non prioritaire en calme reste coupée (comportement
    inchangé).
- Écrire les artefacts de test dans `/tmp` (jamais les vrais fichiers).

### C4 — Chemin tempête cohérent
- Vérifier que le fichier d'état tempête lu par le hub existe OU que le fallback
  (alarme / zone ADA) est utilisable : `Index_Maison/strategie/alarme.json` lisible
  (ou `ada_gardienne_live.json`). Attention : le bloc hub v1 lisait
  `~/prise-ia/strategie/etat_tempete.json` (mauvais chemin) — vérifier que le chemin
  corrigé pointe vers la zone ADA/alarme réelle (`Index_Maison/strategie/`).

## SORTIE DU PRÉCHAUFFAGE

- Écrit `~/prise-ia/prechauffage_reserve.json` :
  ```json
  {
    "ts": "...",
    "verdict": "OK" | "KO",
    "points": [
      {"id": "C1", "ok": true, "detail": "budget=... reserve=..."},
      {"id": "C2", "ok": true, "detail": "gratuits=..."},
      {"id": "C3", "ok": true, "detail": "bascule reserve OK (simulee)"},
      {"id": "C4", "ok": true, "detail": "chemin tempete=..."}
    ],
    "alerte": "..."   // message clair si KO
  }
  ```
- Si verdict KO : message clair sur stderr + exit code 1 (pour qu'un launchd / un
  humain le voie). Exit 0 si OK.
- Affichage console lisible en français : « ✅ Prééchauffage réserve OK (budget X,
  réserve Y, N gratuits) » ou « 🔴 Prééchauffage KO : ... ».

## INTÉGRATION MINIMALE

- Le préchauffage doit pouvoir être lancé juste après le recalcul quotidien du
  budget (même moment, même check). Fournir la ligne d'appel dans le commentaire
  d'en-tête : `python3 prechauffage_reserve.py` (et mentionner qu'on peut le lancer
  juste après `budget_hub.py --apply`).

## TESTS À FOURNIR

Le script inclut `--test` : simulateurs hermétiques en /tmp qui vérifient que
chaque point C1-C4 détecte bien un cas KO (fichier absent, réserve 0, gratuit
absent) et un cas OK.

## CONTRAT DE SORTIE

`prechauffage_reserve.py` COMPLET (check-list C1-C4 + rapport + `--test`),
prêt à copier dans `~/prise-ia/`. Zéro placeholder, syntaxe Python 3.9 valide,
commentaires en français, non fatal.
