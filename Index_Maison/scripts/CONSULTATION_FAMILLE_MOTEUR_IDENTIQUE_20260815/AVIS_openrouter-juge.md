# AVIS openrouter-juge (provider OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant, 35.4s)

**1) Confirmation du moteur**  
- Les quatre fichiers CSV scellés (ALPHA + BETA pour chaque run) portent le même **genesis_md5 = 8d9ee8d6997eeadabf3da642f326d3d7**.  
- Les 17 333 premières lignes du fichier du 15 / 08 / 2026 05:45Z sont **identiques octet‑pour‑octet** aux 17 333 lignes du fichier du 14 / 08 / 2026 21:19Z ; le fichier du 15 n’est que le même fichier avec 3 629 lignes supplémentaires (le run de nuit).  
- Les en‑têtes CSV sont exactement les mêmes : `ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,exitReason,holdSec,msg`.  
- Les séquences de cycles ALPHA présentées (ex. : cyc 458→524 du run 4h#1, cyc 230→409 du run V2, cyc 859→872 du run Nuit) montrent le même schéma : entrée BUY, taille de position qui varie selon le champ `size` (strong_conf_full, hunter_revenge_1.5x, etc.) et des raisons de sortie identiques (`shock_inversion_stop`, `fluid_exit_inversion`, `fluid_exit_brake`).  

**Conclusion** : aucun élément des séquences ni des preuves CSV ne indique un changement de code, de paramètres ou de binaire entre les trois runs. Le même moteur ACE (SCOUT = BETA x5, HUNTER = ALPHA x13) a été exécuté dans les trois intervalles temporels.

---

**2) Le pattern “revenge” : normal ou artefact ?**  

| Run | % ALPHA en revenge | PNL revenge ALPHA | % du PNL total ALPHA provenant du revenge |
|-----|-------------------|-------------------|-------------------------------------------|
| 4h #1 | 80 % | +25,61 $ | 91 % |
| V2    | 68 % | +9,55 $  | 57 % |
| Nuit  | 91 % | +8,28 $  | 96 % |

Le design du système prévoit que le mode **revenge** ne s’active que lorsqu’un état du SCOUT rempli les conditions :

```
role == "SCOUT" && status == "CLOSED" && pnl < 0
&& reason ∈ [stop_loss, shock_inversion_stop, shock_exit_10bps,
             fluid_exit_inversion, fluid_exit_brake, beta_sentinel_cut]
```

et que cet état soit **frais** (moins de `DUO_EVENT_TTL_SEC = 20 s`).  
Après activation, ALPHA passe en taille `1.5 ×` (DUO_HUNTER_REVENGE_MULT) **une seule fois** jusqu’à ce que l’état devienne stale.

**Observation du code (ligne 1545 du genesis)**  
```c
duo_touch_heartbeat() {   // appelé à chaque cycle du SCOUT
    duo_state.ts_ms = now_ms();   // rafraîchit uniquement le timestamp
    // les autres champs (role, status, pnl, reason, …) restent inchangés
}
```
- Ce heartbeat **met à jour `ts_ms` à chaque cycle du SCOUT** (≈ 200 trades/nuit → ~un trade toutes les 180 s en moyenne, mais en réalité beaucoup plus fréquent pendant les périodes actives).  
- Comme le TTL est basé sur la différence `now_ms() - duo_state.ts_ms`, le fait de ré‑écrire `ts_ms` à chaque cycle **réinitialise le compteur à zéro** tant que le SCOUT continue de tourner.  
- Tant que le SCOUT reste en boucle (ce qui est le cas pendant tout le run), l’état ne devient jamais *stale* ; il reste considéré comme “frais” indéfiniment.  

**Conséquence**  
- Dès qu’une perte du SCOUT survient et que la raison appartient à la liste ci‑dessus, le drapeau *revenge* est mis à vrai.  
- Parce que le heartbeat empêche l’état de devenir stale, le drapeau reste vrai **pour tous les cycles suivants** jusqu’à ce que le SCOUT change délibérément son `status` ou sa `reason` (par exemple en ouvrant une nouvelle position).  
- Ainsi, ALPHA voit en permanence l’état “revenge actif” et applique le multiplicateur 1,5× à presque chacune de ses décisions, d’où les pourcentages de revenge observés (68‑91 %).  

