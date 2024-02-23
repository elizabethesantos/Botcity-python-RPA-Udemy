numero = 10
texto = "Charles"
verdade = True

# print(numero, texto, verdade)
print('Numero: ' +str(numero), f' Texto: {texto}',f' Verdade: {str(verdade)}')
# print(type(numero), type(texto), type(verdade))

if texto != 'João':
    print(texto)
    print(numero)
else:
    texto = 'Pedro'
    numero = 12
    print(texto)
    print(numero)

funcionarios = ['Pedro', "Charles", 'Maria']

for item in funcionarios:
    print(item)

while numero <= 20:
    print(numero)
    numero = numero +1

def frase():
    print('Curso de RPA!')

frase()

def calculaNumero(num1, num2):
    resultado = num1 + num2
    # print(resultado)
    return resultado

valor = calculaNumero(2, 5)
print(valor)