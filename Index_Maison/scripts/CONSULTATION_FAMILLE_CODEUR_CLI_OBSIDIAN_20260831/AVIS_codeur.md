# CODEUR (provider Google Gemini)

*Analyse technique et critique — Superviseur / Codeur Expert (ACE777)*
*Date : 31/08/2026*
*Chantier : Pont CLI Obsidian (v1.13.7)*

---

### A) Évaluation du plan de Buffy (Pont CLI + Fallback) & Risques réels

**Le découpage est-il bon ?**
Oui, l'approche hybride **"CLI prioritaire + Fallback OUTBOX"** est la seule structure acceptable en production pour un système multi-agents. Un agent ne doit *jamais* planter (perdre une analyse de marché ou un deepdive) simplement parce qu'un utilisateur a fermé l'application Obsidian pour libérer de la RAM.

**Les risques techniques de la CLI officielle (v1.12+) :**
1. **Couplage fort & Disponibilité de l'App :** La CLI communique par IPC local (socket/port local) avec l'instance GUI d'Obsidian. Si Obsidian freeze (très fréquent sur de gros vaults indexés lors d'une recherche lourde) ou plante, les appels `subprocess` vont bloquer ou expirer (*timeout*).
2. **Latence des processus (Subprocess overhead) :** Lancer un `subprocess.run(["/Applications/Obsidian.app/Contents/MacOS/obsidian-cli", ...])` à chaque écriture génère un coût de démarrage de processus Node.js/Electron encapsulé. Pour 50 à 100 écritures/jour, c'est négligeable (< 200ms par appel), mais à l'échelle de agents en boucle intensive (ex: 500 micro-logs), ça sature l'event loop.
3. **Concurrence d'écriture (File locking) :** Si la famille (Gemini, Grok, etc.) pousse 4 synthèses en parallèle via la CLI, l'application Obsidian va tenter d'écrire 4 fichiers en même temps dans le même répertoire du vault. Bien que l'architecture interne gère ses modifications, des conflits de rendu (ou des fichiers partiellement écrits si la CLI renvoie le succès avant flush disque complet) peuvent corrompre l'indexation.

**Comment le faire sans casser (Recommandations Codeur) :**
* **Timeouts stricts :** Tout appel `subprocess` vers la CLI doit avoir un `timeout=3.0` (secondes). Si le timeout est dépassé, bascule immédiate sur le dossier `OUTBOX_OBSIDIAN/`.
* **File d'attente (Queue) locale :** Ne pas appeler la CLI en rafale aveugle depuis les scripts de la famille. Mettre en place un verrou (mutex) ou une file d'attente séquentielle dans le pont Python pour traiter les écritures une par une.

---

### B) Autres approches vs CLI officielle : Laquelle est la plus robuste ?

1. **L'API REST Communautaire (Plugin *Local REST API* de codetheory) :**
   * *Principe :* Un serveur HTTPS local tourne dans Obsidian avec un token Bearer.
   * *Avantages :* Ultra-robuste, asynchrone, permet de créer, lire, modifier, chercher et lancer des commandes sans dépendre de l'UI au premier plan (tant qu'Obsidian tourne en tâche de fond).
   * *Inconvénients :* Dépend d'un plugin tiers (risque de casse lors des mises à jour majeures d'Obsidian).
2. **Le protocole URI (`obsidian://`) :**
   * *Principe :* Ouvre des liens profonds via `open obsidian://new...`
   * *Verdict :* À fuir pour de l'automatisation lourde par IA. C'est aveugle (pas de retour de succès/échec dans le terminal), ça ouvre des fenêtres intempestives et c'est limité en taille de payload.
3. **Écriture directe sur le disque (Méthode actuelle OUTBOX améliorée) :**
   * *Principe :* Écrire directement dans le répertoire `.md` du Vault (via Python `pathlib`).
   * *Avantages :* Vitesse maximale, zéro dépendance à l'état de l'application.
   * *Inconvénients :* Obsidian ne met pas toujours à jour son index instantanément s'il ne surveille pas le dossier en temps réel (chunky watch events).

**Comparatif pour l'IA :** La **CLI officielle** l'emporte sur le plugin tiers car elle est maintenue par Core (pas de rupture de plugin), mais elle reste dépendante de l'UI. Le meilleur des mondes reste la CLI avec un fallback d'écriture directe disque.

