# AVIS GROK (provider NVIDIA build.nvidia.com (100+ modeles))

**VERDICT : GO AVEC RÉSERVES** (aligné 4/4 codeurs)

**RAISON** : Le plan est sain — fail-open, mode observation 48h, calibration sur données réelles. C'est exactement la bonne séquence pour une sonde qui touche au rate-limit et à la qualité du signal.

---

**ANGLE MORT** : **La latence réseau MEXC n'est pas bornée.** Tu mesures un "drop" entre deux lectures, mais si la 2e lecture arrive à 0.8s au lieu de 0.5s (jitter réseau, throttling), ton drop_pct est faussé — tu vas voir des "murs qui fondent" qui sont en fait des murs qui bougent normalement. **Il faut timestamp chaque lecture et calculer le drop RAPPORTÉ au delta réel**, pas à un DELAY_S théorique.

---

**AMÉLIORATION CONCRÈTE** : **Normaliser le drop par le temps réel écoulé** : `drop_pct_per_sec = drop_pct / (t2 - t1)`. Ça transforme ton seuil statique (12-20%) en seuil dynamique (ex: 25%/sec). Un mur qui fond de 15% en 0.3s = aspiration forte ; le même drop en 1.2s = bruit. Tu gardes ton seuil de percussion mais tu le rends insensible au jitter réseau. C'est la différence entre une sonde qui "voit" et une sonde qui "hallucine".
