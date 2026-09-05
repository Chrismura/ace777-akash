# AVIS JUGE (task juge.tranche · Google Gemini · 2026-09-01T09:21Z)

VERDICT : GO AVEC RESERVES
CONFIANCE : 95 %

HYPOTHÈSES :
1. **Cache navigateur persistant (Brave/Chromium) :** Le navigateur s'attache à une session existante (`Opening in existing browser session`) et sert les scripts JS/HTML depuis son cache local sans réinterroger le port 17800.
2. **Double instance de serveur :** Un ancien serveur HTTP fantôme tourne peut-être sur un autre pid/contexte, bien que le port 17800 soit vérifié.

CE QUI CHANGERAIT L'AVIS :
- La preuve que l'affichage persiste même après un rechargement en navigation privée (`Incognito`) et un vidage complet du cache du port 17800.

AMÉLIORATION PROPOSÉE :
1. **En-têtes anti-cache stricts :** Modifier le serveur HTTP local pour injecter systématiquement `Cache-Control: no-store, no-cache, must-revalidate` sur tous les fichiers statiques (`.js`, `.html`).
2. **Versioning dynamique (Cache-Busting) :** Ajouter un paramètre temporel (`?v=timestamp`) dans les balises `<script>` du HTML généré pour invalider mécaniquement le cache client à chaque redémarrage du serveur cockpit.

SYNTHÈSE (5 lignes max) :
Le serveur et le feed exécutés sont corrects, mais Brave sert une version en cache via sa session existante. 
La cause racine est un cache client récalcitrant ignorant le port 17800 rafraîchi. 
Hulk n'est absolument pas concerné ni altéré. 
Correction : forcer le rechargement sans cache et injecter des en-têtes HTTP `no-cache` sur le serveur.
