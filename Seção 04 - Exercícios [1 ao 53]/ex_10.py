# Exercício 10

def conversao_velocidade(velocidade):
    conversao = velocidade/3.6

    return conversao


# Código principal
velo = float(input('Digite uma velocidade [Km/h]: '))
conv = conversao_velocidade(velo)
print(f'{velo}Km/h --> {conv}m/s')
