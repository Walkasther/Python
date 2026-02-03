#Aula 06 - Tipos primitivos: String, int, float, bool
#
# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite mais um numero: '))
# s = n1 + n2
# print('A soma entre {} e {} vale {}'.format(n1,n2,s))

#Desafios
# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele

algo = input('Digite algo: ')

print(type(algo))
print('É alfa-numerico? ', algo.isalnum())
print('É uma letra? ', algo.isalpha())
print('É um número? ', algo.isnumeric())
print('É tudo maiúsculo? ', algo.isupper())
print('É somente espaço? ', algo.isspace())
print('É tudo minusculo? ', algo.islower())
print('É ascii? ', algo.isascii())
print('É decimal? ', algo.isdecimal())
print('É um digito? ', algo.isdigit())
print('É um identificador válido? ', algo.isidentifier())
print('Todos os caracteres são imprimíveis? ', algo.isprintable())
print('Está no formato Title Case? ', algo.istitle())











# .isalnum()
# O método .isalnum() é usado para verificar se todos os caracteres de uma string são alfanuméricos (ou seja, apenas letras e números, sem espaços, pontuação ou caracteres especiais).
#
# Retorna True → se todos os caracteres forem letras (a-z, A-Z) ou números (0-9) e a string não estiver vazia.
# Retorna False → se houver espaços, pontuação, símbolos ou a string estiver vazia.
#
#
# 🖋 Exemplo no contexto de um redator com IA
# Imagine que você está criando um redator inteligente que pede ao usuário um título para um texto.
# Você pode usar .isalnum() para garantir que o título não contenha caracteres inválidos.
# Python# Exemplo: Validação de título em um redator com IA
# def validar_titulo(titulo):
#     """
#     Valida se o título contém apenas letras e números.
#     """
#     if titulo.isalnum():
#         return True
#     else:
#         return False
#
# # Simulação de uso no redator
# titulo_usuario = input("Digite o título do seu texto: ")
#
# if validar_titulo(titulo_usuario):
#     print("✅ Título válido! Gerando conteúdo com IA...")
#     # Aqui entraria a lógica de geração de texto com IA
# else:
#     print("❌ Título inválido! Use apenas letras e números, sem espaços ou símbolos.")
#
#
# 🔍 Observações importantes
#
#
# Espaços não são considerados alfanuméricos
#
# "MeuTitulo" → ✅ True
# "Meu Título" → ❌ False (tem espaço)
#
#
#
# Acentos contam como letras
#
# "Café123" → ✅ True
# "Café 123" → ❌ False (tem espaço)
#
#
#
# Uso em IA
#
# Pode ser útil para filtrar entradas antes de enviar para um modelo de IA, evitando erros ou interpretações erradas.
# Em um redator com IA, você pode combinar .isalnum() com outros métodos como .isalpha() (apenas letras) ou .isdigit() (apenas números) para regras mais específicas.










# .isalpha()
# Em Python, o método .isalpha() é usado para verificar se todos os caracteres de uma string são letras do alfabeto (A–Z ou a–z, incluindo letras acentuadas e caracteres de outros alfabetos Unicode).
#
# Sintaxe
# Pythonstring.isalpha()
#
#
# Retorno:
#
# True → se todos os caracteres forem letras e a string não estiver vazia.
# False → se houver números, espaços, símbolos ou a string for vazia.
#
#
#
#
# Exemplos
# Python# Apenas letras
# print("Python".isalpha())       # True
# print("Olá".isalpha())          # True (aceita acentos)
#
# # Contém espaço
# print("Olá Mundo".isalpha())    # False
#
# # Contém número
# print("Python3".isalpha())      # False
#
# # String vazia
# print("".isalpha())             # False
#
#
# Observações importantes
#
# Aceita letras acentuadas e caracteres de alfabetos diferentes (ex.: cirílico, grego, etc.).
# Não ignora espaços — se precisar validar apenas letras ignorando espaços, é necessário removê-los antes:Pythontexto = "Olá Mundo"
# print(texto.replace(" ", "").isalpha())  # True
#
#
# É útil para validação de nomes, filtros de entrada e processamento de texto.











