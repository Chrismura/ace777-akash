# BRIEF AGENT EXTERNE (Gemini/Antigravity) — À LIRE AVANT TOUTE ÉCRITURE
*2026-09-17 · rédigé par Buffy pour le propriétaire · lecture locale, zéro quota d'historique*

## 1. La maison en 5 lignes
Prototype de trading BTC **PAPIER** (zéro ordre réel, zéro clé API) du propriétaire
Christophe, dans `~/ace777-test-day1`. Moteurs, replays, journaux et verdicts sont
**scellés par commits git** — chaque résultat doit être reproductible depuis la source
(données Binance réelles), jamais depuis les logs d'un moteur.

## 2. Les règles NON NÉGOCIABLES (le propriétaire les a arrachées à nos propres erreurs)
1. **Spec figée AVANT le run** — commitée avant d'avoir vu un résultat. Une variante = un nouveau GO explicite.
2. **Verdict pré-enregistré, pas de 3e verdict** — le chiffre décide, jamais l'envie ni la politesse.
3. **Aucun chiffre non sourcé** — toute performance annoncée doit pointer un fichier de résultat daté + commit. (Un « +133.02 $ PROUVÉ » sans source a été attrapé et rejeté ce soir même.)
4. **Rejouer contre la source, pas contre le log** — Binance direct, pas les journaux du moteur.
5. **Preuves préservées** — JAMAIS modifier un fichier scellé ; on crée une copie variante en Git.
6. **Rien en arrière-plan sans GO explicite** — logs visibles, jamais `/dev/null`.
7. **Toute écriture dans le dépôt passe par un commit signé de ton identité** — le propriétaire doit toujours savoir QUI a écrit QUOI.

## 3. Les erreurs déjà commises (pour ne pas les refaire) — journal : `engle/JOURNAL_ERREURS.md`
- **E25** : veto zone morte 0,0002 rendant le moteur muet par construction (incohérent avec la porte voisine funding > moy30) — personne ne l'a vu pendant 5 jours.
- **E26/E27** : deux replays confondus (hunter ≠ confirmation) ; le replay du setup réel donnait 0 trades 23 min AVANT le lancement live — résultat jamais lu.
- **E28** : 5 jours de silence présentés comme « correct ». Dénonciation sabotage consignée par le propriétaire.
- **E29-E31** : 5 replays du setup V2 → 5 ÉCHECS (0 trade, ou 1 trade perdant, ou 12 trades −203,87 $ en 4H). Le goulot est la conjonction d'entrée, pas le veto.
- **E32** : Duo Originel (Scout 200 $ SL 16 bps + Hunter Revenge 800 $ sens opposé) sur signaux V2 4H : **ÉCHEC, net −64,19 $** (WR 16,3 %). Verdict scellé. Deux bugs d'implémentation de Buffy attrapés par contrôle de cohérence interne avant consignation.
- **Leçon E32** : un résultat « trop beau » (WR 1.0, gains garantis) = bug jusqu'à preuve du contraire. Toujours vérifier la cohérence interne des chiffres.

## 4. L'état actuel (ce qui tourne, ce qui est scellé)
- **En cours** : `v2_duo_live.py` (révisé Buffy, conforme E32, SHA 3deb9bf7…) — moteur PAPIER jusqu'à 07h00, logs dans `Index_Maison/thermo/`. Interface : `bash Index_Maison/scripts/v2conf_live.sh`.
- **Spec Duo scellée** : Scout 200 $ SL 16 bps trailing 1,0σ/0,4σ · Hunter 800 $ SENS OPPOSÉ, hard stop 32 bps, durée max 240 s · entrée 2/3 confirmations None-safe (funding>avg30, flux ledger ≥ +5 BTC, chute 4H ≤ −0,5 %) · veto négatif seul (funding ≤ 0) · frais 16 bps AR.
- **Règles originelles du Duo** : `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt` (SHA 7d1ed5f6, copie scellée `champion_sealed_20260901T205022Z/`).

## 5. Protocole de collaboration (décision du propriétaire)
- Le propriétaire souhaite la **collaboration**, pas la compétition, entre agents.
- Tu peux : **lire** tout le dépôt, **proposer** des correctifs/variantes en respectant les règles §2.
- Tu ne dois pas : modifier un fichier scellé, lancer un processus de fond sans GO, annoncer un résultat sans fichier source + commit.
- Toute proposition d'écriture : décris-la au propriétaire, attends son GO, puis committe avec ton identité.
- Si tu modifies un script que Buffy a scellé, ta modification sera auditée à la source avant exécution — comme la tienne l'a été ce soir.

## 6. Le seul juge
Le propriétaire, Christophe. Son argent, ses règles, ses GO. La vigilance humaine est
l'organe qui a attrapé ce que tous les agents ont raté — elle prime sur tout.
