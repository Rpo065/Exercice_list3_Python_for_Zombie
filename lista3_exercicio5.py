'''
5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando 
o algoritmo de Euclides.
'''
while True:
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: ' ))

    if n1 == 0 or n2 == 0 :
        print("Impossível realizar divisão por 0!!! Por favor tente outro número!!")
    else:
        break

if n1>n2:
    numerador = n1
    denominador = n2
else:
    numerador = n2
    denominador = n1


resto = numerador%denominador

while resto != 0.0:
    
    
    numerador = denominador
    denominador = resto
    resto = numerador%denominador
    

print(f"O MDC de {n1} e {n2} é: {denominador}")
