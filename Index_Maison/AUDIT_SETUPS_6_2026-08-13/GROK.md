# AVIS GROK (task supervise.decision)

provider: Puter Grok (gratuit)

**Verdict : GO AVEC RESERVES**

### Analyse superviseur (brut, sans filtre)

Le système a bien été corrigé par rapport à l’incident du 13/08 (boucle famille incontrôlée). Les garde-fous demandés sont globalement en place et respectent le principe fondateur (« valeur fixe → on coule »). Cependant, il reste quelques points qui justifient des réserves avant un décollage demain matin.

### Points solides (GO)

- **Verrou flock** : correctement posé au début dans `consulter_famille()`, détenu par le thread `_thread_trio` pendant toute la durée des appels (jusqu’au `finally`). Pas de relâche prématurée.
- **TTL anti-spam** : créé uniquement dans le thread quand une occasion réelle existe (`_creer_etat_ttl()`). Le timestamp initial est conservé (`_noter_fin_consultation` n’écrase pas le timestamp). Bon.
- **Mode tempête** : déclencheurs réels (ROUGE / PRENDS_LA_PERTE, vortex >= 2, alarme récente, etat_tempete). Bypass du cap horaire (60s au lieu de 5 min). Correct.
- **Budget & gratuits dynamiques** : `budget_hub.py` lit vraiment `providers.json` (champ `free`), recalcule le budget + réserve 20 %. Pas de liste figée dans le code. Bon.
- **Réserve storm** : 20 % calculée dynamiquement, présente dans `routing.json` (156 sur 624). `prechauffage_reserve.py` et le check preflight sont prévus.
- **Robustesse 24/7** : erreurs non fatales partout, chemins absolus via `Path(__file__)`, pas de fuite de descripteurs évidente (os.close + flock unlock dans finally).

### Points qui justifient les réserves

1. **preflight_ace777.sh**  
   Tu n’as fourni que `SYNTAXE_OK`. On n’a pas la preuve que les checks R1 (budget/réserve), R2 (gratuits), R3 (rapport récent), R4 (exécutable) sont réellement implémentés et non fatals. C’est le point le plus critique pour un décollage propre.

2. **prechauffage_reserve.py – C2 défaillant**  
   La logique `p.get("name") in str(data)` est incorrecte. Elle ne détecte pas correctement les providers gratuits. Ce check peut passer à tort ou à tort. À corriger avant demain.

3. **État actuel**  
   `{"raison": "alerte en cours", "ts": 1786630266}` → le système est déjà en mode tempête/alerte. Le premier run demain risque de consommer la réserve tout de suite. C’est acceptable en tempête, mais il faut le monitorer.

4. **Providers gratuits**  
   Plusieurs providers ont `"free": true` mais certains sont en `enabled: false` ou en observation. Le budget dynamique va bien les prendre en compte, mais il faut s’assurer que `providers_actifs()` + `gratuits_actifs()` ne ramènent pas des providers morts.

### Recommandations avant décollage demain matin

- Exécuter **manuellement** :
  ```bash
  python3 budget_hub.py --apply
  python3 prechauffage_reserve.py
  ```
- Vérifier que le preflight renvoie bien les 4 checks (R1-R4) sans planter.
- Surveiller le premier run avec un log visible (`tail -f` sur les fichiers d’état).
- Nettoyer l’ancien `etat_tempete.json` si encore présent (C4).

### Verdict final

**GO AVEC RESERVES**

Le run peut partir demain matin, **à condition** que tu valides le preflight_ace777.sh et que tu corriges le check C2 du préchauffage. Sans ces deux points, on reste en zone grise.

Tu veux que je te rédige la version corrigée du check C2 + un squelette minimal du preflight_ace777.sh qui implémente vraiment R1-R4 ?
