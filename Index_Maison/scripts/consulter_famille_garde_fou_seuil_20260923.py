#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONSULTATION FAMILLE — 23/09/2026 — « comment empêcher la classe d'erreur ? »
=============================================================================
Demande Christophe : « consultation avec la famille (voyons si on peut éviter que tu
continues de faire des erreurs) — prompt spécifique et contexte améliorent les réponses. »

Le brief est VOLONTAIREMENT brutal et précis : chiffres exacts, la faute nommée, ce qui a
été construit, et une mission de CONTREDICTION (pas d'approbation). La famille donne un
AVIS ; rien n'est appliqué automatiquement.
"""
import json
import os
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_GARDE_FOU_SEUIL_20260923")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (Buffy, superviseur ACE777/HULK, 23/09/2026) — LA FAUTE DE MÉTHODE ET LE
GARDE-FOU QUI DOIT LA RENDRE IMPOSSIBLE

=== 1. LE SYSTÈME, factuel ===
Moteur HULK : trader PAPER (aucun euro réel) sur MEXC, 20 paires, un seul fichier
(`paper_diprip.py`, ~3 100 lignes), relancé en continu par launchd + watchdog. En vol :
pnl +42,17 $ sur une base de référence de 150 $ (~21 jours), 175 trades, 9 positions.
Les décisions d'entrée sortent d'une fonction `score_pair()` qui écrit chaque cycle :
prix, régime (IMPULSE / IMPULSE_WAIT / WATCH / QUIET / COOLING), cadence, m6, dd6.
La règle d'entrée en régime IMPULSE est :
    dip   = max(dip_pct_du_profil ; DIP_CADENCE_MULT × cadence)          [DIP_CADENCE_MULT = 0,50]
    need  = max(dip ; IMPULSE_PULLBACK_MIN_PCT=5 ; IMPULSE_PULLBACK_FRAC=0,30 × m6)
    la porte du régime s'ouvre à 0,85 × need   (sinon le régime reste IMPULSE_WAIT)
La « cadence » est la médiane des ranges de blocs de 24 h sur une fenêtre 15 j glissante
(score_pair, l.535-543) — pour une paire violente elle vaut 50 %, donc le repli exigé
vaut 25 %.

=== 2. MA FAUTE (classe F) ===
J'ai écrit, publié et RÉPÉTÉ pendant trois jours que le repli exigé valait
`max(dip 4,2 % ; 5 % ; 0,30 × m6)` = 5 à 12,75 % sur RIZE. C'était FAUX d'un facteur ~4 :
le moteur appliquait 21,70 %. Il me manquait LE terme dominant (`0,50 × cadence`).
Diagnostic : je n'ai pas recalculé un seuil, je l'ai RECOPIÉ DE MÉMOIRE dans mes instruments
au lieu de le confronter à ce que le moteur ÉCRIT. Le chiffre faux a servi à publier
« RIZE est structurellement inattaquable » puis à chiffrer un levier d'entrée.
La leçon que j'en tire : « un chiffre recalculé n'est pas un chiffre vérifié ».

=== 3. CE QUE J'AI CONSTRUIT (le garde-fou, en vol depuis 3 h) ===
`verif_seuil_moteur.py`, appelé toutes les 3 h par le push automatique, état affiché dans
le cockpit (un verdict non affiché n'existe pas). Quatre mécanismes :
  a) INVARIANT SUR DONNÉES RÉELLES : chaque ligne où le moteur écrit ses propres chiffres
     (`ATTENTE:IMPULSE_WAIT dd6=2.50 seuil=21.70 manque=19.20pt m6=12.5` + sa cadence,
     colonne 9 du journal) est RECALCULÉE depuis la config et le profil, puis comparée.
     Résultat à l'instant : 6/6 conformes.
  b) DÉTERMINANCE (règle maison R15) : il nomme LE terme qui fixe le seuil par paire
     (RIZE -> cadence ; TEL/ZBCN -> plancher). 0,85 × max(...) est recalculé par instrument.
  c) DÉTECTEUR STATIQUE : tout script qui recalcule un seuil d'entrée SANS le terme
     cadence est signalé (motif textuel + filtre « ligne de calcul » pour éviter les faux
     positifs, ex. un fichier qui se contente de LISTER les clés lues par le moteur).
  d) AUTOTEST : on lui injecte un seuil faux (la formule tronquée, 4,25 % au lieu de
     20,87 %) et il DOIT sortir en faute (rc=3). Un gardien qui ne peut pas échouer n'est
     pas un gardien.

=== 4. CE QUE LE GARDE-FOU A TROUVÉ EN 10 SECONDES ===
`chiffrage_entree_sortie_replay.py` — l'instrument du 21/09 qui avait produit les chiffres
ayant mené au câblage d'un flag du MOTEUR en production (`IMPULSE_SANS_REPLI_ON` sur EDEL) —
portait LA MÊME ERREUR dans 3 calculs de seuil. Corrigé, puis rejoué hors ligne
(90 j × 20 paires, klines locales) :
    EDEL E0 : −1,10 $ -> +3,88 $   ·   EDEL E2 (sans repli) : +18,58 $ (inchangé)
    => le gain du levier était GONFLÉ de 25 % (+19,68 -> +14,70 $ sur 90 j)
    => rafales structurellement inaccessibles : 66 % -> 84 %
    => E2+X2 (sans repli + trailing) : test +62,50 -> +59,42 $, 1re moitié +21,80 $ (cohérent)
Conclusion : le flag tient, son motif est plus fort qu'annoncé, mais son gain était surévalué.

=== 5. TROIS MESURES QUI EN DÉCOULENT (toutes lecture seule, 0 ordre, 0 €) ===
(A) SORTIE : RIZE est la seule paire dont le prix monte (+37 % de jambe) et la seule
    perdante (−1,12 $ sur 23 clôtures). Décomposition : STOP/GUARD 8 clôtures −2,79 $ ·
    DUST_SWEEP 5 clôtures −1,39 $ · TRAILING 2 +0,87 $ · PALIERS rip 8 +2,18 $.
    LES PERTES DE STOP RÉALISÉES : 9,58 · 9,58 · 9,58 · 13,75 · 14,58 · 16,51 · 16,51 ·
    39,23 % — pour un stop ANNONCÉ à 8 % dans le profil de la paire. 5 sorties sur 23 se
    font en « dust sweep » (le carnet ne porte pas la position).
(B) CADENCE : le seuil réellement exigé va de 1,70 % (BTC) à 11,22 % (EDEL) — facteur 6,6.
    RIZE : 100 % de ses 4 jambes ≥ 20 % étaient INACCESSIBLES (il aurait fallu un repli de
    21,8-26,9 %, le prix n'a jamais rendu plus de 17,45 % en montant).
(C) TAILLE : la mise utilisée est plafonnée à `2 % du mur bid`. Mesure du carnet public
    (médiane de 4 instantanés) : RIZE porte 604 $ absorbables sous −2 % et la mise réellement
    utilisée est de 4,88 $ (0,75 % de la profondeur) — MAIS le plafond calculé vaut
    15 936 $ = 2 641 % de la profondeur, parce que le « mur » lu est un niveau AFFICHÉ
    (801 457 $ sur RIZE, soit 1 234× la profondeur réelle du carnet ; 569 M$ sur ZBCN).
    Sur d'autres paires le même plafond est sain (CHIP 15 % de la profondeur, BIO 22 %).

=== 6. VOTRE MISSION — CONTREDIRE, PAS APPROUVER ===
Répondez à ces cinq questions, dans cet ordre, en citant les chiffres du brief :
 1. MON GARDE-FOU PEUT-IL RATER ? Nommez le trou le plus probable (angle mort de méthode,
    pas bug de code). Que faudrait-il lui ajouter pour qu'il ne puisse PAS rater ?
 2. QUELLE AUTRE CLASSE D'ERREUR DE MÉTHODE menace un système comme celui-ci (moteur qui
    écrit ses propres décisions, instruments qui les recalculent, humain/IA qui publient des
    chiffres) ? Pour chacune : comment la DÉTECTER MÉCANIQUEMENT ?
 3. Parmi ces 3 mesures — (A) stop qui ne tient pas, (B) seuil proportionnel à la violence de
    la paire, (C) plafond de taille calculé sur un niveau affiché — LAQUELLE traiter en
    premier, et pourquoi ? Qu'est-ce qui vous ferait dire NON à chacune ?
 4. QUELLE EST L'ERREUR QUE JE SUIS EN TRAIN DE COMMETTRE MAINTENANT et que je ne vois pas
    dans ce brief ? (cherchez dans ce qui N'EST PAS dit : pas de test statistique, un seul
    marché haussier, un moteur paper sans mesure d'impact, un flag câblé sur une seule paire…)
 5. Qu'est-ce qui vous ferait changer d'avis (fait mesurable) ?

Puis donnez :
  VERDICT : sur le GARDE-FOU (suffisant | insuffisant mais utile | insuffisant)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3
  CE QUI CHANGERAIT L'AVIS : fait(s) mesurable(s)
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes et réalisables (ou « aucune »)
  SYNTHÈSE (5 lignes max).

Factuel, concis, français. Pas de flagornerie, pas de généralités. Info manquante ->
« information insuffisante ». Vous DONNEZ UN AVIS ; vous ne touchez à RIEN et vous ne
proposez aucun ordre de marché."""

MODELS = ["gemini-flash-lite-latest", "nvidia/nemotron-3-super-120b-a12b:free",
          "x-ai/grok-4.3", "deepseek-ai/DeepSeek-V3-0324"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 3000, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=600) as resp:
        d = json.loads(resp.read().decode())
    return (d["choices"][0]["message"]["content"], d.get("provider", "?"),
            round(time.time() - t0, 1))


def main():
    print(f"FAMILLE : {len(MODELS)} modèles · sortie {OUT}")
    for model in MODELS:
        nom = model.replace("/", "_").replace(":", "_")
        out_file = os.path.join(OUT, f"AVIS_{nom}.md")
        if os.path.exists(out_file) and os.path.getsize(out_file) > 200:
            print(f"[SKIP] {model} a déjà répondu")
            continue
        try:
            content, provider, dur = ask(model)
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(f"# AVIS {model} (provider {provider}, {dur}s)\n\n{content}\n")
            print(f"[OK] {model} ({dur}s, {len(content)} car.)")
        except Exception as e:
            print(f"[ERREUR] {model}: {e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
