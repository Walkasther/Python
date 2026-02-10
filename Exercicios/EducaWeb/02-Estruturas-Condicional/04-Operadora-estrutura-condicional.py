# Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
# telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
# ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.

minutos = int(input('Digite a quantidade de minutos: '))

valor_a_pagar = 50

if minutos > 100:
    excedente = (minutos - 100) * 2
    valor_a_pagar += excedente

print(f'Valor a pagar: R$ {valor_a_pagar:.2f}')