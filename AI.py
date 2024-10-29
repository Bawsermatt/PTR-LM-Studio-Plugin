# Example: reuse your existing OpenAI setup
from openai import OpenAI
import argparse
import json


with open('config.json', 'r') as f:
    config = json.load(f)


# Configura argparse
parser = argparse.ArgumentParser(description="enter a prompt for the AI")
parser.add_argument("-Ask", type=str, default="ciao", help="""AI.py + -Ask + "Whatever you think" """)

# Analizza gli argomenti
args = parser.parse_args()

# Usa il valore passato
Ask = args.Ask

print("genarating...")
print("")

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key=config['API'])

completion = client.chat.completions.create(
  model=config['Model'],
  messages=[
    {"role": "system", "content": (str("speak in ") + config['Language'])},
    {"role": "user", "content": Ask}
  ],
  temperature=config['Temperature'],
)


print(completion.choices[0].message.content)
