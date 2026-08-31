from google import genai
from pathlib import Path


client = genai.Client(api_key="")

caminho_pdf = Path(__file__).parent / "Plano_alimentar-Mateus_Douglas_De_Azevedo_Serafim.pdf"

arquivo = client.files.upload(
    file=caminho_pdf
)


prompt = """
Analise este plano alimentar.

Quero que você identifique:

1. Todas as refeições;
2. O horário de cada refeição;
3. Os grupos alimentares;
4. As opções de cada grupo;
5. Os alimentos de cada opção;
6. A quantidade de cada alimento;
7. A unidade utilizada;
8. O peso em gramas, quando informado;
9. O volume em mililitros, quando informado;
10. As opções de substituição;
11. Os grupos da lista de substituição;
12. As observações importantes.

Não invente informações que não estejam no documento.

Organize a resposta de maneira clara e hierárquica.
"""


interaction = client.interactions.create(
    model="gemini-3.7-flash",
    input=[
        {
            "type": "document",
            "uri": arquivo.uri,
            "mime_type": arquivo.mime_type
        },
        {
            "type": "text",
            "text": prompt
        }
    ]
)


print(interaction.output_text)