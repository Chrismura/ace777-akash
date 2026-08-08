# Protocole — Début / fin de session

**Statut :** 🟢 scripts prêts · 🟡 **cadence à ancrer** (raté 31 juil. matin)  
**Pourquoi :** trop d’énergie brûlée à refaire hygiène / sync / « où on en est » à la main.  
**Valeur :** A3 (temps/RAM mentale) · pas de trading auto.

**Cousins :** [[AUTO_PROCESSUS]] · [[JOURNAL_COCKPIT]] · [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]] · [[REPRISE_APRES_COUPURE]] · [[CHOSES_A_FINIR_REVOIR]]

---

## Avis

Oui — **début et fin de session doivent être une commande**, pas un roman.  
Comme une checklist UAT légère : tu lances, ça range, ça dit OK/NOK, tu décides le GO trading.

| Automatiser | Ne jamais auto |
|-------------|----------------|
| Check machine / stérile / RAM | `GO_USINE` / Hulk |
| Thermo + mission feed + pastilles liens | Purge hard pendant vol |
| Journal + mémoire + OUTBOX prêt | Force-push Obsidian sans Terminal |
| Ouvrir cockpit (demain : app native) | Promouvoir test → réel |

---

## Début de session (cible script)

Ordre figé :

1. `etat_mac` (lecture)  
2. Hygiène RAM orphelins (si froid)  
3. `verif_sterilite --pre-run` si on prévoit un run  
4. `cockpit_hygiene_check` (+ pont si lecture UI)  
5. Lire [[PLAN_DE_VOL]] + [[CONSOLE_GENERALE]] (1 écran)  
6. Afficher : STERILE / PONT / ACE / NET  

**Commandes :**
```bash
bash ~/ace777-test-day1/Index_Maison/scripts/session_debut.sh          # auto VOL/FROID
bash ~/ace777-test-day1/Index_Maison/scripts/session_debut.sh --vol    # pendant run
bash ~/ace777-test-day1/Index_Maison/scripts/session_debut.sh --froid  # pré-GO
bash ~/ace777-test-day1/Index_Maison/scripts/session_debut.sh --open   # + cockpit app
```

---

## Fin de session

### Cas A — Tu dors, le prototype **reste** en vol (nuit / matin tôt)

1. **Ne pas** tuer ACE / Hulk (pas de `--stop-ace`, pas de purge NUAGE)  
2. Snapshot : journal + 1 ligne [[MEMOIRE_COLLAB]] + OUTBOX  
3. Sync Obsidian (`_sync_now.sh` dans **ton** Terminal)  
4. Noter clairement : « vol laissé tourner »

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/session_fin.sh
bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh
```

### Cas B — Stop explicite (GO humain « arrête »)

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/session_fin.sh --stop-ace
bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh
```

---

## Matin après nuit en vol

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/session_debut.sh --vol --open
```

Auto détecte aussi VOL si ACE/LIVE frais. **Pas** de purge stérile agressive en mode vol.

Rappel validation : [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]] (portes P0→P2) avant tout « réel ».

---

## Cockpit app native

```bash
# une fois : pip3 install --user pywebview
bash ~/ace777-test-day1/Index_Maison/scripts/open_cockpit_app.sh
```

Démarre le pont `:17777` si besoin · fenêtre **ACE777 COCKPIT** (pas Electron).  
Repli : `open …/cockpit/index.html` si pywebview absent.

Voir [[PLAN_DE_VOL]] · [[JOURNAL_COCKPIT]] C-00.
