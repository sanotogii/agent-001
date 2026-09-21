import os, argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`

# print(f"User prompt: {args.user_prompt}")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key)
messages = [
    {"role": "user", "content": args.user_prompt},
]
response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,)

# Prompt tokens: X
# Response tokens: Y
print("User prompt: Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
print(f"Prompt tokens: {response.usage.prompt_tokens}")
print(f"Response tokens: {response.usage.completion_tokens}")

print("Response:")
print(response.choices[0].message.content)