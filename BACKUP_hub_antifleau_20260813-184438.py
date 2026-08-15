#!/usr/bin/env python3
"""Prise IA — Hub leger local (compatible API OpenAI)
Bascule automatique entre fournisseurs (Qwen locale, Gemini, OpenRouter...)
Zero dependance : stdlib Python uniquement. Port par defaut : 11435
"""
import json, os, sys, threading, time, socket, subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib import request as urllib_request, error as urllib_error
from datetime import datetime, timezone

# == BLACKLIST BACKOFF PROGRESSIF (patch 13/08, spec Christophe) ==
# Un fournisseur qui ECHOUE 3 fois de suite (timeout PATIENCE / quota) est mis en
# pause temporaire (backoff x2 : 15min, 30min, 1h, ... plafond 4h) puis RE-ESSAYE
# automatiquement. S'il revient sain, il reprend sa place — on ne le punit plus
# jusqu'a minuit. Exemple : Gemini down pendant une coupure redevient actif
# des que l'API repond, au lieu d'attendre le changement de jour.
_fails = {}       # {provider_id: compteur d'echecs consecutifs}
_blacklist = {}   # {provider_id: {'until': timestamp_unix, 'level': n}}
_blacklock = threading.Lock()  # thread-safe (hub = ThreadingHTTPServer) — reserve audit tiers 09/08
_loglock = threading.Lock()   # ecritures logs/usage thread-safe (audit famille 6, 13/08)
_health_cache = {"ts": 0, "data": None}  # cache /health 30s (audit famille 6)

# == ANTI-FLEAU TIMEOUT DEBUT DE SESSION (spec 13/08, Christophe) ==
# Au boot, le hub demarre avant que le reseau soit pret : les appels echouent en DNS
# (Errno 8) et la PATIENCE x3 les transformait en attente de 12-80 min, avec faux
# blacklist des providers sains. Corrections : ReseauIndisponible (bascule immediate,
# pas de blacklist) + budget temps global par requete (REQUEST_MAX_SECONDS).
class ReseauIndisponible(Exception):
    """Erreur de connectivite reseau (DNS, connexion refusee). PAS une panne provider."""
    pass

REQUEST_MAX_SECONDS = 180  # budget temps global par requete (surchargeable routing.json)
                          # 180s : un LLM lourd legitime (DeepSeek 129s) doit tenir, mais
                          # jamais les 12-80 min du fleau. GROK/ULTRA/INFERX (audit 13/08).

# Hote de reference pour le test DNS rapide (_reseau_disponible)
RESEAU_REFERENCE_HOST = "api.openai.com"
# Cache du check reseau (audit famille 13/08 : eviter un test DNS par requete au boot)
_reseau_cache = {"ts": 0, "ok": True}
RESEAU_CACHE_TTL = 15  # secondes

ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT, "providers.json")
EVENTS_PATH = os.path.join(ROOT, "hub_events.jsonl")
ROUTING_PATH = os.path.join(ROOT, "routing.json")
USAGE_PATH = os.path.join(ROOT, "usage.jsonl")
ENV_PATH = os.path.join(ROOT, ".env")
HOST, PORT = "127.0.0.1", 11435


def load_env(path):
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


load_env(ENV_PATH)


def load_config():
    """Charge providers.json. Non fatal : fichier corrompu -> [] + log (audit famille 6)."""
    try:
        with open(CONFIG_PATH, encoding="utf-8") as f:
            data = json.load(f)
        providers = []
        for p in data.get("providers", []):
            if not p.get("enabled", True):
                continue
            key = p.get("api_key_env")
            api_key = os.environ.get(key, "") if key else p.get("api_key", "")
            providers.append({**p, "api_key": api_key})
        providers.sort(key=lambda x: x.get("order", 99))
        return providers
    except Exception as e:
        log_event("error", "providers.json corrompu ou illisible", str(e)[:200])
        return []


