# Exercício 03

count = 1
somatorio = 0

while count <= 3:
    num = int(input(f'Digite o {count}º número: '))
    count += 1
    somatorio += num

print('-'*15)
print(f'A soma entre os núemros digitados é: {somatorio}')
