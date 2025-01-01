import os
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
import openai

# Ladda miljövariabler
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key is not set in the .env file")

# Konfigurera OpenAI
openai.api_key = OPENAI_API_KEY

# Skapa Blueprint
bp = Blueprint('gpt', __name__)

@bp.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    """
    Endpoint för att generera ölrecept baserat på användarens input.
    """
    data = request.json
    style = data.get('style', 'IPA')
    flavor_profile = data.get('flavor_profile', 'hoppy and bitter')

    try:
        # Anropa OpenAI API för att generera recept
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a brewing assistant."},
                {"role": "user", "content": f"Create a beer recipe for a {style} with a {flavor_profile} flavor profile."}
            ]
        )
        recipe = response['choices'][0]['message']['content']
        return jsonify({"recipe": recipe})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
