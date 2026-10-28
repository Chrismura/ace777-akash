# 📌 POINT DE REPRISE — DERNIER (à lire en premier)

> **Pour la prochaine session (Buffy ou autre IA, 29/10/2026)** : lis CE fichier d'abord,
> puis **`REGISTRE_ECHECS_ET_ERREURS.md` §§26-39** (tout le 28/10 est là).
> 60 secondes. Pas plus. Le détail est dans les schémas, pas ici.
> **Règle d'entretien : ce fichier se réécrit EN FIN DE SESSION. Jamais d'écart > 24 h.**

---

## 🧭 LES 3 CARTES (stables)

| Fichier | Contenu |
|---|---|
| `ETAT_SYSTEME.md` | carte organique globale : cœur ACE + HULK + veilleuses + rythmes |
| `SCHEMA_ACE.md` / `hulk-mexc/SCHEMA_HULK.md` | ACE et HULK en détail |
| `REGISTRE_ECHECS_ET_ERREURS.md` §§26-39 | tout le 28/10 : holds, boucle RAISON, entrée, trailing, ré-entrée, TEL, métacognition |
| `REGLE_D_OR.md` R16-R24 | métacognition (28/10, 4 voix) + antériorités maison |

---

## 1. Ce qui s'est passé (28/10) — l'essentiel

**Argent :** 620 $ misés → ~872 $ (+67 $ vs tout-investi, +8,3 %). Hypothèses : `hulk-mexc/runs/HYPOTHESES.jsonl`.
**Moteur HULK :** vivant (`paper_diprip --resume`, state `PAPER_V1_20261028_212843_state.json`,
trades 366, 19 paires, TEL purgé partout). 3 restarts ce soir (dont 1 crash de ma faute, §32).
**Shadow actif (0 ordre)** : `REDEPLOY_CONFIRM_ON=1`, paires RWAINC/KITE/PYTH, sorties COOLING
uniquement, confirmation +0,5 % après 48 h, fenêtre 14 j. Règle §33 (48 h > 24 h, COOLING +50 $ vs IMPULSE +1 $).
**TEL :** retiré 05/10, purgé ce soir (reentry + notionals) — ne plus y toucher sauf GO.
**Règles :** R16-R24 écrites (hypothèse scellée, déflation +30 %/N ≤ 5, acteur/juge séparés,
désaccords + contrefactuel, dead-man 48 h, kill 7 j, chaos monkey, smoke test, veto froid).

## 2. État actuel (à vérifier en début de session)

```bash
ps aux | grep paper_diprip | grep -v grep        # 1 seul process, = lock runs/.paper_diprip.lock
tail -2 hulk-mexc/runs/PAPER_V1_*.csv             # journal vivant, 16 colonnes
ls -t hulk-mexc/runs/PAPER_V1_*_state.json | head -1  # dernier state + TEL absent (reentry, notionals)
grep -a -c Traceback hulk-mexc/runs/PAPER_WATCHDOG_STDOUT.log  # 2 connus (§32) — tout nouveau = enquête
grep -a "REDEPLOY_SHADOW" hulk-mexc/runs/PAPER_WATCHDOG_STDOUT.log | tail -5  # le shadow parle ?
```

## 3. Échéancier — QUOI vérifier et QUAND (ne plus oublier la moitié)

| Quand | Quoi | Où |
|---|---|---|
| **29/10 matin** | Moteur vivant + 0 traceback nouveau + state propre | commandes §2 |
| **29/10** | 1ers `REDEPLOY_SHADOW_ARMED/ACHAT/EXPIRE` ? | journal + stdout |
| **04/11 (J+7 shadow)** | Bilan 7 j du shadow : ACHAT vs EXPIRE, PnL contrefactuel | `chiffrage_attribution_reentree.py` à relancer |
| **11/11 (J+14)** | Fin fenêtre TTL : le 48 h tient en live ? Câbler ou tuer (kill-switch) | décision Christophe |
| **27/11 (J+30)** | Verdict contrefactuel DeepSeek (le juge gagne ou coûte ?) | ligne juge/acteur à brancher (§36-Q4) |
| **Chaque fin de session** | Réécrire CE fichier + resceler + § registre | R15/R5 |

## 4. Chantiers proposés (attente GO, par priorité)

1. **Ligne contrefactuelle** (DeepSeek Q4) : `juge_a_dit|acteur_a_fait|issue|contrefactuel` sans ordre — c'est la mesure qui manque le plus.
2. **Singe du chaos** : 5 % slippage + micro-coupures au fantôme (petit, 0 risque live).
3. **Cortana-méthode** : brancher la dimension méthode (spec §36) — jour, pas nuit.
4. **2e provider** : recouper P2/P3 (tout le tour était Gemini, §34).

## 5. Commandes clés

```bash
cd ~/ace777-test-day1/hulk-mexc && python3 scripts/paper_diprip.py --resume   # relance manuelle (le watchdog le fait seul)
grep -a "RETRAIT_PAIRE\|REDEPLOY_SHADOW\|Traceback" runs/PAPER_WATCHDOG_STDOUT.log | tail -10
python3 scripts/hypothese.py liste          # hypothèses ouvertes (R16)
python3 scripts/hypothese.py sceller "traitre..." "métrique" "+seuil" "abandon si..."
bash Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh  # pousse vers Obsidian
```
