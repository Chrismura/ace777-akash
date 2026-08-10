# BRIEF AUDIT FAMILLE E2+E3 (loi 1quinquies) — 10/08

CONTEXTE : Systeme ACE777 - Mac 8 Go, hub local 11435 (9 providers gratuits),
29 services launchd. Setup 3 étages validé (SPEC V2.1 GO unanime famille).
E1 (system_state_generator.py) déjà audité : GO (GEMINI) + GO AVEC RESERVES
(JUGE, 3 mineures corrigées). Maintenant AUDIT FAMILLE DIFF de E2 + E3.

ÉTAPE E2 (couche système en continu) :
- com.ace777.state-generator.plist : StartInterval 120 (state.json toutes les
  2 min — réserve P2 latence). CHARGÉ dans launchd.
- com.ace777.backup-check.plist : StartInterval 1800 (présence toutes les
  30 min — réserve P5 I/O légères). CHARGÉ dans launchd.
- backup_light_check.sh : présence (métadonnées) chaque run + tailles du -sk
  ESPACÉES 6 h (réserve JUGE E1 : pas de I/O lourdes). Écrit
  backup_presence.json + backup_sizes.json bruts.
- system_state_generator.py v2.1 fusionne ces 2 bruts dans state.json (champ
  backup_light) — réserve P5 respectée.

ÉTAPE E3 (réversibilité + compatibilité — CODE PRODUIT PAR LE HUB) :
- README_MIROFISH.md dans DESACTIVES_2026-08-10/ : procédure exacte de
  ré-activation de Mirofish (réserve P3) — décision option (c) documentée,
  membre d'équipe en pause budgétaire.
- _check_rust_version() dans cortana_cockpit_bridge.py (réserve P4) : lit
  crypto-voice-assistant-core/VERSION, warning si != attendu, error si manquant,
  NON FATALE (try/except).

PREUVES RÉELLES (pas de mémoire) :
- tests unitaires E1 : 7/7 OK
- hub /health : {"status": "ok", "providers": 9} (non-régression)
- cockpit-pont (le service qui lance le bridge) : vivant
- state.json : généré automatiquement par launchd (mtime frais)
- _check_rust_version testée : non-fatale (VERSION absent -> error propre)

=== PLIST state-generator ===
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>com.ace777.state-generator</string>
	<key>ProgramArguments</key>
	<array>
		<string>/usr/bin/python3</string>
		<string>/Users/christophe/ace777-test-day1/Index_Maison/scripts/system_state_generator.py</string>
	</array>
	<key>StartInterval</key>
	<integer>120</integer>
	<key>RunAtLoad</key>
	<true/>
	<key>StandardOutPath</key>
	<string>/tmp/state-generator.log</string>
	<key>StandardErrorPath</key>
	<string>/tmp/state-generator.err.log</string>
	<key>LowPriorityIO</key>
	<true/>
	<key>ProcessType</key>
	<string>Background</string>
</dict>
</plist>


=== PLIST backup-check ===
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>com.ace777.backup-check</string>
	<key>ProgramArguments</key>
	<array>
		<string>/bin/bash</string>
		<string>/Users/christophe/ace777-test-day1/Index_Maison/scripts/backup_light_check.sh</string>
	</array>
	<key>StartInterval</key>
	<integer>1800</integer>
	<key>RunAtLoad</key>
	<true/>
	<key>StandardOutPath</key>
	<string>/tmp/backup-check.log</string>
	<key>StandardErrorPath</key>
	<string>/tmp/backup-check.err.log</string>
	<key>LowPriorityIO</key>
	<true/>
	<key>ProcessType</key>
	<string>Background</string>
</dict>
</plist>


=== backup_light_check.sh ===
#!/bin/bash
# backup_light_check.sh — contrôle backup LÉGER (réserve P5 + JUGE E1).
# - Présence des 5 dossiers hors zone : métadonnées uniquement (test -d), rapide.
# - Taille (du -sk) : ESPACÉE toutes les 6 h (fichier cache de timestamp).
# - Écrit DEUX fichiers bruts (loi du brut), fusionnés par le générateur :
#     system/backup_presence.json   (présence, à chaque run)
#     system/backup_sizes.json      (tailles, espacé 6 h)
# Usage : lancé par launchd (plist com.ace777.backup-check, StartInterval 1800).
set -u

