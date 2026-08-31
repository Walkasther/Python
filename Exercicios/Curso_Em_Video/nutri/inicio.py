from google import genai


client = genai.Client(api_key="")

arquivo = client.files.upload(file="Plano_alimentar-Mateus_Douglas_De_Azevedo_Serafim.pdf")


prompt = """
Analise o plano alimentar deste PDF.

Quero que você identifique e organize:

1. Todas as refeições;
2. O horário de cada refeição;
3. As opções de cada refeição;
4. Os alimentos de cada opção;
5. A quantidade de cada alimento;
6. A unidade utilizada;
7. O peso em gramas, quando informado;
8. O volume em mililitros, quando informado;
9. As opções de substituição;
10. Os grupos da lista de substituição;
11. As observações importantes.

Não invente informações que não estejam no documento.

Apresente o resultado de forma organizada e fácil de ler.
"""


interaction = client.interactions.create(
    model="gemini-3.7-flash",
    input=[
        arquivo,
        prompt
    ]
)


print(interaction.output_text)