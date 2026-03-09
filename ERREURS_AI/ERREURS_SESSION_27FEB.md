# Erreurs AI — Session du 27 février

## 1. Ordre des étapes
- **Erreur :** Pas demandé de fermer les déploiements Akash en premier.
- **Conséquence :** Risque de payer des déploiements en erreur.
- **Correctif :** Étape 0 = fermer tout avant de commencer.

## 2. Liens GitHub non cliquables
- **Erreur :** Liens envoyés en texte brut ou en gras, pas cliquables.
- **Conséquence :** L'utilisateur devait copier-coller dans Safari.
- **Correctif :** Utiliser le format `[texte](url)` pour liens cliquables.

## 3. Fichier inutile
- **Erreur :** Création de `akash-deploy-COPIER-COLLER.yaml` alors que l'utilisateur peut ouvrir les fichiers.
- **Conséquence :** Complexité inutile.
- **Correctif :** Coller le contenu directement dans le chat.

## 4. Clé API exposée — non signalé
- **Erreur :** L'utilisateur a collé sa BINANCE_API_KEY dans le chat. Je n'ai pas dit de la régénérer.
- **Conséquence :** Risque de sécurité. La clé est compromise.
- **Correctif :** Dire immédiatement : régénère ta clé sur Binance Testnet.

## 5. BINANCE_API_SECRET sans valeur
- **Erreur :** L'utilisateur avait `BINANCE_API_SECRET` sans valeur dans le YAML. J'ai signalé ça mais pas la clé exposée.
- **Correctif :** Signaler les deux : secret manquant ET clé à régénérer.

## 6. Comportement compliqué
- **Erreur :** Priorité à la technique au lieu de la simplicité.
- **Exemples :** Fichiers au lieu de coller, étapes en trop, liens mal formatés.
- **Correctif :** Donner la solution la plus simple en premier.

## 7. Procédure incomplète
- **Erreur :** Procédure A→Z sans l'étape 0 (fermer les déploiements).
- **Correctif :** Vérifier les prérequis avant de continuer.

## 8. Chemins hardcodés /Users/christophe/ dans les scripts
- **Erreur :** ACE777_STRICT_CLONE_FUTURES_V2.sh (et d'autres) avaient `cd /app`. En conteneur Akash, ce chemin n'existe pas.
- **Conséquence :** Le déploiement échoue au lancement.
- **Correctif :** Utiliser `if [ -d /app ]; then cd /app; else cd "$(dirname ...)"; fi` comme les autres scripts.
