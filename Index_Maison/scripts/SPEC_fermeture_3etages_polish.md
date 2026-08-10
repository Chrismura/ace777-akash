# SPEC — POLISH ROBUSTESSE de la FERMETURE 3 ÉTAGES (réserves DEEPSEEK R2/R4/R5)

**Auteur spec** : Ada (orchestratrice)
**Destinataire** : LE CODEUR DU HUB (task code.ia — tu codes, Ada intègre/teste)
**Date** : 10/08/2026 — suite à l'audit famille (GO 4/4, 3 réserves d'amélioration DEEPSEEK)
**Loi du brut** : code complet, prêt à copier, commentaires en français, bash macOS.

---

## CONTEXTE

Le correctif précédent (SPEC_fermeture_3etages.md) est intégré et validé GO par
la famille. DEEPSEEK a émis 3 réserves d'amélioration (R2, R4, R5) — NON
bloquantes, mais on veut le durable. Les fichiers actuels sont :

- `~/ace777-test-day1/stop_ace777.sh` (section 3 étages en tête, déjà intégrée)
- `~/ace777-test-day1/ERREURS_AI/COMMANDES_ARRET_ACE777.md`

---

## AMÉLIORATION R4 — Élargir la recherche du filet de sécurité (trivial)

**Fichier A, `stop_ace777.sh`** : la recherche du processus résiduel du gardien
utilise `pgrep -f 'superviseur_core\.sh$'` (le `$` final). Si le processus avait
des arguments (`superviseur_core.sh --mode=...`), elle raterait.

→ Remplacer PARTOUT dans `stop_ace777.sh` :
`pgrep -f 'superviseur_core\.sh$'` par `pgrep -f 'superviseur_core\.sh'`

(idem dans la section « Vérifier que tout est éteint » de la doc, fichier B.)

---

## AMÉLIORATION R5 — Garde-fou si le WATCHDOG refuse de s'arrêter

**Fichier A, `stop_ace777.sh`** : actuellement, si le `bootout` du watchdog
échoue (WARN), le script continue quand même → le watchdog pourrait relancer le
gardien pendant la séquence d'arrêt.

→ Remplacer le bloc `# 1. watchdog` actuel par une version avec garde-fou :

1. `launchctl bootout gui/$(id -u)/com.ace777.watchdog 2>/dev/null`
2. Si succès → `echo "[3ETAGES] com.ace777.watchdog arrêté"` comme aujourd'hui.
3. Si échec :
   a. Si `launchctl list | grep -q "com.ace777.watchdog"` est FAUX → service déjà
      arrêté → `echo "[3ETAGES] com.ace777.watchdog absent (déjà arrêté)"`.
   b. Si le service est ENCORE enregistré → **filet de sécurité** :
      `pkill -9 -f 'watchdog_superviseur' 2>/dev/null` puis re-vérifier avec
      `pgrep -f 'watchdog_superviseur'`. Si le processus est mort → message
      `[3ETAGES] com.ace777.watchdog arrêté EN FORCE (bootout échoué, kill -9)`.
      Si le processus est TOUJOURS vivant → **message d'alerte très visible**
      `!!! ALERTE : LE WATCHDOG EST ENCORE ACTIF — arrêt interrompu, vérifier manuellement !!!`
      puis `exit 1` (ne PAS continuer la séquence : le watchdog relancerait tout).

Le reste de la section 3 étages (superviseur-core, cockpit-pont, cockpit-http)
reste INCHANGÉ.

---

## AMÉLIORATION R2 — La doc doit refléter l'arrêt COMPLET

**Fichier B, `COMMANDES_ARRET_ACE777.md`** : le one-liner actuel ne tue qu'une
partie des anciens processus (master/genesis/tail), alors que le script réel en
tue beaucoup plus (launch_vortex_v2_collab, watchdog_ace777, caffeinate, bash -s,
radar_gate, ruby.*sleep, vortex_supervisor_v2_llm.rb...). Un copier-coller de la
doc laisserait des résidus.

→ Restructurer la doc ainsi :

1. **« LA commande officielle »** en tête : `./stop_ace777.sh` (qui fait TOUT :
   les 4 bootout 3 étages + tous les anciens processus). C'est LA façon de faire.
2. **One-liner de secours** (si on ne peut pas lancer le script) : les 4
   `launchctl bootout` (ordre watchdog en premier) + la liste COMPLÈTE des
   `pkill -9 -f` du script réel (copier la section « anciens processus » de
   `stop_ace777.sh` telle quelle) + `echo "Arrêté"`.
3. Conserver les sections « Vérifier que tout est éteint » (avec le pgrep élargi
   R4) et « Redémarrer SANS reboot » (inchangées).

---

## CONTRAT DE SORTIE

- Le code COMPLET des 2 fichiers modifiés, prêt à copier-coller.
- Explication brève (3-5 lignes max) de ce qui a changé par rapport à la version
  précédente (R2, R4, R5).
- Zéro changement ailleurs. `set -uo pipefail` conservé. Commentaires en français.
