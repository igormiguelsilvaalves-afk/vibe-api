

import os





response = client.responses.create(
    model="gpt-5-mini",
    input="Responda apenas: Conexão realizada com sucesso!"
)

print(response.output_text)