BASE="${ACE777_BASE:-$HOME/ace777-test-day1/Index_Maison}"
SYSTEM_DIR="$BASE/system"
PRESENCE_FILE="$SYSTEM_DIR/backup_presence.json"
SIZE_FILE="$SYSTEM_DIR/backup_sizes.json"
CACHE_TS="$SYSTEM_DIR/.backup_size_ts"
SIX_HOURS=21600

mkdir -p "$SYSTEM_DIR"

DIRS=(
  "$HOME/mirofis"
  "$HOME/crypto-voice-assistant-core"
  "$HOME/ACE777_ARCHIVES_BRUTES_DONNEES"
  "$HOME/Assistant_Vocal_HORS_VAULT"
  "$HOME/Obsidian_BACKUPS_HORS_VAULT"
)
now=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# --- 1. Présence (à CHAQUE run — 30 min via plist) : métadonnées uniquement ---
{
  echo "{"
  echo "  \"generated_at\": \"$now\","
  echo "  \"present\": {"
  first=1
  for d in "${DIRS[@]}"; do
    name=$(basename "$d")
    if [ -d "$d" ]; then v="true"; else v="false"; fi
    if [ "$first" = "1" ]; then first=0; else echo "    ,"; fi
    printf '    "%s": %s' "$name" "$v"
  done
  echo ""
  echo "  }"
  echo "}"
} > "$PRESENCE_FILE"

# --- 2. Taille (ESPACÉE 6 h — jamais bloquant) ---
need_size=0
if [ ! -f "$CACHE_TS" ]; then
  need_size=1
else
  ts=$(cat "$CACHE_TS" 2>/dev/null || echo 0)
  now_epoch=$(date +%s)
  if [ $(( now_epoch - ts )) -ge $SIX_HOURS ]; then
    need_size=1
  fi
fi

if [ "$need_size" = "1" ]; then
  {
    echo "{"
    echo "  \"generated_at\": \"$now\","
    echo "  \"sizes_ko\": {"
    first=1
    for d in "${DIRS[@]}"; do
      name=$(basename "$d")
      if [ -d "$d" ]; then
        s=$(du -sk "$d" 2>/dev/null | awk '{print $1}')
        [ -z "$s" ] && s=0
      else
        s=0
      fi
      if [ "$first" = "1" ]; then first=0; else echo "    ,"; fi
      printf '    "%s": %s' "$name" "$s"
    done
    echo ""
    echo "  }"
    echo "}"
  } > "$SIZE_FILE"
  date +%s > "$CACHE_TS"
fi

exit 0


=== state.json (brut, extrait backup_light) ===

      "com.ace777.gitpush-vault",
      "com.ace777.graph-cerveau",
      "com.ace777.heartbeat",
      "com.ace777.journal-soir",
      "com.ace777.observatoire",
      "com.ace777.propose-ameliorations",
      "com.ace777.pulse-sous-loeil",
      "com.ace777.qwen-btc",
      "com.ace777.qwen-elabore",
      "com.ace777.rotation-logs",
      "com.ace777.superviseur",
      "com.ace777.surveillance-quotas",
      "com.ace777.veille-hub",
      "com.ace777.verif-setup",
      "com.ace777.vigie"
    ]
  },
  "hub": {
    "status": "ok",
    "providers": 9
  },
  "ram_raw": "The system has 8589934592 (524288 pages with a page size of 16384).",
  "hors_zone": {
    "mirofis": {
      "present": true
    },
    "crypto_voice_core": {
      "present": true
    },
    "archives_brutes": {
      "present": true
    },
    "vocal_hors_vault": {
      "present": true
    },
    "obsidian_backups": {
      "present": true
    }
  },
  "backup_light": {
    "presence": {
      "mirofis": true,
      "crypto-voice-assistant-core": true,
      "ACE777_ARCHIVES_BRUTES_DONNEES": true,
      "Assistant_Vocal_HORS_VAULT": true,
      "Obsidian_BACKUPS_HORS_VAULT": true
    },
    "sizes_ko": {
      "mirofis": 1068252,
      "crypto-voice-assistant-core": 4041128,
      "ACE777_ARCHIVES_BRUTES_DONNEES": 96136,
      "Assistant_Vocal_HORS_VAULT": 697372,
      "Obsidian_BACKUPS_HORS_VAULT": 14936872
    },
    "presence_at": "2026-08-10T08:22:48Z",
    "sizes_at": "2026-08-10T08:21:14Z"
  }
}


