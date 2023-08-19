materias = ["POO", "Banco de Dados", "Inovação"]
alunos = ["Vinicius", "Bruna", "Davi", "Cristian", "Matheus"]

print(
"""*************************************************************
*                      Lista de alunos                      *
*************************************************************"""
)g

for aluno in alunos:
    print("Aluno: %s" % (aluno))
    print("Matérias: ")
    for materia in materias:
        print(" - %s" % (materia))
    print("*************************************************************")