def log_event(kind, title, detail=""):
    ev = {"ts": datetime.now(timezone.utc).isoformat(), "kind": kind, "title": title, "detail": detail}
    try:
        with _loglock:
            with open(EVENTS_PATH, "a", encoding="utf-8") as f:
                f.write(json.dumps(ev, ensure_ascii=False) + "\n")
    except Exception:
        pass
    return ev


def load_routing():
    if not os.path.exists(ROUTING_PATH):
        return {}
    try:
        with open(ROUTING_PATH) as f:
            return json.load(f)
    except Exception:
        return {}


def usage_today():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    counts = {}
    if os.path.exists(USAGE_PATH):
        with open(USAGE_PATH) as f:
            for line in f:
                try:
                    ev = json.loads(line)
                except Exception:
                    continue
                if ev.get("ts", "")[:10] == today:
                    k = ev.get("kind", "?")
                    counts[k] = counts.get(k, 0) + 1
    return counts


def log_usage(task, provider, model, kind, duration=None):
    ev = {"ts": datetime.now(timezone.utc).isoformat(), "task": task, "provider": provider, "model": model, "kind": kind}
    if duration is not None:
        ev["duration_s"] = round(duration, 2)
    try:
        with _loglock:
            with open(USAGE_PATH, "a", encoding="utf-8") as f:
                f.write(json.dumps(ev, ensure_ascii=False) + "\n")
    except Exception:
        pass


NON_RETRYABLE_HTTP = {401, 402, 403, 404}   # cle / credits / modele -> fallback immediat (correct)


def _raw_call(prov, messages, temperature, max_tokens, timeout):
    base = prov["base_url"].rstrip("/")
    # Patch 09/08 : les modeles Qwen3.5 locaux (Ollama) sont des reasoning models :
    # /v1/chat/completions leur laisse consommer tout le budget en "thinking" et
    # renvoie content vide -> le hub basculait a tort sur Gemini (fallback).
    # Solution : API native /api/chat + think:false = reponse directe (teste 09/08).
    if ":11434" in base:
        url = base.replace("/v1", "") + "/api/chat"
        body = json.dumps({
            "model": prov["model"],
            "messages": messages,
            "stream": False,
            "think": False,
            "options": {"temperature": temperature, "num_predict": max_tokens},
        }).encode()
    else:
        url = base + "/chat/completions"
        body = json.dumps({
            "model": prov["model"],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }).encode()
    headers = {"Content-Type": "application/json"}
    if prov.get("api_key"):
        headers["Authorization"] = "Bearer " + prov["api_key"]
    req = urllib_request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib_request.urlopen(req, timeout=timeout) as resp:
            if getattr(resp, "status", 200) != 200:
                raise RuntimeError("HTTP status " + str(getattr(resp, "status", "?")))
            raw = resp.read().decode("utf-8")
            data = json.loads(raw)
    except (socket.gaierror, ConnectionError) as e:
        # ANTI-FLEAU (13/08) : DNS KO (Errno 8) ou connexion impossible = panne RESEAU,
        # pas une panne provider. Bascule immediate, pas de blacklist (C1 spec).
        raise ReseauIndisponible(str(e)[:150]) from e
    except urllib_error.URLError as e:
        reason = getattr(e, "reason", None)
        if isinstance(reason, socket.gaierror) or isinstance(reason, ConnectionError):
            # URLerror qui enveloppe une erreur DNS/connexion (souvent le cas) :
            # meme traitement reseau (C1 spec)
            raise ReseauIndisponible(str(reason)[:150]) from e
        raise
    if ":11434" in base:
        content = data.get("message", {}).get("content", "")
    else:
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
    if not content or not content.strip():
        raise RuntimeError("Reponse vide")
    return content


class BlacklistedProvider(Exception):
    """Levee quand un fournisseur est blackliste pour la journee (patch 09/08)."""
    def __init__(self, provider_name):
        super().__init__("Fournisseur %s blackliste pour aujourd'hui" % provider_name)
        self.provider_name = provider_name


