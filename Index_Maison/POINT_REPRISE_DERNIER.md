# 📌 POINT DE REPRISE — DERNIER (à lire en premier)

> **Pour la prochaine session (Buffy ou autre IA)** : lis CE fichier d'abord, puis
> **`ETAT_SYSTEME.md`** (la carte organique complète : organes, connexions, rythmes).
> 60 secondes. Pas plus. Le détail est dans les schémas, pas ici.

---

## 🧭 LES 3 CARTES (à tenir à jour)

| Fichier | Contenu |
|---|---|
| `ETAT_SYSTEME.md` (racine, copies OUTBOX+Obsidian) | **carte organique globale** : cœur ACE + HULK + veilleuses + rythmes + connexions |
| `SCHEMA_ACE.md` (racine) | ACE en détail : duo BETA/ALPHA, champion, réfs md5, fixes du jour |
| `hulk-mexc/SCHEMA_HULK.md` | HULK en détail : tier/classe, flux, config, commandes |
| **`architecture/` (4 tableaux HTML)** — `carte.html` CARTE · `index.html` VUE · `tech.html` TECH · `apprentissage.html` CYCLE | **boussole visuelle d'arrivée** : la flottille + les connexions colorées · `open ~/ace777-test-day1/Index_Maison/architecture/carte.html` |

---

## 1. Ce qui s'est passé (16/08) — la journée

**ACE (le cœur) :**
- Analyse des runs 13→16/08 : le run de nuit avait **0 fill `hunter_revenge_1.5x`** (vs 24-52 avant)
  → cause : le FIX-HEARTBEAT du 15/08 bornait le revenge à 20s puis `stale_state` → 0 revenge.
- **FIX-LAST-LOSS** (09:13) : TTL revenge 120s sur `last_loss_ts` (champ nouveau) — re-scellé `3d760592`.
- **FIX-PRICE-STASIS** (09:56) : garde-fou prix figé 0.5 bps/30s (8/10 fills flat du run matin)
  — re-scellé **`8bce77b1`** (md5 ACTUEL). Réfs md5 à jour partout (10 fichiers + REGISTRE_SYNAPSES).
- ⚠️ Run de test **ACTIF** (PID 27655, `GO_VORTEX_V2.sh 02:00:00`) → teste les 2 fixes.

**HULK (2ᵉ organe) :**
- Perte −7.02$ en 4 stops (13→16/08) → cause : double distinction TIER (liquidité) vs CLASSE (stratégie) mélangées.
- **FIX TIER/RIP** (famille 4/4 GO) : tier B ×0.25, `pick_pairs` ne contourne plus le filtre (EDEL exclue),
  **RIP implémenté** (vente partielle 50% au 1er rebond), re-entry max 1 + cooldown 4h, spread ≤100 bps.
- **Fix ghost** : `AbandonProcessGroup=true` (le paper mourait en boucle via launchd).
- Paper ACTIF (PID 99387) + veille ACTIVE (PID 99573).

**Infra :**
- Boutons cockpit ajoutés : ⛔ ALARME + ✓ DÉCLARER MODIFS (bridge).
- Alarmes veilleuse acquittées (re-scellage déclaré au registre).

## 2. État actuel (à vérifier en début de session)

```bash
ps -e -o pid,etime,args | grep -E "ace777-test-day1" | grep -v grep   # ce qui tourne
cat runs/duo_state.json                                                # cœur ACE
tail -3 hulk-mexc/runs/PAPER_V1_2026*.csv                              # HULK
ls Index_Maison/A_Mon_Attention/ | tail -3                             # alertes
```

## 3. Ce qui reste à faire (backlog)

1. **Analyser la fin du run ACE** (2 fixes) : %revenge 30-60% · `price_stasis skips` > 0 · fills flat < 20% · PnL > +1
2. **Analyser les ~10 premiers trades HULK** : raisons `rip_*` présentes · pas de stop > −7% · PnL ≥ 0
3. Réactiver STORM_HUNTER K2v2 (anti no_trigger, 0 arm depuis le 13/08) — en option
4. Kelly HULK en actif si win_rate ≥ 50% sur ≥ 20 trades (ombre actuellement)

## 4. Commandes clés

```bash
# ACE test
cd ~/ace777-test-day1 && ./GO_VORTEX_V2.sh 02:00:00
# ACE arrêt
./stop_ace777_hard.sh && rm -f STOP STOP_ALPHA STOP_BETA   # retirer STOP avant relance
# HULK paper
cd hulk-mexc && rm -f STOP_PAPER STOP_DIGEST && python3 scripts/paper_diprip.py
# Sync Obsidian
bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh
```

---

*Historique (avant 16/08) : 15/08 = FIX-HEARTBEAT (remplacé par LAST-LOSS le 16/08) + 2 classes HULK +
contrat Cortana + kill-switch veille · 13/08 = position orpheline réparée, champion restauré `98c80b5c`.*
