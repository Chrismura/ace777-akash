# 🧬 ETAT_SYSTEME — carte organique ACE777 (mise à jour 16/08/2026 ~11:40 locale)

> **ACE777 est un organisme** : plusieurs organes qui battent à des rythmes différents, reliés
> par des fichiers-ponts. Cette page = la vue d'ensemble. Détails : `SCHEMA_ACE.md` (cœur),
> `hulk-mexc/SCHEMA_HULK.md` (2ᵉ organe). À relire en début de session.

```
                          ┌─────────────────────────────┐
                          │         OBSIDIAN            │  mémoire externe
                          │  (Documents/Obsidian_ACE777)│  + INDEX_COMMANDES
                          └──────────▲──────────────────┘
                                     │ sync (OUTBOX_OBSIDIAN)
        ┌──────────────┐   ┌─────────┴─────────┐   ┌──────────────┐
        │   COCKPIT    │◄──┤   CORTANA (voix)  │──►│   VEILLEUSE  │
        │ (http 17800) │   │  bridge 17777     │   │  synapses    │
        └──────▲───────┘   └─────────▲─────────┘   │ (registre    │
               │ boutons            │ ponts        │  md5)        │
        ┌──────┴───────┐   ┌─────────┴─────────┐   └──────┬───────┘
        │  HUB LLM     │   │  HULK (paper)     │   ┌──────┴───────┐
        │ (11435, 13   │   │  MEXC dip&rip     │   │  PRISE-IA    │
        │  providers)  │   │  PID 99387 +      │   │  (obs, hub   │
        │  + OLLAMA    │   │  veille 99573     │   │  cockpit)    │
        └──────▲───────┘   └─────────▲─────────┘   └──────────────┘
               │ llm_gate          │ SCHEMA_HULK.md
        ┌──────┴───────────────────┴───────────────┐
        │  ♥ ACE (LE CŒUR) — champion scellé       │
        │  BETA scout 200$ + ALPHA hunter 800$     │
        │  RUN ACTIF PID 27655 (02:00:00)          │
        │  duo_state.json = battement du cœur      │
        └──────────────────────────────────────────┘
```

## 1. ♥ Le cœur : ACE (voir SCHEMA_ACE.md)

- Champion : `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt` → md5 `8bce77b1…` (2 fixes du 16/08)
- **RUN ACTIF** : PID 27655 `launch_vortex_v2_collab_4h_binance.sh --duration 02:00:00`
  (lancé par Christophe après le re-scellage → teste last_loss + price_stasis)
- Battement : `runs/duo_state.json` (mis à jour à chaque cycle scout/hunter)
- BETA x5 / ALPHA x13 · Binance **testnet** · POLL 64ms

## 2. 🦾 HULK (2ᵉ organe, séparé volontairement)

- Paper MEXC dip&rip : PID 99387 (`paper_diprip.py`) + veille PID 99573 (`digest_watch --live`)
- Fix du jour : tier B ×0.25 · rip partiel 50% · re-entry max 1 · spread ≤100 bps
- Gardien : `com.ace777.hulk-watchdog` (120s) — fix AbandonProcessGroup fait (16/08)

## 3. 🧠 Le système nerveux (toujours en vie)

| Process | PID | Rôle |
|---|---|---|
| `llm_gate_hub_bridge.py` | 27447 | HUB LLM (11435) : consultations famille + llm_gate du champion |
| `cortana_cockpit_bridge.py` | 38709 | pont Cortana ↔ cockpit (17777) + boutons (ALARME, DÉCLARER MODIFS) |
| `cockpit_http_server.py` | 38714 | tableau de bord (17800) |
| `open_cockpit_app.py` | 52062 | app cockpit |
| OLLAMA (11439) | — | llm_gate du champion (qwen2.5-coder:1.5b) |

## 4. 🛡️ Les veilleuses (immunité)

| Veilleuse | Rythme | Surveille | Alerte si |
|---|---|---|---|
| `veilleuse_synapses` | 600s | md5 des fichiers stables (registre `REGISTRE_SYNAPSES.json`) | fichier modifié non déclaré → « INTRUSION » vocale |
| `superviseur-core` | 900s | hub, PULSE, process ACE/HULK | process mort, RAM |
| `superviseur-process` | 900s | superviseur.sh (boucle process) | process mort |

