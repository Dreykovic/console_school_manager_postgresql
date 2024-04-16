# Application de gestion de note

## Dépendences

- Avoir PostgreSQL installé
  Lancer les commandes suivantes pour satisfaire les dépendences

```bash
sudo apt update
sudo apt install python3-pip
pip install datetime
pip install python-dotenv
pip install psycopg2-binary
```

## Variables d'environnements

Créer un fichier _.env_ à la racine du projet à partir du _.env.ecemple_

```
cp .env.exemple .env
```

Compléter les variables pour la connection à la base de donnée

## Initialisation

Tout d'abord il faut réinitialisé votre base de donné.
Pour cela dans le dossier racine du projet exécuter la commande suivante:

```bash
psql --file=init.sql
```

## configuration de la bases de données et création des relations

La prochaine étape consiste à configurer la base de donnée, ajouter les **triggers** et les **fonctions** necessaires au bon fonctionnement de l'application.
Pour cela dans le dossier racine du projet exécuter la commande suivante:

```bash
python3 dbconfig.py
```

## Insertion des données par défauts (Facultatif)

L'insertion des données par défaut est facultative mais recommendé pour un utilisation plus conviviale.
Pour cela dans le dossier racine du projet exécuter la commande suivante:

```bash
python3 seed.py
```

## Executer le projet

Danss le dossier racine du projet exécuter la commande suivante:

```bash
python3 __main__.py
```

