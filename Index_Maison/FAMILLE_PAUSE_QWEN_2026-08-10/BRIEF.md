# BRIEF pause Qwen soumis a la famille — 10/08

CONTEXTE : Systeme ACE777 - Mac 8 Go, hub local 11435 (9 providers gratuits),
29 services launchd. Setup des 3 étages en cours (SPEC V2.1 GO unanime famille).
La consultation avant fusion a conclu : AMELIORER D'ABORD (unanimité
GEMINI + JUGE + CODEUR).

PROPOSITION DE CHRISTOPHE (validée par lui, à soumettre à la famille) :
mettre en PAUSE RÉVERSIBLE les services Qwen-Ollama MAINTENANT, et les
ré-introduire PLUS TARD une fois la fusion faite et ACE testé sur le banc
d'essai (mode probatoire C6 : on ajoute après validation, pas avant).

Pourquoi (raisonnement Christophe) : « j'ai Buffy et le hub à disposition
pour faire bien mieux ce job » — qwen3.5:4b est un petit modèle local (4B) ;
le hub (nvidia deepseek-v4-flash, grok, gemini) fait mieux ce travail.

FAITS RÉELS MESURÉS (brut) :
- Qwen-Ollama (qwen3.5:4b, 3,4 Go sur disque) est utilisé :
  * PROVIDER PRINCIPAL de 5 tâches : ada.sanity, signets.synthese, chat.local,
    qwen.elabore, qwen.btc
  * FALLBACK de 4 tâches Gemini : cortana.brief, audit.protocol, cortana.analyse,
    coffre.ask
- Ollama au repos : ~17 Mo RAM (modèle chargé à la demande) — coût RAM minime.
- Routing actuel (tâches qwen) :
ada.sanity -> qwen-local | fb: gemini
cortana.brief -> gemini | fb: qwen-local
audit.protocol -> gemini | fb: qwen-local
signets.synthese -> qwen-local | fb: gemini
chat.local -> qwen-local | fb: gemini
cortana.analyse -> gemini | fb: qwen-local
coffre.ask -> gemini | fb: qwen-local
qwen.elabore -> qwen-local | fb: gemini
qwen.btc -> qwen-local | fb: gemini
- Modèles Ollama : ['qwen3.5:4b', 'qwen2.5:3b', 'moondream:latest']
- Hub /health : {"status": "ok", "providers": 9}

LA SOLUTION PRÉPARÉE (PAS encore exécutée — soumise pour GO) :
1. Désactiver les 2 services launchd qwen-btc + qwen-elabore
   (plists -> DESACTIVES_2026-08-10/, réversible)
2. Retirer le provider qwen-local du routing hub (5 tâches principales)
3. Basculer les 4 fallbacks Gemini (actuellement qwen-local) vers nvidia/grok
   -> AUCUNE tâche sans filet de secours
4. RIEN n'est supprimé du disque (modèle 3,4 Go conservé, ré-activable)
5. README de ré-introduction (comme Mirofish) : procédure exacte pour
   remettre Qwen après fusion + banc d'essai

QUESTIONS À LA FAMILLE :
1. Cette pause réversible de Qwen-Ollama est-elle SAINE avant la fusion ?
   (simplifie-t-elle la fusion ? y a-t-il un risque à retirer le fallback
   local gratuit ?)
2. Le basculement des 4 fallbacks Gemini vers nvidia/grok est-il le bon choix,
   ou faut-il un autre provider ?
3. La ré-introduction « après fusion + banc d'essai » (mode C6) est-elle la
   bonne temporalité ?
4. Verdict : GO / GO AVEC RESERVES / NON (1 phrase + réserves concrètes).

