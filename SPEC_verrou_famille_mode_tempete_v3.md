# SPEC v3 — VERROU FAMILLE + MODE TEMPÊTE (INTÉGRATION DU TRIO RÉEL)

## Statut

v2 validée structurellement par la famille (verrou corrigé : le thread détient le
flock jusqu'à la fin réelle + état TTL ; chemin absolu corrigé ; tests qui importent
le module réel). **RÉSERVE 2 reste ouverte** : le trio hub est encore simulé
(`_appel_hub` factice, `build_sujet` bidon, `est_une_occasion` = True, `TASKS` faux).
La famille a exigé du code INTÉGRABLE sans placeholder.

Cette v3 fournit **le code réel exact** (copié depuis `Index_Maison/scripts/
famille_session.py` actuel) à intégrer tel quel dans le livrable. Le codeur ne doit
PAS réécrire ces fonctions : il doit les COPIER mot pour mot dans son module.

## RÈGLES ABSOLUES

1. **Python 3.9 stdlib**, pas de dépendance externe.
2. **INTERDIT** `str | None` → `typing.Optional`.
3. **NE PAS TOUCHER AU MOTEUR ACE** ni changer les formats produits.
4. **Non fatal** : aucune exception ne casse la chaîne.
5. **UTF-8.**
6. Fichiers : `Index_Maison/scripts/` + `Index_Maison/strategie/`.
7. **Code COMPLET, zéro placeholder** : les fonctions réelles ci-dessous sont COPIÉES
   telles quelles (seuls les appels au chemin `STRATEGIE_DIR` restent ceux de la v2).

---

## INTÉGRATION OBLIGATOIRE (copier tel quel depuis l'existant)

### A. Constantes réelles (à ajouter au module)

```python
import urllib.request
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple, Dict, Any

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ALARME_FRAICHEUR_H = 6
ANTI_SPAM_MIN = 5

ROLES = {
    "audit.protocol": (
        "Tu es Gemini, analyste senior de la maison ACE777. Donne un avis CONCIS "
        "(2-3 phrases max) : les risques, les angles morts, ce qu'on pourrait rater. "
        "Important : notre système tourne sur macOS (pas Windows). Réponds en français."
    ),
    "mission": (
        "Tu es DeepSeek, expert technique de la maison ACE777. Donne un avis CONCIS "
        "(2-3 phrases max) : la cohérence du setup, ce qui peut casser, la faisabilité. "
        "Important : notre système tourne sur macOS (pas Windows). Réponds en français."
    ),
    "signets.juge": (
        "Tu es le JUGE de la maison ACE777. Après avoir pesé les arguments, TRANCHE la "
        "décision de façon claire et concise (2-3 phrases max) : OUI / NON / SOUS CONDITION. "
        "Important : notre système tourne sur macOS (pas Windows). Réponds en français."
    ),
}
TASKS = ["audit.protocol", "mission", "signets.juge"]
NOMS = ["GEMINI (analyste)", "DEEPSEEK (technique)", "LE JUGE tranche"]
```

### B. Fonctions réelles (COPIER mot pour mot, seule la signature de `est_une_occasion`
et `build_sujet` reste identique à l'existant)

