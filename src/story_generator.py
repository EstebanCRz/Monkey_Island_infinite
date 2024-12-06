import ollama
from markdown import markdown

# Journal pour stocker les actions et prompts échangés
history_log = []


def generate_prompt(game_state, action, debut):
    if action == "":
        action = "explore"

    # Récupère les trois derniers prompts/réponses du journal
    last_interactions = history_log[-3:] if len(history_log) >= 3 else history_log
    context = " ".join([f"Player did: {entry['prompt']}. Result: {entry['response']}" for entry in last_interactions])

    # Si aucun historique n'existe
    if not context:
        context = "This is the beginning of the adventure. "+debut
    return f"Context: {context} Action: {action}. Describe the next step."


def log_interaction(prompt, response):
    """Ajoute une interaction (prompt et réponse) au journal."""
    history_log.append({"prompt": prompt, "response": response})


def generate_story_stream(prompt, action):
    """Génère une narration en streaming."""
    if action == "":
        action = "explore"

    # Utiliser Ollama pour obtenir la réponse en streaming
    stream = ollama.chat(
        model='llama3.2',
        messages=[
            {'role': 'system', 'content': "tu es un narrateur, tu narres l'histoire et le décor dans lequel le joueur se trouve, dis ce que le joueur fait et ce qu'il pourrait faire (en fonction de son choix qui est :" + action + " . Raconte en fonction des actions du joueur. Ne fais que 1 à 2 lignes soit environ 30 mots. N'oublie pas que tu parles directement au joueur. La regles la plus importante et que tu dois utiliser l'humour et l'univers du jeu MONKEY ISLANDS dans la génération de l'environnement, des blagues et des interventions narrateur. Soit rigolo casse le 4eme mur et fait des blagues BEAUCOUP de BLAGUE. n'oublie pas c'est un jeu de role"},
            {'role': 'user', 'content': prompt}
        ],
        stream=True,
    )

    # Renvoyer chaque chunk de texte
    for chunk in stream:
        yield chunk['message']['content']

    # Enregistrer l'interaction dans le journal
    log_interaction(prompt, ''.join(chunk['message']['content'] for chunk in stream))
