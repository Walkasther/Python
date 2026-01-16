notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print(notas)
print('notas 7: {}'.format(notas.count(7)))
notas[-1] = 4
print(notas)
print('nota mais alta: {}'.format(max(notas)))
notas.sort()
print(notas)

media = sum(notas) / len(notas)

print('média: {:.2f}'.format(media))