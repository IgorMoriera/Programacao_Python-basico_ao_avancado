# Exercício 06

def conversao_temperatura(temperatura_celsius):
    conv_fahrenheit = ((temperatura_celsius*(9/5)) + 32)

    return conv_fahrenheit


# Código principal
temperatura = float(input('Digite o valor da temperatura [ºC]: '))
conv = conversao_temperatura(temperatura)
print(f'O valor de {temperatura}ºC, equivale à {conv}ºF')
