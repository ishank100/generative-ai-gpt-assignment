# AI Study Assistant

A simple Generative AI application built with Python and the OpenAI API.

## Features

- Accepts a study topic from the user
- Generates a simple definition
- Provides a clear explanation
- Gives two real-world examples
- Generates three practice questions

## Technologies

- Python
- OpenAI API
- Generative AI
- Prompt Engineering

## Installation

Install the required package:

```bash
pip install -r requirements.txt
```

## API Key

Set your OpenAI API key as an environment variable.

### Windows PowerShell

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

### macOS/Linux

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Do NOT put your API key directly in `app.py` or upload it to GitHub.

## Run

```bash
python app.py
```

## Example

```text
=============================================
        AI STUDY ASSISTANT
=============================================

Enter a topic to study: Machine Learning

Generating study material...

The application generates:
1. A simple definition
2. A clear explanation
3. Two real-world examples
4. Three practice questions
```

## Project Structure

```text
ai-study-assistant/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Purpose

This project demonstrates how a GPT model can be integrated into a Python application using an API and prompt engineering.
