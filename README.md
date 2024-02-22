# APPLICATION DE GESTION DE TOURNOIS D'ECHECS

## Description du projet
Bienvenue dans l'application de gestion de tournois d'échecs ! Ce projet, réalisé dans le cadre de ma formation Développeur Python sur OpenClassrooms, vise à mettre en pratique divers concepts de programmation orientée objet (POO) ainsi que le modèle vue contrôleur (MVC).
L'objectif fonctionnel de cette application est de permettre la création et la gestion de tournois d'échecs via une interface en ligne de commande.
Les fonctionnalités principales comprennent la saisie des informations du tournoi, l'ajout des joueurs, la génération des tours de jeu avec les matchs correspondants, la saisie des résultats des matchs et l'affichage du classement final des joueurs.

## Mise en place et exécution de l'application
### Prérequis
Python 3.x

### Installation
1. Téléchargement du projet : Téléchargez le projet depuis GitHub en utilisant l'option de téléchargement direct (format zip) ou en clonant le dépôt à l'aide de la commande suivante dans Git Bash : 
```python
git clone https://github.com/Guwoop00/chess_tournament
```
1. Création de l'environnement virtuel : Dans le répertoire du projet, créez un environnement virtuel Python en exécutant la commande suivante dans votre terminal : 
```python
python -m venv env
```
3. Activation de l'environnement virtuel : Activez votre environnement virtuel.
Sous Linux, utilisez la commande : 
```python
source env/bin/activate
```
   Sous Windows, utilisez la commande :
```python
env\Scripts\activate.bat
```
4. Installation des dépendances : Installez les packages Python requis en utilisant la commande suivante :  
```python
pip install -r requirements.txt
```
### Exécution
1. Lancement de l'application : Vous pouvez maintenant exécuter l'application en utilisant l'IDE de votre choix ou directement depuis votre terminal avec la commande 
```python
python main.py
```
3. Navigation dans l'application : L'application se compose de menus successifs. Chaque menu affiche les actions possibles, et vous pouvez interagir en tapant un caractère dans la console suivi de la touche Entrée.

### Génération d'un rapport Flake8
Si vous souhaitez générer un rapport Flake8 pour vérifier que le code est conforme à la PEP8, utilisez la commande suivante :

```python
flake8 --exclude=env --max-line-length=79 --format=html --htmldir=<nom_rapport>
```
