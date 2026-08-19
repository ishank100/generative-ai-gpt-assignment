import os
from openai import OpenAI

def main():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OPENAI_API_KEY is not set.")
        print("Set your API key as an environment variable before running.")
        return

    client = OpenAI(api_key=api_key)

    print("=" * 45)
    print("        AI STUDY ASSISTANT")
    print("=" * 45)

    topic = input("\nEnter a topic to study: ").strip()

    if not topic:
        print("Please enter a topic.")
        return

    prompt = f"""
You are an AI study assistant helping a college student.

Topic: {topic}

Provide:
1. A simple definition
2. A clear explanation
3. Two real-world examples
4. Three practice questions

Use simple English and clear headings.
Do not make up facts. If you are uncertain, say so.
"""

    print("\nGenerating study material...\n")

    try:
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-5"),
            input=prompt
        )
        print(response.output_text)

    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
