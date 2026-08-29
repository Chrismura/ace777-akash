#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
soumettre_famille_vs_cortana_n4.py
===================================
Round 2 du débat : on soumet à CORTANA les RÉPONSES DE LA FAMILLE à ses
critiques (affinage famille n°4), et on la POUSSE à réfléchir sans l'influencer.

Objet : Cortana a critiqué nos 4 corrections (fenêtre 24h du p30, plage UTC
02-06, entropie locale). La famille (6 membres + JUGE) a répondu — en partie
en lui donnant raison, en partie en la contestant. On lui présente ces avis et
on la pousse à se poser, à défendre ou à réviser sa position, en la laissant
libre. PAS de réponse orientée.

Session UNIFIÉE (même fenêtre, contexte conservé), multi-tours + recherche de
saturation. Contenu journalisé dans data/cortana_chats.jsonl + compte-rendu
dans OUTBOX_OBSIDIAN.

Usage : python3 soumettre_famille_vs_cortana_n4.py
"""
import json
import os
import time
import urllib.request
from datetime import datetime, timezone

INDEX = os.path.expanduser("~/ace777-test-day1/Index_Maison")
SCRIPTS = os.path.join(INDEX, "scripts")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
CHATS_LOG = os.path.join(INDEX, "data", "cortana_chats.jsonl")
MAX_TOURS = 4
MARK_SATURATION = (
    "plus rien", "rien de nouveau", "rien de plus", "aucune amélioration",
    "rien à ajouter", "rien d'autre", "je n'ai rien", "je n'ai plus rien",
    "on ne peut pas aller plus loin", "on ne peut aller plus loin",
)


def load_system_prompt():
    for p in (
        os.path.join(SCRIPTS, "prompts", "PROMPT_MASTER_ANALYSTE.md"),
        os.path.expanduser("~/Documents/Obsidian_ACE777/PROMPT_MASTER_ANALYSTE.md"),
    ):
        if os.path.exists(p):
            try:
                return open(p, encoding="utf-8").read()
            except Exception:
                pass
    return "Tu es Cortana, master analyste crypto du cockpit ACE777. Réponds en français, concis."


def charge_reponses_famille() -> str:
    """Les avis famille, présentés factuellement, sans parti pris. On lui montre
    le désaccord y compris au sein de la famille (pour qu'elle voie qu'aucun
    exercice n'est truqué), et la CONSIGNE est d'être libre."""
    return (
        "=== DONNÉES DU ROUND 1 : TES CRITIQUES + LES RÉPONSES DE LA FAMILLE ===\n\n"
        "RAPPEL DE TES 3 CRITIQUES (tour 1-4 de la session affinage-n4) :\n"
        "  A. La fenêtre 24h du p30 = miroir rétroviseur → remplacer par un percentile "
        "normalisé par volatilité instantanée (ATR court terme).\n"
        "  B. La plage horaire UTC 02-06 rigide = erreur de débutant / angle mort → "
        "remplacer par une fenêtre de volume glissant 3h (si volume panier −60 % vs MM24h).\n"
        "  C. L'entropie temporelle est trop locale → matrice de corrélation croisée des "
        "intervalles d'inter-arrivée entre paires (détection d'essaim).\n\n"
        "La famille ACE777 (6 membres : GEMINI, DEEPSEEK, ULTRA, INFERX, GROK + JUGE) a "
        "répondu point par point, avec nos données réelles. Voici les avis, texte quasi "
        "intégral (sans nos interprétations).\n\n"
        "--- AVIS FAMILLE SUR TES CRITIQUES ---\n"
        "ULTRA : « Courtana raisonne en théorie pure. Sur nos small caps (ZBCN, PYTH) les "
        "carnets subissent des micro-chocs de liquidité d'une violence extrême (facteur 5-10 "
        "en minutes). Remplacer le p30-24h par un ATR court terme va DÉTRUIRE le seuil, le "
        "bruit HF des carnets creux provoquera une explosion des faux signaux. Le p30-24h sert "
        "d'amortisseur anti-bruit. » ; « Sur la plage UTC : oui c'est un angle mort, MAIS ta "
        "solution volume −60 % est un cauchemar de robustesse en tempête — en krach, le volume "
        "s'emballe ou s'effondre de façon chaotique, boucle de rétroaction perverse. Une plage "
        "fixe reste robuste. » ; « La matrice de corrélation = latence inacceptable + point de "
        "défaillance unique, complexité inutile. » VERDICT : GO avec réserves.\n\n"
        "DEEPSEEK : « Courtana partiellement raison sur A (la 24h lisse les ruptures violentes) "
        "mais l'ATR pur sans borne introduit du bruit insupportable. Mon amendement : seuil = "
        "0.7×p30_24h + 0.3×p30_4h (réagit en <60 min sans lâcher l'amortisseur). » ; « Sur B : "
        "tu as RAISON, remplacer par volume glissant 3h (si chute ≥60 % vs MM24h). » ; « Sur C : "
        "tu te trompes sur la priorité, la matrice surcharge le wrapper pour un gain incertain "
        "→ compteur d'essaim léger (si ≥3 paires CV≤15 % en 60 s → +0.25 SAPI). » VERDICT : "
        "GO avec réserves.\n\n"
        "GEMINI : « Hybride A : max(p30_24h, ATR_30m × k) — amortit le bruit ET capture "
        "l'urgence. » ; « B : abandonner la plage 02-06, déclencheur volume −60 % vs MM24h sur "
        "3h. » ; « C : compteur de co-occurrence (si ≥3 paires CV≤15 % même minute → malus +0.25). » "
        "VERDICT : GO avec réserves.\n\n"
        "GROK : « A : ni l'un ni l'autre — fenêtre glissante hybride 4h + ATR 15 min. » ; « B : "
        "tu as RAISON, mais ton seuil −60 % est trop strict → −50 %. » ; « C : tu te trompes, "
        "c'est un modèle de grand fonds, décorrélation naturelle small caps → rejeter la "
        "matrice, garder l'entropie locale + filtre volume panier. » VERDICT : GO avec réserves.\n\n"
        "INFERX : « A : nuancer, ne rien toucher au p30-24h brut mais poids hybride EMA 4h+20h. » ; "
        "« B : tu te TROMPES — nos logs montrent une chute structurelle du volume ×4 à ×6 entre "
        "01:30-06:00, la plage est empiriquement exacte pour notre panier, pas arbitraire. "
        "Conserver 02-06 + gardien dynamique (si volume 1h −80 % HORS plage → basculer en mode "
        "creux). » ; « C : tu as raison sur le fond mais non applicable en l'état, risque de "
        "deadlock → compteur d'essaim ≥2 paires → +0.25. » VERDICT : GO avec réserves.\n\n"
        "JUGE (tranche après lecture de tous) : « Courtana a raison sur la rigidité des fenêtres "
        "temporelles (24h et UTC 02-06) qui créent des angles morts sur nos small caps. Valider "
        "le code actuel (14/14) mais : 1) hybride EWMA 4h/24h, 2) remplacer la plage UTC par un "
        "déclencheur volume glissant 3h (si chute ≥60 % vs MM24h), 3) rejeter la matrice lourde "
        "au profit d'un compteur d'essaim minimaliste (≥3 paires CV≤15 % → +0.20 SAPI). » "
        "VERDICT : GO avec réserves.\n\n"
        "== NOTE MÉTHODO POUR TOI == la famille est à 6/6 GO avec réserves sur ton travail, "
        "mais ils jugent QUE 2 DE TES PROPOSITIONS (ATR pur, matrice lourde) sont, à leur stade "
        "de données/prod, plus risquées qu'utiles. Ils sont en DÉSACCORD ENTRE EUX-MÊMES sur la "
        "plage UTC (2 membres veulent la garder, l'autre moitié veut la remplacer).\n\n"
        "=== CE QU'ON TE DEMANDE ===\n"
        "Réfléchis VRAIMENT, sans chercher ni à confirmer ni à te défendre. On ne te demande pas "
        "de te soumettre. On te demande :\n"
        "1) Après avoir lu ces réponses (avec leurs arguments sur tes 2 propositions jugées "
        "\"risquées\"), estimes-tu toujours qu'elles sont les bonnes ? Défends-les ou révise-les, "
        "en argumentant.\n"
        "2) Où la famille se trompe-t-elle, à ton avis, ENCORE ? Ils sont 6/6 GO avec réserves — "
        "qu'est-ce qu'ils ratent en refusant ta solution ?\n"
        "3) Le désaccord interne sur la plage UTC (garder vs remplacer) : qui a raison, et "
        "pourquoi, avec nos données (chute volume ×4-6 observée 01:30-06:00) ?\n"
        "4) Y a-t-il un point où tu changes d'avis ? Dis-le franchement si oui.\n"
        "Sois directe, autocritique, et même frondeuse si c'est honnête. Tu n'es pas en examen.\n\n"
        "FORMAT OBLIGATOIRE : termine par AVIS STRICT : LONG/SHORT/NEUTRE, HORIZON, CONFIANCE."
    )


def appeler(messages, max_essais=3) -> tuple:
    payload = {
        "task": "cortana.analyse",
        "messages": messages,
        "temperature": 0.4,
        "max_tokens": 1400,
    }
    body = json.dumps(payload).encode("utf-8")
    dernier_err = None
    prov = "?"
    for essai in range(1, max_essais + 1):
        try:
            req = urllib.request.Request(
                HUB, data=body,
                headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=240) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            content = data["choices"][0]["message"]["content"].strip()
            return content, data.get("provider", "?")
        except Exception as e:  # noqa: BLE001
            dernier_err = e
            print(f"  [appeler] essai {essai}/{max_essais} échoué : {type(e).__name__}: {e}", flush=True)
            if essai < max_essais:
                time.sleep(10)
    raise RuntimeError(f"Hub injoignable après {max_essais} essais : {dernier_err}")


def journalise(session_id, question, reponse, provider, tour):
    try:
        os.makedirs(os.path.dirname(CHATS_LOG), exist_ok=True)
        entry = {
            "session": session_id, "tour": tour, "ts": time.time(),
            "ts_iso": datetime.now(timezone.utc).isoformat(),
            "question": question, "reponse": reponse,
            "provider": f"cortana:{provider}",
        }
        with open(CHATS_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        pass


def main():
    print("=== ROUND 2 — FAMILLE vs CORTANA (sans influence) ===\n", flush=True)
    sys_prompt = load_system_prompt()
    session_id = "famille-vs-cortana-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

    messages = [{"role": "system", "content": sys_prompt},
                {"role": "user", "content": charge_reponses_famille()}]

    prev = []
    for tour in range(1, MAX_TOURS + 1):
        print(f"\n----- TOUR {tour} -----", flush=True)
        rep, prov = appeler(messages)
        journalise(session_id, messages[-1]["content"], rep, prov, tour)
        messages.append({"role": "assistant", "content": rep})
        print(f"[{prov}] " + rep.replace("\n", " ")[:900] + "\n", flush=True)

        b = rep.lower()
        if any(k in b for k in MARK_SATURATION) and tour >= 2:
            print("\n[FIN] Saturation détectée.", flush=True)
            break

        if tour == 1:
            next_q = (
                "Reste-là un instant : la famille t'a donné 2 fois la main (GO avec réserves) "
                "mais a REFUSÉ le cœur de tes 2 propositions (ATR pur, matrice). Réfléchis à "
                "CE QU'ILS VOIENT QUE TU NE VOIS PAS : qu'est-ce qui, dans leurs données (pas "
                "la théorie), rend ton ATR et ta matrice réellement risqués pour EUX ? Si tu "
                "devais négocier UN seul compromis qu'ils accepteraient, lequel ? Donne une "
                "réponse précise et codable."
            )
        elif tour == 2:
            next_q = (
                "Maintenant change de lunettes : joue l'AVOCAT DE LA FAMILLE contre toi-même. "
                "Construis le meilleur argument POUR leur p30-24h amorti et leur 02-06 (ou ton "
                "volume −60 %) ET POUR garder l'entropie locale sans matrice — puis dis-nous "
                "franchement s'il te convainc. Termine par ce que tu CONSERVES de ta position "
                "et ce que tu ABANDONNES après cet exercice."
            )
        elif tour == 3:
            next_q = (
                "Dernière passe : nous sommes à la veille d'implémenter une seule chose. "
                "Donne TON verdict final, tranché et concret : 1) un résumé des réels points "
                "d'accord et de désaccord entre toi et la famille (en 4-6 lignes) ; 2) la "
                "DÉCISION que TU prendrais si tu étais à ta place (garder/corrections, lequel "
                "des 3 choix : A hybride JUGE, B garder 02-06+gardien, C statu quo) ; 3) une "
                "dernière justification, sans complaisance. AVIS STRICT + CONFIANCE."
            )
        messages.append({"role": "user", "content": next_q})
        prev.append(f"[tour{tour}] {rep.strip()[:220]}")

    cr = (
        "SESSION famille-vs-cortana : " + session_id + "\n"
        "PROVIDER : " + prov + "\n"
        "TOURS : " + str(len(prev)) + "\n\n" + "\n\n".join(prev) + "\n"
    )
    out = os.path.join(INDEX, "OUTBOX_OBSIDIAN", "VAL_CROISEE_ROUND2_CORTANA_" + datetime.now(timezone.utc).strftime("%Y%m%d") + ".md")
    try:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write("# Round 2 — Famille vs Cortana (réflexion libre)\n\n" + cr)
        print("Compte-rendu écrit : " + out, flush=True)
    except Exception as e:
        print("WARN : écriture compte-rendu : " + str(e), flush=True)
    print("\n=== FIN (archivée, " + session_id + ") ===\n", flush=True)


if __name__ == "__main__":
    main()