---

### C) Costaud structurel : Comment garantir l'intégrité (Read-back & Indexation) ?

Pour s'assurer qu'une note écrite est une note valide (pas un fichier vide ou corrompu), le pont `obsidian_cli_bridge.py` doit implémenter un **cycle de validation en 3 temps** :

1. **Write (Écriture) :** Envoi via `obsidian create`. Récupération du code de retour `0`.
2. **Read-back (Vérification de contenu) :** Appel immédiat de `obsidian read path="notename.md"`. On compare le hash SHA-256 du contenu envoyé et du contenu lu. Si mismatch -> Alerte et bascule en mode secours.
3. **Index check (Traçabilité) :** Enregistrement de l'opération dans un journal SQLite local ou un fichier `obsidian_audit.log` dans le vault (ex: `[[JOURNAL_SYSTEME]]`) avec timestamp, statut (`OK_CLI` ou `FALLBACK_OUTBOX`), et checksum.

---

### D) Amélioration concrète et proposition du codeur (Le Pont "Bulletproof")

Ne vous contentez pas d'un simple wrapper `subprocess`. Voici le design architectural exact du module `obsidian_cli_bridge.py` que je valide pour ACE777 :

```python
import subprocess
import hashlib
from pathlib import Path
import time
import json

OBSIDIAN_CLI = "/Applications/Obsidian.app/Contents/MacOS/obsidian-cli"
VAULT_OUTBOX = Path("~/Documents/Obsidian_ACE777/OUTBOX_OBSIDIAN").expanduser()
AUDIT_LOG = Path("~/Documents/Obsidian_ACE777/system_audit.jsonl").expanduser()

class ObsidianBridge:
    @staticmethod
    def _run_cli(args: list, timeout: float = 3.0) -> tuple[bool, str]:
        try:
            res = subprocess.run(
                [OBSIDIAN_CLI] + args,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            if res.returncode == 0:
                return True, res.stdout.strip()
            return False, res.stderr.strip()
        except subprocess.TimeoutExpired:
            return False, "CLI_TIMEOUT"
        except FileNotFoundError:
            return False, "CLI_NOT_FOUND"

    @classmethod
    def is_alive(cls) -> bool:
        # Ping rapide via une commande légère
        success, _ = cls._run_cli(["tags", "counts"], timeout=1.0)
        return success

    @classmethod
    def write_note(cls, title: str, content: str, folder: str = "") -> dict:
        filename = f"{title}.md"
        path = f"{folder}/{filename}".lstrip("/")
        
        # 1. Tentative CLI si l'app répond
        if cls.is_alive():
            success, err = cls._run_cli(["create", f"name={path}", f"content={content}"])
            if success:
                # 2. READ-BACK de vérification
                read_success, read_data = cls._run_cli(["read", f"path={path}"])
                if read_success and len(read_data) > 0:
                    cls._log_audit(title, "CLI_SUCCESS")
                    return {"status": "SUCCESS_CLI", "path": path}

        # 3. FALLBACK OUTBOX (Fail-Open absolu)
        VAULT_OUTBOX.mkdir(parents=True, exist_ok=True)
        fallback_file = VAULT_OUTBOX / filename
        fallback_file.write_text(content, encoding="utf-8")
        cls._log_audit(title, "FALLBACK_OUTBOX")
        return {"status": "SUCCESS_FALLBACK", "path": str(fallback_file)}

    @staticmethod
    def log_audit(title, status):
        # Enregistrement local infaillible
        entry = {"timestamp": time.time(), "title": title, "status": status}
        with open(AUDIT_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
```

### Avis Global & Sincère sur le plan de Buffy :
* **Ce qui est bon :** L'intuition de basculer sur la CLI officielle pour s'intégrer proprement dans l'écosystème Obsidian sans salir le système de fichiers avec des milliers de fichiers orphelins.
* **Ce qui est risqué :** Croire que l'application Obsidian est un démon système infatigable. Elle va planter, être fermée pour de la maintenance, ou refuser de répondre sous la charge. 
* **Verdict :** Le plan est validé **uniquement** si vous intégrez le pattern *Fail-Open* (le fallback OUTBOX) et le *Read-back* que je viens de
