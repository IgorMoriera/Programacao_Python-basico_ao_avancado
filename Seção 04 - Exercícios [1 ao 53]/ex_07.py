# Exercício 07

def conversao_temperatura(temperatura_fahreinheit):
    conv_celsius = ((temperatura_fahreinheit-32)*(5/9))

    return conv_celsius


# Código principal
temperatura = float(input('Digite o valor da temperatura [ºF]: '))
conv = conversao_temperatura(temperatura)
print(f'O valor de {temperatura}ºF, equivale à {conv}ºC')
