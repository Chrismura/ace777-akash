# Vérification générale ACE777

**Date :** 27 février 2026

---

## 1. Lancement (launch_250_4h.sh)

| Élément | Valeur | OK |
|---------|--------|-----|
| BETA | 250 USDT | ✓ |
| ALPHA | 250 USDT | ✓ |
| Durée | 4h (04:00:00) | ✓ |
| CYCLE_COLORS | TRUE | ✓ |
| LLM_GATE_ENABLED | TRUE | ✓ |
| LLM_MODEL | qwen2.5-coder:1.5b | ✓ |
| Chaîne | → fortress → impact → genesis | ✓ |

---

## 2. Fortress (v8_6)

| Élément | Valeur | OK |
|---------|--------|-----|
| MOM | 0.96 | ✓ |
| WALL_DROP | 6.5% | ✓ |
| GLOBAL_STOP | -45 | ✓ |
| BUY_USDT_BETA | hérité (250) | ✓ |
| BUY_USDT_ALPHA | hérité (250) | ✓ |
| LLM gate | TRUE | ✓ |
| Echo LLM | affiché au démarrage | ✓ |

---

## 3. Impact (v8_5)

| Élément | Valeur | OK |
|---------|--------|-----|
| BETA | x3, SHORT, STOP_BETA | ✓ |
| ALPHA | x5→13, LONG, STOP_ALPHA, BURST | ✓ |
| V8 Resonance, Tension | ON | ✓ |
| Lagrange, PhaseShift | ON | ✓ |
| master.pid, alpha.pid, beta.pid | créés | ✓ |

---

## 4. Genesis — Ligne ORDER

| Élément | Couleur | OK |
|---------|---------|-----|
| Heure (entry_hr) | Cyan | ✓ |
| x13 (levier) | Vert/Jaune/Cyan selon niveau | ✓ |
| #cycle | Bleu | ✓ |
| side pnl | Vert/Rouge/Jaune selon PNL | ✓ |
| tension (chiffre) | Rouge/Vert/Jaune/Cyan selon niveau | ✓ |
| hold (chiffre) | Cyan/Jaune/Vert selon durée | ✓ |
| Après \| (bps, pct, exit, conf, close) | Blanc (C_N) | ✓ |
| Prix de sortie | exit=$exit_price | ✓ |
| Conf | conf=$radar_conf (blanc) | ✓ |
| Violet (C_M) | Supprimé (remplacé par C_G) | ✓ |

---

## 5. Arrêt (stop_ace777.sh)

| Étape | Action | OK |
|-------|--------|-----|
| 1 | touch STOP | ✓ |
| 2 | kill groupe master | ✓ |
| 3 | kill alpha, beta | ✓ |
| 4 | pkill genesis, launch, tail, radar, ruby | ✓ |
| 5 | Boucle PIDs restants | ✓ |

**Commande :** `cd /Users/christophe/ace777-test-day1 && ./stop_ace777.sh`

---

## 6. Fichiers clés

| Fichier | Présent | OK |
|---------|---------|-----|
| launch_250_4h.sh | oui | ✓ |
| launch_test_master_base_v8_6_fortress.sh | oui | ✓ |
| launch_test_master_base_v8_5_impact.sh | oui | ✓ |
| genesis_manifest.txt | oui | ✓ |
| stop_ace777.sh | oui | ✓ |

---

## Résumé

Configuration cohérente. Lancement : `./launch_250_4h.sh`. Arrêt : `./stop_ace777.sh` (nouveau terminal).
