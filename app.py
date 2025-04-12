from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os

from utils import format_message

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Credentials - using consistent naming
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
FRONTEND_URL = os.getenv('FRONTEND_URL')

# Cors
CORS(app, resources={
    r"/send": {
        "origins": [FRONTEND_URL],
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Validate essential config on startup
if not BOT_TOKEN or not CHAT_ID:
    raise ValueError("Missing required environment variables: BOT_TOKEN and CHAT_ID")

@app.route('/send', methods=['POST'])
def send_message():
    if not request.is_json:
        return jsonify({'success': False, 'message': 'Content-Type must be application/json'}), 400

    try:
        data = request.get_json()
        
        required_fields = ['name', 'email', 'content']
        if not all(field in data for field in required_fields):
            missing = [field for field in required_fields if field not in data]
            return jsonify({
                'success': False,
                'message': f'Missing required fields: {", ".join(missing)}'
            }), 400

        message = format_message(data)
        telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }

        try:
            response = requests.post(telegram_url, json=payload, timeout=10)
            response.raise_for_status()
            return jsonify({'success': True, 'message': 'Message sent successfully'}), 200
        except requests.exceptions.RequestException as e:
            app.logger.error(f"Telegram API error: {str(e)}")
            return jsonify({
                'success': False,
                'message': 'Failed to send message to Telegram'
            }), 500

    except Exception as e:
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Internal server error'
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(port=port)