def mostrar_menu():
    print('--- Mini Controle Acadêmico ---')
    print('1. Cadastrar disciplina')
    print('2. Pesquisar disciplina')
    print('3. Listar disciplinas cadastradas')
    print('4. Cadastrar professor em disciplina')
    print('5. Matricular aluno em disciplina')
    print('6. Lançar notas do aluno em uma disciplina')
    print('7. Listar alunos de uma disciplina')
    print('8. Listra notas dos alunos de uma disciplina')
    print('9. Sair')
    print()

lista_disciplinas = [0]
lista_alunos = [0]
lista_professores = [0]
lista_dias_semana = [0]

def gerar_codigo_disciplina(lista_disciplinas):
    codigo_disciplina = len(lista_disciplinas)
    return codigo_disciplina

def gerar_matricula_aluno(lista_alunos):
    matricula_aluno = lista_alunos[-1] + 1
    lista_alunos.append(matricula_aluno)
    return matricula_aluno

def gerar_codigo_professor(lista_professores):
    codigo_professor = len(lista_professores)
    return codigo_professor    

# def inserir_professor():
#     nome = input('Nome: ')
#     codigo = gerar_codigo_professor(lista_professores)
#     dados_professor = (codigo, nome)
#     lista_professores.append(dados_professor)

def ler_disciplina(lista_disciplinas):
    codigo = gerar_codigo_disciplina(lista_disciplinas)
    nome = input('Nome: ')
    semestre = float(input('Semestre: '))
    lista_professores = None
    lista_alunos = None
    carga_horaria = int(input('Carga horária: '))
    lista_dias_semana = None
    horario = int(input('Horário: '))

    dados_disciplina = (codigo, nome, semestre, lista_professores, lista_alunos, carga_horaria, lista_dias_semana, horario)

    return dados_disciplina

def inserir_disciplina(dados_disciplina):
    lista_disciplinas.append(dados_disciplina)


ler_opcao = input('Digite uma opção: ')
opcao = int(ler_opcao)
while opcao != 9:
    dados_disciplina = ler_disciplina(lista_disciplinas)
    inserir_disciplina(dados_disciplina)

    print(lista_disciplinas)

    dados_disciplina = ler_disciplina(lista_disciplinas)
    inserir_disciplina(dados_disciplina)

    print(lista_disciplinas)