#!/usr/bin/env bash
# Install UNE FOIS — automation mémoire / molettes / sessions.
# Ne touche PAS au trading. Lancer dans Terminal :
#   bash ~/ace777-test-day1/Index_Maison/scripts/install_memoire_auto.sh
set -euo pipefail
ROOT="/Users/christophe/ace777-test-day1"
WS="$ROOT/Index_Maison"
OB="$WS/OUTBOX_OBSIDIAN"
PY=/usr/bin/python3
BIN="$HOME/bin"

echo "=== INSTALL MÉMOIRE AUTO ==="
echo "ts: $(date -u +%Y-%m-%dT%H:%MZ)"
echo

# 1) Scripts exécutables
chmod +x \
  "$WS/scripts/memoire_log.py" \
  "$WS/scripts/molette_log.py" \
  "$WS/scripts/session_debut.sh" \
  "$WS/scripts/session_fin.sh" \
  "$WS/scripts/install_memoire_auto.sh" \
  "$OB/_sync_now.sh" 2>/dev/null || true
echo "OK chmod scripts"

# 2) Règles Cursor présentes
for r in vulgariser-par-defaut.mdc memoire-auto.mdc stacking-functions.mdc recherche-agora.mdc; do
  if [[ -f "$ROOT/.cursor/rules/$r" ]]; then
    echo "OK rule $r"
  else
    echo "WARN rule manquante: $r"
  fi
done

# 3) Smoke test scripts (PAS de ★ — zsh le prend pour une glob sort)
"$PY" "$WS/scripts/memoire_log.py" install "STAR" "memoire_auto" "install_memoire_auto.sh — smoke OK" | head -1
echo "OK memoire_log"

# 4) Miroir OUTBOX (canons)
mkdir -p "$OB" "$OB/Index_Maison"
for f in \
  MEMOIRE_COLLAB.md JOURNAL_MOLETTES_SETUP.md COUTUMES_AGORA.md AUTO_PROCESSUS.md \
  OSSATURE_INDEX.md PREFS_STACK.md INDEX_COMMANDES.md CHOSES_A_FINIR_REVOIR.md \
  PLAN_DE_VOL.md PHASE_EQUIPE_AGENTS.md PROTOCOLE_SESSION_DEBUT_FIN.md
do
  [[ -f "$WS/$f" ]] && cp -f "$WS/$f" "$OB/$f" && cp -f "$WS/$f" "$OB/Index_Maison/$f" 2>/dev/null || true
done
echo "OK OUTBOX miroir"

# 5) Binaires réels dans ~/bin (marchent SANS alias / SANS source .zshrc)
mkdir -p "$BIN"
for name in memoire ace777-memoire; do
  cat >"$BIN/$name" <<'EOF'
#!/bin/bash
exec /usr/bin/python3 /Users/christophe/ace777-test-day1/Index_Maison/scripts/memoire_log.py "$@"
EOF
  chmod +x "$BIN/$name"
done
for name in molette ace777-molette; do
  cat >"$BIN/$name" <<'EOF'
#!/bin/bash
exec /usr/bin/python3 /Users/christophe/ace777-test-day1/Index_Maison/scripts/molette_log.py "$@"
EOF
  chmod +x "$BIN/$name"
done
echo "OK ~/bin/memoire · molette · ace777-*"

ALIAS_FILE="$WS/scripts/ace777_aliases.sh"
cat >"$ALIAS_FILE" <<'EOF'
# ACE777 — source une fois dans ~/.zshrc :
#   source ~/ace777-test-day1/Index_Maison/scripts/ace777_aliases.sh
export PATH="$HOME/bin:$PATH"
# binaires déjà dans ~/bin ; alias = raccourci équivalent
alias memoire='python3 ~/ace777-test-day1/Index_Maison/scripts/memoire_log.py'
alias molette='python3 ~/ace777-test-day1/Index_Maison/scripts/molette_log.py'
alias session-debut='bash ~/ace777-test-day1/Index_Maison/scripts/session_debut.sh'
alias session-fin='bash ~/ace777-test-day1/Index_Maison/scripts/session_fin.sh'
alias sync-obsidian='bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh'
EOF
echo "OK $ALIAS_FILE"

# 6) PATH permanent (login shell Terminal.app) — avant .zshrc
ZPROFILE="$HOME/.zprofile"
PATH_LINE='export PATH="$HOME/bin:$PATH"'
if [[ -f "$ZPROFILE" ]] && grep -qF 'HOME/bin' "$ZPROFILE" 2>/dev/null; then
  echo "OK .zprofile PATH déjà"
else
  {
    echo ""
    echo "# ACE777 ~/bin (memoire / molette) $(date -u +%Y-%m-%d)"
    echo "$PATH_LINE"
  } >>"$ZPROFILE"
  echo "OK .zprofile += ~/bin"
fi

# 7) Brancher ~/.zshrc (aliases EN PREMIER — avant réveil qui peut planter)
ZSHRC="$HOME/.zshrc"
LINE='source ~/ace777-test-day1/Index_Maison/scripts/ace777_aliases.sh'
if [[ -f "$ZSHRC" ]] && grep -qF "ace777_aliases.sh" "$ZSHRC" 2>/dev/null; then
  echo "OK .zshrc déjà branché"
else
  {
    echo ""
    echo "# ACE777 mémoire auto ($(date -u +%Y-%m-%d))"
    echo "$LINE"
  } >>"$ZSHRC"
  echo "OK .zshrc += ace777_aliases"
fi

# 8) Journal soir : ligne mémoire après snapshot
JS="$WS/scripts/journal_soir_launchd.sh"
if [[ -f "$JS" ]] && ! grep -q memoire_log "$JS"; then
  if grep -q 'thermo_quotidien_free' "$JS"; then
    perl -i -pe 's|(thermo_quotidien_free\.py.*\n)|$1  /usr/bin/python3 "\$ROOT/Index_Maison/scripts/memoire_log.py" journal_soir "STAR" "journal" "snapshot soir auto" \|\| true\n|' "$JS" 2>/dev/null \
      || echo "WARN patch journal_soir manuel"
  fi
fi
if grep -q memoire_log "$JS" 2>/dev/null; then
  echo "OK journal_soir → memoire_log"
else
  echo "WARN journal_soir: vérifie memoire_log à la main si besoin"
fi

# 9) Smoke binaire (chemin absolu — pas besoin de PATH)
"$BIN/memoire" install "STAR" "bin" "wrapper ~/bin/memoire OK" | head -1
echo "OK smoke ~/bin/memoire"

echo
echo "=== INSTALL OK ==="
echo "Sync déjà fait de ton côté. Colle SEULEMENT ceci (sans étoile unicode) :"
echo
echo "  export PATH=\"\$HOME/bin:\$PATH\""
echo "  memoire Humain STAR test \"boucle automation OK\""
echo
echo "Ou chemin absolu (marche toujours) :"
echo "  ~/bin/memoire Humain STAR test \"boucle automation OK\""
echo
