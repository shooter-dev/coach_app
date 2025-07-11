# Coach_APP

![Image Coach](static/images/image_1.gif)

# 🎯 Présentation du projet

---

Ce projet est une application web de prise de rendez-vous en ligne développée avec le framework Django (Python).

Elle est destinée à un coach en développement personnel qui souhaite offrir à ses clients une plateforme :

- ✅ Simple à utiliser
- 🔐 Sécurisée grâce à un système d’authentification
- ⚙️ Automatisée dans la gestion des créneaux et des disponibilités

L'application permet à deux types d’utilisateurs d’interagir :

- Les clients : peuvent s’inscrire, se connecter, prendre rendez-vous et consulter leur historique.

- Le coach : peut visualiser tous les rendez-vous, créer des créneaux et annoter les séances passées.

Ce projet a été réalisé dans un contexte pédagogique, avec une durée de développement de 4 à 5 jours, 
dans le cadre d’un travail individuel visant à valider les compétences suivantes :

- Maîtrise de Django (modèles, vues, templates, forms)
- Gestion des utilisateurs et des permissions
- Application des règles métiers
- Organisation d’un dépôt GitHub et présentation orale

# 🛠️ Fonctionnalités principales

---

L’application intègre l’ensemble des fonctionnalités nécessaires à une gestion fluide et automatisée des
rendez-vous entre le coach et ses clients.

### 👤 Authentification
- Création de compte (inscription)
- Connexion / déconnexion sécurisées
- Gestion des sessions utilisateurs
- Redirection vers un dashboard personnalisé selon le rôle (client ou coach)

### 🗓️ Prise de rendez-vous
- Formulaire de création de rendez-vous accessible aux clients
- Affichage dynamique des créneaux disponibles
- Vérification des contraintes horaires (heures autorisées, conflits, délai entre séances)

### 📋 Dashboard client
- Visualisation des séances à venir
- Historique des rendez-vous passés

### 🎯 Dashboard coach
- Vue globale sur tous les rendez-vous
- Ajout de notes personnelles sur chaque séance
- Filtrage par client ou par date

### ⚠️ Gestion des règles métiers
- Plage horaire autorisée : 09h00 à 18h00
- Minimum 10 minutes entre deux rendez-vous
- Un rendez-vous = un seul créneau possible

### ✅ Interface utilisateur simple et responsive
- Navigation claire
- Design basé sur Bootstrap (ou CSS personnalisé)
- Composants réutilisables via un base.html central

# 🧱 Architecture du projet Django

---

Le projet est structuré de manière modulaire autour de trois applications Django distinctes, chacune ayant une responsabilité claire :

### 📁 Structure générale
``` text
coach_app/
├── accounts/            # Gestion des utilisateurs et de l’authentification
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── booking/             # Gestion des prises de rendez-vous
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── services.py
│   ├── urls.py
│
├── dashboard/           # Interfaces personnalisées selon le rôle utilisateur
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│
├── templates/           # Dossier global des templates HTML
│   ├── base.html
│
├── static/              # Fichiers CSS / JS / Images
│   ├── css/
│   ├── js/
│
├── core/           # Répertoire du projet (settings, urls, wsgi)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── app/           # Répertoire du site (urls, views)
│   ├── urls.py
│   ├── views.py
│
├── Makefile             # Automatisation des commandes (run, migrate, test...)
├── manage.py
├── db.sqlite3
```
### 🔄 Flux de navigation simplifié
``` 
Visiteur anonyme → Page d’accueil (accueil.html)
     ↓
Inscription ou Connexion (registred.html | login.html)
     ↓
Dashboard personnalisé :
   - Client → prise de RDV, historique
   - Coach → consultation globale, annotations
```

Cette architecture respecte les bonnes pratiques Django :

- Séparation des responsabilités
- Réutilisabilité des composants
- utilisation de Service
- Organisation claire du code et des fichiers statiques/templates

# 🧩 Technologies et dépendances

---

Ce projet repose sur un environnement Python/Django moderne, renforcé par un outil d’automatisation
(Makefile) pour simplifier les tâches en ligne de commande.

### 🧰 Technologies principales
- Python 3.12	Langage principal du backend
- Django 5.x	Framework web complet pour la gestion des vues, modèles, templates, etc.
- SQLite3	Base de données légère, intégrée par défaut
- Bootstrap 5	(Optionnel) Pour le design responsive et moderne
- HTML5 / CSS3	Création des interfaces utilisateur
- Makefile	Automatisation des commandes courantes (run, migrate, etc.)
### 📦 Dépendances Python (extrait du requirements.txt)
- Django>=5.0
### ⚙️ Commandes automatisées via Makefile
Le projet utilise un fichier Makefile pour fluidifier le développement :

### Commande Fonction

- Lance le serveur Django
``` bash
    make run
```

- Execute makemigration && migrate

``` bash
    make database 
```

# 📈 Perspectives d’évolution (mise à jour)

---

Bien que l’application couvre les fonctionnalités principales, elle peut être enrichie à moyen ou long terme
pour améliorer l’expérience utilisateur, l’automatisation et l’évolutivité.

### 🔔 Notifications et emails automatiques
- Envoi de rappels automatiques avant les rendez-vous
- Confirmation ou annulation par email
- Ces tâches peuvent être traitées de manière asynchrone avec Celery et RabbitMQ pour ne pas bloquer l’expérience utilisateur.

### ⚙️ Intégration de Celery + RabbitMQ
- Utilisation de Celery pour l’exécution différée de tâches lourdes ou périodiques
- RabbitMQ comme broker de messages pour orchestrer la communication entre Django et Celery
- Exemple d’usages :
- Notification quotidienne des rendez-vous du lendemain
- Archivage des séances passées
- Synchronisation avec des calendriers externes

### 📆 Calendrier visuel interactif
- Vue calendrier pour les rendez-vous disponibles
- Intégration possible avec des bibliothèques JS comme FullCalendar

### 💳 Paiement en ligne (Stripe / PayPal)
- Réservation + paiement dans un seul processus
- Facturation automatique

### 📊 Statistiques et reporting
- Nombre de séances par client
- Temps total de coaching
- Export PDF/CSV

### 🧠 Suivi personnalisé du client
- Notes privées pour le coach
- Suivi de l’évolution des objectifs






