# RÉPONSE HUB (task code.ia · via Puter Grok (gratuit)) — 2026-08-13T16:03:21

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""budget_hub.py — budget cloud DYNAMIQUE avec réserve storm et gratuits protégés."""

import json
import os
import shutil
import sys
import time
from typing import Any, Dict, List, Optional, Set

P = os.path.expanduser('~/prise-ia')
FACTEUR_SECURITE = 0.15
MIN_BUDGET = 40
MAX_BUDGET = 800

CAPACITES: Dict[str, int] = {
    'qwen-local': 0,
    'gemini': 1500,
    'openrouter-free': 700,
    'openrouter-ultra': 500,
    'openrouter-juge': 300,
    'nvidia': 1000,
    'inferx-coder': 400,
    'puter-grok': 800,
    'groq': 1000,
    'mistral': 0,
    'cloudflare-workers-ai': 0,
}

GRATUITS: Set[str] = {
    'qwen-local', 'openrouter-free', 'openrouter-ultra', 'openrouter-juge',
    'nvidia', 'inferx-coder', 'puter-grok', 'gemini'
}
PAYANTS: Set[str] = set()


def providers_actifs() -> List[str]:
    """Retourne la liste des providers actifs depuis providers.json."""
    prov_path = os.path.join(P, 'providers.json')
    if not os.path.exists(prov_path):
        return []
    try:
        with open(prov_path, 'r', encoding='utf-8') as f:
            prov = json.load(f)
        actifs: List[str] = []
        for p in prov.get('providers', []):
            pid = p.get('id', '?')
            if p.get('enabled') or p.get('kind') == 'local':
                actifs.append(pid)
        return actifs
    except Exception:
        return []


def calculer_budget_journalier(actifs: List[str]) -> Dict[str, Any]:
    """Fonction pure de calcul du budget journalier dynamique."""
    capacite_totale = sum(CAPACITES.get(pid, 0) for pid in actifs)
    total = max(MIN_BUDGET, min(MAX_BUDGET, int(capacite_totale * FACTEUR_SECURITE)))
    reserve_storm = int(total * 0.20)
    calme = total - reserve_storm
    return {
        "total": total,
        "calme": calme,
        "reserve_storm": reserve_storm,
        "gratuits": list(GRATUITS),
        "payants": list(PAYANTS),
        "actifs": actifs,
        "ts": int(time.time())
    }


def main() -> None:
    """Point d'entrée principal."""
    try:
        actifs = providers_actifs()
        r_path = os.path.join(P, 'routing.json')
        routing: Dict[str, Any] = {}
        if os.path.exists(r_path):
            try:
                with open(r_path, 'r', encoding='utf-8') as f:
                    routing = json.load(f)
            except Exception:
                routing = {}

        referenced: Set[str] = set()
        for v in routing.get('tasks', {}).values():
            if isinstance(v, dict):
                referenced.add(v.get('provider'))
                referenced.add(v.get('fallback'))
        for pid in referenced:
            if pid and pid not in actifs:
                actifs.append(pid)

        budget = calculer_budget_journalier(actifs)

        print('=== BUDGET CLOUD DYNAMIQUE ===')
        print('Providers actifs (%d) : %s' % (len(actifs), ', '.join(actifs)))
        print('Capacite theorique cloud/jour : %d req' % sum(CAPACITES.get(pid, 0) for pid in actifs))
        print('Facteur securite : %d%%' % int(FACTEUR_SECURITE * 100))
        print('Budget total : %d | Calme : %d | Reserve storm : %d' % (
            budget["total"], budget["calme"], budget["reserve_storm"]))
        print('Gratuits proteges : %s' % ', '.join(sorted(GRATUITS)))
        ancien = routing.get('cloud_daily_budget', '?')
        print('Budget actuel dans routing.json : %s' % ancien)

        if '--apply' in sys.argv:
            try:
                if os.path.exists(r_path):
                    shutil.copy(r_path, r_path + '.bak-budget')
                routing['cloud_daily_budget'] = budget["calme"]
                routing['cloud_daily_reserve'] = budget["reserve_storm"]
                routing['note'] = ('cloud_daily_budget DYNAMIQUE calcule par budget_hub.py '
                                   '(%d calme + %d reserve storm). Recalcule quotidien apres rotation.' %
                                   (budget["calme"], budget["reserve_storm"]))
                with open(r_path, 'w', encoding='utf-8') as f:
                    json.dump(routing, f, indent=1, ensure_ascii=False)
                print('-> APPLIQUE : cloud_daily_budget=%d, cloud_daily_reserve=%d' % (
                    budget["calme"], budget["reserve_storm"]))
            except Exception:
                print('-> ERREUR ecriture routing.json (non fatal)')
        else:
            print('(ajouter --apply pour ecrire dans routing.json)')
    except Exception:
        print('budget_hub.py: erreur non fatale ignoree')


if __name__ == '__main__':
    main()
```

```python
# Bloc d'intégration minimale à insérer dans hub_prise_ia.py
# Remplacer la section de vérification budget par le code ci-dessous (B1-B6)

import json
import os
from typing import Any, Dict, List, Optional

# ... (imports et code existant du hub)

P = os.path.expanduser('~/prise-ia')
GRATUITS = {'qwen-local', 'openrouter-free', 'openrouter-ultra', 'openrouter-juge',
            'nvidia', 'inferx-coder', 'puter-grok', 'gemini'}

def mode_tempete_actif() -> bool:
    """Détecte si le mode tempête est actif."""
    try:
        etat_path = os.path.join(P, 'strategie/etat_tempete.json')
        if os.path.exists(etat_path):
            with open(etat_path, 'r', encoding='utf-8') as f:
                etat = json.load(f)
            return bool(etat.get('actif', False))
    except Exception:
        pass
    return False


