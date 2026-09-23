# Tour 2 — demandé « nvidia/nemotron-3-super-120b-a12b:free » — RÉPONDU PAR « nvidia/nemotron-3-super-120b-a12b:free » (OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant, 34.5s)

**VERDICT** : Méthode recevable, latence de lecture du prix non conforme, stop toujours excessif · CE QUE J'EXIGE AVANT LE PROCHAIN TOUR : 1️⃣ Nouvelle mesure du délai de lecture du prix (médiane et p90) montrant une médiane ≤ 0,8 s sur au moins 1 h de fonctionnement live ; 2️⃣ Délai d’exécution du stop après GO 2 (médiane et p90) sur les premiers stops qui se produiront, avec coût de retard ≤ 0,05 $ ; 3️⃣ Décision chiffrée sur le plafond de stop pour RIZE : soit implémenter un plafond câblé à 15 % (ou inférieur) avec le gain net attendu, soit fournir une analyse de risque montrant que le stop actuel à 44 % est acceptable pour la stratégie.  
**CE QUI ME FERAIT CHANGER D'AVIS** : Une mesure montrant que la médiane du délai de lecture du prix est ≤ 0,8 s sur une période de 24 h de trading live.  

---  
**Détails des chiffres fournis**  

- Latence lecture prix : **médiane 1,057 s**, p90 **2,020 s**, part < 1 s **22,8 %** → **MESURÉ** (échec à la barre < 1 s).  
- Fréquence de scrutation : `POLL_SEC = 20 s` → **MESURÉ** (config).  
- Âge du prix à la décision (journal vivant) : médiane **0,00 s**, max **37,0 s** → **MESURÉ**.  
- Décisions de sortie avec tag `_impact_av…` (prix frais GO 2) : **0** → **MESURÉ** (aucun stop depuis GO 2).  
- Espérance `cooling` : **+0,605 $/trade** (n=12) → **MESURÉ** (net à la main).  
- Source bougies MEXC : API vérifiable, hash SHA‑256 fournis → **MESURÉ**.  
- Formule stop RIZE : `stop = max(8,0 ; cadence × 0,80)` → **MESURÉ** (code + config).  
- Médiane cadence RIZE : **16,88 %**, max **55,58 %** → **MESURÉ** (journal).  
- Stop RIZE résultant : médiane **13,50 %**, pire **44,46 %** → **MESURÉ** (dérivée).  
- Plafond 15 % sur RIZE : réduction drawdown mesurée **−1,87 $ → −0,99 $** (‑47 %) sur 2 trades → **MESURÉ** (bougies 1 min).  
- Effet portefeuille plafond 15 % : **+0,87 $** sur **+32,97 $** net → **MESURÉ** (recalcul).  
- Audit des autres planchers : vérifié que le motif porte toujours une valeur > plancher → **MESURÉ** pour les cas examinés, **INFORMATION INSUFFISANTE** pour audit complet motif‑par‑motif.  
- Délai de stop après GO 2 : aucun stop observé depuis mise en vol → **INFORMATION INSUFFISANTE**.  
- Âge × glissement : aucune observation depuis GO 2 → **INFORMATION INSUFFISANTE**.  

Toute présentation d’un estimé comme fait a été évitée ; les incertitudes ont été étiquetées.  

---  
**FIN**
