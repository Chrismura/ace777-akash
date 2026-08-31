#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""soumettre_codeur_phase1_moteur_leger_20260831.py — Le CODEUR écrit le patch
de la Phase 1 (moteur léger et costaud). Buffy supervise. GO Christophe + famille 7/7.

Le codeur (canal code.ia) reçoit le contexte EXACT des fonctions à modifier et
les règles issues de la consultation. Il doit rendre du code prêt à intégrer.
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_CODEUR_MOTEUR_LEGER_20260831")
os.makedirs(OUT, exist_ok=True)

PROMPT = """CODEUR EXPERT — Phase 1 « moteur léger et costaud » (Hulk paper MEXC).

RÈGLE ABSOLUE : la logique métier (achats, ventes, bags, stops, régimes) NE DOIT
PAS CHANGER. Tu produis un patch de PERFORMANCE + ROBUSTESSE réseau uniquement.
Fichier : /Users/christophe/ace777-test-day1/hulk-mexc/scripts/paper_diprip.py

CONTEXTE MESURÉ : le moteur fait ~21 appels GET single-pair par cycle de 20s
(via last_price() dans tick_pair) → ~200-270 req/min vs limite MEXC ~200. Objectif
Phase 1 : passer à 1 appel batch par cycle + durcir les timeouts + écriture
atomique + corriger le drift de boucle.

### FONCTIONS EXISTANTES À MODIFIER (contexte exact)

1) http_json (ligne ~176) :
```python
def http_json(url, timeout=40.0, retries=4):
    # SIGALRM + urllib ; retries = for _ in range(retries) avec time.sleep(1.2*(attempt+1))
```
2) last_price (ligne ~270) :
```python
def last_price(pair):
    q = urllib.parse.urlencode({"symbol": pair})
    j = http_json(f"https://api.mexc.com/api/v3/ticker/price?{q}")
    return float(j["price"])
```
3) Boucle run() : dans le while (ligne ~2354), il fait `for pair in self.pairs: self.tick_pair(pair)`
   -> chacun appelle last_price(pair) (1 GET/paire). Puis `time.sleep(self.poll)` (drift).
4) log_contexte (ligne ~853) : écrit une ligne en append dans runs/croisement_contexte.jsonl
   via `with open(..., "a")`.

### CE QUE JE VEUX (rends le code final prêt à intégrer, sans trivialité)

A) **BATCH PRIX + CACHE PAR CYCLE** (remplace les 21 appels par 1 appel) :
- Ajouter `def fetch_all_prices(self):` qui fait UN appel GET /api/v3/ticker/price
  (sans symbole) → retourne dict `{symbol: float(price), ...}`. Parser en dict,
  jamais itérer la liste brute hors transformation.
- Garder `last_price(pair)` comme API mais lui faire lire UN CACHE : le moteur
  charge `self.price_cache` au tout début de chaque cycle (1 appel batch), et
  last_price(pair) lit d'abord `self.price_cache[pair]` ; si la paire est ABSENTE
  du cache → fallback GET unitaire ciblé (jamais de KeyError, jamais de crash) ;
  si le fetch_all_prices a échoué → fallback GET unitaire aussi.
- La variable du batch est FIGÉE pour tout le tour de boucle (visible par tick_pair,
  manage_open, manage_bag, maybe_enter, etc.). Le plus sûr : un module-level ou un
  attribut self.price_cache mis à jour une fois par cycle ; last_price(où il sert)
  le lit.
- Prévoir : réponse batch = liste de {symbol, price} du MEXC. Si le format change
  ou qu'une paire est delistée, on ne plante JAMAIS (try/except + log warning).

B) **HTTP_JSON DURCI** (Timeout + backoff 429/5xx) :
- timeout par défaut ~15s (au lieu de 40).
- retries par défaut 1 (au lieu de 4).
- Backoff exponentiel UNIQUEMENT si statut 429 (rate-limit) ou 5xx : 1s puis 2s.
- En cas d'échec final, l'appelant doit avoir un fallback propre (last_price ->
  garder le précédent prix connu s'il existe, sinon signaler sans planter).
- TOUJOURS garder la ceinture SIGALRM existante (elle est vitale).

C) **DRIFT DE BOUCLE** (run()) : au lieu de `time.sleep(self.poll)`, calculer le
   prochain tick absolu (start = time.time(); … ; sleep = max(0, poll - (now-start)))
   pour que le cycle reste cadencé même si le calcul prend du temps.

D) **ÉCRITURE ATOMIQUE** : fournir `def atomic_write_json(path, data)` (fichier
   .tmp dans le même dossier + os.replace). Donner le point EXACT où l'appliquer
   à la Phase 1 (ex. save_state) sans casser le JSONL append de croisement_contexte
   (qui reste append-only et est déjà lu avec try/except par les satellites).

### LIVRABLE
Donne le code COMPLET des fonctions modifiées/ajoutées (pas de pseudo-code), prêt
à copier. Marque clairement chaque point d'insertion (ex. "# ===== INSERTX =====").
Ajoute une NOTE D'INTÉGRATION de 5 lignes max : l'ordre d'application (pour ne pas
casser), et ce qui doit être testé avant de redémarrer le moteur.

Contrainte finale : CONCIS, français, du code exécutable, zéro baratin."""


def main():
    payload = json.dumps({
        "task": "code.ia",
        "messages": [{"role": "user", "content": PROMPT}],
        "max_tokens": 4000, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"},
                                 method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    f = os.path.join(OUT, "RESPONSE_CODEUR.md")
    with open(f, "w", encoding="utf-8") as fh:
        fh.write(f"# CODEUR — Phase 1 moteur léger et costaud (provider {provider}, {round(time.time()-t0,1)}s)\n\n{content}\n")
    print(f"[OK] CODEUR ({provider}) → {f} ({len(content)} chars)")


if __name__ == "__main__":
    sys.exit(main())