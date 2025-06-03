# 🧠 Projet RAG - Administration Malgache

## ✅ Objectif
Créer un assistant intelligent capable de répondre aux questions administratives malgaches à l’aide de documents officiels (RAG).

---

## 📅 Timeline
**Début :** 3 juin 2025  
**Fin estimée :** 30 juin 2025  
**Équipe :** 5 membres

---

## 🔍 Phase 1 – Collecte de documents [Deadline : 7 juin]

- [ ] Identifier les sites sources fiables (service-public.mg, ministères, lois)
- [ ] Récupérer manuellement les documents utiles (PDF, Word, HTML)
- [ ] Organiser les documents par thème (Identité, État civil, Justice...)
- [ ] Noter les sources et dates de mise à jour

👤 **Responsable : Membre 1 + Membre 2**

---

## 🧹 Phase 2 – Prétraitement [Deadline : 10 juin]

- [ ] Convertir les fichiers en texte brut (.txt)
- [ ] Nettoyer les textes (caractères spéciaux, en-têtes inutiles)
- [ ] Découper les textes en "chunks" (100-300 mots)
- [ ] Ajouter des métadonnées (titre, source, thème)

👤 **Responsable : Membre 2 + Membre 3**

---

## 🧠 Phase 3 – Embedding & Base vectorielle [Deadline : 14 juin]

- [ ] Choisir un modèle d'embedding (OpenAI ou sentence-transformers)
- [ ] Générer les embeddings pour tous les chunks
- [ ] Stocker les embeddings dans une base vectorielle (FAISS ou Chroma)
- [ ] Tester la recherche sémantique simple

👤 **Responsable : Membre 3 + Membre 4**

---

## 🤖 Phase 4 – Intégration LLM (Génération) [Deadline : 18 juin]

- [ ] Choisir le LLM (GPT-4 ou modèle open source)
- [ ] Construire le prompt (avec documents + question)
- [ ] Implémenter la génération avec LangChain ou autre
- [ ] Valider que le modèle répond en se basant sur les documents fournis

👤 **Responsable : Membre 4 + Membre 5**

---

## 🖥️ Phase 5 – Interface utilisateur [Deadline : 23 juin]

- [ ] Choisir le type d’interface (Web ou Chatbot)
- [ ] Implémenter une UI simple (Streamlit / Flask / Telegram bot)
- [ ] Connecter l’interface à la chaîne RAG
- [ ] Tester avec des utilisateurs

👤 **Responsable : Membre 1 + Membre 5**

---

## 🧪 Phase 6 – Évaluation & Amélioration [Deadline : 27 juin]

- [ ] Créer un jeu de questions-réponses tests (20–30 exemples)
- [ ] Vérifier la précision, la clarté et la fiabilité des réponses
- [ ] Ajouter des réponses "ne sait pas" si besoin
- [ ] Corriger les erreurs et améliorer les documents si besoin

👤 **Responsable : Toute l’équipe**

---

## 🚀 Livraison finale [Deadline : 30 juin]

- [ ] Préparer une démo fonctionnelle
- [ ] Documenter le projet (README, fonctionnement, corpus utilisé)
- [ ] Organiser une présentation orale ou enregistrée

👤 **Responsable : Toute l’équipe**

---

## 🗂️ À faire plus tard (Backlog)

- [ ] Ajouter support multilingue (malgache + français)
- [ ] Ajouter un moteur d’actualisation automatique des textes
- [ ] Héberger le système en ligne (cloud / serveur)