# .isnumeric()
# Em Python, o método .isnumeric() é usado para verificar se todos os caracteres de uma string são números (caracteres numéricos).
# Ele retorna:
#
# True → se todos os caracteres forem numéricos e a string não estiver vazia.
# False → se houver qualquer caractere que não seja numérico ou se a string estiver vazia.
#
#
# Sintaxe
# Pythonstring.isnumeric()
#
#
# string: variável ou literal de texto que você quer verificar.
#
#
# Características importantes
#
# Reconhece dígitos decimais (0 a 9), números em outros sistemas (como números romanos em Unicode) e caracteres numéricos especiais (como frações ½, ², ³).
# Não reconhece sinais (+, -), pontos decimais (.) ou vírgulas (,), pois eles não são caracteres numéricos.
# Funciona apenas com strings — se você passar um número diretamente, precisa convertê-lo para string antes.
#
#
# Exemplos
# Python# Apenas dígitos
# print("12345".isnumeric())   # True
#
# # Números com expoentes Unicode
# print("²³".isnumeric())      # True
#
# # Fração Unicode
# print("½".isnumeric())       # True
#
# # Contém letra
# print("123a".isnumeric())    # False
#
# # Contém espaço
# print("123 456".isnumeric()) # False
#
# # String vazia
# print("".isnumeric())        # False
#
# # Número com ponto decimal
# print("3.14".isnumeric())    # False
#
#
# ✅ Dica:
# Se você quer verificar apenas dígitos de 0 a 9, use .isdigit().
# Se quer verificar se é um número inteiro ou decimal válido, é melhor tentar converter com int() ou float() usando try/except.











# .isupper()
# Em Python, o método .isupper() é usado para verificar se todas as letras alfabéticas de uma string estão em maiúsculas.
# Funcionamento:
#
# Retorna True se todas as letras forem maiúsculas e houver pelo menos uma letra na string.
# Retorna False se houver qualquer letra minúscula ou nenhuma letra (mesmo que haja números, espaços ou símbolos).
#
#
# Sintaxe:
# Pythonstring.isupper()
#
#
# Exemplos:
# Python# Todas as letras maiúsculas
# print("PYTHON".isupper())   # True
#
# # Mistura de maiúsculas e minúsculas
# print("Python".isupper())   # False
#
# # Apenas números e símbolos (nenhuma letra)
# print("123!".isupper())     # False
#
# # Letras maiúsculas com números e símbolos
# print("HELLO123!".isupper()) # True
#
# # String vazia
# print("".isupper())         # False
#
#
# Observações importantes:
#
# Números, espaços e símbolos são ignorados na verificação — apenas letras contam.
# É útil para validação de entrada, por exemplo, verificar se o usuário digitou algo em caixa alta.












# .isspace()
# Em Python, o método .isspace() é usado para verificar se todos os caracteres de uma string são apenas espaços em branco.
# Isso inclui:
#
# Espaço comum (" ")
# Tabulação (\t)
# Quebra de linha (\n)
# Retorno de carro (\r)
# Outros caracteres Unicode classificados como espaço em branco.
#
#
# Sintaxe
# Pythonstring.isspace()
#
#
# Retorna:
#
# True → se todos os caracteres forem espaços em branco e a string não estiver vazia.
# False → se houver qualquer caractere não branco ou se a string for vazia.
#
#
#
#
# Exemplos
# Python# Apenas espaço comum
# print("   ".isspace())   # True
#
# # Espaço + tabulação
# print("\t".isspace())    # True
#
# # Espaço + quebra de linha
# print("\n".isspace())    # True
#
# # Mistura de espaço e letra
# print(" a ".isspace())   # False
#
# # String vazia
# print("".isspace())      # False
#
#
# Uso comum
#
# Validação de entrada: verificar se o usuário digitou apenas espaços.
# Limpeza de dados: detectar campos que parecem preenchidos, mas só têm espaços.
# Processamento de texto: ignorar linhas em branco.









# .islower()
# O método .islower() em Python é usado para verificar se todos os caracteres alfabéticos de uma string estão em minúsculas.
#
# Ele ignora números, espaços e símbolos na verificação.
# Retorna True se pelo menos um caractere alfabético existir e todos estiverem em minúsculas.
# Retorna False caso haja alguma letra maiúscula ou não haja letras.
#
#
# Exemplo de uso:
# Python# Exemplos básicos
# texto1 = "python"
# texto2 = "Python"
# texto3 = "python123"
# texto4 = "12345"
# texto5 = "python com ia"
#
# print(texto1.islower())  # True  -> todas as letras minúsculas
# print(texto2.islower())  # False -> contém 'P' maiúsculo
# print(texto3.islower())  # True  -> letras minúsculas, números ignorados
# print(texto4.islower())  # False -> não há letras
# print(texto5.islower())  # True  -> todas as letras minúsculas, espaços ignorados
#
#
# Uso prático — "Redator com IA"
# Se você estiver criando um redator com IA e quiser verificar se o texto gerado está todo em minúsculas antes de aplicar formatação, pode fazer assim:
# Pythondef verificar_minusculas(texto):
#     if texto.islower():
#         print("✅ O texto está todo em minúsculas.")
#     else:
#         print("⚠️ O texto contém letras maiúsculas.")
#
# # Exemplo
# saida_ia = "este é um texto gerado por ia."
# verificar_minusculas(saida_ia)