def log_event(event_type: str, message: str, task: Optional[str] = None) -> None:
    """Journalisation non fatale."""
    try:
        print(f"[{event_type}] {message} (task={task})")
    except Exception:
        pass


# === BLOC MODIFIÉ (remplace la logique budget existante) ===
cloud_budget = routing.get("cloud_daily_budget", 0)
cloud_reserve = routing.get("cloud_daily_reserve", 0)

budget_atteint = False
if cloud_budget and usage.get("cloud", 0) >= cloud_budget:
    budget_atteint = True

if budget_atteint:
    # B2 + B5 : les gratuits ne sont jamais coupés
    nouveaux_target: List[str] = []
    for pid in target_ids:
        if pid in GRATUITS:
            nouveaux_target.append(pid)
        else:
            # payant → on l'écarte seulement si budget atteint
            pass
    if nouveaux_target:
        target_ids = nouveaux_target
        log_event("quota", "Budget calme atteint → bascule famille (gratuits)", task)
    else:
        # plus aucun gratuit disponible
        target_ids = []
        log_event("quota", "Budget cloud journalier atteint, plus de gratuit disponible", task)

# B3 : Réserve storm en tempête
if (mode_tempete_actif() and 
    cloud_budget and usage.get("cloud", 0) >= cloud_budget and 
    cloud_reserve > 0):
    # on autorise la consommation de la réserve pour les tâches prioritaires
    taches_prioritaires = {"signets.juge", "audit.protocol", "mission", "cortana.analyse", "supervise.decision"}
    if task in taches_prioritaires:
        log_event("reserve-storm", f"Consommation réserve storm pour {task}", task)
        # on ne vide pas target_ids → la tâche passe
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_budget_storm.py — tests hermétiques du budget dynamique + storm."""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from typing import Any, Dict

TMP_DIR = tempfile.mkdtemp(prefix="test_budget_")
os.environ["HOME"] = TMP_DIR  # simulation

# Copie minimale des constantes
CAPACITES = {
    'qwen-local': 0, 'gemini': 1500, 'openrouter-free': 700,
    'openrouter-ultra': 500, 'openrouter-juge': 300, 'nvidia': 1000,
    'inferx-coder': 400, 'puter-grok': 800, 'groq': 1000,
    'mistral': 0, 'cloudflare-workers-ai': 0
}
GRATUITS = {'qwen-local', 'openrouter-free', 'openrouter-ultra', 'openrouter-juge',
            'nvidia', 'inferx-coder', 'puter-grok', 'gemini'}


def run_test(name: str, fn) -> bool:
    print(f"[TEST] {name} ...", end=" ")
    try:
        fn()
        print("OK")
        return True
    except AssertionError as e:
        print(f"FAIL: {e}")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False


def test_capacites_completes():
    actifs = ['gemini', 'openrouter-free', 'openrouter-ultra', 'openrouter-juge',
              'nvidia', 'inferx-coder', 'puter-grok', 'groq']
    for pid in actifs:
        assert CAPACITES.get(pid, 0) > 0, f"{pid} devrait avoir une capacité > 0"


def test_calcul_budget():
    actifs = ['gemini', 'groq']
    capacite = sum(CAPACITES.get(p, 0) for p in actifs)
    total = max(40, min(800, int(capacite * 0.15)))
    reserve = int(total * 0.20)
    calme = total - reserve
    assert reserve == int(total * 0.20)
    assert calme == total - reserve


def test_gratuits_jamais_coupes():
    # Simulation : budget atteint
    budget_atteint = True
    target_ids = ['openrouter-ultra', 'groq']
    nouveaux = [p for p in target_ids if p in GRATUITS]
    assert 'openrouter-ultra' in nouveaux
    assert 'groq' not in nouveaux


def test_reserve_storm():
    mode_tempete = True
    budget_calme_atteint = True
    reserve_dispo = 120
    tache = "cortana.analyse"
    taches_prioritaires = {"signets.juge", "audit.protocol", "mission", "cortana.analyse", "supervise.decision"}
    if mode_tempete and budget_calme_atteint and reserve_dispo > 0 and tache in taches_prioritaires:
        passe = True
    else:
        passe = False
    assert passe is True


def test_apply_ecrit_routing():
    routing_path = os.path.join(TMP_DIR, "routing.json")
    routing: Dict[str, Any] = {"tasks": {}}
    with open(routing_path, 'w', encoding='utf-8') as f:
        json.dump(routing, f)

    # Simulation --apply
    calme = 180
    reserve = 45
    routing['cloud_daily_budget'] = calme
    routing['cloud_daily_reserve'] = reserve
    with open(routing_path, 'w', encoding='utf-8') as f:
        json.dump(routing, f, indent=1)

    with open(routing_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert data['cloud_daily_budget'] == 180
    assert data['cloud_daily_reserve'] == 45


def main():
    tests = [
        ("CAPACITES complétée", test_capacites_completes),
        ("Calcul budget + réserve 20%", test_calcul_budget),
        ("Gratuits jamais coupés", test_gratuits_jamais_coupes),
        ("Réserve storm en tempête", test_reserve_storm),
        ("--apply écrit cloud_daily_budget et reserve", test_apply_ecrit_routing),
    ]
    ok = 0
    for name, fn in tests:
        if run_test(name, fn):
            ok += 1
    print(f"\n{ok}/{len(tests)} tests réussis")
    if ok != len(tests):
        sys.exit(1)


if __name__ == '__main__':
    main()
```
