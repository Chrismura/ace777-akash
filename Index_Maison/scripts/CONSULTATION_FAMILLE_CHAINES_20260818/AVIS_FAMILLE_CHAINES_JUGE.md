

GO-AVEC-RÉSERVE.  
La chaîne est globalement logique, mais le double sas est contradictoire : toute nouvelle offre, y compris `obs-*`, doit passer par observation `enabled:false` pendant 48h avant activation, avec rollback par désactivation uniquement.  
Le roulement à >2 jours est accepté s’il reste backup avant écriture, atomique, 1 remplacement max, kill switch `STOP_HUB` et journal d’audit.