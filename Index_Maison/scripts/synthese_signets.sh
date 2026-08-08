#!/usr/bin/env bash
# ============================================================
# SYNTHESE SIGNETS X - v4 FINALE (plus de patch a coller)
# - lots de 5 : la Reine respire
# - PAS de fusion par l'IA : le script assemble le brief
#   lui-meme (comptages calcules par grep, tous les lots ecrits)
# - verification structurelle : chaque numero 1..N present
# - liens t.co resolus -> README GitHub lus + resumes en francais
# - reprise automatique si ca casse (relance, il continue)
# Respecte : 0 API payante · Mac froid · 1 place/info
# ============================================================

# ---------- CONFIG ----------
VAULT="$HOME/Documents/Obsidian_ACE777"
SIGNETS_DIR="$VAULT/Signets_X"
OUT_FILE="$VAULT/Evaluations/BRIEF_SIGNETS_X.md"
LOTS_DIR="$HOME/.signets_lots_v4"
MODEL="qwen2.5:3b"
OLLAMA_URL="http://localhost:11434"
BATCH=5
GITHUB=1
MAX_GITHUB=8
QUI="Humain+Cursor"
# -----------------------------

if [ "${1:-}" = "--clean" ]; then
  rm -f "$LOTS_DIR"/lot_*.md "$LOTS_DIR"/gh_*.md 2>/dev/null
  echo "[i] lots nettoyes (--clean)"
fi

mkdir -p "$LOTS_DIR"
TS=$(date -u +%Y-%m-%dT%H%MZ)

echo "== Pre-vol =="
pgrep -lf 'GO_USINE|paper_diprip' >/dev/null 2>&1 && {
  echo "[X] ACE ou Hulk tourne : Mac pas froid. Relance apres le vol."
  exit 1
}
curl -s --max-time 5 "$OLLAMA_URL/api/tags" >/dev/null 2>&1 || {
  echo "[X] Ollama ne repond pas. Lance Ollama, puis relance."
  exit 1
}
curl -s --max-time 5 "$OLLAMA_URL/api/tags" | grep -q "\"$MODEL\"" || {
  echo "[!] Modele '$MODEL' absent. Verifie 'ollama list' et change MODEL en haut."
  exit 1
}

