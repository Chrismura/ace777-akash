# 📋 INVENTAIRE 3 ÉTAGES — Étape 0 [C1] — 2026-08-10 13:01:39 CEST

> Inventaire MÉCANIQUE (lecture seule, aucune modification). Point C1 du jugement famille : aucun service ne sera supprimé sans cet inventaire.

## 1. launchctl list (services ace777)

`-	0	com.ace777.observatoire`
`-	0	com.ace777.catalogue`
`-	0	com.ace777.gitpush-vault`
`-	0	com.ace777.superviseur`
`684	0	com.ace777.cockpit-http`
`-	0	com.ace777.cortana.horaire`
`-	0	com.ace777.propose-ameliorations`
`-	0	com.ace777.state-generator`
`-	0	com.ace777.graph-cerveau`
`27669	-15	com.ace777.prise-ia`
`-	0	com.ace777.analyse-usage`
`-	0	com.ace777.analyste-cadence`
`-	0	com.ace777.superviseur-core`
`-	1	com.ace777.verif-setup`
`701	0	com.ace777.cockpit-pont`
`-	0	com.ace777.journal-soir`
`-	0	com.ace777.gitpush`
`32184	0	com.ace777.cortana.urgent`
`-	0	com.ace777.eval-offres`
`-	0	com.ace777.brief-matin`
`-	0	com.ace777.backup-check`
`-	0	com.ace777.autopilote`
`-	0	com.ace777.veille-hub`

## 2. RAM RSS réelle par service (Mo)

| Service | PID | RAM (Mo) |
|---|---|---|
| com.ace777.observatoire | - | - |
| com.ace777.catalogue | - | - |
| com.ace777.gitpush-vault | - | - |
| com.ace777.superviseur | - | - |
| com.ace777.cockpit-http | 684 | 1 |
| com.ace777.cortana.horaire | - | - |
| com.ace777.propose-ameliorations | - | - |
| com.ace777.state-generator | - | - |
| com.ace777.graph-cerveau | - | - |
| com.ace777.prise-ia | 27669 | 22 |
| com.ace777.analyse-usage | - | - |
| com.ace777.analyste-cadence | - | - |
| com.ace777.superviseur-core | - | - |
| com.ace777.verif-setup | - | - |
| com.ace777.cockpit-pont | 701 | 1 |
| com.ace777.journal-soir | - | - |
| com.ace777.gitpush | - | - |
| com.ace777.cortana.urgent | 32184 | 2 |
| com.ace777.eval-offres | - | - |
| com.ace777.brief-matin | - | - |
| com.ace777.backup-check | - | - |
| com.ace777.autopilote | - | - |
| com.ace777.veille-hub | - | - |
| **TOTAL** | — | **26 Mo** (4 services vivants) |

## 3. Dépendances / config (launchctl print)

### com.ace777.observatoire

```
program = /usr/bin/python3
			keepalive = 0
	properties = inferred program | managed LWCR | has LWCR
```

### com.ace777.catalogue

```
program = /usr/bin/python3
			keepalive = 0
	properties = inferred program | managed LWCR | has LWCR
```

### com.ace777.gitpush-vault

```
program = /bin/bash
	properties = low priority i/o | inferred program | managed LWCR | has LWCR
```

### com.ace777.superviseur

```
program = /usr/bin/python3
	properties = runatload | inferred program | managed LWCR | has LWCR
```

### com.ace777.cockpit-http

```
program = /usr/bin/python3
	properties = keepalive | runatload | inferred program | managed LWCR | has LWCR
```

### com.ace777.cortana.horaire

```
program = /bin/bash
	properties = runatload | inferred program | managed LWCR | has LWCR
```

### com.ace777.propose-ameliorations

```
program = /usr/bin/python3
			keepalive = 0
	properties = inferred program | managed LWCR | has LWCR
```

### com.ace777.state-generator

```
program = /usr/bin/python3
	properties = runatload | low priority i/o | inferred program
```

### com.ace777.graph-cerveau

```
program = /bin/bash
			keepalive = 0
	properties = inferred program | managed LWCR | has LWCR
```

### com.ace777.prise-ia

```
program = /usr/bin/python3
	properties = keepalive | runatload | inferred program | managed LWCR | has LWCR
```

### com.ace777.analyse-usage

```
program = /usr/bin/python3
			keepalive = 0
	properties = inferred program | needs LWCR update | managed LWCR
```

### com.ace777.analyste-cadence

```
program = /bin/bash
			keepalive = 0
			keepalive = 0
	properties = inferred program | managed LWCR | has LWCR
```


## 4. Plists présents dans ~/Library/LaunchAgents

- `com.ace777.analyse-usage.plist`
- `com.ace777.analyste-cadence.plist`
- `com.ace777.autopilote.plist`
- `com.ace777.backup-check.plist`
- `com.ace777.brief-matin.plist`
- `com.ace777.catalogue.plist`
- `com.ace777.cockpit-http.plist`
- `com.ace777.cockpit-pont.plist`
- `com.ace777.cortana.horaire.plist`
- `com.ace777.cortana.urgent.plist`
- `com.ace777.eval-offres.plist`
- `com.ace777.gitpush-vault.plist`
- `com.ace777.gitpush.plist`
- `com.ace777.graph-cerveau.plist`
- `com.ace777.journal-soir.plist`
- `com.ace777.observatoire.plist`
- `com.ace777.prise-ia.plist`
- `com.ace777.propose-ameliorations.plist`
- `com.ace777.state-generator.plist`
- `com.ace777.superviseur-core.plist`
- `com.ace777.superviseur.plist`
- `com.ace777.veille-hub.plist`
- `com.ace777.verif-setup.plist`

**Total plists : 23**
---

## 💾 ÉTAPE 1 [C3] — BACKUP PLISTS (10/08 13:02)

- **Backup** : `~/Backups/ace777/plists_avant_3etages_20260810_1302/`
- **23 plists** copiés avec permissions préservées (`cp -p`)
- **Checksums** : `checksums.txt` (SHA-256 des 23 plists)
- **Test de réversibilité** : restore + comparaison → **identique ✅**
- **Hashs vérifiés vs live** : prise-ia, superviseur-core, cockpit-http → **tous identiques ✅**

→ Aucune suppression possible sans ce backup. Rollback = recopier les plists + `launchctl load`.
