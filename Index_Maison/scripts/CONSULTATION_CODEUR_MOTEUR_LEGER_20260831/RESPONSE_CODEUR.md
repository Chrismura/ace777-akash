# CODEUR — Phase 1 moteur léger et costaud (provider Google Gemini, 5.9s)

Voici le patch complet et prêt à intégrer pour le fichier `/Users/christophe/ace777-test-day1/hulk-mexc/scripts/paper_diprip.py`. 

La logique métier reste strictement inchangée. Seules la robustesse réseau, la gestion des requêtes (batch), le drift et l'écriture atomique sont modifiés.

### Code des fonctions modifiées et ajoutées

```python
# ===== INSERT 1 : ÉCRITURE ATOMIQUE =====
def atomic_write_json(path, data):
    """Écriture atomique d'un fichier JSON via un fichier temporaire."""
    p = Path(path)
    tmp_path = p.with_suffix(p.suffix + ".tmp")
    p.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, p)
    except Exception as e:
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except Exception:
                pass
        raise e


# ===== INSERT 2 : HTTP_JSON DURCI (Timeout, backoff 429/5xx, sigalrm) =====
def http_json(url, timeout=15.0, retries=1):
    """Effectue un appel HTTP GET et retourne le JSON parsé avec backoff 429/5xx et SIGALRM."""
    def _alarm_handler(signum, frame):
        raise TimeoutError(f"HTTP GET timeout after {timeout}s: {url}")

    old_handler = signal.signal(signal.SIGALRM, _alarm_handler)
    
    for attempt in range(retries + 1):
        signal.alarm(int(math.ceil(timeout)))
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "HulkPaperBot/1.0", "Accept": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=timeout) as response:
                signal.alarm(0)
                if response.status != 200:
                    raise urllib.error.HTTPError(url, response.status, "Non-200 status", response.headers, None)
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, socket.timeout, json.JSONDecodeError) as e:
            signal.alarm(0)
            status_code = getattr(e, "code", None)
            is_rate_limit_or_server_err = status_code == 429 or (status_code and status_code >= 500) or isinstance(e, (TimeoutError, socket.timeout))
            
            if attempt < retries and is_rate_limit_or_server_err:
                sleep_time = 1.0 * (attempt + 1) # 1s puis 2s
                time.sleep(sleep_time)
                continue
            if attempt == retries:
                raise e
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)
    return None


# ===== INSERT 3 : BATCH PRIX & CACHE =====
    # (À insérer en tant que méthode dans la classe principale du bot)

    def fetch_all_prices(self):
        """Récupère tous les prix du marché en un seul appel batch."""
        cache = {}
        try:
            data = http_json("https://api.mexc.com/api/v3/ticker/price", timeout=15.0, retries=1)
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and "symbol" in item and "price" in item:
                        try:
                            cache[item["symbol"]] = float(item["price"])
                        except (ValueError, TypeError):
                            continue
        except Exception as e:
            if hasattr(self, "logger") and self.logger:
                self.logger.warning(f"fetch_all_prices batch failed: {e}")
        return cache

    def last_price(pair):
        """Lit le prix depuis le cache du cycle ou fait un fallback unitaire ciblé."""
        # Si le cache de classe existe et contient la paire
        if hasattr(self, "price_cache") and isinstance(self.price_cache, dict) and pair in self.price_cache:
            return self.price_cache[pair]
        
        # Fallback unitaire ciblé en cas d'absence dans le cache ou échec batch
        try:
            q = urllib.parse.urlencode({"symbol": pair})
            j = http_json(f"https://api.mexc.com/api/v3/ticker/price?{q}", timeout=10.0, retries=1)
            p = float(j["price"])
            if hasattr(self, "price_cache") and isinstance(self.price_cache, dict):
                self.price_cache[pair] = p
            return p
        except Exception as e:
            # Dernier recours : si on a un ancien prix dans self, le conserver sinon propager
            if hasattr(self, "last_known_prices") and pair in self.last_known_prices:
                return self.last_known_prices[pair]
            raise e


# ===== INSERT 4 : MISE À JOUR DE LA BOUCLE RUN() (Anti-drift & Batch par cycle) =====
    # (Extrait de la boucle while dans def run(self):)

    def run(self):
        # Initialisation de l'attribut de cache des prix
        self.price_cache = {}
        if not hasattr(self, "last_known_prices"):
            self.last_known_prices = {}

        while self.running:
            loop_start = time.time()
            try:
                # 1. UN SEUL APPEL BATCH PAR CYCLE
                self.price_cache = self.fetch_all_prices()
                # Sauvegarde pour persistance en cas de panne réseau au tour suivant
                for k, v in self.price_cache.items():
                    self.last_known_prices[k] = v

                # 2. Exécution des ticks paires habituels (qui lisent self.price_cache)
                for pair in self.pairs:
                    self.tick_pair(pair)

                # ... (conserver le reste de la logique de fin de boucle existante : manage, etc.)

            except Exception as e:
                if hasattr(self, "logger") and self.logger:
                    self.logger.error(f"Erreur dans la boucle principale run(): {e}")

            # 3. ANTI-DRIFT DE BOUCLE
            elapsed = time.time() - loop_start
            sleep_time = max(0.0, self.poll - elapsed)
            time.sleep(sleep_time)
```

---

### NOTE D'INTÉGRATION (Max 5 lignes)
1. Remplacer `http_json` et ajouter `atomic_write_json` au niveau global.
2. Ajouter `fetch_all_prices` et modifier `last_price` dans la classe du bot.
3. Remplacer le contenu du `while` de `run()` pour charger `self.price_cache` au début et appliquer le calcul anti-drift (`max(0, poll - elapsed)`).
4. Remplacer les sauvegardes d'état critiques (ex: `save_state`) par `atomic_write_json(path, data)`.
5. **Test avant redémarrage** : Lancer un dry-run manuel pour vérifier que `self.price_cache` se peuple bien en 1 unique requête et que le bot ne dépasse plus ~10 req/min.
