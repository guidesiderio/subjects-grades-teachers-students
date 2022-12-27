lista_disciplinas = list()
lista_professores = list()
lista_alunos = list()
lista_dias_semana = list()

def mostrar_menu():
    print('--- Mini Controle Acadêmico ---')
    print('1. Cadastrar disciplina')
    print('2. Pesquisar disciplina')
    print('3. Listar disciplinas cadastradas')
    print('4. Cadastrar professor em disciplina')
    print('5. Matricular aluno em disciplina')
    print('6. Lançar notas do aluno em uma disciplina')
    print('7. Listar alunos de uma disciplina')
    print('8. Listar notas dos alunos de uma disciplina')
    print('9. Sair')
    print()

def gerar_codigo_disciplina(lista_disciplinas):
    codigo_disciplina = len(lista_disciplinas) + 1
    return codigo_disciplina

def ler_disciplina(lista_disciplinas):
    codigo = gerar_codigo_disciplina(lista_disciplinas)
    nome = input('Nome: ')
    semestre = float(input('Semestre: '))
    lista_professores = []
    lista_alunos = []
    carga_horaria = int(input('Carga horária: '))
    lista_dias_semana = None
    horario = int(input('Horário: '))

    dados_disciplina = (codigo, nome, semestre, lista_professores, lista_alunos, carga_horaria, lista_dias_semana, horario)

    return dados_disciplina

def inserir_disciplina(dados_disciplina):
    lista_disciplinas.append(dados_disciplina)

def mostrar_disciplinas(lista_disciplinas):    
    for disciplina in lista_disciplinas:
        print(disciplina)

def pesquisar_disciplina(lista_disciplinas, codigo):
    for disciplina in lista_disciplinas:
        if codigo in disciplina:
            print(disciplina)

def gerar_codigo_professor(lista_professores):
    codigo_professor = len(lista_professores) + 1
    return codigo_professor

def ler_professor(lista_professores):
    codigo = gerar_codigo_professor(lista_professores)
    nome = input('Nome: ')    

    dados_professor = (codigo, nome)

    return dados_professor

def inserir_professor_disciplina(lista_disciplinas, dados_professor, codigo):
    lista_disciplinas[codigo - 1][3].append(dados_professor)
    lista_professores.append(dados_professor)

def gerar_matricula_aluno(lista_alunos):
    matricula_aluno = len(lista_alunos) + 1
    str_matricula_aluno = str(matricula_aluno)
    return str_matricula_aluno

def ler_aluno(lista_alunos):
    matricula = gerar_matricula_aluno(lista_alunos)
    nome = input('Nome: ')
    curso = input('Curso: ')

    dados_aluno = (matricula, nome, curso)

    return dados_aluno

def inserir_aluno_disciplina(dados_aluno, codigo):
    lista_disciplinas[codigo - 1][4].append(dados_aluno)
    lista_alunos.append(dados_aluno)  

def mostrar_alunos_disciplina(codigo):
    nome_disciplina = lista_disciplinas[codigo - 1][1]
    alunos_disciplina = lista_disciplinas[codigo - 1][4]
    print(f'Disciplina: {nome_disciplina}, Alunos: {alunos_disciplina}')

mostrar_menu()
ler_opcao = input('Qual a opção? ')
opcao = int(ler_opcao)
while opcao != 9:
    if opcao == 1:
        print('\nCadastrar Disciplina:')
        dados_disciplina = ler_disciplina(lista_disciplinas)
        inserir_disciplina(dados_disciplina)
    if opcao == 2:
        print('\nPesquisar Disciplina:')
        codigo = int(input('Código da disciplina: '))
        pesquisar_disciplina(lista_disciplinas, codigo)
    if opcao == 3:
        print('\nDisciplinas Cadastradas:')
        mostrar_disciplinas(lista_disciplinas)   
    if opcao == 4:
        print('\nCadastrar Professor em Disciplina:')
        codigo = int(input('Código da disciplina: '))
        dados_professor = ler_professor(lista_professores)
        inserir_professor_disciplina(lista_disciplinas, dados_professor, codigo)
    if opcao == 5:
        print('\nCadastrar Aluno em Disciplina')
        codigo = int(input('Código: '))
        dados_aluno = ler_aluno(lista_alunos)
        inserir_aluno_disciplina(dados_aluno, codigo)

    if opcao == 6:
        ...
    if opcao == 7:
        print('\nListar alunos de uma Disciplina:')
        codigo = int(input('Código: '))
        mostrar_alunos_disciplina(codigo)
    if opcao == 8:
        ...
    
    print()
    mostrar_menu()
    ler_opcao = input('Qual a opção? ')
    opcao = int(ler_opcao)    