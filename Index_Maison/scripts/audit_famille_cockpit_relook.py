#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — chantier RELOOK COCKPIT v2 (13/08).
Heure locale unifiée + graph synapse sans bulles + cosmos lisible + tableaux côte à côte + live polling.
Verdict attendu : GO / GO AVEC RÉSERVES / NON, + suggestions logique/perf/stabilité (3 coups une pierre).
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.expanduser("~/ace777-test-day1/Index_Maison/AUDIT_COCKPIT_RELOOK_2026-08-13")
os.makedirs(OUT, exist_ok=True)

FAMILLE = [
    ("audit.protocol", "GEMINI"),
    ("mission", "DEEPSEEK"),
    ("signets.juge", "JUGE"),
    ("ultra.analyse", "ULTRA"),
    ("inferx.analyse", "INFERX"),
    ("supervise.decision", "GROK"),
]

BRIEF = """Tu es membre de la FAMILLE de validation ACE777 (audit qualité, niveau hedge fund suisse).
Audite ce chantier de RELOOK COSMÉTIQUE + ROBUSTESSE du cockpit (interface de pilotage).

## CE QUE CHRISTOPHE A DEMANDÉ (13/08)
1. **Heure** : mélangée entre UTC (clock + refresh, suffixe Z) et heure locale (cosmos) -> décalage de 2h.
   Règle : TOUT en heure locale HH:MM:SS, jamais de Z, libellé discret « locale ».
2. **Onglet GRAPH** : le graph synapse = « bulles » (noms écrits DANS les cercles) illisibles qui se superposent.
   -> relook neurone/synapse : petit soma + label EXTERNE avec leader line + anti-chevauchement.
3. **Cosmos** (graphe du HUB) : providers sur un cercle serré, noms superposés. -> orbite aérée (2 anneaux si >8),
   labels externes avec leader line et anti-chevauchement vertical, toujours lisibles.
4. **Tableaux de droite** : empilés en colonne avec lignes vides. -> grille 2 colonnes côte à côte
   (Budget + État du Hub / File d'attente + Quotas / Événements pleine largeur).
5. **LIVE** : hub.js était un snapshot chargé UNE fois -> jamais rafraîchi. -> polling fetch('hub.json')
   toutes les 10 s (servi no-store par :17800), mise à jour window.__HUB__ + buildNodes + renderCosmos.
   Les fenêtres d'info (cosmos-detail au clic, node-info, tooltip) sont CONSERVÉES (Christophe les adore).

## CODE RÉEL INTÉGRÉ (extraits clés, fichier Index_Maison/cockpit/index.html)
- tickClock : document.getElementById('clock').textContent = d.toLocaleTimeString('fr-FR'); + title 'heure locale'
- refresh : meta.textContent = 'MAJ ' + new Date().toLocaleTimeString('fr-FR') + ' (locale)'
- sessionSince : new Date(M.sessionSince).toLocaleTimeString('fr-FR', {hour,minute})
- queue cosmos : secondes ajoutées + feed : ' (locale)' + âge en secondes calculé via Date.now()
- Graph synapse : r = 4..6 (petit soma), label externe labelX = x<W*0.5 ? x+18 : x-18, labelY = y<H*0.5 ? y+14 : y-14,
  leader line + fillText '11px Share Tech Mono' avec shadow ; sélection/hover conservés.
- buildNodes : useTwoRings = data.length > 8 ; R = min(W,H)*0.42 ; R2 = R*0.72 ; step selon nombre par anneau.
- drawNodes : label du hub seul au centre (17px), providers = boucle externe avec drawnLabels[],
  anti-chevauchement (while guard<10, décalage ±14 si dist<14 et distX<120), leader line #4a5568.
- cosmos-right : display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px;
  @media (max-width:1100px){1fr}. HTML : ordre Budget, État du Hub, File d'attente, Quotas, Événements (grid-column:1/-1).
- pollHubLive() : fetch('hub.json',{cache:'no-store'}) -> window.__HUB__=data; buildNodes(); renderCosmos();
  appel immédiat + setInterval 10000. Pas de touche à graph-meta (écrasé par drawSynapses à 60fps).

## PREUVES DE TEST (headless Brave réel, 8 s de budget virtuel)
- Page chargée sans erreur JS (seule erreur GPU sans rapport), DOM 317 Ko.
- clock = 19:55:15 (locale), queue = 19:54:32 avec secondes, health = OK 8 providers.
- budget = 1613/624 vs snapshot initial 1602 -> le polling a bien rechargé un feed plus frais (LIVE prouvé).
- Syntaxe JS : node --check 2 blocs OK ; ids/fonctions uniques vérifiés.

## TA MISSION (3 coups une pierre — décision Christophe 13/08)
1. Verdict : GO / GO AVEC RÉSERVES / NON (argumenté sur le code réel ci-dessus).
2. EN PLUS, cherche des AMÉLIORATIONS logique/perf/stabilité utiles : anti-chevauchement de labels robuste ?
   coût du polling 10s (léger ?) ; gestion erreurs fetch ; cohérence heure sur TOUT le cockpit
   (y a-t-il d'autres endroits UTC restants ?) ; interactions avec les autres onglets ?
3. Réponds en FRANÇAIS, structuré, concis (max 300 mots)."""


def ask(task, prompt):
    payload = json.dumps({
        "task": task,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1200,
        "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(
        HUB, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.loads(resp.read().decode())


def main():
    for task, label in FAMILLE:
        out_path = os.path.join(OUT, label + ".md")
        if os.path.exists(out_path):
            print("[déjà fait]", label)
            continue
        print("[audit]", label, "...", flush=True)
        try:
            d = ask(task, BRIEF)
            content = d["choices"][0]["message"]["content"]
            provider = d.get("provider", "?")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(f"# {label} — verdict famille\n\nProvider: {provider}\n\n{content}\n")
            print("[ok]", label, "->", out_path)
        except Exception as e:
            print("[ÉCHEC]", label, ":", str(e)[:160])


if __name__ == "__main__":
    main()
