import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Carrega as variáveis de ambiente (sua chave API do arquivo .env)
_ = load_dotenv(find_dotenv())

# Inicializa o cliente usando a nova sintaxe da versão 1.0.0+
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    
    # Nova forma de chamar a API
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    
    return response.choices[0].message.content