alunos = []

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    aluno = {
        "nome": nome,
        "idade": idade
    }

    alunos.append(aluno)

print("\nAlunos cadastrados:")

for aluno in alunos:
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print()