# .istitle()
# O método .istitle() do Python é usado para verificar se uma string está no formato Title Case, ou seja, se cada palavra começa com letra maiúscula e as demais letras estão em minúsculo.
# Ele ignora números e símbolos na verificação.
#
# Sintaxe
# Pythonstring.istitle()
#
#
# Retorna: True se a string estiver em Title Case, caso contrário False.
#
#
# Exemplo de uso
# Python# Exemplos de strings
# texto1 = "Python É Incrível"
# texto2 = "Python é Incrível"
# texto3 = "PYTHON É INCRÍVEL"
# texto4 = "Python3 É Incrível"
#
# # Verificando com .istitle()
# print(texto1.istitle())  # True  -> Todas as palavras seguem o padrão
# print(texto2.istitle())  # False -> "é" não começa com maiúscula
# print(texto3.istitle())  # False -> Todas as letras estão maiúsculas
# print(texto4.istitle())  # True  -> Números são ignorados
#
#
# Observações importantes
#
# Sensível a acentos: "Árvore Bonita".istitle() retorna True.
# Palavras pequenas (como "de", "da", "em") também precisam começar com maiúscula para retornar True.
# Útil para validar títulos, nomes próprios ou formatação de textos.
#
#
# Se quiser, posso criar um script em Python com IA que corrige automaticamente um texto para o formato Title Case antes de verificar com .istitle().
# Quer que eu faça isso?







# .isprintable()
# O método .isprintable() em Python é usado para verificar se todos os caracteres de uma string são imprimíveis. Caracteres imprimíveis incluem
#  letras, números, pontuação e espaços — basicamente tudo que você consegue exibir em um terminal ou salvar em texto legível. Caracteres como
#  de linha ( ) ou tabulação (\t) não são considerados imprimíveis.
#
# Sintaxe
# string.isprintable()
# Retorna: True se todos os caracteres da string forem imprimíveis ou se a string for vazia. Caso contrário, retorna False.
# Exemplos práticos
# # Exemplos básicos
# texto1 = "Olá, mundo!"
# print(texto1.isprintable())  # True
#
# texto2 = "Olá
# mundo!"
# print(texto2.isprintable())  # False,
#  não é imprimível
#
# # Strings vazias
# texto3 = ""
# print(texto3.isprintable())  # True
#
# # Todos os caracteres especiais imprimíveis
# texto4 = "1234!$%&*()"
# print(texto4.isprintable())  # True
# Possível uso em um redator com IA
# Se você está construindo um redator com IA, pode por exemplo filtrar ou validar textos gerados para garantir que não contenham caracteres
# que quebrem a formatação ou que não possam ser exibidos:
#
# def validar_texto(texto):
#     if texto.isprintable():
#         print("Texto válido para exibição.")
#     else:
#         print("Atenção: texto contém caracteres não imprimíveis.")
#
# texto_ia = "Gerado pela IA:
# Confidencial"
# validar_texto(texto_ia)  # Avisará sobre caracteres não imprimíveis
# Nesse caso, você consegue capturar quebras de linha ou outros caracteres invisíveis que podem causar problemas em interfaces de usuário ou sistemas que manipulam strings.
# Resumo
# .isprintable() é útil para verificar se uma string é segura de exibir ou armazenar como texto simples.
# Retorna True para strings apenas com caracteres visíveis/imprimíveis e False se houver qualquer caractere “invisível”, como  , \t, etc.
# Ele pode ser facilmente integrado ao fluxo de um redator por IA para validação de conteúdo.








# .isidentifier()
# O método .isidentifier() do Python é usado para verificar se uma string é um identificador válido segundo as regras da linguagem.
# Um identificador é o nome que você pode dar a variáveis, funções, classes, etc., seguindo as regras do Python:
#
# Pode conter letras (Unicode), dígitos e _ (underscore).
# Não pode começar com um dígito.
# Não pode conter espaços ou caracteres especiais como @, -, !, etc.
# Não pode ser uma palavra reservada (if, for, class, etc.).
#
#
# Exemplo prático em Python
# Pythonimport keyword
#
# def validar_identificador(nome: str) -> bool:
#     """
#     Verifica se a string é um identificador Python válido
#     e não é uma palavra reservada.
#     """
#     if not isinstance(nome, str):
#         raise TypeError("O valor deve ser uma string.")
#
#     # Primeiro verifica se é um identificador válido
#     if not nome.isidentifier():
#         return False
#
#     # Depois verifica se não é palavra reservada
#     if keyword.iskeyword(nome):
#         return False
#
#     return True
#
#
# # Exemplos de uso
# testes = ["variavel", "2teste", "meu_teste", "class", "nome!", "_privado"]
#
# for t in testes:
#     print(f"{t!r} -> {validar_identificador(t)}")
#
# Saída:
# 'variavel' -> True
# '2teste' -> False
# 'meu_teste' -> True
# 'class' -> False
# 'nome!' -> False
# '_privado' -> True
#
#
# ✅ Resumo:
#
# .isidentifier() só verifica a forma (sintaxe) do identificador.
# Para garantir que não seja uma palavra reservada, use também keyword.iskeyword().




