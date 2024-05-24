# Exercício 04

def potenciacao(expoente=1):
    base = int(input('Digite um número: '))
    output = base ** expoente

    return output


# Código principal
calculo = potenciacao(expoente=2)
print(f'O quadrado do número escolhido é: {calculo}')