FILES=()
for f in "$SIGNETS_DIR"/Bookmark_*.md; do [ -f "$f" ] && FILES+=("$f"); done
TOTAL=${#FILES[@]}
[ "$TOTAL" -eq 0 ] && { echo "[X] Aucun Bookmark_*.md dans $SIGNETS_DIR"; exit 1; }
echo "[OK] $TOTAL signets - modele : $MODEL - lots de $BATCH"

ask_reine() {
  local prompt="$1"
  local payload resp text
  payload=$(python3 -c 'import json,sys; print(json.dumps({"model":sys.argv[1],"messages":[{"role":"user","content":sys.argv[2]}],"stream":False}))' "$MODEL" "$prompt")
  for attempt in 1 2 3; do
    resp=$(curl -s --max-time 600 "$OLLAMA_URL/api/chat" -d "$payload")
    if [ -n "$resp" ]; then
      text=$(printf '%s' "$resp" | python3 -c 'import json,sys
try:
    d=json.load(sys.stdin); print(d.get("message",{}).get("content",""))
except Exception:
    print("")')
      if [ -n "$text" ]; then printf '%s' "$text"; return 0; fi
    fi
    echo "   (retentative $attempt...)" >&2
    sleep 8
  done
  echo "" >&2
  return 1
}

echo ""
echo "== Phase 1 : liens t.co -> vraies URLs (GitHub) =="
GH_URLS=()
if [ "$GITHUB" = "1" ]; then
  GH_URLS+=($(grep -hoE 'https?://github\.com/[A-Za-z0-9._/-]+' "${FILES[@]}" 2>/dev/null | sed 's/[).,;]*$//' | sort -u))
  TCO=$(grep -hoE 'https://t\.co/[A-Za-z0-9]+' "${FILES[@]}" 2>/dev/null | sort -u | head -60)
  for u in $TCO; do
    real=$(curl -s -o /dev/null -I -L --max-time 8 -w '%{url_effective}' "$u" 2>/dev/null)
    [ -z "$real" ] && real=$(curl -s -o /dev/null -L --max-time 8 --max-filesize 2000000 -w '%{url_effective}' "$u" 2>/dev/null)
    case "$real" in
      https://github.com/*|http://github.com/*) GH_URLS+=("$real");;
    esac
  done
  GH_URLS=($(printf '%s\n' "${GH_URLS[@]}" | sort -u | head -"$MAX_GITHUB"))
  echo "   ${#GH_URLS[@]} lien(s) GitHub trouves (max $MAX_GITHUB)"
fi

echo ""
echo "== Phase 2 : README GitHub (contenu, pas juste le lien) =="
if [ "$GITHUB" = "1" ] && [ ${#GH_URLS[@]} -gt 0 ]; then
  : > "$LOTS_DIR/gh_readmes_raw.md"
  for url in "${GH_URLS[@]}"; do
    repo=$(printf '%s' "$url" | sed -E 's#https?://github\.com/([^/]+/[^/]+).*#\1#')
    echo "### $repo" >> "$LOTS_DIR/gh_readmes_raw.md"
    echo "Lien : $url" >> "$LOTS_DIR/gh_readmes_raw.md"
    readme=$(curl -s --max-time 15 -H "Accept: application/vnd.github.raw" "https://api.github.com/repos/$repo/readme" 2>/dev/null | head -c 1200)
    if [ -n "$readme" ]; then
      echo "$readme" >> "$LOTS_DIR/gh_readmes_raw.md"
    else
      echo "(README introuvable ou limite API atteinte)" >> "$LOTS_DIR/gh_readmes_raw.md"
    fi
    echo "" >> "$LOTS_DIR/gh_readmes_raw.md"
  done
  echo "   [OK] ${#GH_URLS[@]} readme(s) telecharge(s)"
else
  echo "   (pas de lien GitHub resolu - on continue sans)"
fi

echo ""
echo "== Phase 3 : lots de $BATCH =="
LOT=0
idx=0
OK=0
SUSPECT=""
while [ "$idx" -lt "$TOTAL" ]; do
  LOT=$((LOT+1))
  M=0
  content=""
  for ((j=0; j<BATCH && idx<TOTAL; j++, idx++)); do
    M=$((M+1))
    content="$content$M. Fichier: $(basename "${FILES[$idx]}")
$(cat "${FILES[$idx]}")

"
  done
  INCOMPLETE=""
  if [ -f "$LOTS_DIR/lot_$LOT.md" ]; then
    for n in $(seq 1 "$M"); do
      grep -qE "^[[:space:]]*[*_-]*[[:space:]]*${n}[.)]" "$LOTS_DIR/lot_$LOT.md" || INCOMPLETE="$INCOMPLETE $n"
    done
  else
    INCOMPLETE="absent"
  fi
  if [ -z "$INCOMPLETE" ]; then
    echo "   Lot $LOT : deja complet (reprise) - controle OK"
    OK=$((OK+1))
    continue
  fi
  [ "$INCOMPLETE" != "absent" ] && { echo "   Lot $LOT : incomplet (manque :$INCOMPLETE) - refait"; rm -f "$LOTS_DIR/lot_$LOT.md"; }
  echo "   Lot $LOT : $M signets -> la Reine..."
    if text=$(ask_reine "LOT de $M signets X numerotes 1 a $M. Pour CHAQUE signet, ecris UNE seule ligne, au format :
NUM. @auteur - idee centrale (1 ligne, en francais) - VERDICT
VERDICT = GARDÉ (utile maintenant pour le prototype) / PISTE (a explorer) / WATCH (a surveiller) / BRUIT (inutile ou hors sujet).
Exemple : 3. @user - agent IA gratuit pour appels API -> GARDÉ
Rien d'autre : pas d'introduction, pas de conclusion, pas de texte entre les lignes.

$content"); then
      printf '%s\n' "$text" > "$LOTS_DIR/lot_$LOT.md"
    else
      echo "   [X] La Reine n'a pas repondu (lot $LOT). Ferme Brave/cockpit pour la RAM, puis relance : les lots faits seront repris."
      exit 1
    fi
  MISSING=""
  for n in $(seq 1 "$M"); do
    grep -qE "^[[:space:]]*[*_-]*[[:space:]]*${n}[.)]" "$LOTS_DIR/lot_$LOT.md" || MISSING="$MISSING $n"
  done
  if [ -z "$MISSING" ]; then
    echo "   [OK] couverture $M/$M verifiee par le script"
    OK=$((OK+1))
  else
    echo "   [!] couverture incomplete : postes manquants :$MISSING"
    SUSPECT="$SUSPECT lot$LOT($MISSING)"
  fi
done
LOTS_FAITS=$(ls "$LOTS_DIR"/lot_*.md 2>/dev/null | wc -l | tr -d ' ')

echo ""
echo "== Phase 4 : resume des README en francais =="
if [ -s "$LOTS_DIR/gh_readmes_raw.md" ]; then
  if text2=$(ask_reine "Voici des extraits de README GitHub. Pour CHAQUE '### nom', ecris UNE ligne : nom - ce que ca fait (1 phrase, en francais, simple). Reponds uniquement par ces lignes.

$(cat "$LOTS_DIR/gh_readmes_raw.md" | head -c 6000)"); then
    printf '%s\n' "$text2" > "$LOTS_DIR/gh_readmes.md"
  else
    cp "$LOTS_DIR/gh_readmes_raw.md" "$LOTS_DIR/gh_readmes.md"
    echo "   (resume impossible - readmes bruts inclus)"
  fi
  echo "   [OK] readmes resumes"
fi

echo ""
echo "== Phase 5 : ameliorations pour le prototype =="
AMELIO=""
GARDES=$(cat "$LOTS_DIR"/lot_*.md 2>/dev/null | grep -E "GARD[ÉE]|PISTE" | head -40)
if [ -n "$GARDES" ]; then
  if text3=$(ask_reine "Voici des signets jugees utiles (GARDÉ/PISTE) pour un prototype de trading crypto multi-agents (ACE777 testnet, Hulk paper, Cortana voix, Qwen local, 8 Go RAM, 0 API payante). Propose 8 ameliorations concretes, chacune en UNE ligne, format :
- idee (source : @auteur)
Reponds uniquement par ces 8 lignes.

$GARDES"); then
    AMELIO="$text3"
  fi
fi

echo ""
echo "== Phase 6 : assemblage du brief (par le script, PAS par l'IA) =="
G=$(cat "$LOTS_DIR"/lot_*.md 2>/dev/null | grep -oiE "GARD[ÉE]" | wc -l | tr -d ' ')
P=$(cat "$LOTS_DIR"/lot_*.md 2>/dev/null | grep -oiE "PISTE" | wc -l | tr -d ' ')
W=$(cat "$LOTS_DIR"/lot_*.md 2>/dev/null | grep -oiE "WATCH" | wc -l | tr -d ' ')
B=$(cat "$LOTS_DIR"/lot_*.md 2>/dev/null | grep -oiE "BRUIT" | wc -l | tr -d ' ')
if [ -z "$SUSPECT" ]; then STATUS="COMPLET (couverture $OK/$OK lots)"; else STATUS="PARTIEL - manques :$SUSPECT"; fi
{
  echo "---"
  echo "date: $TS"
  echo "agent: $MODEL (local, gratuit, Ollama)"
  echo "type: veille_sectorielle_globale"
  echo "source: Signets_X ($TOTAL signets · $LOTS_FAITS lots de $BATCH)"
  echo "verification: comptages et couverture calcules par le script (pas par l'IA)"
  echo "statut: $STATUS"
  echo "---"
  echo ""
  echo "# Brief Signets X — synthese"
  echo ""
  echo "## Comptage des verdicts (calcule par le script)"
  echo ""
  echo "| Verdict | Nombre |"
  echo "|---|---|"
  echo "| GARDÉ (a garder) | $G |"
  echo "| PISTE (a explorer) | $P |"
  echo "| WATCH (a surveiller) | $W |"
  echo "| BRUIT (a jeter) | $B |"
  echo ""
  echo "## 1. Verdicts par lot"
  echo ""
  for ((l=1; l<=LOTS_FAITS; l++)); do
    [ -f "$LOTS_DIR/lot_$l.md" ] || continue
    echo "### Lot $l"
    echo ""
    cat "$LOTS_DIR/lot_$l.md"
    echo ""
  done
  echo "## 2. Liens GitHub (contenu lu)"
  echo ""
  if [ -s "$LOTS_DIR/gh_readmes.md" ]; then
    cat "$LOTS_DIR/gh_readmes.md"
  else
    echo "Aucun lien GitHub resolu (les liens t.co ne menaient pas vers GitHub, ou pas de lien)."
  fi
  echo ""
  echo "## 3. Ameliorations a faire (pistes TABLEAU_VIVANT)"
  echo ""
  if [ -n "$AMELIO" ]; then
    printf '%s\n' "$AMELIO"
  else
    echo "_Aucune proposee (modele muet) - on peut les tirer des GARDÉ a la main._"
  fi
  echo ""
} > "$OUT_FILE"
echo "[OK] Brief ecrit : $OUT_FILE"
echo "   couverture lots : $OK/$LOTS_FAITS OK$SUSPECT"
echo ""

MEMOIRE_LOG="$HOME/ace777-test-day1/Index_Maison/scripts/memoire_log.py"
if [ -f "$MEMOIRE_LOG" ]; then
  python3 "$MEMOIRE_LOG" "$QUI" "★" "Evaluations/BRIEF_SIGNETS_X" "v4 : $TOTAL signets ($LOTS_FAITS lots, couverture $OK/$LOTS_FAITS, GitHub lu) -> brief ecrit"
  echo "[OK] memoire collab loggee"
else
  echo "memoire_log.py introuvable - colle cette ligne toi-meme :"
  echo "python3 ~/ace777-test-day1/Index_Maison/scripts/memoire_log.py \"$QUI\" \"★\" \"Evaluations/BRIEF_SIGNETS_X\" \"v4 : $TOTAL signets -> brief ecrit\""
fi

mkdir -p "$HOME/ace777-test-day1/Index_Maison/scripts" 2>/dev/null
cp "$0" "$HOME/ace777-test-day1/Index_Maison/scripts/synthese_signets.sh" 2>/dev/null && echo "[OK] copie rangee : Index_Maison/scripts/synthese_signets.sh"

echo ""
echo "Ligne pour le TABLEAU_VIVANT :"
echo "| GARDÉ | Brief narratif auto | $TOTAL signets synthetises (v4, couverture $OK/$LOTS_FAITS, GitHub lu) | Evaluations/BRIEF_SIGNETS_X.md |"
echo ""
echo "Fait. Va lire $OUT_FILE dans Obsidian."
