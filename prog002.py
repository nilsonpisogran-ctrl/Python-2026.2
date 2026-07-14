# Lista para armazenar os cadastros
cadastros = []

while True:
    print("\n===== CADASTRO DE FUNCIONÁRIOS =====")

    # Entrada de dados
    nome = input("Digite o nome: ")
    salario = float(input("Digite o salário: R$ "))

    # Armazena os dados em um dicionário
    funcionario = { "nome": nome,"salario": salario }

    # Adiciona na lista
    cadastros.append(funcionario)

    # Exibe as 5 últimas ocorrências
    print("\n===== ÚLTIMOS CADASTROS =====")

    # Se houver menos de 5 registros, mostra todos
    inicio = max(0, len(cadastros) - 5)

    for i in range(inicio, len(cadastros)):
        print(f"{i+1} - Nome: {cadastros[i]['nome']} | Salário: R$ {cadastros[i]['salario']:.2f}")

    # Pergunta se deseja continuar
    opcao = input("\nDeseja cadastrar outro funcionário? (S/N): ").upper()

    while opcao not in ("S", "N"):
        opcao = input("Digite apenas S ou N: ").upper()

    if opcao == "N":
        break
        print("\nPrograma encerrado.")