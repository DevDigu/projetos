#Cálculo imc corporal

peso = float(input('Qual o seu peso?'))
altura = float(input('Qual sua altura?'))

imc = peso / altura ** 2
if imc < 16 and imc <= 18.5:
    print('Você estah abaixo do peso')

elif imc < 18.6 and imc <= 24.9 :
    print('Voce estah dentro do peso ideal')

elif imc < 25 and imc <= 29.9 :
    print('Você estah em sobrepeso')

elif imc < 30 and imc <= 34.9 :
    print('Voce estah obeso GRAU I')

elif imc < 35 and imc <= 39.9 :
    print('Voce estah obeso GRAU II')
else:
    print("Obesidade Grau III")