=== _check_rust_version (dans cortana_cockpit_bridge.py) ===
def _check_rust_version() -> None:
    """E3 (SPEC V2.1, reserve P4) : verifie la version du coeur Rust
    (hors perimetre setup, backup uniquement). Warning si version != attendue,
    error si VERSION manquant. NON FATAL : ne plante jamais le script."""
    version_file = RUST_CORE_DIR / "VERSION"
    try:
        if not version_file.exists():
            print(f"[ERROR] Fichier VERSION manquant : {version_file}",
                  file=sys.stderr)
            return
        with open(version_file, "r", encoding="utf-8") as f:
            rust_version = f.read().strip()
        if rust_version != EXPECTED_RUST_VERSION:
            print(f"[WARNING] Version Rust inattendue : {rust_version} "
                  f"(attendu : {EXPECTED_RUST_VERSION})", file=sys.stderr)
        else:
            print(f"[INFO] Version Rust OK : {rust_version}")
    except Exception as e:
        print(f"[ERROR] Erreur verification Rust : {e}", file=sys.stderr)


def _net_link() -> dict:
    """Ping public Binance futures — internet trading path."""
    import urllib.request

    url = "https://fapi.binance.com/fapi/v1/ping"
    t0 = __import__("time").time()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ace777-cockpit-link/1"})
        with urllib.request.urlopen(req, timeout=2.0) as r:
            r.read(32)
        ms = int((__import__("time").time() - t0) * 1000)
        if ms < 400:
            return {"state": "OK", "label": "OK", "ms": ms}
        if ms < 1200:
            return {"state": "SLOW", "label": "SLOW", "ms": ms}
        return {"state": "SLOW", "l

=== README_MIROFISH.md (extrait) ===
# 🐟 Mirofish — Mise en pause budgétaire (10/08/2026)

## Décision
- **Date** : 10 août 2026
- **Statut** : Membre de l'équipe (simulation sociale multi-agents, recherche-grade)
- **Motif** : Pause budgétaire — tournait à vide pendant 14 heures (09/08 10:00 → 10/08 00:20, zéro requête)
- **Décision famille** : Option (c) — désactivé + sorti de la liste surveillée (règle `skip_check` dans le superviseur) — validée GEMINI + JUGE (GO unanime SPEC V2.1)
- **Code** : `~/mirofis/` (1 Go, backend Python 35 110 fichiers + frontend) conservé en backup uniquement (backup 3 étages 21 Go + GitHub privé `ace777-hub-backup`)

## Données sauvegardées
- **Emplacement** : `~/ace777-test-day1/Index_Maison/MIROFISH_DONNEES_2026-08-10/`
- **Taille** : 728 Ko
- **Contenu** : rapport de simulation BTC/Fed complet (scénario Fed -75bp, 4 agents, volatilité en hausse + 4 risques), états des agents

## Procédure de ré-activation (réversible — décision famille requise)

> Mirofish est un membre de l'équipe, pas un bot trading. Sa ré-activation
> se décide COLLECTIVEMENT (famille + Christophe), jamais seul.

### Étape 1 — Restaurer les plists
```bash
cp ~/Library/LaunchAgents/DESACTIVES_2026-08-10/com.ace777.mirofish*.plist ~/Library/LaunchAgents/
```

### Étape 2 — Retirer la règle skip_check
- Fichier superviseur : `~/ace777-test-day1/Index_Maison/scripts/superviseur_auto.py` (ou le superviseur unique `com.ace777.superviseur-unique` à terme)
- Rechercher la section `skip_check` ou `mirofish`
- Supprime

QUESTIONS À LA FAMILLE (audit diff E2+E3) :
1. Les 2 plists (120 s / 1800 s) respectent-ils les réserves P2 (latence) et
   P5 (I/O légères) ? Y a-t-il un risque pour le Mac 8 Go ?
2. backup_light_check.sh : l'espacement 6 h des tailles du -sk est-il
   correctement implémenté et sûr ?
3. _check_rust_version : le code produit par le hub est-il correct, non-fatal,
   conforme à la réserve P4 ?
4. README_MIROFISH.md : la procédure de ré-activation est-elle complète et
   conforme à la décision famille (option c) ?
5. Verdict final E2+E3 : GO / GO AVEC RESERVES / NON (1 phrase + réserves).