def _gratuits_actifs():
    """Liste DYNAMIQUE des providers gratuits (free: true) depuis providers.json.
    Aucune valeur figée dans le code : la rotation choisit le meilleur gratuit au
    moment T (décision Christophe 13/08 : "gratuit jamais coupé, on change
    immédiatement si un autre est meilleur/plus rapide")."""
    gratuits = set()
    try:
        for p in load_config():
            if p.get("free"):
                gratuits.add(p.get("id"))
    except Exception:
        pass
    return gratuits


def _get_strat_path() -> str:
    """Chemin du dossier strategie (détection tempête). Dérivé de ROOT avec
    repli sur le chemin historique (audit famille 6 : plus de chemin en dur)."""
    candidats = [
        os.path.join(ROOT, "..", "Index_Maison", "strategie"),
        os.path.expanduser("~/ace777-test-day1/Index_Maison/strategie"),
    ]
    for c in candidats:
        if os.path.exists(c):
            return c
    return candidats[-1]


def _mode_tempete_actif():
    """Détecte le mode tempête (machine de tempête) : zone ADA ROUGE/
    PRENDS_LA_PERTE, alarme récente, vortex >= 2, ou fichier etat_tempete.
    En tempête on s'arrange au mieux : aucune coupure pour les tâches
    prioritaires."""
    try:
        strat = _get_strat_path()
        g = None
        try:
            with open(os.path.join(strat, "ada_gardienne_live.json"), encoding="utf-8") as f:
                g = json.load(f)
        except Exception:
            pass
        if g and isinstance(g, dict):
            zone = str(g.get("zone", "")).upper()
            if zone in ("ROUGE", "PRENDS_LA_PERTE"):
                return True
        try:
            alarme_path = os.path.join(strat, "alarme.json")
            if os.path.exists(alarme_path) and (time.time() - os.path.getmtime(alarme_path)) < 3600:
                with open(alarme_path, encoding="utf-8") as f:
                    a = json.load(f)
                if isinstance(a, dict) and a.get("type"):
                    return True
        except Exception:
            pass
        try:
            saison_path = os.path.join(strat, "ada_saison_live.json")
            with open(saison_path, encoding="utf-8") as f:
                saison = json.load(f)
            if int(saison.get("vortex", {}).get("force", 0) or 0) >= 2:
                return True
        except Exception:
            pass
        try:
            etat_path = os.path.join(strat, "etat_tempete.json")
            if os.path.exists(etat_path):
                with open(etat_path, encoding="utf-8") as f:
                    etat = json.load(f)
                if etat.get("actif"):
                    return True
        except Exception:
            pass
    except Exception:
        pass
    return False


def _is_blacklisted(prov):
    """True si le provider est en pause (backoff). Expire automatiquement."""
    prov_id = prov.get("id")
    if not prov_id:
        return False
    with _blacklock:
        b = _blacklist.get(prov_id)
        if not b:
            return False
        if time.time() >= b.get("until", 0):
            del _blacklist[prov_id]  # pause terminee : re-essai autorise
            _fails[prov_id] = 0
            log_event("blacklist", "Fin de pause " + prov.get("name", prov_id), "re-essai automatique")
            return False
        return True


def _backoff_duree(level: int) -> int:
    """Pause en secondes : 15 min, 30 min, 1h, 2h, plafond 4h."""
    duree = 15 * 60 * (2 ** max(0, level - 1))
    return min(duree, 4 * 3600)


