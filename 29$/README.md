# 29$ — Point de départ ACE777

Setup **IDENTIQUE session 204206** : moteur **37fca367**, GEMINI **BETA x3**, ALPHA **x13 fixe**, VERIF OK.

## Contenu

```
29$/
├── README.md                 ← ce fichier
├── REDEMARRER.sh             ← script principal (vérif / lancer)
├── CHECKSUMS.txt             ← empreintes genesis
└── historique/
    ├── genesis/              ← 3 moteurs + actif
    ├── rapports_20260710/    ← 204206 (+29$), 193940, 163716, 083706
    ├── rapports_20260712/    ← session #42 ratée, dernier stop
    ├── scripts/              ← snapshot lanceurs + verif
    ├── conversation/         ← transcript JSONL complet + résumé MD
    ├── SESSIONS_20260710_DEDUP.txt
    └── RESTORE_CLEAN_20260710.log
```

## Faits MD5 (ne pas mélanger)

| Moteur | MD5 | Barrière | PHI | Run associé |
|--------|-----|----------|-----|-------------|
| **Champion +29$** | `37fca367` | OUI | NON | 204206 vendredi soir |
| Matin PHI | `67a12f85` | NON | OUI | ~+5,69 $ 12/07 |
| Bonnet erroné | `9fe9f105` | NON | NON | Session #42 → perte / ALPHA dormante |

## Redémarrer depuis ici

### Vérification seule (recommandé d'abord)

```bash
cd /Users/christophe/ace777-test-day1
./LANCER_IDENTIQUE_204206.sh
```

Attendu : **`=== VERIF OK — setup identique 204206 prêt ===`**

### Lancer le run (toi seul)

```bash
./LANCER_IDENTIQUE_204206.sh lancer
```

Ou manuellement :

```bash
cd /Users/christophe/ace777-test-day1
./stop_ace777_hard.sh                    # si doute
cp 29$/historique/genesis/genesis_manifest.txt.SAUVE_avant_champion_restore genesis_manifest.txt
rm -f STOP STOP_ALPHA STOP_BETA
unset ALPHA_RAMP_MODE
LAUNCH_V85_SCRIPT=./launch_test_master_base_v8_5_impact_GEMINI_TEST.sh \
  ./launch_vortex_v2_collab_4h_binance.sh
```

### Boot attendu (~15 s)

```
=== V8.5 OVERRIDE === ./launch_test_master_base_v8_5_impact_GEMINI_TEST.sh
GEMINI_TEST ramp=gemini (x13 fixe dès cycle 1)
Leverage ramp ON: start=13 end=13
BETA Symbol=BTCUSDT Leverage=3
ALPHA Symbol=BTCUSDT Leverage=13
```

### Arrêt

```bash
./stop_ace777_hard.sh
```

## Chaîne historique 10/07 (soir → +29$)

| Rapport | PnL | Rôle |
|---------|-----|------|
| 163716 | -0,33 $ | Premier de la chaîne soir |
| 193940 | +13,23 $ | Premier boot x13 identique (même profil) |
| **204206** | **+29,41 $** | Session connue |

Cumul journée dédupliqué : ~**84,66 USDT** (voir `historique/SESSIONS_20260710_DEDUP.txt`).

## Conversation (LES INFOS SONT LÀ)

| Fichier | Contenu | Taille |
|---------|---------|--------|
| `historique/conversation/HISTORIQUE_CHAT_RUNS_A_MAINTENANT.txt` | **Depuis juste avant « historique des run » → maintenant** | ~200 Ko |
| `historique/conversation/HISTORIQUE_CHAT_COMPLET.md` | Toute la conversation en Markdown lisible | ~9 Mo |
| `historique/conversation/HISTORIQUE_CHAT_COMPLET.txt` | Même chose en texte brut (grep) | ~9 Mo |
| `historique/conversation/HISTORIQUE_CHAT_29USD_DERNIERE_SESSION.md` | Filtré 29$ / MD5 / champion / genesis | ~500 Ko |
| `historique/conversation/transcript_complet.jsonl` | Source brute Cursor (JSONL) | ~12 Mo |
| `historique/conversation/RESUME_CONVERSATION.md` | 35 derniers échanges (court) | ~36 Ko |

Transcript ID Cursor : `ed12efcb-1aef-4d0e-aac4-90354d843fdd`

Ouvre en priorité : **`29$/historique/conversation/HISTORIQUE_CHAT_COMPLET.md`**
