# Hulk × MEXC — dip & rip (dossier séparé)

**But :** watchlist CMC [The Hulk Crypto Portfolio Picks](https://coinmarketcap.com/watchlist/68f096217962d710267cb472/) → trader sur **MEXC** : acheter les descentes, revendre les remontées / spikes.

**Hors scope :** ACE777 NUAGE / genesis champion (`ace777-test-day1` racine) — **jamais modifié** depuis ce dossier.

---

## 🧭 PHILOSOPHIE HULK — texte canonique (à lire, pas à redemander)

> *Dicté par Christophe le 16/08/2026. Toute IA / tout agent qui travaille sur Hulk lit CE texte d'abord.
> Ne pas redemander « c'est quoi la philosophie ? » — elle est ici, en une page.*

**Les small caps du portefeuille ne sont PAS des paires à scalper.** Ce sont des **projets étudiés avec attention** : gros potentiel, gros investisseurs, sélectionnés un par un. On y croit. Le bag EST le but.

**Il n'y a pas de cash à injecter** : on ne peut pas acheter de nouvelles positions avec de l'argent frais. La seule façon de faire grandir le portefeuille, c'est de **trader ces tokens eux-mêmes** : vendre les rebonds (rip), racheter les creux (dip), récupérer du cash à chaque vente partielle, et le **redéployer pour accumuler plus de tokens** → le bag grandit.

**« Une pierre trois coups » — l'équilibre visé :**

1. **J'achète les creux** (dip)
2. **Je vends sur les gains** (rip **scale-out 2 paliers**, 25 % à chaque palier — décision Christophe 16/08 soir) :
   - **XRP / HBAR** (liquides, gros volumes) : palier 1 à **+2 %**, palier 2 à **+6 %**
   - **reste (small caps)** : palier 1 à **+6 %**, palier 2 à **+8 %** (laisser courir les pumps d'altsaison)
3. **Je garde la position pour le cash** (chaque paire garde son propre cash pour se racheter elle-même)
4. **Je ferme une partie, avec le cash j'attends le creux** (cash redéployé sur le prochain vrai dip)
5. **Je laisse un runner** (les 50 % restants continuent ; à 2× ils deviennent bag maison)

**Le vrai objectif :** faire des **plus-values** et surtout **limiter les pertes par rapport à un wallet statique** (si on n'avait rien touché). Le benchmark, c'est « Hulk vs wallet statique » — pas un indice, pas un trader.

**Setup de référence (ce que représentent les chiffres) :**
- `SEED_USDT=150 / SEED_MAX_PAIRS=15` → **10 $ par paire = les tokens DÉJÀ détenus** (crypto en portefeuille), vendables dès la première seconde (rip/stop actifs dès le seed).
- `NOTIONAL_USDT=20` → **le cash dispo pour acheter les creux** (à part du seed).
- Le seed **ne passe pas par le sizing** (tier B ×0.25 etc.) : c'est l'état initial du wallet, pas un achat. Les règles de sizing s'appliquent aux ACHATS, pas aux avoirs.

**Priorités de Christophe (16/08) :** 1) plus-values + limiter la casse vs wallet statique — c'est le principal ; 2) prises de positions, runner, bags (déjà ajoutés).

**Historique de calibrage :** le setup n'était pas correct avant le 16/08 (journée entière passée à corriger ACE). Les runs antérieurs au 16/08 soir **ne reflètent pas Hulk** — ne jamais calibrer dessus. Les vrais tests commencent le 16/08.

---

## Idée marché

Beaucoup de paires Hulk = **peu liquides** mais **gros spikes**.  
→ Opportunité de % élevés, **et** risque : slippage, gap, impossible de sortir.  
On filtre : volume mini + spread max, tout en gardant les candidats « spike ».

## Arborescence

```
hulk-mexc/
  README.md
  config/          # seuils, clés (env), mode paper/live
  data/            # univers, snapshots liquidité
  docs/            # plan, règles stratégie
  scripts/         # inventaire MEXC, paper tests
  runs/            # logs / CSV tests
```

## Phases

| Phase | Contenu | Statut |
|-------|---------|--------|
| 0 | Dossier + univers CMC Hulk | **ici** |
| 1 | Inventaire MEXC (paire USDT + volume 24h) | scripts |
| 2 | Paper : règles dip/rip simples | à faire |
| 3 | Testnet / petit live MEXC | plus tard |

## Commandes utiles

```bash
cd /Users/christophe/ace777-test-day1/hulk-mexc

# 1) Rafraîchir liquidité MEXC
python3 scripts/inventory_mexc.py

# 2) Stop l'ancien paper puis paper v1.5 — TON terminal (PISTE A)
touch STOP_PAPER   # si l'ancien tourne encore
# Ctrl+C sur l'ancien process, puis :
rm -f STOP_PAPER
python3 scripts/paper_diprip.py
# Au boot : SEED ~20$ en tokens (config SEED_*) pour tester aussi les VENTES baissières.

# 3) Veille — AUTRE terminal (PISTE B) — LIVE direct (pas de pause 60s)
python3 scripts/digest_watch.py --live
# enchaîne les scans ; écrit ALERT seulement si signal nouveau
# stop : touch STOP_DIGEST

# Clés MEXC (optionnel, plus tard live) — hors repo
# cp config/mexc.env.example ~/.mexc.env && chmod 600 ~/.mexc.env
```

Pistes séparées : `docs/TRACKS_SEPARES.md` · Confrontation : `docs/CONFRONTATION.md` · Veille : `docs/VEILLE_QWEN.md`.  
**Protocole Ghost** (watchdog 30 min) : `docs/PROTOCOLE_GHOST.md` · `scripts/watchdog_hulk_ghost.sh`.
