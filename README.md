MÉTÉO & ACTIVITIES

Description

MÉTÉO & ACTIVITIES est une application web qui propose des suggestions d’activités en fonction des conditions météorologiques dans une ville donnée. L’utilisateur entre le nom d’une ville, et l’application fournit des informations telles que la température, la description du temps, et la vitesse du vent. Basée sur ces données, l’application recommande des activités adaptées (intérieur ou extérieur).

Fonctionnalités principales :
	•	Recherche météorologique : Affiche la température, la description du temps et la vitesse du vent pour une ville donnée.
	•	Suggestions d’activités : Recommande des activités en fonction de la météo.
	•	Interface simple et attrayante avec un arrière-plan personnalisé.
	•	Gestion des données sécurisée avec csrf_token.

Technologies utilisées
	•	Backend : Django (Python)
	•	Frontend : HTML5, CSS
	•	API météo : Une API externe pour récupérer les données météorologiques.
	•	Base de données : SQLite (intégrée à Django)

Fonctionnement de l’application
	1.	L’utilisateur entre le nom d’une ville dans le champ de recherche.
	2.	Une requête est envoyée au backend, qui interagit avec l’API météo.
	3.	Les informations météorologiques sont récupérées et affichées à l’écran :
	•	Température
	•	Description du temps
	•	Vitesse du vent
	4.	Selon la température, des activités adaptées sont suggérées
Installation et exécution
	1.	Cloner le projet :
      git clone (https://github.com/Marionne2005/PROJET_API.git)
  2.	Se déplacer dans le répertoire du projet :
      cd MeteoAndActivities
  3.	Créer un environnement virtuel :
        python -m venv env
        source env/bin/activate   # Sur Linux/macOS
        env\Scripts\activate      # Sur Windows
  4.	Installer les dépendances :
       pip install -r requirements.txt

  5.	Configurer les clés d’API :
	     •	Ajouter la clé de votre API météo dans un fichier settings.py ou .env.
	6.	Lancer le serveur :
       python manage.py runserver
  7.	Accéder à l’application :
	    •	Ouvrez votre navigateur et rendez-vous sur : http://127.0.0.1:8000/
Améliorations futures
	•	Ajouter une carte interactive pour localiser les villes.
	•	Permettre à l’utilisateur de sauvegarder ses villes préférées.
	•	Ajouter des recommandations d’activités plus détaillées (par exemple, musées, parcs, événements locaux).
	•	Traduction multilingue (par exemple, anglais et français).

Contributeurs
	•	Marionne GANNAVI : Développeuse principale
	•	Toute contribution est la bienvenue ! Veuillez soumettre une pull request pour des améliorations.




