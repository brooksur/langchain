# LangChain Code Generator

This project uses LangChain and OpenAI to generate short code snippets based on user input.

## Prerequisites

- Docker and Docker Compose
- OpenAI API key

## Setup

1. Clone this repository.

2. Create a `.env` file in the project root with your OpenAI API key:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. Build the Docker image:

   ```
   docker-compose build
   ```

## Usage

Run the app using the provided `app` script:
