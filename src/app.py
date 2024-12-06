import requests
from flask import Flask, render_template, request, Response
from game_state import GameState
from rules import resolve_action
from story_generator import generate_prompt, generate_story_stream
from openai import OpenAI

app = Flask(__name__)

# DeepAI API Key
client = OpenAI(api_key="")

def generate_image(prompt):
    """Génère une image avec DALL-E à partir d'un prompt."""
    try:
        response = client.images.generate(model='dall-e-2',
                                          prompt=prompt,
                                          size='256x256',
                                          n=1,
                                          style='vivid')

        return response.data[0].url

    except Exception as e:
        print(f"Erreur lors de la génération de l'image: {e}")
        return None


# Initialisation du jeu
parameters = {
    "player": {"name": "Hero"},
    "world": {"name": "FantasyLand"}
}
game = GameState(parameters)

@app.route('/')
def index():
    # Affiche l'état initial du jeu
    state = game.get_state()
    return render_template("index1.html", state=state)

@app.route('/action', methods=['GET'])
def action():
    action = request.args.get('action', '').strip()
    if not action:
        return Response("Aucune action fournie.", status=400)

    debut = "nous sommes des pirates."
    state = game.get_state()
    prompt = generate_prompt(state, action, debut)

    # Résolution de l'action et mise à jour de l'état du jeu
    outcome = resolve_action(state, action)
    game.update_state(action, outcome)

    def generate():
        try:
            complete_response = ""  # Accumuler la réponse complète

            # Collecter les chunks de narration
            for chunk in generate_story_stream(prompt, action):
                complete_response += chunk
                yield f"data: {chunk}\n\n"  # Envoyer les chunks narratifs au frontend

            # Générer l'image après la narration
            image_url = generate_image(complete_response)
            if image_url:
                yield f"data: [IMAGE] {image_url}\n\n"  # Envoyer l'URL de l'image au frontend
            else:
                yield f"data: [IMAGE] Erreur lors de la génération de l'image.\n\n"

        except Exception as e:
            yield f"data: Erreur : {str(e)}\n\n"

    return Response(generate(), content_type='text/event-stream')


if __name__ == "__main__":
    app.run(debug=True)
