# LangChain

## 1. Using Chains

The `1-using-chains` directory demonstrates how to use LangChain's sequential chains to generate code and tests.

### Features

- Generates a short code snippet based on a specified language and task
- Creates a corresponding test for the generated code
- Uses Docker for easy setup and execution

### Usage

1. Ensure you have Docker and Docker Compose installed.
2. Set your OpenAI API key in the `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
3. Navigate to the project root directory and run:

   ```
   ./1-using-chains/app [--language LANGUAGE] [--task TASK]
   ```

   - `--language`: Programming language for the generated code (default: python)
   - `--task`: Description of the task to generate code for (default: generate a random number between 0 and 10)

## 2. Chat App

The `2-chat-app` directory contains a simple chat application using LangChain.

### Features

- Implements a basic chat interface
- Stores conversation history in a JSON file
- Uses Docker for easy setup and execution

### Usage

1. Ensure you have Docker and Docker Compose installed.
2. Set your OpenAI API key in the `.env` file in the project root (if not already done).
3. Navigate to the project root directory and run:
   ```
   ./2-chat-app/app
   ```

This will start the chat application. You can then interact with the AI by typing your messages. The conversation history will be saved in `messages.json`.

To exit the chat, type 'exit' or use Ctrl+C.
