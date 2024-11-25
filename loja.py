import random

# Dicionário de itens da loja
loja = {
    "Caneta": {"preço": 1.0, "quantidade": random.randint(1, 30)},
    "Lapis": {"preço": 2.0, "quantidade": random.randint(1, 15)},
    "Borracha": {"preço": 3.0, "quantidade": random.randint(1, 20)},
    "Caderno": {"preço": 5.0, "quantidade": random.randint(1, 10)},
    "Calculadora": {"preço": 50.0, "quantidade": random.randint(1, 5)},
}

# Função para remover um item
def remover_item(nome_item):
    if nome_item in loja:
        del loja[nome_item]
        print(f"{nome_item} foi removido da loja.")
    else:
        print(f"{nome_item} não encontrado na loja.")

# Função para calcular o número total de itens
def calcular_numero_itens():
    total_itens = 0
    for item in loja.values():
        total_itens += item["quantidade"]
    return total_itens

# Função para criar um novo item
def criar_item(nome_item, preco, quantidade):
    if nome_item not in loja:
        loja[nome_item] = {"preço": preco, "quantidade": quantidade}
        print(f"{nome_item} foi adicionado à loja.")
    else:
        print(f"{nome_item} já existe na loja.")

# Função para calcular o valor total da loja
def calcular_valor_total():
    valor_total = 0
    for item in loja.values():
        valor_total += item["preço"] * item["quantidade"]
    return valor_total

# Função para exibir o menu de ações
def exibir_menu():
    print("\nMenu de Ações:")
    print("1. Remover Item")
    print("2. Calcular Número de Itens")
    print("3. Criar Novo Item")
    print("4. Calcular Valor Total da Loja")
    print("5. Terminar")

# Função principal para rodar a loja
def rodar_loja():
    while True:
        exibir_menu()
        acao = input("Escolha uma opção (1-5): ")

        if acao == '1':
            nome_item = input("Digite o nome do item a ser removido: ")
            remover_item(nome_item)
        elif acao == '2':
            total_itens = calcular_numero_itens()
            print(f"Total de itens na loja: {total_itens}")
        elif acao == '3':
            nome_item = input("Digite o nome do novo item: ")
            preco = float(input("Digite o preço do item: "))
            quantidade = int(input("Digite a quantidade do item: "))
            criar_item(nome_item, preco, quantidade)
        elif acao == '4':
            valor_total = calcular_valor_total()
            print(f"O valor total da loja é: R${valor_total:.2f}")
        elif acao == '5':
            print("Fim da loja.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Rodando a loja
rodar_loja()
