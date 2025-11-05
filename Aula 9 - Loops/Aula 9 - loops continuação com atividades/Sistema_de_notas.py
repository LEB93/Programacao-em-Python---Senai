login_professor = "ABC"
senha_professor = 12345
tentativas = 0

alunos = {}

print("\nSeja bem-vindo ao Sistema de Notas de Alunos")

while tentativas < 3:
    login = input("\nDigite seu login: ")
    senha = int(input("Digite sua senha: "))

    if login == login_professor and senha == senha_professor:
        print("\nAcesso concedido.")
        break  # Sai do loop de tentativas
    else:
        tentativas += 1
        print(f"\nLogin ou senha incorretos. Você tem {3 - tentativas} tentativas restantes.")

# Se o número de tentativas for excedido, bloqueia o sistema
if tentativas == 3:
    print("\nConta bloqueada! Número máximo de tentativas excedido.")
else:
    # Menu principal após o login bem-sucedido
    while True:
        print("\n=== MENU DO SISTEMA ===")
        print("1 - Inserir notas de um aluno")
        print("2 - Ver todas as médias")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("\nDigite o nome do aluno: ").capitalize()
            notas = []

            # Inserir 3 notas para o aluno
            for i in range(1, 4):
                while True:
                    try:
                        nota = float(input(f"Digite a {i}ª nota: "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("A nota deve estar entre 0 e 10.")
                    except ValueError:
                        print("Por favor, insira um valor numérico válido.")

            # Calcula a média do aluno e armazena no dicionário
            media = sum(notas) / len(notas)
            alunos[nome] = media
            print(f"\n✅ Média do aluno {nome} calculada com sucesso.")

        elif opcao == "2":
            if alunos:
                print("\n=== MÉDIAS DOS ALUNOS ===")
                for nome, media in alunos.items():
                    print(f"{nome}: {media:.2f}")
            else:
                print("\nAinda não há alunos cadastrados.")

        elif opcao == "3":
            print("\n👋 Saindo do sistema... Até logo!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")
