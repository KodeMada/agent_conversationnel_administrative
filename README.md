Equipe chargé de la digitalisation de l’Administration publique
Le 28/05/2025
Compte Rendu sur la lecture des ressources pour le projet data L2 MIT

### Introduction
Dans le cadre du projet **Data**, notre équipe, chargée de la **digitalisation de l’Administration publique**, a été invitée à consulter un ensemble de ressources variées (documents PDF, pages web et vidéos) afin de mieux comprendre les enjeux, les outils et les approches liés à la gestion et à l’exploitation des données publiques.  
Le présent **compte rendu** a pour objectif de **synthétiser les informations principales** tirées de ces lectures et visionnages, tout en y apportant **notre propre réflexion et raisonnement**.  
### Résumé et synthèse

Dans la ressource **"Appel à manifestation d'intérêt (AMI)« Solutions d'IA pour le public »"**,    on a constaté 2 principaux enjeux : les  obstacles à  l'intégration de l'IA et de la digitalisation dans les services publics ainsi que les possibles solutions à ces défis.

Les principaux obstacles:
1) la méfiance envers l’IA et la crainte de ses effets sur l’emploi
2) nécessité d'infrastructure et formation d'agents publics
3) Les enjeux réglementaires, sécurité de données et éthique

Les solutions applicatives pour les administrations:
1) Agent conversationnel pour interagir avec les usagers
2) Outils de traduction automatique pour les services multilingues
3) Speech-to-text permettant de formalisé en document les échanges oraux
4) Synthèse et analyse de texte dans la prise de décision 
5) Détection de fraude et d'anomalie
6) Aide à la production et à l’optimisation de code informatique

## Réflexions

##  Objectifs de l'agent conversationnel

- **Informer les citoyens** sur leurs droits et obligations.
    
- **Guider** les usagers dans les démarches administratives.
    
- **Répondre aux questions juridiques simples** (par ex. droit foncier, état civil, droit du travail).
    
- **Réduire la charge des agents** de guichets physiques.
    

---

##  Étapes de mise en œuvre

### 1. **Définir les cas d’usage prioritaires**

- Les questions les plus fréquentes des usagers (FAQ).
    
- Les procédures juridiques complexes mais courantes (ex: déclaration de naissance, mariage, titre foncier).
    
- Les services publics concernés (ministères, communes, tribunaux…).
    

### 2. **Collecter les données juridiques pertinentes**

- Textes de loi en vigueur (traduits en malgache si possible).
    
- Guides administratifs.
    
- Modèles de formulaires.
    
- Dialogue-type avec des agents juridiques.
	  
- Créer des annotations Q/A:
	```json
	{"question": "Inona avy ireo antontan-taratasy ilaina amin’ny fisoratana anarana amin’ny tany?", 
	 "answer":   "Ilaina: kopia, titra fananan-tany, rosia fandoavana hetra…"}
  ```



### 3. **Concevoir les dialogues**

Créer des **scénarios conversationnels** simples, par exemple :

- _"Aiza no toerana tokony alehako raha te hanao taratasy fanambadiana?"_
    
- _"Inona avy ireo antontan-taratasy ilaina amin’ny fisoratana anarana amin’ny tany?"_
    

### 4. **Choisir une plateforme technique**

Plusieurs options sont possibles :

- **Plateformes open-source** (Rasa, Botpress) → personnalisables et adaptées pour les langues locales.
    
- **GPT via API** (OpenAI, Mistral ou Claude) → nécessite adaptation linguistique au malgache.

---

##  Entraînement du modèle en malgache

### A. Collecte de corpus en malgache

- Documents juridiques traduits.
    
- Données de conversation réelles (avec anonymisation).
    
- Articles de vulgarisation juridique.
    

### B. Méthodes possibles :

- **Fine-tuning d’un modèle existant** (comme un LLaMA ou Mistral, si ressources disponibles).
    
- **RAG (Retrieval-Augmented Generation)** : le modèle récupère les documents juridiques malgaches pour répondre.
    
- **Traduction automatique + vérification humaine** : traduire la question en français, répondre, puis re-traduire.
    

---

##  Interface utilisateur (plus tard)

- Interface web ou mobile simple, en malgache (possibilité multilingue)
    
- Intégration possible sur les sites gouvernementaux.
    
- Support audio pour les zones à faible alphabétisation (text-to-speech en malgache si il y en a) .
    

---

##  Limites

- Ne jamais fournir de **conseils juridiques personnalisés** (le bot ne remplace pas un avocat).
    
- Les réponses sont **à titre informatif**.
    
- Prévoir une **escalade humaine** vers un juriste pour les cas complexes.


		

