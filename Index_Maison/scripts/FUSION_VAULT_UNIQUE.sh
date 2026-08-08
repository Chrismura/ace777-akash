#!/bin/bash
# Fusion vault unique — rien ne se perd. Lancer dans Terminal.app.
set -euo pipefail
MAIN="/Users/christophe/Documents/Obsidian_ACE777"
NESTED="$MAIN/Projet_2_Assistant_Vocal"
TARGET="$MAIN/Assistant_Vocal"
TS=$(date -u +%Y%m%dT%H%MZ)
BAK="$MAIN/_backup_vault_merge_$TS"

echo "=== Fusion vault unique $TS ==="
mkdir -p "$BAK"

if [[ -d "$NESTED/.obsidian" ]]; then
  cp -R "$NESTED/.obsidian" "$BAK/Projet_2_dot_obsidian"
  rm -rf "$NESTED/.obsidian"
  echo "OK 2e vault désactivé (.obsidian → backup)"
fi

if [[ -d "$NESTED" ]]; then
  if [[ ! -e "$TARGET" ]]; then
    mv "$NESTED" "$TARGET"
    echo "OK Projet_2 → Assistant_Vocal (tout le contenu gardé)"
  else
    mkdir -p "$TARGET/_from_Projet_2_$TS"
    shopt -s dotglob nullglob
    for item in "$NESTED"/* "$NESTED"/.[!.]* "$NESTED"/..?*; do
      [[ -e "$item" ]] || continue
      base=$(basename "$item")
      [[ "$base" == "." || "$base" == ".." ]] && continue
      [[ "$base" == ".obsidian" ]] && continue
      mv "$item" "$TARGET/_from_Projet_2_$TS/" 2>/dev/null || true
    done
    rmdir "$NESTED" 2>/dev/null || mv "$NESTED" "$BAK/Projet_2_reste_$TS"
    echo "OK merge dans Assistant_Vocal existant"
  fi
else
  echo "INFO Projet_2 déjà absent — OK"
  mkdir -p "$TARGET"
fi

cat > "$TARGET/00_LIRE_MOI.md" << MD
# Assistant Vocal (ex Projet_2)

Fait partie du **vault unique** \`Obsidian_ACE777\`.
- Agora : [[AGORA]]
- Swarm : [[Swarm_Bus/00_LIRE_MOI]]
- Mémoire : [[Swarm_Bus/09_MEMOIRE_COLLAB]]

Fusion : $TS — ancien \`.obsidian\` sauvegardé dans \`$BAK\`.
Ne pas rouvrir ce dossier comme vault séparé.
MD

echo "=== VERIFY ==="
ls -la "$MAIN/AGORA.md" 2>&1
ls -la "$MAIN/Swarm_Bus/09_MEMOIRE_COLLAB.md" 2>&1
ls -la "$TARGET" 2>&1 | head -20
if [[ -d "$TARGET/.obsidian" ]]; then echo "FAIL encore .obsidian"; exit 2; else echo "OK un seul vault (.obsidian absent dans Assistant_Vocal)"; fi
if [[ -d "$NESTED" ]]; then echo "WARN Projet_2 existe encore"; else echo "OK plus de Projet_2 comme vault"; fi
echo "DONE — rouvre Obsidian → coffre Obsidian_ACE777"
