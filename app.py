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

lista_disciplinas = list()
lista_dias_semana = []

def gerar_codigo_disciplina(lista_disciplinas):
    codigo_disciplina = len(lista_disciplinas) + 1
    return codigo_disciplina

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

def mostrar_disciplinas(lista_disciplinas):    
    for disciplina in lista_disciplinas:
        print(disciplina)

def pesquisar_disciplina(lista_disciplinas, codigo):
    for disciplina in lista_disciplinas:
        if codigo in disciplina:
            print(disciplina)
    
mostrar_menu()
ler_opcao = input('Qual a opção? ')
opcao = int(ler_opcao)
while opcao != 9:
    if opcao == 1:
        dados_disciplina = ler_disciplina(lista_disciplinas)
        inserir_disciplina(dados_disciplina)
    if opcao == 2:
        print('\nPesquisar Disciplina:')
        codigo = int(input('Código: '))
        pesquisar_disciplina(lista_disciplinas, codigo)
    if opcao == 3:
        print('\nDisciplinas Cadastradas:')
        mostrar_disciplinas(lista_disciplinas)   
    if opcao == 4:
        ...
    if opcao == 5:
        ...
    if opcao == 6:
        ...
    if opcao == 7:
        ...
    if opcao == 8:
        ...
    
    print()
    mostrar_menu()
    ler_opcao = input('Qual a opção? ')
    opcao = int(ler_opcao)    