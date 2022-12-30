lista_disciplinas = list()

disciplina1 = (0, 'Matematica', 2022.2, ['jose', 'arnaldo'], ['gui', 'luisa'], 60, ([1, 3, 4], 60))
disciplina2 = (1, 'Português', 2021.2, ['val', 'beca'], ['wilton', 'arnaldo'], 50, ([2, 5, 6], 50))

input_string = "1,2,3,4,5"
numbers = input_string.split(",")
numbers = [int(x) for x in numbers]  # converte cada elemento da lista para um inteiro
print(numbers)  # imprime [1, 2, 3, 4, 5]

 
