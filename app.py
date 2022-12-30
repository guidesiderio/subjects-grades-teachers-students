lista_disciplinas = list()
lista_professores = list()
lista_alunos = list()
lista_dias_semana = list()
lista_notas_aluno = list()

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
    print('9. Listar alunos de uma disciplina')
    print('10. Mostra professores de uma disciplina')
    print('11. Sair')
    print()

def mostrar_dias_semana_disponiveis():
    print('1 - segunda, 2 - terça, 3 - quarta, 4 - quinta, 5 - sexta, 6 - sábado.')   

def mostrar_horarios_disponiveis():
    print('1 - 8 às 10, 2 - 10 às 12, 3 - 12 às 14, 4 - 14 às 16, 5 - 16 às 18, 6 - 18 às 20 e 7 - 20 às 22.')     

def gerar_codigo_disciplina(lista_disciplinas):
    codigo_disciplina = len(lista_disciplinas) + 1
    return codigo_disciplina

def ler_disciplina(lista_disciplinas):
    codigo = gerar_codigo_disciplina(lista_disciplinas)
    nome = input('Nome: ')
    ano = int(input('Ano: '))
    periodo = int(input('Período: '))
    semestre = ano + (periodo / 10)
    lista_professores = []
    lista_alunos = []
    carga_horaria = int(input('Carga horária: '))
    mostrar_dias_semana_disponiveis()
    dias_semana = input('Dias da semana: ')
    numbers = dias_semana.split(" ")
    numbers = [int(x) for x in numbers]
    mostrar_horarios_disponiveis()
    horario = int(input('Horário: '))

    dados_disciplina = (codigo, nome, semestre, lista_professores, lista_alunos, carga_horaria, numbers, horario)

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

def ler_notas_aluno(codigo, matricula):
    primeira_nota = float(input('Primeira nota: '))    
    segunda_nota = float(input('Segunda nota: '))    
    terceira_nota = float(input('Terceira nota: ')) 

    matricula_aluno = int(matricula)   

    aluno = lista_disciplinas[codigo - 1][4][matricula_aluno - 1]

    notas = [primeira_nota, segunda_nota, terceira_nota]

    notas_aluno = (codigo, aluno, notas)
    return notas_aluno

def inserir_notas_aluno(notas_aluno):
    lista_notas_aluno.append(notas_aluno)

def mostrar_notas_alunos(codigo):
    notas = lista_notas_aluno[codigo - 1]
    print(notas)

def mostra_alunos_disciplina(codigo):
    alunos = lista_disciplinas[codigo - 1][4]

    print(alunos)

def mostra_professores_disciplina(codigo):
    professores = lista_disciplinas[codigo -1][3]

    print(professores)

mostrar_menu()
ler_opcao = input('Qual a opção? ')
opcao = int(ler_opcao)

while opcao != 11:
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
        print('\nLançar Notas de um Aluno em uma Disciplina:')
        codigo = int(input('Código: '))
        matricula = input('Matrícula: ')
        notas_aluno = ler_notas_aluno(codigo, matricula)
        inserir_notas_aluno(notas_aluno)

    if opcao == 7:
        print('\nListar alunos de uma Disciplina:')
        codigo = int(input('Código: '))
        mostrar_alunos_disciplina(codigo)

    if opcao == 8:
        print('\nListar notas dos alunos de uma disciplina:')
        codigo = int(input('Código: '))
        mostrar_notas_alunos(codigo)

    if opcao == 9:
        print('\nAlunos matriculados em uma disciplina:')
        codigo = int(input('Código: '))
        mostra_alunos_disciplina(codigo)  

    if opcao == 10:
        print('\nProfessores de uma disciplina:')
        codigo = int(input('Código: '))
        mostra_professores_disciplina(codigo) 
    
    print()
    mostrar_menu()
    ler_opcao = input('Qual a opção? ')
    opcao = int(ler_opcao)    