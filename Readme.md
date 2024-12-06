# Jeu d'Aventure - Chatbot avec Génération d'Images

Bienvenue dans le projet "Jeu d'Aventure" où vous explorez un monde fantastique avec un chatbot qui vous guide à travers une histoire générée dynamiquement. Le jeu inclut la génération de texte en temps réel et l'affichage d'images en fonction des événements du jeu.  
N'oubliez pas que le jeu tourne en local pour fonctionner hors connexion, mais cela implique certaines lenteurs dans le modèle, alors soyez patient lors de la génération du texte et des images.

## Table des matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Exécution](#exécution)
- [Utilisation](#utilisation)
- [Technologies utilisées](#technologies-utilisées)
- [Contribuer](#contribuer)

## Prérequis

Avant de commencer l'installation, assurez-vous d'avoir les outils suivants installés sur votre machine :

1. **Python 3.12+** : Vous pouvez télécharger Python [ici](https://www.python.org/downloads/).
2. **Pip** : Le gestionnaire de packages Python pour installer les dépendances.
3. **Clé API OpenAI** : Nécessaire pour la génération d'images avec le modèle DALL-E 2. (partagé par mail et à rajouter dans le fichier `app.py`).

## Installation

1. Installer le LLM :
   1. Installer [Ollama](https://ollama.com/) pour Windows ou Mac.
   2. Inclure Ollama dans le PATH.
2. Installer les dépendances et lancer le projet :
```bash
pip install -r requirements.txt
ollama run llama3.2
```

3. Clé API OpenAI : Vous devez ajouter votre clé API OpenAI dans le fichier app.py à la ligne suivante :
```python
client = OpenAI(api_key="votre_clé_api_openai")
```

4. Lancer le serveur Flask :
```bash
python app.py
```

## Exécution
Une fois le serveur Flask lancé, vous pouvez ouvrir un navigateur et accéder à l'adresse suivante :

```http
   http://127.0.0.1:5000/
```

Vous pourrez commencer à interagir avec le chatbot dans un monde fantastique, générant des histoires et des images en fonction de vos actions.

## Limitations
N'oubliez pas que le jeu tourne en local, ce qui peut entraîner des temps de réponse plus lents, notamment lors de la génération du texte et des images. Soyez patient !

## Utilisation
Une fois l'application en cours d'exécution, vous serez invité à saisir des actions dans un champ de texte. Selon l'action choisie, une réponse dynamique sera générée par le chatbot, accompagnée d'une image correspondante générée par DALL-E 2. Les images et textes sont envoyés et affichés en temps réel grâce à la technologie SSE (Server-Sent Events).

Exemple d'interactions :
1. Action : "Explorer"
- Le narrateur vous décrit l'environnement du jeu.
- Une image générée par DALL-E 2 représentant l'environnement exploré est affichée.
2. Action : "Discuter avec un personnage"
- Le narrateur crée un dialogue et vous guide dans l'interaction avec les personnages.

## Génération d'images :
Les images sont générées en fonction des événements ou de l'environnement décrit dans le texte du chatbot. Par exemple, lorsque vous effectuez une action, le texte généré est envoyé à l'API DALL-E 2 d'OpenAI pour produire une image en réponse à la description. Cette image est ensuite affichée sur le frontend de l'application.

## Technologies utilisées
- Flask : Un micro-framework Python pour créer l'application web.
- OpenAI DALL-E 2 : Modèle d'OpenAI pour la génération d'images à partir de texte.
- LLama : Un modèle de langage pour générer du texte et de la narration en fonction des actions du joueur.
- HTML/CSS/JavaScript : Pour l'interface utilisateur et l'affichage dynamique des messages.
- SSE (Server-Sent Events) : Pour transmettre en temps réel les événements et les images au frontend.