numero1 = int(input('Digite o 1° número: '))
numero2 = int(input('Digite o 2° número: '))
par = 0

if numero2 < numero1:
    primeiro = numero2
    segundo = numero1

else:
    primeiro = numero1
    segundo = numero2

while primeiro <= segundo:
    if primeiro % 2 == 0:
        par += 1
    primeiro += 1

print(f'Existem {par} números pares entre os números escolhidos!/')