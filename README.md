# Python AI Research Agent

This is a simple command-line AI research assistant built with Python, LangChain, and OpenAI.

The goal of this project was to understand how AI agents work, how they can use tools, and how to structure their final response into a clean format. The agent can take a research question, search for information, generate a summary, list sources, and optionally save the result to a text file.

## Features

- Ask a research question from the terminal
- Uses an OpenAI chat model through LangChain
- Can search the web for information
- Returns structured results using Pydantic
- Can save the research output to a local `.txt` file
- Uses environment variables to keep API keys private

## Tech Stack

- Python
- LangChain
- OpenAI API
- Pydantic
- DuckDuckGo Search
- python-dotenv
