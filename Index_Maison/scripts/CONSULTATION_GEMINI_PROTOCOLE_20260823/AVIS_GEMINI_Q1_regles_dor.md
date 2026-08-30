# AVIS GEMINI · Q1_regles_dor (NaraRouter (7M tokens/jour gratuits) · 136s)

Règle : aucune action sans preuve fraîche, versionnée, corroborée par 2 détecteurs indépendants.  
Seuil : TTL ≤ 30 s ; latence ≤ 2 s ; divergence ≤ 5 % ; quorum 2/3.  
Erreur neutralisée : signal unique, périmé ou incohérent.  
Point faible : panne commune/collusion des détecteurs.  
Garde-fou : heartbeat 10 s, audit immuable, kill-switch après 3 incohérences.
