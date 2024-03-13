#Projeto Calculadora 1.0 by Arthur
from calculadora import *
arquivo = "dados.json"
dados = carregaDados(arquivo)
teste = ''
resultado = ''
while True:
    menu = int(input(('''
Digite a opção desejada:
1- Cadastro de usuário
2- Visualizar histórico da calculadora do usuário
3- Editar informações de usuário
4- Utilizar usuário temp
5- Soma
6- Subtração
7- Multiplicação
8- Divisão 
9- Exportar relatório
10- Remover usuário
11- Informação
0- Sair
Opção desejada:''')))
    if menu == 1:
        id = input('Digite o id do usuário:')
        nome = input('Digite o nome do usuário:')
        senha = input('Crie uma senha:')
        print(cadastrarUsuario(dados,id,nome,senha))
        gravaDados(arquivo,dados)

    elif menu == 2:
        print('Acessando histórico....')
        id = int(input('Confirme o id do usuário:'))
        senha = input('Digite a senha do usuário:')
        teste = input('Digite algo testes:')
        print(historico(dados,id,senha,teste))

    elif menu ==3:
        pass

    elif menu == 5:
        #Soma
        print('Selecionada opção de soma!')    
        num1= float(input('Digite um número:'))
        num2 = float(input('Diite o segundo número:'))
        print(soma(num1,num2))
        print(convert(soma,num1,num2))
        

    elif menu == 6:
        print('Selecionada a opção de subtração!')
        num1= float(input('Digite um número:'))
        num2 = float(input('Diite o segundo número:'))
        print(subtrair(num1,num2))
        print(convert(subtrair,num1,num2))
    
    elif menu == 7:
        num1= float(input('Digite um número:'))
        num2 = float(input('Diite o segundo número:'))
        print(multiplication(num1,num2))
        print(convert(multiplication,num1,num2))

    elif menu == 8:
        num1= float(input('Digite um número:'))
        num2 = float(input('Diite o segundo número:'))
        print(multiplication(num1,num2))
        print(convert(division,num1,num2))
    
    elif menu == 11:
        print(f'''Gerando relatório de usuários....
Aguarde um momento por gentileza!
{"=-" * 20}

              ''')

        print(informarUsuario(dados))
        print(f'''
Relatório de usuários gerados com sucesso!
{"=-" * 20}
              ''')
              
    elif menu == 0:
        print('Saindo...')
        break
    else:
        print('Código inválido ou indisponível!')
