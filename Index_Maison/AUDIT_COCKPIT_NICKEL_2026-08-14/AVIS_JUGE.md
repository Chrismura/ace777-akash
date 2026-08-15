# JUGE — juge.tranche

**1. Verdict par correctif :**
1. **PONT /mission TTL 30s** : GO — Élimine efficacement le spam CPU du sous-processus toutes les 10s.
2. **ada_saison : archive JSONL** : GO — Sauve l'inode disque en passant d'une explosion de fichiers à un historique propre avec rotation.
3. **cortana_urgent_poll.sh TTL 30s** : GO — Aligné sur le correctif #1, bloque la redondance inutile du cron/launchd.
4. **Conflit de pont résolu** : GO — Nettoie proprement l'orphelin et redonne le contrôle absolu à launchd.
5. **MUTE aligné (5 chemins voix)** : GO — Enfin cohérent, la Cortana locale respecte le mode silencieux global.
6. **Cortana dit la vérité** : GO — Interroge le pont en direct et évite les affabulations sur l'état des moteurs.
7. **Graph + hub résidus** : GO AVEC RESERVES — Z-index corrigé et lecture JSONL fiabilisée, mais attention à la taille maximale du tampon 256 Ko si les flux s'emballent.

**2. Risque résiduel le plus important :**
Le découplage par cache TTL (30s sur `/mission` et le poll) peut masquer un blocage ou un gel du `mission.json` en amont pendant une demi-minute, affichant un état périmé trompeur si un bot plante soudainement.

**3. Amélioration concrète GO-sized :**
Ajouter un indicateur visuel de fraîcheur (ex: couleur ou âge exact en secondes "il y a X sec") sur le cockpit basé sur le timestamp réel du cache pour voir immédiatement si le fichier `mission.json` cesse d'être mis à jour.