**Validation**  
- Le mécanisme décrit est **plausible** et directement soutenu par le code du heartbeat.  
- Aucune autre modification du code (par exemple un changement de `DUO_EVENT_TTL_SEC` ou de la liste de raisons) n’est mentionnée dans le contexte ; donc l’explication la plus simple du taux de revenge anormalement élevé est bien le heartbeat qui neutralise le TTL.

---

**3) BETA “inutile” ?**  

| Run | BETA trades | BETA PNL | ALPHA trades | ALPHA PNL | Ratio BETA/ALPHA (trades) | Ratio BETA/ALPHA (PNL) |
|-----|-------------|----------|--------------|-----------|---------------------------|------------------------|
| 4h #1 | 155 | +0,40 $ | 65 | +28,26 $ | 2,38 × | 0,014 × |
| V2    | 156 | +1,97 $ | 37 | +16,61 $ | 4,22 × | 0,119 × |
| Nuit  | 204 | +2,51 $ | 56 | +8,61 $  | 3,64 × | 0,291 × |

- Le rôle du **SCOUT (BETA)** est délibérément celui d’un *probe* : il effectue un grand nombre de micro‑trades (forte fréquence, petite taille) afin de détecter des signaux de marché et, le cas échéant, d’encaisser les petites pertes qui déclenchent le revenge du HUNTER.  
- Sa rentabilité attendue est donc faible ; il n’est pas conçu pour générer du PNL substantiel, mais pour fournir l’information de déclenchement.  
- Les chiffres observés (quelques dixièmes de dollar sur plusieurs centaines de trades) sont cohérents avec ce rôle : le SCOUT subit effectivement de petites pertes ou gains nets proches de zéro, tandis que le HUNTER, en réagissant rarement mais avec des positions beaucoup plus grosses (taille multipliée par 1,5 en revenge), capte la majorité du profit.  
- Ainsi, le déséquilibre de PNL n’est pas une anomalie ; il reflète la répartition des tâches prévue dans l’architecture DUO.

---

**4) Les trades “flat” (pnl = 0)**  

- Pourcentages de trades ALPHA avec pnl = 0 : 25 % (run 4h#1), 32 % (run V2), 39 % (run Nuit).  
- Dans le code du HUNTER, lorsqu’il est en mode **suffer** (status == "OPEN" && bps <= seuil) ou lorsqu’il décide de ne pas prendre de position (par exemple parce que le signal du SCOUT est jugé insuffisant), il peut envoyer un ordre d’entrée et de sortie immédiate au même prix, résultant en un pnl nul.  
- Ces plats sont donc le résultat du **filtre de qualité / de la logique de retenue** du HUNTER : il préfère rester flat plutôt que d’ouvrir une position risquée quand les conditions ne sont pas suffisamment favorables.  
- Ils ne représentent pas forcément du “capital immobilisé pour rien” ; ils sont une conséquence intentionnelle de la stratégie de risque du HUNTER qui évite les trades à faible espérance.

---

**5) Anomalie de la colonne `holdSec`**  

- La spécification du CSV indique que la colonne `holdSec` doit contenir la **durée de détention** (en secondes) de la position.  
- Dans les fichiers fournis, cette colonne contient plutôt le **message détaillé** (ex. : `radar=... size_note=... soft=... tension=...`), tandis que la colonne `msg` est systématiquement vide.  
- Cette inversion provient clairement d’une **erreur de traçage** dans le code qui écrit le CSV : au lieu d’écrire `hold_sec` (la variable qui mesure le temps entre l’entrée et la sortie), le développeur a écrit le champ de debug/log qui regroupe les métadonnées internes.  
- Aucun autre élément du contexte ne suggère que cette inversion soit intentionnelle ; elle constitue donc bien une anomalie de journalisation qui doit être corrigée pour permettre une analyse précise du temps de détention.

---

### Réponse synthétique aux
