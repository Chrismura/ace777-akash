# CHANTIER — Veilleuse / Synapse + alerte vocale en boucle (15/08/2026)

**Statut** : ✅ LIVRÉ et TESTÉ · famille GO-AVEC-RÉSERVE (gemini 92% / nvidia 78%) ·
**décision Christophe : boucle vocale STRICTE 24h/24** (réserve nvidia sur l'atténuation
nocturne écartée — volonté du propriétaire) · réversible

## L'idée (Christophe)
« Un fil logique comme une synapse : savoir d'où vient chaque chose, qui l'a modifiée,
sans courir pour comprendre — surtout en cas de panne. Une veilleuse qui hurle. Voir les
intrusions tout de suite. » + **alertes vocales en boucle jusqu'à extinction manuelle**
(« moi j'oublie, et les tâches automatisées doivent être bouclées »).

## Ce qui a été fait
| Livrable | Rôle |
|---|---|
| `strategie/REGISTRE_SYNAPSES.json` | Index du noyau critique : 14 fichiers md5 (scripts prod, plists, configs, moteur) + 2 fichiers fraîcheur (live.json 120 min, whales 360 min). Chaque entrée : nom, rôle, origine, md5, verif |
| `scripts/veilleuse_synapses.py` | Cadence 10 min (launchd) : md5 fichiers (INTRUSION) · process attendus (PANNE) · fraîcheur données (PANNE) · kill-switches · **auto-intégrité**. Rapport `thermo/VEILLEUSE.md` + journal + ALERTE_[ts].json + lance l'alerte vocale. `MAINTENANCE_PREVUE` suspend |
| `scripts/alerte_vocale.py` | Boucle STRICTE 24h/24 : répète toutes les 30s (edge_tts Vivienne), piste unique, **extinction manuelle** (STOP_ALERTE / arret_alerte), journal ALERTE_[id].json |
| `plists/com.ace777.veilleuse.plist` | Launchd StartInterval=600, RunAtLoad |
| `scripts/arret_alerte.sh` | Raccourci d'arrêt d'urgence (STOP_ALERTE + pkill + killall) |

## Tests réels
1. État sain → rc=0, VEILLEUSE.md STABLE ✅
2. **Intrusion réelle** (fichier indexé modifié sans déclaration) → INTRUSION détectée, rc=1,
   ALERTE json, **alerte vocale lancée** ✅
3. **Bug trouvé en test + corrigé** : la veilleuse empilait une boucle vocale à CHAQUE run
   (3 boucles simultanées en test !) → correctif anti-empilement (`pgrep alerte_vocale` →
   « déjà active, pas de nouvel empilement ») ✅
4. Extinction manuelle `arret_alerte.sh` → boucle coupée + nettoyage ✅
5. Auto-intégrité : veilleuse modifiée sans déclaration → détectée ✅

## Erreurs du codeur corrigées par la supervision
1. `veilleuse_synapses.py` **ne compilait pas** : `from pathlib5 import Path if False else...`
   (code invalide), `tempfile` utilisé avant import, **`def` manquant** sur `déclencher_alerte`
2. **Chemins relatifs faux** : RACINE pointait sur Index_Maison au lieu du repo racine →
   « 16 fichiers manquants » en test (corrigé)
3. **Registre faux** : md5 d'un fichier VIDE (d41d8cd9), chemins erronés
   (`config/defaults.env` = hulk-mexc/, pas Index_Maison/)
4. **plist chemin faux** : `/Users/christophe/Index_Maison/...` (manquait ace777-test-day1)
5. **Process attendus incohérents** : discipline-quotidienne = 1×/jour (pas permanent) → retiré

## Décisions
- **Boucle vocale stricte 24h/24** (Christophe) — la limite de sécurité 24h famille est
  désactivée par défaut, réactivable si Christophe change d'avis.
- **Anti-empilement** : 1 seule boucle vocale à la fois (sinon empilement infini).

## Réversibilité
- `launchctl unload com.ace777.veilleuse` + `rm` plist + `rm` des scripts/registre = retour
  à l'état antérieur. Aucune modif du moteur Hulk.
- Release Receipt : RELEASE_RECEIPT_veilleuse_2026-08-15.md