> ⚠️ **LEÇON 16/08** : `stop_ace777_hard.sh` a tué les process superviseur-core/superviseur-process
> (09:58 locale) et **les plists n'étaient pas chargés** → trou de surveillance jusqu'à 11:29
> (masqué par l'autopilote qui rafraîchit SOUS_L_OEIL). **Fixé : rechargés** (`launchctl load`).
> ➡️ Après un stop_hard : vérifier `launchctl list | grep superviseur` — recharger si absent.

> ⚠️ **LEÇON 16/08 (2ᵉ)** : le superviseur disait « ACE OFF » alors que le run tournait — le
> pattern de détection (`GO_USINE_NUAGE|ace777_launch_v85|launch_vide_froid`) ne couvrait pas
> le lanceur actuel `launch_vortex`. **Fixé 11:36** : `launch_vortex` ajouté aux patterns de
> `superviseur_core.sh`, `pulse_sous_loeil.sh`, `checkup_garage.sh`, `session_debut/fin.sh`.
> ➡️ Si SOUS_L_OEIL dit OFF alors que ACE tourne : vérifier que le pattern couvre le lanceur.
> Les superviseurs (parent auto-heal 10:04/11:04, core PID 51238, process) sont **VIVANTS**.
| `cortana.urgent` | 10s | `A_Mon_Attention/` | nouveau fichier → son `temp_alerte.mp3` |
| `hub-cockpit-feed` | 30s | hub → cockpit | — |
| `state-generator` | 120s | STATE.md | — |
| `checkup_garage` | manuel | fantômes (pgrep élargi) | process résiduel |

**Acquitter une alarme** : bouton ⛔ ALARME (cockpit) ou `touch Index_Maison/STOP_ALERTE_<id>`.
**Déclarer une modif volontaire** : bouton ✓ DÉCLARER MODIFS (met le registre à jour + backup).

## 5. ⏱️ Les rythmes (agents launchd actifs — 30+)

| Rythme | Agents |
|---|---|
| 10s | cortana.urgent |
| 30s | hub-cockpit-feed |
| 120s | hulk-watchdog · state-generator |
| 300s | journal-intention |
| 600s | veilleuse · cpfp (10 min) |
| 900s | autopilote · superviseur-core |
| 1800s | backup-check |
| 3600s | cortana.horaire · superviseur |
| 3-6h | gitpush · gitpush-vault · routeur-auto |
| horaire/quotidien | brief-matin, brief-offres, journal-soir, discipline-quotidienne, analyste-cadence… |

## 6. 🔗 Les connexions (fichiers-ponts)

| Pont | Relie | Écrit par |
|---|---|---|
| `runs/duo_state.json` | BETA ↔ ALPHA (revenge) | champion |
| `runs/STATE.md` | système → cockpit | state-generator |
| `runs/DIGEST_LATEST.md` | HULK veille → Qwen/Cortana | digest_watch |
| `strategie/REGISTRE_SYNAPSES.json` | veilleuse ↔ fichiers surveillés | veilleuse |
| `strategie/cortana_pilot.json` | Cortana → HULK (ADVISORY) | cortana_contract |
| `A_Mon_Attention/` | Christophe/Buffy → Cortana | nous (notes datées) |
| `Index_Maison/OUTBOX_OBSIDIAN/` | workspace → Obsidian | nous (copies) |
| `~/Documents/Obsidian_ACE777/` | mémoire humaine | sync |
| GitHub | sauvegarde | gitpush (3h) |

## 7. 📍 État actuel (16/08 ~11:20)

| Organe | Statut |
|---|---|
| ACE run de test | 🟢 ACTIF (PID 27655, fin ~11:19Z) — à analyser après fin |
| HULK paper | 🟢 ACTIF (PID 99387, fix tier/rip appliqué) |
| HULK veille | 🟢 ACTIF (PID 99573) |
| Hub LLM / cockpit / Cortana | 🟢 ACTIF |
| HULK fix ghost (AbandonProcessGroup) | ✅ fait |
| ACE fixes (last_loss + price_stasis) | ✅ scellés `8bce77b1` |
| Chantiers ouverts | 16/08 : ACE last_loss ✅ · ACE price_stasis ✅ · HULK tier/rip ✅ · ghost ✅ |

## 8. 🧭 Pour reprendre une session (checklist 60s)

```bash
# 1. Qu'est-ce qui tourne ?
ps -e -o pid,etime,args | grep -E "ace777-test-day1" | grep -v grep
# 2. Le cœur bat-il ?
cat runs/duo_state.json          # ACE (si run actif)
tail -3 hulk-mexc/runs/PAPER_V1_2026*.csv   # HULK
# 3. Y a-t-il des alarmes ?
ls Index_Maison/A_Mon_Attention/ | tail -3
# 4. Les schémas à jour ?
cat SCHEMA_ACE.md | head -30 && cat hulk-mexc/SCHEMA_HULK.md | head -30
# 5. Ce fichier (ETAT_SYSTEME.md) = la carte → mettre à jour à chaque fin de session
```

## 9. Règles de vie (pour ne pas casser l'organisme)

1. **Ne jamais modifier le champion sans le protocole complet** (spec → famille → tests → re-scellage → réfs → autorisation)
2. **Toute modif volontaire d'un fichier surveillé** → bouton ✓ DÉCLARER MODIFS (sinon la veilleuse sonne)
3. **3 copies** de chaque doc : workspace + OUTBOX_OBSIDIAN + Obsidian
4. **STOP files** (STOP/STOP_ALPHA/STOP_BETA/STOP_PAPER) : posés = arrêt volontaire, retirés = relance OK
5. **La famille décide** des changements de stratégie (GO/NO-GO), jamais en force
