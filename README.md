# Application de gestion de note.

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
python3 config.py
```
## Insertion des données par défauts (Facultatif)
L'insertion des données par défaut est facultative mais recommendé pour un utilisation plus conviviale.
Pour cela dans le dossier racine du projet exécuter la commande suivante:
```bash
python3 default.py
```

## Executer le projet
Danss le dossier racine du projet exécuter la commande suivante:
```bash
python3 __main__.py
```

**Bonne gestion d'ecole Monsieur**