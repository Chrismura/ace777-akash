# Commande d'arrêt ACE777

**Ouvre un NOUVEAU terminal** (pas celui où le cycle tourne), puis :

```bash
cd /Users/christophe/ace777-test-day1 && ./stop_ace777.sh
```

**One-liner (copier-coller) :**
```bash
cd /Users/christophe/ace777-test-day1 && touch STOP STOP_ALPHA STOP_BETA && kill -9 -$(cat runs/master.pid 2>/dev/null) 2>/dev/null; kill -9 $(cat runs/master.pid runs/alpha.pid runs/beta.pid 2>/dev/null) 2>/dev/null; pkill -9 -f genesis_manifest; pkill -9 -f launch_test_master_base; pkill -9 -f "tail.*genesis"; echo "Arrêté"
```

**Si ça ne marche pas :** Ctrl+C dans le terminal où le cycle tourne.
