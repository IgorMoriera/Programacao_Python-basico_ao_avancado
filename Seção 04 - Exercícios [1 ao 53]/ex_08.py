# Exercício 08

def conversao_temperatura(temperatura_kelvin):
    conv_celsius = (temperatura_kelvin-273.15)

    return conv_celsius


# Código principal
temperatura = float(input('Digite o valor da temperatura [ºC]: '))
conv = conversao_temperatura(temperatura)
print(f'O valor de {temperatura}ºC, equivale à {conv}ºK')