def _register_result(prov, ok):
    """Comptabilise succes/echec. 3 echecs consecutifs -> pause backoff (re-essai auto)."""
    prov_id = prov.get("id")
    if not prov_id:
        return
    with _blacklock:
        if ok:
            _fails[prov_id] = 0
            return
        _fails[prov_id] = _fails.get(prov_id, 0) + 1
        if _fails[prov_id] >= 3:
            level = _blacklist.get(prov_id, {}).get("level", 0) + 1 if _blacklist.get(prov_id) else 1
            duree = _backoff_duree(level)
            _blacklist[prov_id] = {"until": time.time() + duree, "level": level}
            _fails[prov_id] = 0
            log_event("blacklist", "Pause " + prov.get("name", prov_id) + " (3 echecs) %dmin" % (duree // 60), "backoff x%d -> re-essai auto" % level)


def call_provider(prov, messages, temperature, max_tokens, timeout_budget=None):
    """PATIENCE (fix definitif 09/08) : un fournisseur LENT mais vivant n'est PAS un echec.
    Retry 1x avec timeout x3 (plafonne a 600s) avant de laisser jouer le fallback.
    Erreurs deterministes (401/402/403/404) -> fallback immediat, sans retry inutile.
    Historique : l'appel d'audit DeepSeek V4 (129s) basculait a tort sur Gemini (timeout 120s).
    ANTI-FLEAU (13/08) : ReseauIndisponible (DNS/connexion) -> echec immediat SANS retry
    ni blacklist (C1 spec timeout debut de session). timeout_budget borne le timeout
    (C2 budget temps global par requete)."""
    if _is_blacklisted(prov):
        raise BlacklistedProvider(prov.get("name", prov.get("id", "inconnu")))
    base = prov.get("timeout", 600)
    if timeout_budget is not None:
        base = min(base, max(1, int(timeout_budget)))
    try:
        content = _raw_call(prov, messages, temperature, max_tokens, base)
        _register_result(prov, True)
        return content
    except ReseauIndisponible as e:
        # C1 spec : panne RESEAU (DNS/connexion) -> bascule immediate, on ne punit pas
        # le provider (c'est le reseau qui est down, pas lui). Pas de _register_result(False).
        log_event("network", "Reseau indisponible: " + prov["name"], str(e)[:150])
        raise
    except urllib_error.HTTPError as e:
        if e.code in NON_RETRYABLE_HTTP:
            _register_result(prov, False)
            raise  # deterministe : cle, credits, modele inconnu
        log_event("timeout", "Patience " + prov["name"] + " (HTTP " + str(e.code) + ")", str(e)[:150])
        time.sleep(3)
        try:
            content = _raw_call(prov, messages, temperature, max_tokens, min(base * 3, 900))
            _register_result(prov, True)
            return content
        except Exception as e2:
            _register_result(prov, False)
            raise
    except (TimeoutError, socket.timeout, ConnectionError, urllib_error.URLError) as e:
        log_event("timeout", "Patience " + prov["name"] + " (lenteur)", str(e)[:150])
        time.sleep(2)
        try:
            content = _raw_call(prov, messages, temperature, max_tokens, min(base * 3, 900))
            _register_result(prov, True)
            return content
        except Exception as e2:
            _register_result(prov, False)
            raise
    except RuntimeError as e:
        if "Reponse vide" in str(e):
            log_event("timeout", "Patience " + prov["name"] + " (reponse vide)", str(e)[:150])
            time.sleep(2)
            try:
                content = _raw_call(prov, messages, temperature, max_tokens, min(base * 3, 900))
                _register_result(prov, True)
                return content
            except Exception as e2:
                _register_result(prov, False)
                raise
        _register_result(prov, False)
        raise


ARCHI_VIVANTE = os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/strategie/ARCHITECTURE_VIVANTE.md")
ARCHI_SCRIPT = os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/scripts/archi_vivante.py")
ARCHI_MAX_AGE = 120  # secondes : le doc se régénère au plus 1×/2 min
_TASKS_CONTEXTE = ("famille", "audit", "juge", "strategie", "signets", "protocole")


def _regenerer_contexte_vivant():
    """Régénère le doc vivant s'il est trop vieux (jamais figé). Non bloquant :
    échec = on garde l'ancien doc ou on continue sans contexte."""
    try:
        if os.path.exists(ARCHI_VIVANTE):
            age = time.time() - os.path.getmtime(ARCHI_VIVANTE)
            if age < ARCHI_MAX_AGE:
                return True
        subprocess.run([sys.executable, ARCHI_SCRIPT],
                       capture_output=True, timeout=20)
        return os.path.exists(ARCHI_VIVANTE)
    except Exception:
        return os.path.exists(ARCHI_VIVANTE)


def _injecter_contexte_vivant(task, messages):
    """Ajoute l'état vivant d'ACE777 (régénéré au besoin) aux prompts de
    décision — la famille valide avec la vraie photo du moment, pas un doc
    figé. Non bloquant : si le doc est absent, on continue sans contexte."""
    if not task or not any(k in task for k in _TASKS_CONTEXTE):
        return messages
    if not _regenerer_contexte_vivant():
        return messages
    try:
        with open(ARCHI_VIVANTE, "r", encoding="utf-8") as f:
            ctx = f.read()[:6000]
        system = (
            "CONTEXTE VIVANT ACE777 (généré automatiquement à l'instant) — "
            "fie-toi à CES données pour valider, elles reflètent l'état réel :\n\n"
            + ctx
        )
        if messages and messages[0].get("role") == "system":
            # Fusionner au lieu d'empiler deux messages système
            messages = list(messages)
            precedent = messages[0].get("content", "")
            messages[0] = {"role": "system",
                           "content": precedent + "\n\n" + system}
            return messages
        return [{"role": "system", "content": system}] + messages
    except Exception:
        return messages


def _reseau_disponible():
    """Test DNS rapide (C3 spec anti-fleau) : au boot, le reseau n'est pas encore
    pret -> le hub doit repondre vite en mode degrade au lieu de faire 80 min de
    PATIENCE. Non bloquant : echec = False, on tente quand meme mais timeout court.
    CACHE TTL 15s (audit famille 13/08, 4 membres convergents) : on ne sonde pas le
    DNS a chaque requete quand une rafale arrive au boot."""
    now = time.time()
    if now - _reseau_cache["ts"] < RESEAU_CACHE_TTL:
        return _reseau_cache["ok"]
    try:
        socket.getaddrinfo(RESEAU_REFERENCE_HOST, 443, socket.AF_INET, socket.SOCK_STREAM)
        ok = True
    except Exception:
        ok = False
    _reseau_cache["ts"] = now
    _reseau_cache["ok"] = ok
    return ok


def chat_completions(payload):
    providers = load_config()
    messages = payload.get("messages", [])
    temperature = payload.get("temperature", 0.7)
    max_tokens = payload.get("max_tokens", 2048)
    task = payload.get("task")
    only_model = payload.get("model")

    # C2 spec anti-fleau : budget temps global demarre AVANT l'injection de contexte
    # (qui peut prendre jusqu'a 20s via subprocess) — le budget couvre TOUTE la requete.
    t0 = time.time()
    max_seconds = REQUEST_MAX_SECONDS
    try:
        routing_cfg = load_routing() or {}
        max_seconds = int(routing_cfg.get("request_max_seconds", REQUEST_MAX_SECONDS))
    except Exception:
        pass
    reseau_ok = _reseau_disponible()
    if not reseau_ok:
        log_event("network", "Reseau pas pret — mode degrade (timeout court)", "")

    messages = _injecter_contexte_vivant(task, messages)

    routing = load_routing()
    usage = usage_today()
    cloud_budget = routing.get("cloud_daily_budget")

    # 1) Ordre cible : tâche routée -> [pref, fallback, secondary] ; sinon model= ; sinon tous
    #    (secondary = 3e niveau, chaine complementaire par specialite — spec 13/08)
    target_ids = []
    if task and task in routing.get("tasks", {}):
        rule = routing["tasks"][task]
        target_ids = [i for i in (rule.get("provider"), rule.get("fallback"), rule.get("secondary")) if i]
        # Routage par complexite (inspire LLMRouter — @tom_doerr) : simple -> local, complexe -> cloud
        if rule.get("route_by_complexity") and (not only_model or only_model == "auto"):
            user_text = " ".join(str(m.get("content", "")) for m in messages if m.get("role") == "user")
            length = len(user_text)
            threshold = rule.get("complexity_threshold", 600)
            try:
                threshold = int(threshold)
            except (TypeError, ValueError):
                threshold = 600
            local_ids = [p.get("id") for p in providers if p.get("kind") == "local"]
            cloud_ids = [p.get("id") for p in providers if p.get("kind") == "cloud"]
            cloud_ok = not (cloud_budget and usage.get("cloud", 0) >= cloud_budget)
            if length < threshold:
                target_ids = [i for i in local_ids if i in target_ids] + [i for i in target_ids if i not in local_ids]
                log_event("routing", "Complexite: SIMPLE (" + str(length) + " car.) -> local", task)
            elif cloud_ok:
                target_ids = [i for i in cloud_ids if i in target_ids] + [i for i in target_ids if i not in cloud_ids]
                log_event("routing", "Complexite: COMPLEXE (" + str(length) + " car.) -> cloud", task)
            else:
                log_event("routing", "Complexite: COMPLEXE (" + str(length) + " car.) mais budget cloud atteint -> local", task)
        # Budget calme atteint : les gratuits ne sont JAMAIS coupés (bascule même
        # famille, décision 13/08). Les payants sont écartés. En tempête, aucune
        # coupure pour les tâches prioritaires (réserve storm).
        gratuits = _gratuits_actifs()
        if cloud_budget and usage.get("cloud", 0) >= cloud_budget:
            en_tempete = _mode_tempete_actif()
            taches_prio = set(routing.get("priority_tasks", [
                "signets.juge", "audit.protocol", "mission", "cortana.analyse", "supervise.decision"
            ]))
            if en_tempete and task in taches_prio:
                log_event("reserve-storm", "Tempête active + budget calme atteint -> réserve storm pour " + str(task), task)
                # target_ids reste intact : on s'arrange au mieux en tempête
            else:
                gardes = [pid for pid in target_ids if pid in gratuits]
                if gardes:
                    target_ids = gardes
                    log_event("quota", "Budget calme atteint -> bascule famille (gratuits)", task)
                else:
                    # C2 - Coupure reelle ou bascule sur TOUS les gratuits du systeme
                    # (audit famille 6 : l'ancien code faisait une copie no-op)
                    tous_gratuits = [p for p in providers if p.get("id") in gratuits]
                    if tous_gratuits:
                        target_ids = [p["id"] for p in tous_gratuits]
                        log_event("quota", "Budget calme atteint -> bascule famille (tous gratuits)", task)
                    else:
                        target_ids = []
                        log_event("quota", "Budget calme atteint, aucun gratuit dispo -> coupure reelle", task)
    elif only_model and only_model not in ("", "auto"):
        target_ids = [only_model]
        # Patch local (Ada 08/08) : un modele seul herite du fallback defini dans routing.tasks
        # (ex. model=nvidia -> nvidia puis gemini via la regle de analyse.profonde)
        for rule in routing.get("tasks", {}).values():
            if rule.get("provider") == only_model and rule.get("fallback"):
                if rule["fallback"] not in target_ids:
                    target_ids.append(rule["fallback"])

    if target_ids:
        ordered = []
        for tid in target_ids:
            for p in providers:
                if (p.get("id") == tid or p.get("model") == tid) and p not in ordered:
                    ordered.append(p)
        providers = ordered
    if not providers:
        raise RuntimeError("Aucun fournisseur branche")

    attempts, last_err, tried = [], "", 0
    # Circuit-breaker reseau (audit famille 13/08, JUGE+ULTRA) : en mode degrade
    # (reseau KO au check), un echec reseau = tout va echouer -> arret immediat
    # au lieu d'epuiser la boucle. En mode normal, une erreur DNS ponctuelle
    # continue vers le provider suivant (le reseau peut revenir entre deux).
    reseau_ko_confirme = False
    for prov in providers:
        if _is_blacklisted(prov):
            attempts.append(prov.get("name", "?") + ": blacklist du jour (saute)")
            log_event("failover", "Saute (blacklist) depuis " + prov.get("name", "?"), "0 attente")
            continue
        tried += 1
        budget_restant = max_seconds - (time.time() - t0)
        if budget_restant <= 0:
            last_err = "Budget temps requete depasse"
            attempts.append("budget: " + last_err)
            log_event("error", "Budget temps requete depasse", "")
            break
        try:
            _t0 = time.time()
            # C2/C3 spec anti-fleau : timeout borne par le budget restant, et
            # encore plus court en mode degrade (reseau pas pret au boot).
            # Plancher 5s (INFERX audit 13/08) : on ne coupe pas une reponse
            # valide a 12s sous budget restant minuscule.
            timeout_eff = budget_restant
            if not reseau_ok:
                timeout_eff = min(timeout_eff, 15)
            timeout_eff = max(5, int(timeout_eff))
            content = call_provider(prov, messages, temperature, max_tokens, timeout_budget=timeout_eff)
            log_event("message", "« " + prov["name"] + " » a repondu", "bascule" if attempts else "")
            log_usage(task or only_model or "auto", prov.get("id", "?"), prov.get("model", "?"), prov.get("kind", "?"), duration=time.time() - _t0)
            return {"content": content, "provider": prov["name"], "attempts": attempts}
        except ReseauIndisponible as e:
            # C1 spec : panne reseau -> bascule IMMEDIATE, pas de PATIENCE
            last_err = str(e)[:300]
            attempts.append(prov["name"] + ": reseau KO " + last_err)
            log_event("failover", "Reseau KO (bascule immediate) depuis " + prov["name"], last_err)
            if not reseau_ok:
                reseau_ko_confirme = True
                break  # circuit-breaker : mode degrade + 1er echec reseau = tout KO
            continue
        except Exception as e:
            last_err = str(e)[:300]
            attempts.append(prov["name"] + ": " + last_err)
            log_event("failover", "Bascule depuis " + prov["name"], last_err)
    # Filet de securite (reserve audit 09/08) : si TOUS les providers etaient blacklistes
    # (tried == 0), on force UNE derniere tentative sans blacklist pour ne jamais planter
    # silencieusement en cas de panne generale.
    # C1 - Filet de dernier recours : on contourne volontairement le blacklist
    # (but du mecanisme, audit famille 6). On appelle _raw_call directement
    # car call_provider commencerait par _is_blacklisted -> levee immediate.
    if tried == 0 and providers:
        log_event("failover", "Tous blacklistes - tentative de dernier recours sans blacklist", "")
        for prov in providers:
            budget_restant = max_seconds - (time.time() - t0)
            if budget_restant <= 0:
                last_err = "Budget temps requete depasse (dernier recours)"
                attempts.append("budget: " + last_err)
                break
            try:
                _t0 = time.time()
                timeout_eff = budget_restant
                if not reseau_ok:
                    timeout_eff = min(timeout_eff, 15)
                timeout_eff = max(5, int(timeout_eff))
                content = _raw_call(prov, messages, temperature, max_tokens, timeout_eff)
                _register_result(prov, True)
                log_event("message", "« " + prov["name"] + " » a repondu (dernier recours)", "")
                log_usage(task or only_model or "auto", prov.get("id", "?"), prov.get("model", "?"), prov.get("kind", "?"), duration=time.time() - _t0)
                return {"content": content, "provider": prov["name"], "attempts": attempts}
            except ReseauIndisponible as e:
                # Meme en dernier recours : reseau down -> on ne fait pas 80 min de PATIENCE
                last_err = str(e)[:300]
                attempts.append(prov["name"] + ": reseau KO " + last_err)
                log_event("failover", "Reseau KO (dernier recours) depuis " + prov["name"], last_err)
            except Exception as e:
                last_err = str(e)[:300]
                attempts.append(prov["name"] + ": " + last_err)
                log_event("failover", "Bascule depuis " + prov["name"], last_err)
    log_event("error", "Toutes les IA ont echoue", " | ".join(attempts)[:500])
    raise RuntimeError("Toutes les IA branchees ont echoue. Derniere erreur : " + last_err)


class Handler(BaseHTTPRequestHandler):
    def _json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass  # client deconnecte (audit famille 6)

    def _read_body(self):
        # C4 - limite de taille + JSON invalide propre (audit famille 6)
        try:
            length = int(self.headers.get("Content-Length", 0))
        except (TypeError, ValueError):
            length = 0
        if length > 10 * 1024 * 1024:  # 10 Mo max
            raise ValueError("Payload trop volumineux")
        raw = self.rfile.read(length).decode("utf-8") if length else "{}"
        try:
            return json.loads(raw or "{}")
        except json.JSONDecodeError:
            raise ValueError("JSON invalide")

    def do_GET(self):
        if self.path == "/health":
            # C4 - cache 30s (audit famille 6 : load_config relu a chaque appel)
            now = time.time()
            if now - _health_cache["ts"] > 30 or _health_cache["data"] is None:
                _health_cache["data"] = {"status": "ok", "providers": len(load_config())}
                _health_cache["ts"] = now
            self._json(200, _health_cache["data"])
        elif self.path == "/v1/models":
            self._json(200, {"object": "list", "data": [
                {"id": p["model"], "name": p["name"], "kind": p.get("kind")}
                for p in load_config()
            ]})
        elif self.path == "/events":
            events = []
            if os.path.exists(EVENTS_PATH):
                with open(EVENTS_PATH) as f:
                    for line in f.readlines()[-25:]:
                        try:
                            events.append(json.loads(line))
                        except Exception:
                            pass
            self._json(200, {"events": events})
        elif self.path == "/usage":
            rows = []
            if os.path.exists(USAGE_PATH):
                with open(USAGE_PATH) as f:
                    for line in f.readlines()[-50:]:
                        try:
                            rows.append(json.loads(line))
                        except Exception:
                            pass
            self._json(200, {"usage": rows, "today": usage_today()})
        elif self.path == "/routing":
            self._json(200, {"routing": load_routing(), "today": usage_today()})
        else:
            self._json(404, {"error": "not found"})

    def do_POST(self):
        if self.path == "/v1/chat/completions":
            try:
                payload = self._read_body()
            except ValueError as e:
                self._json(400, {"error": {"message": str(e)}})
                return
            try:
                result = chat_completions(payload)
                self._json(200, {
                    "id": "chatcmpl-priseia",
                    "object": "chat.completion",
                    "choices": [{"index": 0, "message": {"role": "assistant", "content": result["content"]}, "finish_reason": "stop"}],
                    "provider": result["provider"],
                    "attempts": result["attempts"],
                })
            except Exception as e:
                self._json(502, {"error": {"message": str(e)}})
        else:
            self._json(404, {"error": "not found"})

    def log_message(self, format, *args):
        # C5 - logue les erreurs 4xx/5xx (audit famille 6)
        try:
            msg = (format % args) if args else format
            if any(c in msg for c in ("4", "5")) and " 2" not in msg[:6]:
                log_event("http", "requete HTTP: " + msg, "")
        except Exception:
            pass


if __name__ == "__main__":
    print("⚡ Prise IA — hub leger sur http://" + HOST + ":" + str(PORT))
    print("   POST /v1/chat/completions · GET /v1/models · GET /events · GET /routing · GET /usage · GET /health")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
