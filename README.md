
# BrewAssistantApp

A Python Flask web app to assist in homebrewing and recipe creation.

## Features

- User registration and login
- Integration with Brewfather API to sync inventory
- Recipe creation using GPT-4 with BJCP styles

## Installation

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `flask run`

## API Keys
- OpenAI API Key: Add to the `app/routes/gpt.py`
- Brewfather API integration is available under `app/routes/brewfather.py`.
