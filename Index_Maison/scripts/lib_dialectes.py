import urllib.request
import urllib.parse
import json
import time
import sys

def to_int(value, base="auto"):
    """
    Convertit une valeur en entier en gérant le décimal et l'hexadécimal.
    Règle absolue : une chaîne sans préfixe 0x est STRICTEMENT décimale.
    """
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if not isinstance(value, str):
        raise TypeError(f"Type non supporté pour to_int: {type(value)}")
    
    val_str = value.strip()
    if not val_str:
        raise ValueError("Chaîne vide pour to_int")

    if base == "auto":
        if val_str.lower().startswith("0x"):
            return int(val_str, 16)
        else:
            return int(val_str, 10)
    elif base == 16:
        if val_str.lower().startswith("0x"):
            return int(val_str, 16)
        return int(val_str, 16)
    elif base == 10:
        return int(val_str, 10)
    else:
        raise ValueError(f"Base non supportée: {base}")

def to_ms(ts):
    """
    Détecte si un timestamp est en secondes ou millisecondes.
    Seuil : 10^11 (environ l'année 5138 en secondes, ou fin 1973 en millisecondes).
    Renvoie toujours des millisecondes (int).
    """
    val = to_int(ts)
    if val < 100000000000:
        return val * 1000
    return val

def to_s(ts):
    """
    Détecte si un timestamp est en secondes ou millisecondes et renvoie des secondes (int).
    """
    val = to_int(ts)
    if val >= 100000000000:
        return val // 1000
    return val

def fetch_json(url, timeout=15, retries=3, backoff=1.5):
    """
    Effectue une requête GET HTTP avec retries exponentiels et gère le JSON.
    """
    attempt = 0
    current_backoff = backoff
    while attempt < retries:
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0 ACE777-DialectLib"}
            )
            with urllib.request.urlopen(req, timeout=timeout) as response:
                if response.status == 200:
                    data = response.read().decode('utf-8')
                    return json.loads(data)
                else:
                    raise IOError(f"HTTP Status {response.status}")
        except Exception as e:
            attempt += 1
            if attempt >= retries:
                raise RuntimeError(f"Échec définitif de fetch_json pour {url} après {retries} essais. Erreur: {e}")
            time.sleep(current_backoff)
            current_backoff *= 1.5

def paginate_klines(url_base, params, max_candles, limit_per_call=1000):
    """
    Pagine une API de bougies style Binance (startTime/endTime en ms, limit) 
    jusqu'à max_candles ou fin de fenêtre.
    """
    all_candles = []
    current_params = dict(params)
    
    start_time = to_int(current_params.get("startTime", 0))
    end_time = to_int(current_params.get("endTime", int(time.time() * 1000)))
    
    current_params['limit'] = limit_per_call

    while len(all_candles) < max_candles:
        current_params['startTime'] = start_time
        current_params['endTime'] = end_time
        
        query_string = urllib.parse.urlencode(current_params)
        full_url = f"{url_base}?{query_string}"
        
        chunk = fetch_json(full_url)
        if not chunk or not isinstance(chunk, list):
            break
            
        all_candles.extend(chunk)
        
        if len(chunk) < limit_per_call:
            break
            
        last_candle_open_time = to_int(chunk[-1][0])
        next_start = last_candle_open_time + 1
        
        if next_start <= start_time:
            break
            
        start_time = next_start
        
        if start_time >= end_time:
            break

    return all_candles[:max_candles]

def self_test():
    """
    Teste tous les pièges réels de la semaine.
    Renvoie True si tout passe, False et log si échec.
    """
    try:
        # Test 1: to_int décimal sans 0x (Le bug x402)
        val1 = to_int("106985381")
        assert val1 == 106985381, f"Échec to_int décimal: attendu 106985381, obtenu {val1}"

        # Test 2: to_int hexadécimal avec 0x (la vraie paire du bug x402 : 0x66077A5 = 106985381)
        val2 = to_int("0x66077A5")
        assert val2 == 106985381, f"Échec to_int hex: attendu 106985381, obtenu {val2}"
        val2b = to_int("0x660F6BB")
        assert val2b == 107017915, f"Échec to_int hex 2: attendu 107017915, obtenu {val2b}"

        # Test 3: to_int avec int direct
        val3 = to_int(107)
        assert val3 == 107, f"Échec to_int int: attendu 107, obtenu {val3}"

        # Test 4: to_ms secondes vs millisecondes
        ts_sec = 1789000000
        ts_ms = 1789000000000
        assert to_ms(ts_sec) == ts_ms, f"Échec to_ms secondes: obtenu {to_ms(ts_sec)}"
        assert to_ms(ts_ms) == ts_ms, f"Échec to_ms millisecondes: obtenu {to_ms(ts_ms)}"

        # Test 5: paginate_klines réel (Binance klines 1m BTC, > 1000 bougies sur 3 jours)
        # 3 jours = 3 * 24 * 60 * 60 * 1000 = 259,200,000 ms
        end_t = int(time.time() * 1000)
        start_t = end_t - (3 * 24 * 3600 * 1000)
        
        url_binance = "https://api.binance.com/api/v3/klines"
        params = {
            "symbol": "BTCUSDT",
            "interval": "1m",
            "startTime": start_t,
            "endTime": end_t
        }
        
        candles = paginate_klines(url_binance, params, max_candles=1500, limit_per_call=1000)
        assert len(candles) > 1000, f"Échec pagination: attendu > 1000 bougies, obtenu {len(candles)}"

        return True

    except AssertionError as ae:
        print(f"[TEST ÉCHOUÉ] {ae}")
        return False
    except Exception as e:
        print(f"[TEST ERREUR TECHNIQUE] {e}")
        return False

if __name__ == "__main__":
    success = self_test()
    if success:
        sys.exit(0)
    else:
        sys.exit(1)