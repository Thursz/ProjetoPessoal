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

    return f'''
    Calculando...
    O resultado é: {num1 + num2}!'''

def subtrair (num1,num2):
    
    return f'''
    Calculando...
    O resultado é: {num1 - num2}!'''

def multiplication(num1,num2):

    return f'''
    Calculando...
    O resultado é: {num1 * num2}!'''

def division(num1,num2):
    if num1 %2 == 0 or num2:
        print('Não é possível realizar divisão por zero!')
    else:
        
        return f'''
    Calculando...
    O resultado é: {num1 / num2}!'''
    
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

def convert(valor,num1,num2) :
    from gtts import gTTS
    import os
    texto = valor(num1,num2)
    if texto == True:
        language = 'en'
        myobj = gTTS(text=texto, lang=language, slow=True)
        myobj.save("resultado.mp3")
        os.system("resultado.mp3")
    else:
        texto = 'Não é possível realizar divisão por zero'
    
def removerUsuario(dados,id,senha):
    if id and senha in dados[id]:
        dados.pop(id,senha)
        print('Usuário removido com sucesso!')
    else:
        print('Não encontrado')