produtos = {}

print("Bem-vindo ao sistema de cadastro de produtos!")

print(
    """

   [C] Cadastrar produto
   [S] Sair do sistema
   [L] Listar produtos cadastrados

      """
)

print(30 * "-")


def deletar_produto():
    nome = input("Digite o nome do produto que dejesar deletar: ").lower().strip()
    if nome in produtos:
        del produtos[nome]
        print(f"Produto {nome} foi deletado com sucesso!")
    else:
        print(f"Produto {nome} não encontrado. Verifique o nome e tente novamente.")


def sistema_cadastro():

    while True:
        opcao = (
            input(
                "Digite [C] para cadastrar, [D] para deletar, [L] para listar ou [S] para sair: "
            )
            .upper()
            .strip()
        )
        if len(opcao) != 1:
            print("Opção inválida. Por favor, escolha uma das letras acima.")
            continue
        if opcao not in ["C", "D", "L", "S"]:
            print("Opção inválida. Por favor, escolha uma das letras acima.")
            continue

        if opcao == "C":
            nome = input("Digite o nome do produto para cadastro: ").lower().strip()

            if not nome.replace(" ", "").isalpha():
                print("Nome inválido. Por favor, insira apenas letras.")
                continue
            try:
                preco = float(input("Digite o preço do produto: ").replace(",", "."))
            except ValueError:
                print("Preço inválido. Por favor, insira  o preço corretamente.")
                continue
            if nome in produtos:
                print(f"Produto {nome} já foi cadastrado.")
                continue

            produtos[nome] = preco
            mennsagem = f"{nome} foi cadastrado com sucesso! o preço é R${preco:.2f}"
            tamanho = len(mennsagem)
            print(tamanho * "-")
            print(mennsagem)

        elif opcao == "D":
            deletar_produto()
        elif opcao == "L":
            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                print("----------produtos cadastrados ja cadastrados------------")
                for produto, preco in produtos.items():
                    print(f"{produto}: R${preco:.2f}")
        elif opcao == "S":
            print("Saindo do sistema. Até logo!")
            break


sistema_cadastro()
