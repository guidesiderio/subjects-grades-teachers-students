lista_disciplinas = list()

disciplina1 = (0, 'Matematica', 2022.2, ['jose', 'arnaldo'], ['gui', 'luisa'], 60, ([1, 3, 4], 60))
disciplina2 = (1, 'Português', 2021.2, ['val', 'beca'], ['wilton', 'arnaldo'], 50, ([2, 5, 6], 50))

lista_disciplinas.append(disciplina1)
lista_disciplinas.append(disciplina2)

nome = 'Guilherme'

disciplina1[3].append('Guilherme')

print(lista_disciplinas[0][3])