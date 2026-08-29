#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
soumettre_affinage_famille_n4_cortana.py
=========================================
Soumission à Cortana des 4 corrections finales de l'affinage famille n°4
(29/08, GO Buffy) pour VALIDATION CROISÉE avec contexte complet.

Contexte : l'audit famille (6 membres, AUDIT_FAMILLE_OEUVRES_20260829) a fait
converger 4 affinages sur nos œuvres (Signal 3 squeeze du livre écorché, SAPI
poussière institutionnelle, croisement externe, PathRegistry). Christophe veut
que Cortana (extérieure à la construction) VALIDE / CONTESTE / AMÉLIORE ces
corrections avec un regard neuf — c'est la validation croisée de la formule.

PROTOCOLE (session UNIFIÉE, même fenêtre — le contexte compte) :
  TOUR 1 : présentation des 4 corrections + nos données réelles + demander une
           validation/critique honnête point par point.
  TOUR 2 : pousser — « réessaie, trouve ce qui cloche, ce que tu changes ».
  TOUR 3 : pousser plus loin — « va au-delà, propose des améliorations NOUVELLES
           codables ; qu'est-ce qu'on rate ? ». Recherche de saturation en fin.
  TOUR 4 : phase finale — « on a appliqué tes N suggestions ; que reste-t-il
           d'essentiel ? Verdict synthétique + confiance + horizon ».

Usage : python3 soumettre_affinage_famille_n4_cortana.py
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


def charge_corrections() -> str:
    """Les 4 corrections + nos données réelles (validation croisée)."""
    return (
        "=== LES 4 CORRECTIONS DE L'AFFINAGE FAMILLE N°4 (29/08, appliquées et testées) ===\n\n"
        "Contexte racine : l'audit famille (6 IA : GROK, DEEPSEEK, INFERX, GEMINI, ULTRA, JUGE) "
        "a identifié des FAILS dans nos détecteurs. Trois fails techniques + une barrière "
        "structurelle. Tout est déjà codé et testé ICI, on veut TON regard neuf (tu n'as pas "
        "participé à la construction).\n\n"
        "--- CORRECTION 1 : DYNAMIC SPREAD PERCENTILE (Signal 3 — squeeze du livre écorché) ---\n"
        "AVANT : seuil spread FIXE = 70 bps pour toutes les paires. \n"
        "PROBLÈME famille : biais structurel — une small cap illiquide vit naturellement à "
        "150+ bps, une large cap à 5 bps. Un seuil absolu est incomparable.\n"
        "APRÈS : le seuil de chaque paire = PERCENTILE 30 de sa propre distribution de spread "
        "sur les 24 dernières heures (fini le 70 fixe). Fail-open : < 8 mesures → seuil nominal.\n"
        "RÉSULTAT RÉEL (testé à l'instant) : XRP p30=1.45 (au lieu de 70), PYTHUSDT p30=2.12, "
        "ZBCNUSDT p30=18.34, BTCUSDT p30=0.02. Le spread actuel est comparaison vs l'histoire "
        "de la paire.\n\n"
        "--- CORRECTION 2 : HEURES CREUSES UTC (02-06) ---\n"
        "PROBLÈME famille (Juge) : « Heure creuse élargit le spread naturellement → le proxy "
        "confond manque de market-maker avec poussière/squeeze. »\n"
        "APRÈS : 2 endroits. Signal 3 : seuil spread élargi ×1.8 en 02-06 UTC. SAPI : le proxy "
        "carnet ne compte que ×0.35 (le spread large creux n'est plus confondu avec de la "
        "poussière institutionnelle).\n\n"
        "--- CORRECTION 3 : TERME D'ENTROPIE TEMPORELLE (SAPI — poussière institutionnelle) ---\n"
        "IDÉE : une poussière institutionnelle = un SCRIPT qui laisse le carnet à un rythme "
        "suspectement régulier (CV<=15 % = quasi-robotique), vs le chaos retail.\n"
        "APRÈS : bonus +0.10 au SAPI si le taux_de_fantômes a un rythme quasi-robotique ET "
        "qu'une base fantôme est déjà détectée (le bonus ne peut JAMAIS être seul déclencheur).\n"
        "RÉSULTAT RÉEL (live.json) : entropie_tempo=1.0 (rythme régulier), le score SAPI est "
        "monté de 0.15 à 0.399 (sous le seuil 0.75, pas d'alerte).\n\n"
        "--- CORRECTION 4 : PathRegistry centralisé + wrapper plists (erreurs répétées) ---\n"
        "PROBLÈME : erreurs RÉPÉTÉES de (a) chemins relatifs/absolus qui plantent en plist "
        "launchd, (b) processus silencieux qui meurent sans alerte. On s'est mangé les deux "
        "plusieurs fois cette semaine.\n"
        "APRÈS : Index_Maison/scripts/path_registry.py — registre central des chemins, "
        "verifier(oeuvre) valide au démarrage (sys.exit(1) si chemin obligatoire manque), "
        "wrapper plist à heartbeat (début/OK datés) pour les 3 plists critiques (signal3, "
        "croisement-externe, thermo-quotidien).\n\n"
        "=== NOTRE SYSTÈME (pour que tu saches où ça s'insère) ===\n"
        "Le Signal 3 détecte un 'vacuuming' du livre écorché : mur iceberg fictif + retrait de "
        "liquidité → trou d'air → décrochage. Source arXiv 2504.15908 (31 % des grosses ordres "
        "spoofent). Il a déjà (tour précédent famille) : β_asset dynamique (contagion BTC "
        "ignorée si corrélation<0.3), asymétrie directionnelle (contagion seulement si "
        "delta_btc<0), filtre MAD anti-jitter, écriture atomique, persistance 3 ticks.\n"
        "Le SAPI = Score d'Alerte Poussière Institutionnelle : termes z_fee + taux_fantôme + "
        "micro_tx - proxy carnet. Validé par notre corrélation RBF plat −0.275 sur 13 933 "
        "points. Alerte = persistance 3 ticks ≥0.75 + volume ≥500 BTC.\n"
        "Le croisement externe applique la règle des 2 sources (nos prix vs MEXC/Binance, "
        "écart>5 %=bloquant) avec persistance 3 ticks.\n\n"
        "=== CE QU'ON TE DEMANDE (validation croisée) ===\n"
        "1) VALIDE ou CONTESTE chaque correction (1 à 4) avec des arguments précis.\n"
        "2) Les seuils (p30, ×1.8, ×0.35, CV<=15 %, bonus +0.10) te semblent-ils les bons ? "
        "Qu'est-ce que tu aurais calibré différemment ?\n"
        "3) Y a-t-il un RISQUE que ces corrections AVEUGLENT le détecteur (lissent le vrai "
        "signal en voulant tuer le faux positif) ? Nomme le faux-négatif que tu crains.\n"
        "4) Y a-t-il une meilleure façon (architecturale) de régler les erreurs de chemins/"
        "processus silencieux que notre PathRegistry+wrapper ?\n"
        "Note ta confiance et ton horizon pour chaque point."
    )


