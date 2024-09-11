# Django Chatbot with NLP

This is a basic Django-based chatbot that supports anonymous conversation and responds intelligently based on stored questions and answers. It uses a simple Natural Language Processing (NLP) approach to match user questions with variations stored in the database and provides a randomized answer from a set of possible responses.

## Features

- Anonymous chat system.
- Store multiple variations of a question.
- Randomized response from a list of possible answers.
- Basic NLP for matching similar user questions with stored questions.
- REST API for interacting with the chatbot (e.g., posting user queries, retrieving responses).
- Easy-to-extend with additional NLP features or models.

## Project Structure

- **`chatbot/models.py`**: Defines models for conversations, messages, and question-answer pairs.
- **`chatbot/serializers.py`**: Serializes the data for the API views.
- **`chatbot/views.py`**: Contains the logic for handling user messages and responses.
- **`urls.py`**: API routes for interacting with the chatbot.

## Models

### 1. **Conversation**
Stores conversation history.

- `created_at`: Timestamp when the conversation was started.

### 2. **Message**
Stores individual messages in a conversation.

- `conversation`: ForeignKey to the `Conversation` model.
- `sender`: Denotes who sent the message, either `"user"` or `"bot"`.
- `text`: The actual content of the message.
- `timestamp`: Time when the message was sent.

### 3. **QuestionAnswer**
Stores a question, its variations, and possible answers.

- `question`: The main version of the question.
- `question_variations`: Variations of the question, stored as a comma-separated string.
- `answers`: Multiple answers to the question, stored as a comma-separated string.

## API Endpoints

### 1. **POST** `/chatbot/message/`
Send a user message and get a bot response.

#### Request:
```json
{
    "text": "What do they call you?"
}
```

#### Response:
```json
{
    "answer": "Call me Chatbot."
}
```

### 2. **POST** `/api/question-answer/`
Add a new question-answer pair to the database.

#### Request:
```json
{
    "question": "How's the weather?",
    "question_variations": "Tell me the weather,What's it like outside?,Current weather",
    "answers": "It’s sunny.,Cloudy right now.,Looks like rain."
}
```

#### Response:
```json
{
    "id": 1,
    "question": "How's the weather?",
    "question_variations": "Tell me the weather,What's it like outside?,Current weather",
    "answers": "It’s sunny.,Cloudy right now.,Looks like rain."
}
```

### 3. **GET** `/api/question-answer/`
Retrieve all stored question-answer pairs.

#### Response:
```json
[
    {
        "id": 1,
        "question": "What is your name?",
        "question_variations": "Can you tell me your name?,What's your name?,Who are you?",
        "answers": "My name is Chatbot.,I am called Chatbot.,You can call me Chatbot."
    }
]
```

## Setup and Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/django-chatbot.git
    cd django-chatbot
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser or API testing tool (like Postman) to interact with the chatbot API at `http://localhost:8000/`.

## Usage

- You can interact with the chatbot by sending POST requests to the `/chatbot/message/` endpoint.
- Use the `/api/question-answer/` endpoint to add new question-answer pairs or retrieve the existing data.

## Future Enhancements

- **Improve NLP**: Add advanced NLP libraries like `spaCy` or `transformers` for better question understanding and matching.
- **User Authentication**: Implement user authentication if a non-anonymous chat system is required.
- **Chat UI**: Build a simple front-end chat interface using React or another framework.
- **Logging**: Add logging to keep track of conversations and improve user experience over time.

## License

This project is  licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

