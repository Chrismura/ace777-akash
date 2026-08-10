# REPONSE GROK — SPEC V2 CORRIGEE (via Puter Grok (gratuit)) — 10/08/2026

**SPEC V2 CORRIGEE - Système ACE777 - Setup 3 Étages (Mac 8 Go)**

Date de référence : 2026-08-10 12:58:09 CEST  
Objectif : passer de 23 services launchd à 12-14 services tout en maintenant /health OK sur le hub (port 11435).  
Règle absolue : **NE JAMAIS TOUCHER au hub ni à ses providers sur le port 11435**. Tous les services liés au hub restent intacts et inchangés.

**Étape 0 – Inventaire exact avant toute action [C1]**  
Exécuter obligatoirement :  
```bash
launchctl list | grep ace777
for svc in $(launchctl list | grep ace777 | awk '{print $3}'); do launchctl print "$svc"; done
```
Mesurer RAM par service (RSS réel) :  
```bash
ps -eo pid,comm,rss | grep -E 'ace777|cockpit|superviseur'
```
Analyser toutes les dépendances inter-services via launchctl print et les logs.  
Documenter l’inventaire complet (services, RAM, dépendances) dans state.json avant de passer à l’étape suivante. Aucune suppression sans cet inventaire.

**Étape 1 – Backup plists obligatoire [C3]**  
```bash
tar -czf ~/Library/LaunchAgents/backup_ace777_$(date +%Y%m%d_%H%M).tar.gz ~/Library/LaunchAgents/com.ace777.*
shasum -a 256 ~/Library/LaunchAgents/backup_ace777_*.tar.gz > checksums.txt
```
Test de réversibilité :  
- Extraire dans /tmp/test_restore  
- `launchctl load` des plists restaurés  
- Vérifier que les services redémarrent correctement  
- Supprimer le test et confirmer que l’original est intact avant de continuer.

**Étape 2 – Configuration du superviseur [C2][C10]**  
Plist du superviseur :  
- Remplacer KeepAlive:false + ThrottleInterval:1800 par **StartInterval:1800** OU **KeepAlive:true** avec boucle interne sleep 60-120 s.  
- Ajouter un wrapper KeepAlive:true ou un watchdog dédié (com.ace777.watchdog) pour relancer le superviseur en cas de crash.  
Le superviseur ne doit jamais être lancé une seule fois ; il doit être relancé automatiquement.

**Étape 3 – Cohabitation cockpit [C4]**  
cockpit.py doit d’abord **lire et cohabiter** avec com.ace777.cockpit-http et com.ace777.cockpit-pont.  
- Exposer exactement la même API que les services existants.  
- Basculer les consommateurs uniquement après validation de l’API.  
- Ne pas unload cockpit-http ni cockpit-pont à cette étape.

**Étape 4 – Réduction des services un par un [C5]**  
Pour chaque service candidat à la suppression :  
1. Audit des dépendances (launchctl print + logs).  
2. Unload unique.  
3. Attendre 10 minutes.  
4. Vérifier RAM, services vivants, /health hub, et absence de régression.  
5. Valider avant de passer au service suivant.  
Jamais plus d’un service désactivé à la fois.

**Étape 5 – Mode probatoire et compteur journalier [C6]**  
Utiliser un fichier state.json persistant avec compteur journalier.  
Règle : maximum **1 type d’action par jour** (suppression, modification ou test).  
Alternative autorisée : mode dry-run observation uniquement pendant les 7 premiers jours.

**Étape 6 – Gestion des permissions et alertes [C7]**  
Le superviseur effectue uniquement : stat + alerte + journal.  
Aucun chmod 444 automatique (ni aucune écriture).  
En cas de détection de permission incorrecte : alerte + sanction via Étape 4 (unload du service fautif après audit).

**Étape 7 – Contraintes RAM et implémentation [C8]**  
Cible superviseur : < 50 Mo RSS (Python + stdlib uniquement : urllib, subprocess, vm_stat, launchctl).  
Aucune bibliothèque externe lourde. Mesurer RSS réel avant et après chaque modification.

**Étape 8 – Test de charge avant activation pleine [C9]**  
Lancer le superviseur avec les 13 services cibles pendant **1 heure minimum**.  
Mesurer : RAM, CPU, latence, /health hub.  
Comparer avec les métriques de référence prises avant le test.  
Validation obligatoire avant passage en production.

**Étape 9 – Timeouts cockpit.py [C11]**  
Implémenter timeout strict : **max 2 secondes par provider**.  
Si un provider dépasse 2 s, le cockpit l’ignore et continue sans bloquer le cycle.

**Règles transverses**  
- Toutes les modifications passent par les étapes 0 à 9 dans l’ordre.  
- Aucun service du hub (port 11435) n’est jamais listé, unloadé, modifié ni touché.  
- state.json contient l’inventaire, le compteur journalier et les métriques de référence.

VERDICT SPEC V2 : OK.
