# 📍 OÙ ON EN EST — système, sondes, et le débat 02-06 vs volume (29/08)

> Lisible en 2 minutes. Ce document répond à : « explique-moi bien où on en est,
> pourquoi, et ce qu'il reste à faire — sans rien oublier. »

---

## 1. 🧭 OÙ ON EN EST (en une page)

Le débat de la semaine : **l'affinage famille n°4** (4 corrections sur nos
détecteurs de manipulation), validé par la famille (6 IA), critiqué par Cortana
(IA extérieure), re-critiqué par la famille, re-réfléchi par Cortana. Résultat :
**un accord tripartite** (famille + Cortana + moi) sur la direction, ET **une
découverte qui change tout** : on ne pouvait pas trancher le débat principal
parce qu'on n'a **aucune donnée de volume traded**.

### Les 4 corrections de l'affinage n°4 (état : TOUTES codées, testées, branchées)
| # | Correction | Où | Statut |
|---|---|---|---|
| 1 | **Dynamic Spread Percentile** (seuil = p30 des 24h de la paire, plus de 70 bps fixe) | Signal 3 | ✅ testé (XRP p30=1.45 au lieu de 70) |
| 2 | **Heures creuses UTC 02-06** (Signal 3 : seuil ×1.8 ; SAPI : proxy ×0.35) | Signal 3 + SAPI | ✅ testé |
| 3 | **Entropie temporelle** (bonus SAPI si rythme robotique CV≤15 %) | SAPI | ✅ testé (entropie_tempo=1.0, score 0.399) |
| 4 | **PathRegistry + wrapper plists** (chemins validés au démarrage + heartbeat) | Toutes | ✅ testé (3 plists à heartbeat) |

### Le débat et sa conclusion (chronologie)
1. **Famille** (audit) → 4 corrections, « GO avec réserves ».
2. **Cortana** (round 1) → 3 critiques : la 24h du p30 est un « miroir rétroviseur »,
   la plage UTC est « une erreur de débutant / angle mort », l'entropie est trop locale.
3. **Famille** (contre-consultation) → 6/6 « GO avec réserves » : Cortana a raison
   sur la rigidité, mais **ses remèdes (ATR pur, matrice lourde) sont des bombes à
   faux positifs** sur nos small caps. Proposition : hybride + compteur d'essaim léger.
4. **Cortana** (round 2, sans influence) → elle **révise sa position** : l'ATR pur et
   la matrice sont abandonnés, elle propose un compromis codable
   (`max(p30_24h, EWMA_ATR(span=4) × 0.7)`) et son verdict final =
   **« Option A du JUGE + variante INFERX »** : hybride pour le seuil + garder
   02-06 avec gardien dynamique de volume.
5. **Moi (Buffy)** — l'avis que Christophe a validé :
   - **Hybride spread (0.7×p30_24h + 0.3×p30_4h)** : POUR, c'est le vrai gain.
   - **Plage UTC : on garde 02-06 POUR L'INSTANT** — mais surtout parce que
     **l'alternative (volume glissant) n'est pas constructible** : on n'a aucun
     volume traded dans nos données. Toute la discussion volume était théorique.
   - **Compteur d'essaim** : bonne idée de fond (les baleines tapent des paniers,
     pas des jetons), mais la version famille (≥3 paires CV≤15 % simultanément)
     créerait des faux positifs la nuit (toutes les small caps dorment en même
     temps) → à conditionner + mettre en observation.

### 🆕🆕 SUITE LOGIQUE FAITE (29/08 litté, GO Christophe « enchaîne logiquement ») :

**1. Hybride spread codé et testé** (`signal3_livre_ecorche.py`) :
- Le seuil spread n'est plus le p30_24h pur : c'est maintenant **`0.7 × p30_24h + 0.3 × p30_4h`**
  (consensus tripartite famille + Cortana + Buffy).
- Testé sur données réelles : XRP hybride=1.45 (n24=844, n4=142) ; **QAIT** : p30_4h=30.33 vs
  p30_24h=50.48 → seuil baissé à 44.43 (le carnet s'est resserré ces 4h → plus sensible
  MAINTENANT, le « miroir rétroviseur » de Cortana est corrigé) ; **RWAINC** : p30_4h=94.79 vs
  45.26 → seuil monté à 60.12 (spread explosé récemment → pas de faux positif).
