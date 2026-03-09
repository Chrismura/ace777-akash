# ACE777 sur Akash — Procédure complète de A à Z

## Ordre des étapes (à respecter)

---

## ÉTAPE 0 — Fermer tout avant de commencer

1. Va sur **https://console.akash.network**
2. Connecte-toi avec **Keplr**
3. Menu **Deployments**
4. Pour chaque déploiement listé : **Close deployment** → confirmer
5. Vérifier que la liste est vide (ou que tout est fermé)

**Pourquoi en premier :** évite de payer des déploiements en erreur ou inutiles.

---

## ÉTAPE 1 — Rendre le package GHCR public

1. Va sur **https://github.com/Chrismura?tab=packages**
2. Clique sur **ace777-akash**
3. **Package settings** (à droite)
4. **Change visibility** → **Public** → confirmer

**Pourquoi :** le provider Akash ne peut pas pull une image privée (ImagePullBackOff).

---

## ÉTAPE 2 — Vérifier que l’image existe

1. Va sur **https://github.com/Chrismura/ace777-akash**
2. Vérifie qu’un **push sur main** a déclenché le workflow **Build and Push GHCR**
3. Onglet **Actions** → dernier run réussi
4. L’image `ghcr.io/chrismura/ace777-akash:latest` doit exister

**Si le workflow n’a jamais tourné :** fais un petit commit + push sur main pour le lancer.

---

## ÉTAPE 3 — Préparer les variables secrètes

Tu dois avoir :

- `BINANCE_API_KEY` — clé API Binance Testnet
- `BINANCE_API_SECRET` — secret API Binance Testnet

**Optionnel :** `BINANCE_BASE_URL` (par défaut : `https://testnet.binancefuture.com`)

---

## ÉTAPE 4 — Créer le déploiement sur Akash

### Via la console web (recommandé)

1. **https://console.akash.network** → **Deploy**
2. Choisir **Custom** ou coller le SDL
3. Utiliser le YAML ci-dessous en remplaçant `YOUR_BINANCE_API_KEY` et `YOUR_BINANCE_API_SECRET` par tes vraies valeurs

```yaml
version: "2.0"

services:
  ace777:
    image: ghcr.io/chrismura/ace777-akash:latest
    env:
      - BINANCE_API_KEY=YOUR_BINANCE_API_KEY
      - BINANCE_API_SECRET=YOUR_BINANCE_API_SECRET
      - BINANCE_BASE_URL_OVERRIDE=https://testnet.binancefuture.com
      - RUN_DURATION=04:00:00
      - LAUNCH_SCRIPT=./launch_test_master_base_v8_6_fortress.sh
      - MOMENTUM_THRESHOLD=0.95
      - WALL_DROP_THRESHOLD=0.060
      - BUY_USDT_BETA=150
      - BUY_USDT_ALPHA=750
      - GLOBAL_STOP_USDT=-32.00
      - FLUID_EXIT_SENSITIVITY=1.0
      - DYNAMIC_HOLD=TRUE
    expose:
      - port: 3000
        to:
          - global: true

profiles:
  compute:
    ace777:
      resources:
        cpu:
          units: 1
        memory:
          size: 1Gi
        storage:
          - size: 5Gi
  placement:
    dcloud:
      pricing:
        ace777:
          denom: uakt
          amount: 5000

deployment:
  ace777:
    dcloud:
      profile: ace777
      count: 1
```

4. Valider le déploiement et accepter les frais (Keplr)

---

## ÉTAPE 5 — Attendre le déploiement

1. Le provider doit **pull** l’image (quelques minutes si première fois)
2. Statut attendu : **Running** (pas ImagePullBackOff, pas CrashLoopBackOff)

---

## ÉTAPE 6 — Vérifier les logs

1. Dans la console Akash : ouvre ton déploiement
2. **Logs** (ou **Lease logs**)
3. Tu dois voir :
   - `PREFLIGHT_OK: authentification Binance valide.`
   - Puis des lignes `[BETA_X5]` et `[ALPHA_X13]` (ou équivalent selon le script)

**Si erreur :** vérifier BINANCE_API_KEY / BINANCE_API_SECRET et BINANCE_BASE_URL.

---

## ÉTAPE 7 — Arrêter proprement quand tu veux

1. **Deployments** → ton déploiement
2. **Close deployment** → confirmer
3. Vérifier que le déploiement disparaît ou passe en état fermé

---

## Checklist rapide

- [ ] Étape 0 : Tous les déploiements fermés
- [ ] Étape 1 : Package GHCR public
- [ ] Étape 2 : Image `ghcr.io/chrismura/ace777-akash:latest` existe
- [ ] Étape 3 : Clés Binance Testnet prêtes
- [ ] Étape 4 : Déploiement créé avec les bonnes env
- [ ] Étape 5 : Statut Running
- [ ] Étape 6 : PREFLIGHT_OK + logs BETA/ALPHA
- [ ] Étape 7 : Close deployment quand tu as fini
