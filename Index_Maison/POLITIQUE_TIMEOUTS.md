# ⏱️ POLITIQUE DES TIMEOUTS — ACE777 (gravée le 10/08/2026)

> Décision Christophe : *« mettre en temps illimité en mode défaut »* après avoir
> perdu des appels IA entiers (codeur nvidia, audit) à cause de timeouts trop
> courts qui tuaient le processus en plein milieu. Plus jamais ça.

## 🏛️ RÈGLE ABSOLUE : `timeout=None` sur tout appel au hub

Tout `urlopen` qui envoie une mission au hub (port 11435) doit **impérativement**
utiliser `timeout=None` (illimité). **Aucune exception.** On ne coupe JAMAIS une IA
en plein raisonnement — qu'elle mette 30 s ou 30 min, on attend.

```python
# ✅ BON — temps illimité (loi du brut : l'IA répond quand elle est prête)
with urllib.request.urlopen(req, timeout=None) as resp:
    
# ❌ MAUVAIS — timeout numérique, l'IA sera coupée
with urllib.request.urlopen(req, timeout=600) as resp:   # EXTERMINÉ LE 10/08
```

### ⚡ Unicité exception : les health-checks (timeout ≤ 6 s)
Seule exception autorisée : les `health` / `ping` / `/api/tags` qui vérifient
si un service est vivant. Ceux-là doivent être rapides (6-10 s max) car un
service qui ne répond pas en 6 s est soit mort, soit trop lent pour être utile.

```python
# ✅ OK pour health-check uniquement
urllib.request.urlopen(req, timeout=6)
```

## 🛠️ Correction appliquée le 10/08/2026 — 74 scripts assainis

| Zone | Scripts corrigés | Détail |
|---|---|---|
| `~/test-freebuff/*.py` | **59** soumission/délégation/audit → `None` | Tous les scripts de dialogue avec le hub |
| `~/ace777-test-day1/Index_Maison/scripts/*.py` | **8** appels IA longs (coffre, cortana, brancher, qwen...) → `None` | Scripts de production (protégés 444 restaurés) |
| `~/prise-ia/hub_prise_ia.py` | Patience config 180→600s, plafond 600→1800s | Le hub attend plus longtemps les providers |
| Hub routing `max_tokens` | Contexte réduit pour éviter les timeouts génération | Le codeur nvidia répond plus vite avec un payload plus petit |

## 🔧 Comment lancer les soumissions au hub (règle pour l'IA)

Quand tu soumets une mission au hub (script de délégation, audit, consultation) :

1. **Dans le script** : `urllib.request.urlopen(req, timeout=None)`
2. **Dans le basher** : `timeout_seconds: -1` (pas de clamp à 600 s)
3. **Si l'appel est très long (> 10 min)** : utiliser le pattern `setsid` :
   ```bash
   setsid nohup python3 script.py > /tmp/scipt.log 2>&1 &
   ```
   → `setsid` détache du process group → le processus **survit** à la fin du basher.
   → Poller le fichier de sortie.

## 📜 Fichiers de la règle

- `POLITIQUE_TIMEOUTS.md` (ce fichier) — la règle gravée
- `fix_timeouts_masse.sh` — script de correction en masse 59 fichiers
- `fix_timeouts_maison.sh` — correction ciblée maison (timeout ≥ 60)
- Preuve git : commit `89f1db1` + cette entrée

> **LoI du brut** : on ne coupe pas une IA qui réfléchit. Timeout=None.
---

## 📜 Référence contractuelle

La règle des audits regroupés est gravée dans le **CONTRAT_AUTOGESTION** article **1sexies** :
> « On ne soumet pas chaque changement un par un — on accumule les modifications
> et on soumet un seul audit diff par chantier. Maximum 1 audit famille par jour. »

→ Le contrat vit dans le vault Obsidian (`CONTRAT_AUTOGESTION.md`)
  et sa copie dans `Index_Maison/CONTRAT_AUTOGESTION.md`.