- Fail-open hiérarchique : pas assez de mesures 4h → p30_24h pur → sinon seuil nominal.
  Chaque paire expose `spread_seuil_mode` (hybride / 24h_seul / nominal).

**2. Veille d'essaim en OBSERVATION 48h** (`veille_essaim_observation.py`) :
- La trouvaille de Cortana (résonance harmonique inter-actifs : les baleines tapent des
  PANIERS, pas des jetons isolés) codée en version LÉGÈRE (la matrice lourde est rejetée).
- Calcule le CV du spread par paire (fenêtre 1h, seuil ≤ 15 % comme le SAPI) et compte les
  paires « régulières » SIMULTANÉES (dernières mesures alignées < 5 min).
- MODE OBSERVATION STRICT : **aucune décision, aucun seuil modifié** — journalise tout
  (`runs/essaim_hist.jsonl` + `essaim_etat.json`), chaîne cockpit **ESSAIM (OBS)** verte.
- 1er run : 13 paires jugées, 1 régulière (HBAR seule) → 0 essaim (pas de coordination
  actuelle — sain).
- Après 48h : on confronte les essaims capturés aux vrais mouvements pour calibrer le seuil
  N (≥2 ou ≥3 paires ?) et le bonus SAPI (+0.20 ?) AVANT de le passer en décision.

### 🆕 La conséquence : LA SONDE VOLUME PANIER (29/08, GO Christophe)
Pour sortir du débat théorique, on capture DÈS MAINTENANT la donnée qui manquait :
**`sonde_volume_panier.py`** — le volume traded réel (24h + quoteVolume) de
chaque paire du panier, toutes les 30 min.

- **Paires sondées** : 20 = deepdive_validees (BTC, ETH, XRP, CHIP, QAIT, EDEL,
  PYTH, ZBCN, HBAR, RED) + observation_setup (SOL, XLM, ZAMA, PAXG, ALGO, IXS,
  XDC, QNT, JASMY, RIZE).