```python
def lire_json(path, default=None):
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        pass
    return default


def _appel_hub(task, messages, resultats, cle):
    """Appel hub pour un membre du trio (thread). timeout=None (règle maison)."""
    payload = {
        "task": task,
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 500,
    }
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            HUB, data=data,
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=None) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            resultats[cle] = res.get("choices", [{}])[0].get("message", {}).get("content", "")
    except Exception as e:
        print("famille: appel %s en echec (%s)" % (task, e), file=sys.stderr)
        resultats[cle] = None


def est_une_occasion(live, force=False):
    """Détermine si une occasion de consultation existe (déterministe)."""
    if force:
        return True, "demande explicite"

    # 1. Alerte RÉCENTE (la vigie écrit alarme.json seulement quand elle tire)
    try:
        if os.path.exists(FICHIER_ALARME):
            frais = (time.time() - os.path.getmtime(FICHIER_ALARME)) < ALARME_FRAICHEUR_H * 3600
            alarme = lire_json(FICHIER_ALARME, {})
            if frais and alarme and isinstance(alarme, dict) and alarme.get("type"):
                return True, "alerte en cours"
    except Exception:
        pass

    # 2. Session dans le rouge
    bots = (live or {}).get("bots", {})
    alpha = bots.get("alpha", {})
    if alpha.get("fills", 0) > 0 and alpha.get("pnl", 0.0) < 0:
        return True, "session dans le rouge"

    # 3. Rafale revenge
    if alpha.get("revenge", 0) >= 3:
        return True, "rafale de mode revenge"

    return False, ""


def build_sujet(live):
    """Construit le brief compact en français pour le trio."""
    bots = (live or {}).get("bots", {})
    alpha = bots.get("alpha", {})
    beta = bots.get("beta", {})
    story = (live or {}).get("story", [])

    alerte_txt = "aucune"
    try:
        a = lire_json(FICHIER_ALARME, None)
        if a:
            alerte_txt = json.dumps(a, ensure_ascii=False)[:300]
    except Exception:
        pass

    return (
        "SESSION (depuis %s) :\n"
        "• ALPHA (Le Sniper) : %s tirs, %s skips (discipline), pnl %+.2f $, "
        "dont %s revenge 1.5x\n"
        "• BETA (L'Éclaireur) : %s sondes, conf moyenne %s, %s long / %s court\n"
        "• STORY : %s\n"
        "• ALERTE : %s\n"
        "QUESTION : cette session appelle-t-elle une action ? (ajuster le setup, "
        "réduire l'exposition, laisser courir...) Réponds en français, macOS, concis."
        % (
            live.get("since", "N/A"),
            alpha.get("fills", 0), alpha.get("skips", 0), alpha.get("pnl", 0.0),
            alpha.get("revenge", 0),
            beta.get("fills", 0), beta.get("conf_moy", 0),
            beta.get("direction", {}).get("long", 0),
            beta.get("direction", {}).get("short", 0),
            " | ".join(story[-3:]) if story else "aucune",
            alerte_txt,
        )
    )
```

### C. `_thread_trio` avec le VRAI trio (remplacer la boucle simulée)

```python
def _thread_trio(lock_fd):
    """Thread qui détient le verrou flock jusqu'à la fin réelle des 3 appels."""
    resultats = {}
    try:
        live = lire_json(FICHIER_LIVE, {}) or {}
        occasion, raison = est_une_occasion(live)
        if not occasion:
            return  # pas d'occasion : on ne gaspille pas le trio
        sujet = build_sujet(live)

        threads = []
        for task in TASKS:
            t = threading.Thread(
                target=_appel_hub,
                args=(task, [{"role": "system", "content": ROLES[task]},
                             {"role": "user", "content": sujet}], resultats, task),
                daemon=True)
            threads.append(t)
            t.start()
        for t in threads:
            t.join(timeout=240)

        parties = []
        for i, task in enumerate(TASKS):
            r = resultats.get(task)
            if r:
                parties.append("• %s : %s" % (NOMS[i], r.strip()))
            else:
                parties.append("• %s : (injoignable)" % NOMS[i])

        ts = datetime.now().isoformat()
        contenu = (
            "# AVIS FAMILLE SESSION — %s\n"
            "OCCASION : %s\n\n"
            "🟡 CONSULTATION FAMILLE\n\n"
            "%s\n\n"
            "— Famille consultée, %s\n"
            % (ts, raison, "\n\n".join(parties),
               datetime.now().strftime("%d/%m/%Y %H:%M"))
        )
        contenu = contenu.replace("**", "")
        _ecrire_avis_famille(contenu)
    except Exception:
        pass
    finally:
        try:
            fcntl.flock(lock_fd, fcntl.LOCK_UN)
        except Exception:
            pass
        try:
            if os.path.exists(FICHIER_ETAT):
                os.remove(FICHIER_ETAT)
        except Exception:
            pass
```

- `FICHIER_LIVE` = `os.path.join(STRATEGIE_DIR, "journal_intention_live.json")`
  (déjà défini en v2 dans la section chemins absolus — à ajouter si absent).
- `_ecrire_avis_famille(contenu)` : écrit `contenu` dans `FICHIER_AVIS`
  (`STRATEGIE_DIR/AVIS_FAMILLE_SESSION.md`) + historique
  (`STRATEGIE_DIR/historique_famille/AVIS_<ts>.md`), sans changement de format.
- `consulter_famille()` : garde la logique v2 (état TTL au début + lock + join 90),
  mais le contenu réel du trio est celui du bloc C ci-dessus. Ne JAMAIS relâcher le
  lock dans `consulter_famille()` : il appartient au thread.

## CONTRAT DE SORTIE v3

Le fichier `famille_session.py` COMPLET et INTÉGRABLE : les sections v2 (verrou,
état TTL, mode tempête, chemins absolus, `_duree_anti_spam`) + les constantes et
fonctions réelles A/B + le `_thread_trio` réel C. Aucun placeholder, aucune
simulation, aucun `pass` dans `_appel_hub` / `build_sujet` / `est_une_occasion`.
Tests hermétiques réels (v2) conservés, adaptés si besoin aux nouvelles signatures.
