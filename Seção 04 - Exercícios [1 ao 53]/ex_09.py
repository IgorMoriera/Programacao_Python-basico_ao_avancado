# Exercício 09

def conversao_temperatura(temperatura_celsius):
    conv_kelvin = (temperatura_celsius+273.15)

    return conv_kelvin


# Código principal
temperatura = float(input('Digite o valor da temperatura [ºK]: '))
conv = conversao_temperatura(temperatura)
print(f'O valor de {temperatura}ºK, equivale à {conv}ºC')