- **Résultat du 1er run (19:07Z)** : 19/20 présentes sur MEXC (QAIT absente =
  fail-open normal, elle n'est pas sur MEXC spot), **total panier ≈ 546 M$ / 24h**.
- **Sorties** : `hulk-mexc/runs/volume_panier_hist.jsonl` (historique par run) +
  `volume_panier_etat.json` (état live avec la métrique « volume glissant 3h »).
- **Branchement** : plist `com.ace777.sonde-volume-panier` (30 min + RunAtLoad,
  via le wrapper PathRegistry avec heartbeat). **Chargée et tournante** ✓
- **Alerte informative** (PAS bloquante) : si le volume panier chute de −50 % vs
  sa MM24h → warning, mais **la plage 02-06 reste la référence** tant que le
  débat n'est pas tranché avec nos données.

**POURQUOI cette sonde est importante** : dans 48-72h, on aura la base pour
construire le déclencheur « volume glissant » avec de VRAIES données et le
comparer honnêtement à la plage 02-06. C'est exactement le principe qu'on a
appliqué depuis le début : **jamais décider sur des données qu'on n'a pas**.

---

## 2. 🔍 AUDIT DES SONDES (fait à 19:08Z le 29/08)

| Sonde | Fichier vérifié | Fraîcheur | Verdict |
|---|---|---|---|
| observer_murs | `runs/murs_observations.json` | 26 min | ✅ OK |
| croisement externe | `data/croisement_externe_etat.json` | 2 min | ✅ OK |
| signal3 | `runs/signal3_livre_ecorche.json` | 2 min | ✅ OK |
| SAPI (silent_drain) | `data/sdi_latest.json` | 4.6 min | ✅ OK |
| **sonde volume (nouvelle)** | `runs/volume_panier_etat.json` | 0.2 min | ✅ OK |
| bloc privatisé | `data/bloc_privatise.json` | 3 min | ✅ OK |
| thermo (live.json) | `thermo/live.json` | 4.4 min | ✅ OK |
| sante_index | `cockpit/sante_live.js` | 4 min | ✅ OK |
| veille-signal | `data/alertes/ALERTE_poussiere_cpfp.json` | **2 min** | ✅ OK |
| heartbeats plists | `data/heartbeat_*.json` | frais | ✅ OK |

**Résultats de l'audit :**
- **68 jobs launchd chargés**, 9 avec PID actif en permanence, le reste en
  intervalle (normal). **Aucune sonde morte.**
- `ALERTE_poussiere_haute.json` date de 02:11 mais c'est **normal** : ce fichier
  n'est réécrit que quand le score ≥ 45. Le score est redescendu sous le seuil.
- **BONUS découvert à l'audit** : le cockpit est en **amber** car une **alerte
  CPFP est ACTIVE** (poussière 45/50, « signature CPFP détectée — les baleines
  préparent un déplacement massif invisible », 17:16Z). C'est la pépite de
  Cortana (poussière institutionnelle) qui tourne et qui ALERTE pour de vrai.
- **14/14 chaînes OK** au cockpit, état global OK.

---

## 3. 🗓️ FUTURES MISES À JOUR / TESTS — À NE PAS OUBLIER

### Tests à faire dans 48-72h (dès que la sonde volume a assez de données)
- [ ] **Trancher le débat 02-06 vs volume glissant** : comparer la plage horaire
      actuelle à la métrique `volume_glissant_3h` de la sonde sur 2-3 jours.
      Si la corrélation est bonne (creux 02-06 = volume effondré) → on garde 02-06
      + gardien. Si les creux arrivent ailleurs (ex : 23h, 09h) → on bascule.
- [ ] **Valider la métrique volume_glissant** : le ratio au 1er run (8.0) est
      trompeur (pas encore d'historique) — vérifier qu'il se normalise ~1.0 au
      fil des runs, et calibrer le seuil d'alerte (−50 % est-il le bon ?).

### Amendements famille/Cortana — ÉTAT RÉEL
- [x] **Hybride spread** : `0.7×p30_24h + 0.3×p30_4h` **CODÉ ET TESTÉ 29/08 litté**
      (XRP/QAIT/RWAINC vérifiés sur données réelles) — signal3 expose `spread_seuil_mode`.
- [x] **Compteur d'essaim léger** (idée de fond de Cortana) : **EN OBSERVATION 48h**
      depuis le 29/08 litté (`veille_essaim_observation.py`, chaîne cockpit ESSAIM (OBS)).
      Après 48h : calibrer le seuil N et le bonus, puis décider du passage en prod.
- [ ] **Gardien dynamique de volume** (variante INFERX/Cortana r2) : garder 02-06
      mais basculer en « mode creux » si le volume panier s'effondre −80 % hors
      plage — **en attente des 48-72h de données de la sonde volume** pour calibrer.

### Rappels permanents (protocoles)
- [ ] **Croisement externe** : vérifier chaque jour `croisement_externe_etat.json`
      → « 0 fail prix » (règle des 2 sources avant toute décision importante).
- [ ] **Persistance 3 ticks** : un prix en écart devient bloquant seulement au 3ᵉ
      run — ne pas s'alarmer d'un pic isolé.
- [ ] **PathRegistry** : toute nouvelle plist doit passer par le wrapper heartbeat.
- [ ] **Nouvelles paires** : les ajouter au fur et à mesure des deepdives dans
      `paires_croisement.json` (jamais dans `exclues_prudence` sans deepdive).
- [ ] **Obsidian + GitHub** : archiver chaque document de décision (comme celui-ci).

---

## 4. 📁 FICHIERS LIÉS
- Sonde : `hulk-mexc/scripts/sonde_volume_panier.py` + `runs/volume_panier_*.json*`
- Plist : `Index_Maison/plists/com.ace777.sonde-volume-panier.plist`
- Débat complet : `OUTBOX_OBSIDIAN/VAL_CROISEE_CORTANA_AFFINAGE_N4_20260829.md`,
  `SYNTHESE_FAMILLE_vs_CORTANA_N4_20260829.md`, `VAL_CROISEE_ROUND2_CORTANA_20260829.md`
- Avis famille : `scripts/CONSULTATION_FAMILLE_VALIDER_CORTANA_N4/`
- Audit famille : `hulk-mexc/docs/AUDIT_FAMILLE_OEUVRES_20260829.md`
- Mon avis (Buffy) : session « et toi tu en pense quoi » — synthèse ci-dessus §1.
