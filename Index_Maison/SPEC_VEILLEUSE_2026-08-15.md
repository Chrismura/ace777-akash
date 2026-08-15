# SPEC — Veilleuse / Synapse + alerte vocale en boucle (15/08/2026)

**Statut** : approuvée famille (GO-AVEC-RÉSERVE, gemini 92% / nvidia 78%) + arbitrage
supervision + **décision Christophe : boucle vocale STRICTE 24h/24 jusqu'à extinction
manuelle** (la réserve nvidia sur l'atténuation nocturne est écartée — volonté du
propriétaire, documentée honnêtement). Zéro touche moteur Hulk.

---

## 1. Objectif

Un **fil logique (synapse)** qui relie tout le code (d'où vient chaque chose, qui l'a
modifié, son état) + une **veilleuse** qui surveille en continu (pannes + intrusions) +
une **alerte vocale en boucle** qui hurle jusqu'à extinction manuelle.

## 2. Livrables

| Fichier | Rôle |
|---|---|
| `strategie/REGISTRE_SYNAPSES.json` | Index des composants critiques (noyau prod, 30-50 entrées) |
| `scripts/veilleuse_synapses.py` | Vérifie md5 + process + fraîcheur + kill-switches (cadence 10 min) |
| `scripts/alerte_vocale.py` | Alerte vocale EN BOUCLE stricte 24h/24, identifiant unique, extinction manuelle |
| `plists/com.ace777.veilleuse.plist` | Launchd StartInterval=600 |
| `thermo/VEILLEUSE.md` + journal `data/alertes/ALERTE_*.json` | Rapport + traçabilité |

## 3. Registre des synapses — `REGISTRE_SYNAPSES.json`

```json
{
  "version": 1,
  "updated": "2026-08-15",
  "fichiers": [
    {
      "nom": "scripts/paper_diprip.py",
      "role": "Moteur Hulk (paper MEXC dip&rip)",
      "origine": "chantier hulk",
      "md5": "…",
      "maj_attendue": "2026-08-15",
      "auto_modifiable": false,
      "verif": "md5"
    },
    {
      "nom": "thermo/live.json",
      "role": "Données live cockpit/Cortana/Ada",
      "origine": "thermo_quotidien_free",
      "auto_modifiable": true,
      "verif": "fraicheur",
      "fraicheur_max_min": 10
    }
  ]
}
```

### Règles (verdict famille)
1. **Noyau critique uniquement** : scripts lancés par launchd, plists actives, configs
   sensibles, moteur core. **30-50 entrées max.** Pas de logs/caches/dev.
2. **`verif`** : `md5` (fichiers stables) OU `fraicheur` (données qui changent en continu —
   live.json, whales… → timestamp < fraicheur_max_min).
3. **`maj_attendue`** : toute modif légitime met à jour le registre (via RELEASE_RECEIPT).
   Un écart md5 SANS mise à jour = **INTRUSION**.
4. **`auto_modifiable: true`** : fichiers qui se modifient eux-mêmes (journaux internes) —
   exclus de la vérif md5.

## 4. Veilleuse — `veilleuse_synapses.py` (cadence 10 min)

Vérifications hiérarchisées (verdict famille) :
1. **Intégrité md5** des fichiers indexés (`verif: md5`) → écart non déclaré = INTRUSION.
2. **Process attendus vivants** (`launchctl list` + pgrep) → panne/crash.
3. **Fraîcheur** des fichiers `verif: fraicheur` → blocage silencieux.
4. **Kill-switches présents** (STOP, STOP_ALL) → sécurité en place.
5. **Auto-intégrité** : la veilleuse vérifie son propre md5 (compromission de la veilleuse).

Sortie : `thermo/VEILLEUSE.md` (rapport lisible) + journal append-only + **rc ≠ 0 + alerte
vocale si anomalie**. Messages distincts :
- « ALERTE INTRUSION : modification non déclarée de [fichier] »
- « ALERTE PANNE : [process] inactif depuis [durée] »

## 5. Alerte vocale — `alerte_vocale.py` (CARTE BLANCHE Christophe)

- **Boucle STRICTE 24h/24** : répète le message toutes les **30 s** (pause 5 s entre
  répétitions) via edge_tts (voix Vivienne, `speak_text` pattern existant).
- **Priorité absolue** : `killall say` avant chaque lecture (règle maison — l'alerte écrase
  les autres voix).
- **Identifiant unique** : `ALERTE_VEILLEUSE_YYYYMMDD_HHMM` → le fichier d'extinction est
  précis (ne tue pas une autre alerte).
- **Extinction manuelle** : `touch STOP_ALERTE` (fichier avec l'identifiant) OU
  `arret_alerte` (script raccourci) OU kill du process. **C'est la SEULE façon d'arrêter.**
- **Journal** : chaque alerte écrit `data/alertes/ALERTE_[ts].json` (message, cause, heure).
- **`MAINTENANCE_PREVUE`** : si ce fichier existe (avec date de fin), la veilleuse
  suspend ses alertes pendant la fenêtre (évite les fausses alertes pendant une intervention).
- ⚠️ **Limite de sécurité 24h : DÉSACTIVÉE par défaut** (volonté Christophe — boucle stricte).
  Réactivable via config si Christophe change d'avis.

Usage : `python3 alerte_vocale.py --message "..." [--id ALERTE_...] [--arret]`

## 6. Plists

- `com.ace777.veilleuse.plist` : StartInterval=600, `python3 veilleuse_synapses.py`,
  logs /tmp/veilleuse.out.log + .err.log.
- L'alerte vocale est lancée par la veilleuse en détaché (nohup) quand une anomalie est
  détectée — pas de plist propre (elle s'arrête à l'extinction).

## 7. Tests

1. Registre : JSON valide, fichiers indexés existants, md5 calculés.
2. Veilleuse : état sain → rc=0, VEILLEUSE.md écrit ; simulation intrusion (toucher un
  fichier indexé sans maj registre) → rc≠0 + message INTRUSION ; simulation panne
  (process absent de la liste attendue) → message PANNE.
3. Alerte vocale : lancement → voix entendue (edge_tts) · `touch STOP_ALERTE` → arrêt propre
  · identifiant unique.
4. Plist : lint + chargée + run 10 min.

## 8. Réversibilité

- `rm` des 4 fichiers + `launchctl unload` → retour à l'état antérieur.
- Registre : régénérable (le script d'init calcule les md5).
- Release Receipt à remplir à la fin.
