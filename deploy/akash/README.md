# Deployer ACE777 sur Akash (pas a pas)

## 1) Prerequis

- Docker installe localement
- Compte Docker Hub
- Wallet Akash + solde AKT
- Akash CLI installe

## 2) Build + push de l'image

Depuis la racine du projet:

```bash
cd /app
docker build -t docker.io/YOUR_DOCKERHUB_USER/ace777:latest .
docker push docker.io/YOUR_DOCKERHUB_USER/ace777:latest
```

Puis edite `deploy/akash/akash.yml`:

- remplace `YOUR_DOCKERHUB_USER`
- ajuste les variables de strategie si besoin
- ajoute `BINANCE_API_KEY` et `BINANCE_API_SECRET` avant de deployer

## 3) Deploy sur Akash

```bash
akash tx deployment create deploy/akash/akash.yml --from YOUR_KEY_NAME --chain-id akashnet-2 --node https://rpc.akashnet.net:443 --fees 5000uakt -y
akash query market bid list --owner $(akash keys show YOUR_KEY_NAME -a)
akash tx market lease create --dseq <DSEQ> --gseq 1 --oseq 1 --provider <PROVIDER_ADDRESS> --from YOUR_KEY_NAME --chain-id akashnet-2 --node https://rpc.akashnet.net:443 --fees 5000uakt -y
akash provider lease-logs --dseq <DSEQ> --gseq 1 --oseq 1 --provider <PROVIDER_ADDRESS>
```

## 4) Stop propre / fermeture

Le conteneur intercepte SIGTERM et pose les STOP files.

Pour fermer le lease:

```bash
akash tx market lease close --dseq <DSEQ> --gseq 1 --oseq 1 --provider <PROVIDER_ADDRESS> --from YOUR_KEY_NAME --chain-id akashnet-2 --node https://rpc.akashnet.net:443 --fees 5000uakt -y
```

## 5) Est-ce que ca optimise ACE777 ?

Oui pour:

- uptime (instance distante stable)
- isolation (moins de perturbations locales)
- redemarrage propre et repetition de runs

Mais pas toujours pour:

- latence reseau vers Binance (depend du provider Akash)
- debugging interactif (moins confortable que local)

Conclusion: tres bien pour automatiser des runs longs, a valider avec 1-2 runs pilotes avant usage intensif.
