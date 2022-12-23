'''
1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
seja inválido e continue pedindo até que o usuário informe um valor válido.
'''



while True:
    nota = float(input("Informe uma nota de 0 a 10: "))
    if nota<0 or nota >10:
        print("Nota invalida!!! Por favor informe uma nota valida!")
    else:
        break

print(f'Parabéns!! A nota {nota: .2f} é valida') 
