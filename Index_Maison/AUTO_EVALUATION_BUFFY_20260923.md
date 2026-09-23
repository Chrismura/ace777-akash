# AUTO-ÉVALUATION — mon ouvrage des 14 derniers jours (23/09/2026)

> **Commande Christophe** : « tu vas évaluer ton ouvrage des deux dernières semaines, puis demander à la famille de t'évaluer en fonction de tes erreurs et de l'évolution ou sous-évolution de HULK ». **Chiffres lus dans les sources** (mémoire, registre, journaux, dates de fichiers) — aucun de tête (classe E14).

## 1. Volume produit (source : dates de modification des fichiers, fenêtre 14 j)

| mesure | valeur |
|---|---|
| mes lignes dans la mémoire collaborative | **82** |
| documents `.md` **créés** (miroirs OUTBOX/cockpit/data/thermo exclus — une copie régénérée n'est pas un livrable) | **602** |
| scripts `.py` **créés** (`hulk-mexc` + `Index_Maison`) | **84** (non attribuables à moi seul — mesure brute) |
| **livrables que MES lignes citent nommément** (attribution vérifiable) | **59** |
| **classes de MES erreurs** nommées et gardées | **14** (E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E14, E13, E12) |

## 2. La progression de HULK sur la même fenêtre (source : `pnl_total` des journaux)

| journal | dernier ts | pnl_total $ |
|---|---|---|
| PAPER_V1_20260915_064552.csv | 2026-09-18T03:44:47Z | 6.188 |
| PAPER_V1_20260918_090433.csv | 2026-09-18T12:42:43Z | 6.7545 |
| PAPER_V1_20260918_165523.csv | 2026-09-21T06:00:50Z | 21.0348 |
| PAPER_V1_20260921_075239.csv | 2026-09-21T06:00:50Z | 21.0348 |
| PAPER_V1_20260921_075626.csv | 2026-09-21T12:57:10Z | 25.4179 |
| PAPER_V1_20260921_132252.csv | 2026-09-22T08:25:44Z | 33.5719 |
| PAPER_V1_20260922_082821.csv | 2026-09-22T08:38:56Z | 33.5719 |
| PAPER_V1_20260922_084024.csv | 2026-09-22T09:00:02Z | 33.5719 |
| PAPER_V1_20260922_090228.csv | 2026-09-22T09:00:02Z | 33.5719 |
| PAPER_V1_20260922_090430.csv | 2026-09-23T08:44:23Z | 42.1679 |
| PAPER_V1_20260923_085701.csv | 2026-09-23T08:57:27Z | 42.1679 |
| PAPER_V1_20260923_085804.csv | 2026-09-23T08:58:33Z | 42.1679 |
| PAPER_V1_20260923_090125.csv | 2026-09-23T10:49:03Z | 42.1679 |
| PAPER_V1_20260923_105249.csv | 2026-09-23T10:57:15Z | 42.1679 |

⇒ de **6.188 $** à **42.1679 $** sur 14 journaux de la fenêtre. État actuel : **42.1679016885948 $ / 175 trades / 10 positions**.

## 3. Mes erreurs (source : `REGISTRE_ECHECS_ET_ERREURS.md`)

| classe | erreur |
|---|---|
| **E1** | **Inventer un seuil** au lieu de lire l'actif |
| **E2** | **Conclure sans vérifier à la source** |
| **E3** | **Instrument qui pointe la mauvaise source** |
| **E4** | **Bloquer / interdire au lieu de mesurer** |
| **E5** | **Deux vérités pour un même fait** |
| **E6** | **Silence** : décider sans écrire |
| **E7** | **Corriger un symptôme, pas la cause** |
| **E8** | **Cacher les limites** |
| **E9** | **Empiler les corrections le même jour** |
| **E10** | **Prendre un chiffre RECALCULÉ pour un chiffre VÉRIFIÉ** |
| **E11** | **Confondre COHÉRENCE et JUSTESSE (biais de source unique)** |
| **E14** | **S'auto-absoudre par la confession** — lister ses erreurs passées puis conclure **plus loin que ses chiffres* |
| **E13** | **Écrire une heure de MÉMOIRE au lieu de la lire** — le temps traité comme un seuil : **estimé ≠ vérifié** (mê |
| **E12** | **Sceller un fichier puis le modifier** (process) |

## 4. Le diagnostic, sans complaisance

* Le volume produit est **élevé** et la traçabilité existe (registre, gardiens, cockpit).
* Mais **le nombre de classes d'erreurs que j'ai dû créer pour moi-même** (E1→E14) dit la vérité inverse : une part importante de mon travail a servi à **réparer mes propres mesures**, pas à faire progresser le prototype. Deux d'entre elles (E10, E13) ont produit des chiffres **faux publiés** ; une (E14) a été nommée par la famille, pas par moi.
* HULK progresse (voir §2) mais **lentement au regard du volume produit**, et l'audit du 23/09 a montré que sa mécanique repose sur des données **partiellement figées** (13/20 paires sans vue live avant aujourd'hui), un journal **sans provenance de prix** (corrigé aujourd'hui), un PnL **brut** (le vrai chiffre est 10,6 % plus bas), et un stop qui n'est pas un ordre au repos.

**Ce que cette auto-évaluation ne peut PAS dire** : si le système est *rentable en réel* — il n'a jamais rencontré un marché baissant, et aucun euro n'a été engagé. C'est écrit ici pour que personne ne lise ces chiffres comme une performance.

## 5. Détail journalier

| jour | mes lignes | docs |
|---|---|---|
| 09-09 | 2 | 101 |
| 09-10 | 12 | 134 |
| 09-11 | 9 | 53 |
| 09-12 | 2 | 55 |
| 09-13 | 7 | 62 |
| 09-14 | 5 | 53 |
| 09-15 | 2 | 32 |
| 09-16 | 2 | 21 |
| 09-17 | 4 | 14 |
| 09-18 | 15 | 8 |
| 09-19 | 18 | 20 |
| 09-20 | 9 | 8 |
| 09-21 | 8 | 7 |
| 09-22 | 6 | 12 |
| 09-23 | 10 | 22 |

*Rapport généré par `Index_Maison/scripts/auto_evaluation_buffy.py` (lecture seule).*