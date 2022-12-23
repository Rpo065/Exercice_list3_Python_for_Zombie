'''
2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao 
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''


while True:
    nome = input('Informe o usuário: ')
    senha = input('Informe a senha: ')
    
    if nome == senha:
        print("Senha igual ao Usuário!!!Não permitido!!! Informe novamente")
    else:
        print("Login permitido!!!")
        break
        
