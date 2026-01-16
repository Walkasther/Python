import math  # Importa o módulo math para usar funções matemáticas

# Solicita ao usuário os coeficientes da equação de segundo grau
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

# Calcula o valor de delta (discriminante)
delta = b ** 2 - 4 * a * c

# Verifica se delta é maior ou igual a zero para determinar se há raízes reais
if delta >= 0 :
    # Calcula as raízes reais usando a fórmula de Bhaskara
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"X1: {x1:.4f}")  # Exibe a primeira raiz formatada com 4 casas decimais
    print(f"X2: {x2:.4f}")  # Exibe a segunda raiz formatada com 4 casas decimais

else:
    # Caso delta seja negativo, informa que não há raízes reais
    print("Esta equação não possui raízes reais")
