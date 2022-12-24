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

lista_disciplinas = []
lista_alunos = []
lista_professores = []

def gerar_codigo_disciplina(lista_disciplinas):
    codigo_disciplina = len(lista_disciplinas) + 1
    lista_disciplinas.append(codigo_disciplina)
    return codigo_disciplina

def gerar_matricula_aluno(lista_alunos):
    matricula_aluno = len(lista_alunos) + 1
    lista_alunos.append(matricula_aluno)
    return matricula_aluno

def gerar_codigo_professor(lista_professores):
    codigo_professor = len(lista_professores) + 1
    lista_professores.append(codigo_professor)
    return codigo_professor    

def ler_dados_professor(lista_professores):
    nome = input('Nome: ')
    codigo = gerar_codigo_professor(lista_professores)

    dados_professor = (codigo, nome)
    return dados_professor

