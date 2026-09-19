# Patch blacklist 'mort du jour' — ecrit par Google Gemini via hub (loi 1quinquies) 09/08
# A INSPECTER par Ada (checker) puis AUDIT TIERS avant application.

# == AJOUT BLACKLIST : IMPORTS ET ETAT GLOBAL ==
from datetime import datetime

# Dictionnaire de suivi des echecs consecutifs par fournisseur {provider_id: count}
_fails = {}

# Dictionnaire de blacklist journaliere {provider_id: 'YYYY-MM-DD'}
_blacklist = {}


# == AJOUT BLACKLIST : CLASSE D'EXCEPTION ==
class BlacklistedProvider(Exception):
    """Exception levee lorsqu'un fournisseur est blackliste pour la journee."""

    def __init__(self, provider_name):
        super().__init__(f"Fournisseur {provider_name} blackliste pour aujourd'hui")
        self.provider_name = provider_name


# == AJOUT BLACKLIST : FONCTION DE VERIFICATION ==
def _is_blacklisted(prov):
    """Verifie si un fournisseur est blackliste pour le jour courant.
    Purge automatiquement la cle si la date est anterieure.
    """
    prov_id = prov.get("id")
    if not prov_id:
        return False

    if prov_id in _blacklist:
        today_str = datetime.now().strftime("%Y-%m-%d")
        if _blacklist[prov_id] == today_str:
            return True
        else:
            # Nouveau jour : expiration de la blacklist pour ce fournisseur
            del _blacklist[prov_id]
            if prov_id in _fails:
                _fails[prov_id] = 0

    return False


# == AJOUT BLACKLIST : MODIFICATION DE call_provider ==
# A inserer au tout debut de la fonction call_provider(prov, messages, temperature, max_tokens),
# avant d'initier le moindre appel reseau ou mecanisme de PATIENCE :
    if _is_blacklisted(prov):
        raise BlacklistedProvider(prov.get("name", prov.get("id", "inconnu")))


# == AJOUT BLACKLIST : GESTION DES SUCCES ET ECHECS DANS call_provider ==
# A inserer dans la logique d'appel de call_provider :
# 1. En cas de SUCCES de la requete :
    prov_id = prov.get("id")
    if prov_id:
        _fails[prov_id] = 0

# 2. En cas d'ECHEC (timeout PATIENCE, HTTP 402/429, ou reponse vide) :
    prov_id = prov.get("id")
    if prov_id:
        _fails[prov_id] = _fails.get(prov_id, 0) + 1
        if _fails[prov_id] >= 2:
            today_str = datetime.now().strftime('%Y-%m-%d')
            _blacklist[prov_id] = today_str
            prov_name = prov.get('name', prov_id)
            log_event(
                "blacklist",
                "Blacklist " + prov_name + " (2 echecs aujourd'hui)",
                "route directe vers bascule"
            )
            _fails[prov_id] = 0


# == AJOUT BLACKLIST : MODIFICATION DE chat_completions ==
# A inserer dans la boucle de routage de chat_completions (juste apres avoir selectionne ou itere sur un provider) :
        if _is_blacklisted(provider):
            continue