def appeler(messages, max_essais=3) -> tuple:
    """Appelle le hub avec RE-TENTATIVE (3 essais, backoff 10 s) : la panne
    réseau d'une seule requête ne doit plus tuer toute la session."""
    payload = {
        "task": "cortana.analyse",
        "messages": messages,
        "temperature": 0.4,
        "max_tokens": 1300,
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
        except Exception as e:  # noqa: BLE001 — re-tentative, pas crash
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
    print("=== SESSION CORTANA — VALIDATION CROISÉE AFFINAGE FAMILLE N°4 ===\n", flush=True)
    sys_prompt = load_system_prompt()
    session_id = "affinage-n4-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

    messages = [{"role": "system", "content": sys_prompt},
                {"role": "user", "content": charge_corrections()}]

    prev = []
    for tour in range(1, MAX_TOURS + 1):
        print(f"\n----- TOUR {tour} -----", flush=True)
        rep, prov = appeler(messages)
        journalise(session_id, messages[-1]["content"], rep, prov, tour)
        messages.append({"role": "assistant", "content": rep})
        # Synthèse condensée à l'écran
        short = rep.replace("\n", " ")[:900]
        print(f"[{prov}] {short}\n", flush=True)

        b = rep.lower()
        satur = any(k in b for k in MARK_SATURATION)
        if satur and tour >= 2:
            print("\n[FIN] Saturation détectée.", flush=True)
            break

        # Poussées successives (même fenêtre, contexte conservé)
        if tour == 1:
            next_q = (
                "Réessaie, en te FORÇANT à faire l'avocat du diable : tu critiques surtout — "
                "trouve au moins 2 choses concrètes qui clochent dans ces 4 corrections. "
                "Un seuil mal calibré ? Une correction qui désensibilise le vrai signal ? "
                "Un angle mort que la famille (et donc toi) avez raté ? Donne-moi des amendements "
                "PRÉCIS et codables, pas des généralités."
            )
        elif tour == 2:
            next_q = (
                "Va au-delà de ce qui est écrit. PROPOSE des améliorations NOUVELLES et "
                "codables pour le Signal 3 et le SAPI (ex : un autre détecteur de régularité, "
                "une corrélation croisée que personne n'a eue, une fenêtre de session, une "
                "normalisation par volatilité différente, un indicateur avancé). Qu'est-ce qu'on "
                "rate qui ferait une vraie différence pour Hulk (petites caps) ?"
            )
        elif tour == 3:
            next_q = (
                "Dernière passe avant exécution : on a noté tes retours. Réponds en 2 parties. "
                "1) Sur quoi es-tu en désaccord avec la FAMILLE elle-même (elle a validé ces "
                "4 corrections 'GO avec réserves') — incorrigue-la si elle se trompe ? "
                "2) Donne TON verdict final synthétique : laquelle de ces 4 corrections est la "
                "plus utile / la plus risquée pour nous, et le calibrage exact que tu recommandes "
                "de régler en premier. Sois tranchée."
            )
        messages.append({"role": "user", "content": next_q})
        prev.append(f"[tour{tour}] {rep.strip()[:180]}")

    # Compte-rendu final
    cr = (
        "SESSION affinage-n4 : " + session_id + "\n"
        "PROVIDER : " + prov + "\n"
        "TOURS : " + str(len(prev)) + "\n\n"
        + "\n\n".join(prev) + "\n"
    )
    out = os.path.join(INDEX, "OUTBOX_OBSIDIAN", "VAL_CROISEE_CORTANA_AFFINAGE_N4_" + datetime.now(timezone.utc).strftime("%Y%m%d") + ".md")
    try:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write("# Validation croisée Cortana — Affinage famille n°4 (29/08)\n\n" + cr)
        print("Compte-rendu écrit : " + out, flush=True)
    except Exception as e:
        print("WARN : écriture compte-rendu : " + str(e), flush=True)

    print("\n=== FIN DE SESSION (archivée, " + session_id + ") ===\n", flush=True)


if __name__ == "__main__":
    main()