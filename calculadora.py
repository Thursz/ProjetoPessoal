import json

def gravaDados(arquivo,dados):
    arquivo = open(arquivo, 'w')
    dados = json.dumps(dados, indent = 4)
    arquivo.write(dados)
    arquivo.close()

def carregaDados(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    conteudo = arquivo.read()
    arquivo.close()
    if conteudo:
        dados = json.loads(conteudo)
        return dados
    else:
        return {}

def soma (num1,num2):
    soma = num1 + num2
    
    return f'''
    Calculando...
    O resultado é: {soma}!'''

def subtrair (num1,num2):
    subtrair = num1 - num2
    
    return f'''
    Calculando...
    O resultado é: {subtrair}!'''

def multiplication(num1,num2):
    multiplication= num1 * num2

    return f'''
    Calculando...
    O resultado é: {multiplication}!'''

def division(num1,num2):
    if num1 %2 == 0 or num2:
        print('Não é possível realizar divisão por zero!')
    else:

        division = num1 / num2
        return f'''
    Calculando...
    O resultado é: {division}!'''
    
def cadastrarUsuario(dados,id,nome,senha):
    dados[id]= {
        'id': id,
        'nome': nome,
        'senha': senha
    }

def historico(dados,id,senha,teste):
    #fazer verificação de dados! 
    dados[id][senha] = {
        'teste':teste
    }

def informarUsuario(dados):
    for id, nome in dados.items():
        print(f'{id} - {nome['nome']}')
   

