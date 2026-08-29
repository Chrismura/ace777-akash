# 🧭 CE QUI TOURNE MAINTENANT — L'EXPLICATION SIMPLE (29/08/2026)

> Christophe : « il faut que tu rajoutes une explication de tout ça dans Index
> Obsidian, au premier coup d'œil personne ne comprend même devant son nez.
> Ça nous permet aussi de valider et faire valider l'efficacité et le bon
> fonctionnement de cette formule. »
> Ce document est LE point d'entrée pour comprendre — une autre IA doit pouvoir
> lire ça et savoir quoi vérifier.

---

## EN 30 SECONDES (si tu ne lis qu'une section)

| Quoi | En une phrase | Où le voir |
|---|---|---|
| **🩺 SANTÉ DES INDEX** (cockpit) | 13 chaînes surveillées — si une case est rouge, quelque chose ne tourne plus | Cockpit → carte SANTÉ |
| **📡 CROISEMENT EXTERNE** | Avant chaque décision, nos prix sont vérifiés contre MEXC/Binance — écart > 5 % = **on ne décide pas** | Cockpit SANTÉ + `data/croisement_externe_etat.json` |
| **🎭 SIGNAL 3 — LIVRE ÉCORCHÉ** | Détecte le vacuuming (trou d'air du carnet) sur nos paires — le plus mortel pour les small caps | `hulk-mexc/runs/signal3_livre_ecorche.json` |
| **🧪 POUSSIÈRE INSTITUTIONNELLE** | Le RBF plat = script industriel qui connaît ses frais (vs retail qui tatone) — VALIDÉ par nos données (corr −0.275) | Session Cortana `poussiere-20260829-152854` |

---

## 1. 📡 LE PROTOCOLE DE CROISEMENT EXTERNE (règle des 2 sources)

**Le problème qu'il résout** : on a pris plusieurs décisions sur des données
fausses (QAIT 66M BTC impossibles, mempool.space down, structure mal lue).
**La solution** : avant toute décision importante, on vérifie nos chiffres
contre une source externe.

```
NOS PRIX (croisement_contexte.jsonl)  ──┐
                                        ├─→  écart > 5 %  =  ⛔ FAIL = on NE décide PAS
MEXC + BINANCE (ticker live)         ──┘
```

- **Prix** : contrôle FIN (5 %). C'est la donnée critique d'exécution → alerte `data_quality`.
- **Murs** : contrôle d'ORDRE DE GRANDEUR (x0.05-x20). Moyenne historique vs
  snapshot instantané varie naturellement → warning informatif, PAS une alerte.

**Fichiers** :
- Script : `Index_Maison/scripts/croiser_donnees_externes.py`
- État cockpit : `Index_Maison/data/croisement_externe_etat.json`
- Registre d'audit : `Index_Maison/data/croisement_externe.jsonl`
- Plist : `com.ace777.croisement-externe` (toutes les 30 min)
- **Quelles paires** : `hulk-mexc/strategie/paires_croisement.json`
  (deepdive = croisées · observation = prix seul · exclues = JAMAIS)

**Test de validation (comment savoir si ça marche)** : le 29/08, on a simulé un
prix XRP corrompu ×10 → détecté avec écart 900 % → FAIL + alerte. Si tu veux
vérifier : `python3 Index_Maison/scripts/croiser_donnees_externes.py` → il doit
dire « 0 fail prix ».

## 2. 🎭 LE SIGNAL 3 — SQUEEZE DU LIVRE ÉCORCHÉ

**Le mécanisme** : un manipulateur met un faux mur, retire la liquidité réelle
derrière, puis supprime le mur → trou d'air → le prix décroche instantanément.
**Pour nous** : c'est le signal le plus dangereux pour nos small caps (trou
d'air de 10-20 % possible).

```
spoof_pct > 5 %  ET  drop > 100  ET  spread ≤ 70 bps  →  persistance 2/3 mesures
```

**Le chaînon manquant (le plus précieux)** : les manipulateurs n'attaquent PAS
nos small caps directement — ils amorcent sur **BTC/ETH** et l'onde se propage.
Si `btc_spoof_pct > 5 %` → seuils abaissés de 20 % sur certaines paires
(origine = `contagion_btc`).

**CORRECTIONS FAMILLE APPLIQUÉES (29/08 soir)** — fini la contagion aveugle :
- **β_asset** : la contagion n'est appliquée à une paire QUE si sa corrélation
  1h avec BTC ≥ 0,3 (paire découplée = contagion ignorée à 100 %).
- **Asymétrie** : contagion UNIQUEMENT en phase baissière (delta_btc < 0).
  Un spoof haussier sur BTC ne paralyse plus nos paires.
- **Filtre MAD** : anti-jitter (un bot qui retire/remet un ordre en 200 ms ne
  crée plus de faux signal).

**Fichiers** :
- Script : `hulk-mexc/scripts/signal3_livre_ecorche.py`
- Résultat : `hulk-mexc/runs/signal3_livre_ecorche.json`
- Plist : `com.ace777.signal3-livre-ecorche` (30 min)

## 3. 🧪 LA POUSSIÈRE INSTITUTIONNELLE (le RBF plat)

**La pépite de Cortana (29/08, session 4 tours)** : quand un gros acteur
fragmente des milliers de BTC en micro-transactions pour passer inaperçu, il
**connaît ses frais par avance** → son taux de RBF est anormalement bas.
Le retail, lui, tatone et utilise massivement le RBF.

**VALIDÉ PAR NOS DONNÉES** : corrélation micro_tx/RBF = **−0.275** sur 13 933
points — quand les micro-tx montent, le RBF s'effondre (0.286 vs 0.599).

**État** : 3 des 4 termes du SAPI (Score d'Alerte Poussière) sont codables
avec nos données — seul le delta du carnet spot manque (proxy dispo).

**CORRECTIONS FAMILLE APPLIQUÉES (29/08 soir)** :
- **Normalisation σ1h** : le proxy carnet spot est divisé par la volatilité du
  spread sur 1h — un carnet vide/volatile ne déclenche plus de faux positif.
- **Persistance 3 ticks** : l'alerte ne s'allume qu'après 3 runs consécutifs
  ≥ 0,75 (faux positifs isolés tués).
- **Écriture atomique** partout (fichiers jamais corrompus).

## 4. 👩🔬 QUI EST ADA (pour éviter la confusion)

- **Ada l'IA** = l'orchestratrice DÉTERMINISTE (pas une IA) : `ada_saison.py`
  (6 indices → saison CALME→CHAOS) + `ada_gardienne.py` (voilure, zones, alertes).
  Elle tourne dans le cycle `cockpit_mission_feed.py`. **Elle n'a PAS été enlevée** —
  vérifié 29/08 16:03Z (saison CALME, gardienne VERT 91 %).
- **ADA la crypto (Cardano)** = ÉJECTÉE le 28/08 (décision Christophe : confusion
  avec Ada l'IA + aucun intérêt). Absente de observation_list (retired), du
  portefeuille, du croisement. NE PAS la réintroduire sans GO explicite.

## 5. ✅ COMMENT VALIDER QUE ÇA MARCHE (checklist rapide)

1. **Cockpit → SANTÉ DES INDEX** : la chaîne « CROISEMENT EXTERNE » doit être VERTE
   (process chargé + fichier frais + 0 fail prix).
2. **Terminal** : `python3 Index_Maison/scripts/croiser_donnees_externes.py`
   → « 0 fail(s) prix ».
3. **Signal 3** : `python3 hulk-mexc/scripts/signal3_livre_ecorche.py`
   → « aucune alerte » (marché calme) mais les paires à risque ressortent.
4. **Registre** : `tail Index_Maison/data/croisement_externe.jsonl` → des lignes
   avec `"verdict": "ok"` toutes les 30 min.
5. **Persistance croisement (29/08 soir)** : un prix en écart reste en
   « surveillance » (pendant) 2 runs, et ne devient bloquant qu'au 3ᵉ run
   consécutif → `"verdict": "fail"` + alerte data_quality. Micro-pic =
   ignoré.

## 6. 🛡️ LES CORRECTIONS FAMILLE N°4 (29/08 litté — GO)

L'audit famille a fait converger 4 affinages (tous appliqués et testés) :

| Correction | Où | Effet |
|---|---|---|
| **Dynamic Spread Percentile** | Signal 3 | Fini le seuil spread fixe (70 bps) : c'est maintenant le **p30 des 24h de la paire**. Une small cap à 150 bps, une large cap à 5 bps → chacun comparé à SON histoire ✓ |
| **Heures creuses UTC (02-06)** | Signal 3 + SAPI | La nuit le MM se retire et le spread s'élargit naturellement. Signal 3 : seuil ×1.8. SAPI : le proxy carnet ne compte que ×0.35 (ne confond plus manque de liquidité avec poussière) ✓ |
| **Entropie temporelle** | SAPI | Bonus si le carnet a un rythme quasi-robotique (CV ≤ 15%, signature d'un script de poussière), jamais seul déclencheur ✓ |
| **PathRegistry + wrapper plists** | Toutes | `path_registry.py` centralise les chemins : toute œuvre valide au démarrage (arrêt propre si chemin manquant). Les 3 plists écrivent un heartbeat → plus de mort silencieuse ✓ |

**Vérifier que ça tourne** :
1. `ls Index_Maison/data/heartbeat_*.json` → 3 fichiers à `"statut": "ok"`
2. `python3 Index_Maison/scripts/path_registry.py verifier sapi -f` → `OK`
3. Signal 3 → dans `signal3_livre_ecorche.json`, chaque paire expose
   `spread_seuil_dyn` / `spread_p30_24h` (au lieu d'un 70 fixe)
4. SAPI → `Index_Maison/thermo/live.json` expose `sapi.composantes` avec
   `coef_heure_creuse` et `entropie_tempo`

## Fichiers liés
- Protocole détaillé : `PROTOCOLE_CROISEMENT_EXTERNE_20260829.md`
- Deepdive signal 3 : `hulk-mexc/docs/DEEPDIVE_MANIPULATION_3SIGNAUX_20260829.md`
- Vision poussière validée : `hulk-mexc/docs/POUSSIERE_INSTITUTIONNELLE_VISION_20260829.md`
