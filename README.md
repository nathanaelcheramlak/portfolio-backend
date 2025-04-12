# Portfolio Contact Form Backend

A Flask-based backend service that receives contact form submissions and forwards them to Telegram. Designed for portfolio websites with secure CORS configuration.

## Features

- 📩 Receives JSON form data (name, email, message)
- ✨ Formats messages with HTML for Telegram
- 🔒 Secure CORS configuration for specified frontend only
- ⚡ Telegram API integration with error handling

## Prerequisites

- Python 3.8+
- Telegram bot token
- Telegram chat ID

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nathanaelcheramlak/portfolio-backend.git
   cd portfolio-backend
   ```

2. Create and activate virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Configuration
Create a .env file in the project root:
    ```bash
    BOT_TOKEN=your_telegram_bot_token
    CHAT_ID=your_telegram_chat_id
    FRONTEND_URL=https://yourportfolio.com
    PORT=8080  # optional
    ```

5. Running the Application
Development
    ```bash
    flask run --port 8080
    ```

## API Endpoint
### POST /send

#### Request Body:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "content": "Hello, I'd like to discuss a project"
}
```
Successful Response (200):

```json
{
  "success": true,
  "message": "Message sent successfully"
}
```

## Author
Written by Nathanael Cheramlak
(Apr 2025)