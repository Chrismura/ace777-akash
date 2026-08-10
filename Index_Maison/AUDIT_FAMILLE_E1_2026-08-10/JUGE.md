# AUDIT JUGE (task signets.juge) — E1

provider: OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant

**GO AVEC RESERVES**

**Justification**  
Le code implémente fidèlement les huit réserves de la SPEC V2.1 (statut HEALTHY/STALE/DEGRADED, feed_hash SHA‑256 avec ordre fixe, `load_json_safe` non bloquant, écriture atomique `.tmp → os.replace`, métadonnées hors‑zone uniquement, loi du brut – aucune prose, vérification du hash, gestion tolérante des feeds corrompus). Les tests unitaires couvrent toutes ces exigences et passent (7/7). Le `state.json` généré est brut, cohérent et reflète l’état réel du système (status = STALE, hash valide, comptage des services, etc.).

**Réserves concrètes**  
1. **hors_zone size** : `os.path.getsize` sur un répertoire renvoie une taille de métadonnée qui n’est pas significative et peut lever une exception selon les droits ; bien que réservé à de la métadonnée, la valeur retournée peut être trompeuse ou nulle.  
2. **memory_pressure sortie** : la chaîne renvoyée dépend de la locale du système (actuellement en anglais) ; un changement de locale pourrait altérer le champ `ram_raw` sans que cela soit prévu dans la spéc.  
3. **chemin de base hard‑codé** : `BASE = ~/ace777-test-day1/Index_Maison` est adapté au environnement de test ; en production il faudrait le rendre configurable ou le déduire dynamiquement.

Ces réserves n’affectent pas la conformité fonctionnelle de l’étape E1, mais méritent une correction avant le déploiement définitif.
