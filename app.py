
from openai import OpenAI
import os



client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5-mini",
    input="Responda apenas: Conexão realizada com sucesso!"
)

print(response.output_text)