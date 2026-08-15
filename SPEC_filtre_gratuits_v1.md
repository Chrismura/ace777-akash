# SPEC — CORRECTION FILTRE GRATUITS (audit famille 6, 13/08)

## Contexte

L'audit famille 6 cerveaux des setups du jour a fait ressortir UN point convergent
(3 membres : DEEPSEEK, ULTRA, GROK) et confirmé par vérification superviseur du code
réel : **le filtre d'activation des providers gratuits est défectueux** dans
`budget_hub.py` et `prechauffage_reserve.py`.

## Le bug (vérifié en réel)

```python
# budget_hub.py — gratuits_actifs()
if p.get('free') is True and (p.get('enabled') or p.get('kind') == 'local'):
```
- `gemini` n'a **pas** de champ `enabled` dans providers.json (`enabled: None`) →
  `p.get('enabled')` est falsy → et `kind == 'cloud'` → **gemini est EXCLU** des
  gratuits. Or gemini est le provider gratuit principal !
- `qwen-local` est `enabled: false`, `kind: local` → inclus à tort (il est en PAUSE).

```python
# prechauffage_reserve.py — verifier_c2()
if p.get("free") is True and (p.get("enabled") is True or p.get("name") in str(data)):
```
- `p.get("name") in str(data)` est un hack : toujours vrai pour tout provider présent
  dans le fichier → inclut qwen-local (pause) et masque les vrais désactivés.

## La règle (principe Christophe : « valeur fixe → on coule »)

Un provider est **gratuit ACTIF** si et seulement si :
1. `free is True` (dans providers.json)
2. **et** `enabled` n'est pas explicitement `false` (défaut : actif si absent)

La notion de `kind` (local/cloud) ne doit PAS intervenir : un gratuit cloud est un
gratuit. Un provider en pause (`enabled: false`) n'est JAMAIS compté, quel que soit
son kind.

## Corrections demandées (2 fichiers)

### 1. `budget_hub.py` — `gratuits_actifs()`
```python
def gratuits_actifs() -> List[str]:
    prov_path = os.path.join(P, 'providers.json')
    if not os.path.exists(prov_path):
        return []
    try:
        with open(prov_path, 'r', encoding='utf-8') as f:
            prov = json.load(f)
        gratuits: List[str] = []
        for p in prov.get('providers', []):
            # Gratuit ACTIF : free:true ET enabled pas explicitement false
            # (défaut actif si champ absent — gemini n'a pas de champ enabled)
            if p.get('free') is True and p.get('enabled') is not False:
                gratuits.append(p.get('id'))
        return gratuits
    except Exception:
        return []
```

### 2. `prechauffage_reserve.py` — `verifier_c2()`
Même logique :
```python
    for p in providers:
        if p.get("free") is True and p.get("enabled") is not False:
            gratuits += 1
```
(retirer le `p.get("name") in str(data)` et la condition `kind`)

## Vérification attendue (résultat réel)

Avec le providers.json actuel, les gratuits actifs doivent être :
`gemini, openrouter-free, nvidia, openrouter-juge, openrouter-ultra, inferx-coder, puter-grok`
(8 en comptant… vérifier : qwen-local EXCLU, groq/inferx/mistral/cloudflare EXCLUS
car enabled:false ou free:false — la liste exacte dépend des valeurs actuelles).

## Règles
- Python 3.9 stdlib, non fatal, commentaires français.
- Ne rien changer d'autre dans les 2 fichiers.
- Contrat de sortie : les 2 fonctions corrigées, prêtes à copier-coller.
