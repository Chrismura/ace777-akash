#!/usr/bin/env bash
# git_precommit_large_files.sh — refuse tout commit de fichier > 50 Mo
# (leçon : croisement_contexte.jsonl à 286 Mo a bloqué le push GitHub 3 jours,
#  GitHub refuse tout fichier > 100 Mo — on bloque à 50 Mo, marge 2x).
#
# Usage :
#   - Hook pre-commit (appelé par git automatiquement) :
#       ln -sf ~/ace777-test-day1/Index_Maison/scripts/git_precommit_large_files.sh .git/hooks/pre-commit
#     ou copie : cp ... .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
#   - Test manuel : SEUIL_MO=50 bash git_precommit_large_files.sh
#
# Règle : si un fichier staged dépasse le seuil → commit REFUSÉ (rc=1),
# le développeur retire le fichier du suivi (git rm --cached) et le met dans
# .gitignore — les données vivantes ne vont JAMAIS dans git.
set -u

SEUIL_MO="${SEUIL_MO:-50}"
SEUIL_OCTETS=$((SEUIL_MO * 1024 * 1024))

# Fichiers staged (ajoutés/modifiés/renommés — pas les suppressions)
# Boucle ligne par ligne : les noms du projet n'ont jamais de \n (sûr ici).
# IMPORTANT : < <(…) (process substitution) — PAS un pipe, sinon le while tourne
# dans un sous-shell et le `exit 1` ne remonte jamais à git (bug v1 : le commit
# passait malgré le refus affiché).
refuse=0
while IFS= read -r f; do
  [ -z "$f" ] && continue
  # Taille du blob STAGÉ (pas du fichier de travail — ce qui partirait réellement)
  size="$(git cat-file -s ":$f" 2>/dev/null)"
  [ -z "$size" ] && continue
  if [ "$size" -gt "$SEUIL_OCTETS" ]; then
    echo "❌ PRE-COMMIT REFUSÉ : '$f' fait ${size} octets (> ${SEUIL_MO} Mo)" >&2
    echo "   GitHub refuse tout fichier > 100 Mo. Action : git rm --cached '$f' + ajout à .gitignore." >&2
    echo "   (les données vivantes/JSONL restent sur disque, hors git — règle famille)" >&2
    refuse=1
  fi
done < <(git diff --cached --name-only --diff-filter=ACMRT)

exit "$refuse"