# 🛠️ SPEC CODEUR — LIRE LE DERNIER RUN AU LIEU D'AGRÉGER (29/08/2026)

> Contexte de la découverte (Buffy) : lors de l'audit QAIT, l'outil d'analyse
> agrégeait les 18 CSV `PAPER_V1_*.csv` de runs successifs. Or chaque `--resume`
> copie l'ancien CSV dans le nouveau (`shutil.copy2`). Résultat : un même trade
> réel apparaissait 18 fois (même timestamp) → j'ai cru à un "bug de journalisation"
> (−49,91 $) alors que la perte réelle était −22,15 $.
>
> **Conclusion : ce n'est PAS un bug du moteur. C'est un trompe-l'œil de mon
> outil d'analyse qui lisait TOUS les CSV au lieu du dernier run.** Le chantier
> codeur ci-dessous corrige l'OUTIL, pas le moteur.

## Le problème exact

- Les CSV de trades (`runs/PAPER_V1_*.csv`) étant copiés à chaque `--resume`,
  **un seul run cohérent = le CSV le plus récent** (nom `PAPER_V1_<ts_lancement>.csv`,
  qui contient via resume tout l'historique).
- Tout script qui parse plusieurs de ces CSV **double/compte en trop** les trades.
- Il faut un helper qui ouvre **uniquement le dernier run** et dédoublonne par
  timestamp, pour que toute analyse PnL par paire soit fiable.

## Livrables demandés

1. **`hulk-mexc/scripts/trades_last_run.py` (NOUVEAU)** — small lib + CLI :
   - `recent_paper_csv(root) -> Path` : renvoie le CSV `PAPER_V1_*.csv` le plus
     récent dans `runs/` (tri par timestamp du nom, pas par mtime — les copies
     gardent le mtime d'origine).
   - `trades(df_path) -> list[dict]` : parse le CSV, garde chaque ligne, dédoublonne
     par `(ts, pair, action)` (garde la première occurrence).
   - `pnl_par_pair(lignes) -> dict[str, float]` : somme les SELL full (commision
     déduite) par paire ; sépare `SELL_PARTIAL` et `SELL` (full).
   - CLI : `python3 trades_last_run.py [--pair QAITUSDT]` → imprime le run analysé,
     le nb de lignes brutes vs dédupliquées, et le PnL par paire.
   - Robustesse : aucun crash si aucun CSV ; message clair.
   - **NE PAS toucher** au moteur `paper_diprip.py` ni aux scripts de divergence.

2. **`hulk-mexc/scripts/audit_pnl_reel.py` (NOUVEAU, optionnel si simple)** :
   - Utilise `trades_last_run` pour sortir un rapport PnL **réel par paire** (36j)
     → écrit `runs/AUDIT_PNL_REEL_<ts>.md`. C'est le rapport de référence pour
     éviter à l'avenir toute double lecture comme celle de QAIT (bug → −49,91 $
     au lieu de −22,15 $).

## Règles de code ACE777 (rappellant)
- Python 3.9+, **stdlib uniquement** (csv, pathlib, dataclasses) — pas d'import externe.
- Encodage UTF-8, docstring de rôle en tête.
- Écriture ATOMIQUE pour tout fichier (mkstemp + os.replace).
- Robuste (fichier manquant/corrompu → message, pas de trace panic).
- Idempotent, relançable sans effet de bord.

## Format de réponse exigé
- Pour chaque fichier : bloc ```python complet et fermé, précédé du chemin.
- Une seule section « NOTES » finale : choix faits + points d'attention
  (notamment : déduplication par (ts, pair, action) vs (ts, pair) — argumente).
- Réponds en français, factuel, code prêt à l'emploi.