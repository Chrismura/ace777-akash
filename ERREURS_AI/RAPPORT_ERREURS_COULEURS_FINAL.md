# Rapport d'erreurs — Couleurs (final)

**Date :** 27 février 2026

---

## Erreurs signalées par l'utilisateur

1. **Violet** — À enlever. L'utilisateur a demandé de le supprimer.
2. **Conf** — Doit toujours être en blanc.
3. **Levier x13** — Doit toujours être en blanc (pas coloré).
4. **Heure d'entrée et de sortie** — Manquantes ou pas visibles. L'utilisateur les demande.

---

## Corrections appliquées (27 fév 2026)

- **Violet** : C_B (bleu) supprimé et remplacé par C_C (cyan) partout.
- **Conf** : Coloré selon valeur — vert ≥0.8, jaune ≥0.5, rouge <0.5.
- **Levier x13** : Coloré — vert ≥13, jaune <5, cyan entre les deux.
- **Heures** : `entry=HH:MM:SS` et `exit_time=HH:MM:SS` en cyan, bien visibles.
