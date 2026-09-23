# SYNTHÈSE — FAMILLE sur l'AUDIT MEXC × HULK (23/09/2026)

**4 modèles interrogés** (hub local) · **4 réponses** · brief de 5 963 caractères **construit à
partir des JSON des instruments** (aucun chiffre retapé de mémoire) · mission = **CONTREDIRE**,
mes erreurs (E10/E12/E13) explicitement listées dans le brief.

| modèle | verdict | confiance | sa priorité n°1 |
|---|---|---|---|
| Google Gemini | **utile mais incomplet** | 75 % | l'**horodatage** |
| Nemotron-120b | **utile mais incomplet** | 75 % | l'**horodatage** |
| x-ai Grok | **utile mais incomplet** | 75 % | l'**horodatage** |
| DeepSeek-V3 | **utile mais incomplet** | 65 % | l'**horodatage** |

**Aucun ne l'a dit fiable. Aucun ne l'a dit non fiable. Les quatre disent la même chose :
mesure solide, explications en avance sur la mesure.**

---

## 1. Le reproche unanime : j'ai conclu plus loin que mes chiffres

| modèle | ce qu'il attaque | sa raison |
|---|---|---|
| Gemini | le stop « vérification périodique, pas ordre au repos » | **n=32**, et aucune analyse du carnet **au moment de l'impact** |
| Grok | « −3,51 $ sur 39,70 $ (8,8 %) » | ce sont des coûts **ESTIMÉS** (mode paper, aucun frais prélevé) |
| Nemotron | ma conclusion n°1 (cap sur profil figé) | 16/17 profils dérivent, oui — mais **la dérive du profil ne prouve pas** à elle seule l'erreur du cap **en $** : c'est une déduction, pas une mesure |
| DeepSeek | dépassements −16,5 % / −39,2 % | **2 cas extrêmes commentés comme une propriété générale**, et l'impact des trous de données n'est pas quantifié |

⇒ **C'est exactement la même faute que celle que je reproche au moteur** : passer d'un fait mesuré
à une cause non mesurée. Elle est enregistrée au registre comme **classe E14**.

## 2. Le reproche qui vise juste et que je n'avais pas vu (Nemotron)

> « Tu commets une **erreur d'auto-absolution par la confession** : en listant tes erreurs passées
> (E10, E13, E12), tu t'octroies un brevet d'objectivité pour les conclusions que tu tires ensuite —
> **aucun garde-fou `verif_seuil_moteur.py` pour tes propres déductions**. »

**Conséquence appliquée immédiatement** : chaque conclusion de l'audit porte désormais son
étiquette de provenance — **MESURÉ** (lu dans un instrument / une source) · **ESTIMÉ** (modèle de
coût, borne) · **EXTRAPOLÉ** (déduction non mesurée). Un rapport qui mélange les trois sans le dire
est un rapport faux, même quand ses chiffres sont bons.

## 3. Le test qu'ils exigent tous les quatre — et que j'ai passé

> « Mesure l'écart d'horloge entre l'exchange et toi **avant** d'accuser ton cache. »

Fait, le jour même : `probe_prix_mexc_fraicheur.py` (lecture seule).

* **Notre horloge vs l'en-tête HTTP `Date` de MEXC : 0,6 s** → ce n'est pas une horloge folle.
* **Âge du dernier TRADE réel par paire** : **16/20 paires ont échangé dans la dernière minute** ;
  4/20 ont un dernier trade ≥ 1 min (RWAINC **12,9 min**).
* **Verdict corrigé, par paire** : pour les 16 paires liquides, un prix de remplissage vieux de
  2-5 min **n'est PAS expliqué par l'exchange** → c'est **notre chaîne** (H1). Pour les 4 autres,
  le papier a rempli **à un prix qu'aucune contrepartie n'offrait** (H2) — défaut du **paper**.
* **Fait neuf, plus gênant que le retard** : l'écart entre le « dernier prix » et le **milieu du
  carnet** atteint **−90,9 bps sur RIZE** (spread 92,5 bps) et −54,4 bps sur FLUID → sur ces paires,
  le prix utilisé pour remplir est **à 0,5-0,9 % du prix exécutable**, soit **plus que le PnL moyen
  par trade**.

## 4. L'ordre qu'ils imposent (4/4 d'accord sur le premier, 3/4 sur le second)

| rang | chantier | pourquoi (leurs mots) |
|---|---|---|
| **1** | **horodatage du journal** | « tant que l'heure est fausse, toute analyse séquentielle est caduque » (Gemini) |
| **2** | **net de coûts dans le reporting** | « cesser de piloter avec un chiffre brut faux de 8,8 % » (Nemotron) |
| 3 | stop / colonnes / vue live | divergents : Grok met la **vue live en dernier** (« affinage, secondaire »), DeepSeek la met **2e** |

## 5. Critères de changement d'avis (ce qu'ils demandent de mesurer)

1. Rejouer les **124 séquences** avec l'horodatage corrigé : **> 95 % de conformité** des prix
   (Grok) — aujourd'hui **78/100**.
2. **Journaliser l'heure MEXC** (en-tête / champ `timestamp` du carnet) à chaque trade (DeepSeek,
   Gemini, Grok).
3. Montrer que le **PnL net reste positif** après frais + spread **réels par transaction**.
4. Passer le stop en **ordre au repos** et vérifier que les dépassements disparaissent.

## 6. Ce que je retiens (et ce que je ne fais pas sans GO)

**Retenu** : étiquetage de provenance obligatoire · sonde de fraîcheur à **brancher au moment des
remplissages** (pas à un instant arbitraire) · l'écart « ticker vs carnet » doit entrer dans le
jugement de justesse · les 6 colonnes manquantes conditionnent les post-mortems futurs.

**Pas fait** : **aucun** de ces chantiers n'est câblé dans le moteur. Ils attendent le GO de
Christophe, dans l'ordre que la famille propose (l'horodatage d'abord).