#isdigit()
# Em Python, o método .isdigit() é usado para verificar se todos os caracteres em uma string são dígitos (0–9 ou outros caracteres de dígito Unicode).
#
# Sintaxe
# Pythonstring.isdigit()
#
#
# Devoluções:
# True → se todos os caracteres são dígitos.
# False → se houver algum caractere que não seja um dígito (incluindo espaços, sinais ou pontos decimais).
#
#
#
#
# Exemplos
# Python# Basic usage
# print("123".isdigit())      # True
# print("00123".isdigit())    # True
# print("12.3".isdigit())     # False (dot is not a digit)
# print("-123".isdigit())     # False (minus sign is not a digit)
# print("²".isdigit())        # True (superscript 2 is considered a digit in Unicode)
#
# # With spaces
# print("123 ".isdigit())     # False (space is not a digit)
#
#
# Anotações importantes
#
# .isdigit() funciona apenas em strings — chamá-lo em números gerará um erro:Pythonnum = 123
# print(str(num).isdigit())  # Convert to string first
#
#
# Ele não reconhece pontos decimais, sinais negativos ou separadores de milhares como dígitos.
# Ele suporta dígitos Unicode (por exemplo, algarismos arábicos, sobrescritos).
#
#
# ✅ Dica: Se você quiser verificar se uma string representa um número inteiro (incluindo negativos), use:
# Pythons = "-123"
# print(s.lstrip('-').isdigit())  # True
#
# Se você quiser verificar se há flutuadores, você pode usar:
# Pythondef is_float(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False
#
# print(is_float("12.3"))  # True





#isascii()
# Em Python, o método .isascii() é um método de string integrado (disponível desde o Python 3.7) que verifica se todos os caracteres na string são caracteres ASCII.
#
# Sintaxe
# Pitãostring.isascii()
#
#
# Devoluções:
# True → se a cadeia de caracteres estiver vazia ou todos os caracteres forem ASCII (pontos de código de 0 a 127).
# False → se algum caractere estiver fora do intervalo ASCII.
#
#
# Exemplo de uso
# Pitão# Basic examples
# print("Hello".isascii())       # True (all ASCII)
# print("12345".isascii())       # True (digits are ASCII)
# print("Olá".isascii())         # False ('á' is not ASCII)
# print("".isascii())            # True (empty string counts as ASCII)
#
# # Mixed characters
# text = "Python3.9!"
# print(text.isascii())          # True
#
# emoji = "Hello 😊"
# print(emoji.isascii())         # False (emoji is not ASCII)
#
#
# Quando usar
#
# Para validar se uma cadeia de caracteres contém apenas caracteres ASCII antes de salvar em um sistema que não dá suporte a Unicode.
# Para filtrar ou limpar texto para protocolos ou formatos de arquivo que exigem ASCII.
#
#
# ✅ Dica: Se você precisar verificar ASCII para bytes em vez de strings, poderá usar:
# Pitãoall(b < 128 for b in byte_data)





# .isdecimal()
# Em Python, o método .isdecimal() é um método de string integrado que verifica se todos os caracteres em uma string são dígitos decimais ().0–9
# Ele retorna:
#
# True → se todos os caracteres são dígitos decimais.
# False → se algum caractere não for um dígito decimal (incluindo espaços, sinais, letras, pontuação ou até mesmo números em outros sistemas numéricos).
#
#
# Sintaxe
# Pitãostring.isdecimal()
#
#
# Exemplo de uso
# Pitão# Basic examples
# print("123".isdecimal())      # True  → all characters are digits
# print("12.3".isdecimal())     # False → '.' is not a decimal digit
# print("-123".isdecimal())     # False → '-' is not a decimal digit
# print("²".isdecimal())        # False → superscript 2 is not decimal
# print("١٢٣".isdecimal())      # True  → Arabic-Indic digits are decimal
#
# # With input validation
# user_input = "456"
# if user_input.isdecimal():
#     print("Valid integer without sign or decimal point.")
# else:
#     print("Invalid number format.")
#
#
# Pontos-chave
#
# Somente os dígitos de 0 a 9 (e dígitos decimais Unicode equivalentes) retornam .True
# Não são permitidos sinais (+/-), pontos decimais e espaços.
# Se você precisar verificar se há números inteiros com sinais, use ou tente converter com dentro de um ..isdigit()int()try/except
# Se você precisar verificar se há floats, não é adequado - use a conversão com tratamento de erros..isdecimal()float()