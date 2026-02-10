#Fazer um programa para ler a distância total (em KM) percorrida por um carro, bem como o total de combústivel gasto
#por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo médio do carro. Com três casas decimais.

distancia_percorrida = float(input('Distância percorrida(Km): '))
combustivel_gasto = float(input('Combustível gasto: '))

consumo_medio = distancia_percorrida / combustivel_gasto

print(f'Consumo médio = {consumo_medio:.3f}')