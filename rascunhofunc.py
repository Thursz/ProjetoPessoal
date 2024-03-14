def cadastrarAluno(alunos, matricula, nome):
    alunos.append([matricula, nome])

def imprimirAlunos(alunos):
    for aluno in alunos:
        print(f"{aluno[0]} - {aluno[1]}")

def informarNotas(alunos, matricula, nota1, nota2, nota3, nota4):
    for i in range(len(alunos)):
        if alunos[i][0] == matricula:
            alunos[i].append([nota1, nota2, nota3, nota4])

def pesquisarAluno(alunos, nome):
    for aluno in alunos:
        if nome in aluno[1]:
            media = calcularMedia(aluno[2])
            situcao = situcacaoAluno(media)
            print("Matrícula: ", aluno[0])
            print("Nome: ", aluno[1])
            print("Notas: ", aluno[2])
            print("Média: ", media)
            print("Situação: ", situcao)

def relatorioFinal(alunos):
    for aluno in alunos:
        if len(aluno) == 3:
            media = calcularMedia(aluno[2])
            situacao = situcacaoAluno(media)
            print(f"{aluno[0]} - {aluno[1]} | Média: {media} | {situacao}")

def calcularMedia(notas):
    media = sum(notas)/len(notas)
    return media

def situcacaoAluno(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

def excluirAluno(alunos, matricula):
    for i in range(len(alunos)):
        if alunos[i][0] == matricula:
            alunos.pop(i)
            return 'Aluno excluído com sucesso.'
    
    return 'Matrícula inválida!'