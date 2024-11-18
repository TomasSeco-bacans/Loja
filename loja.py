# Dicionário inicial da loja
loja = {
    "produto1": {"nome": "Camisa", "preco": 50, "quantidade": 10},
    "produto2": {"nome": "Calça", "preco": 100, "quantidade": 5},
    "produto3": {"nome": "Sapato", "preco": 200, "quantidade": 2}
}

# 1. Remover um item
loja.pop("produto1", None)

# 2. Calcular número de itens
num_itens = sum(produto["quantidade"] for produto in loja.values())

# 3. Criar um item com listas dentro de dicionários
loja["produto4"] = {"nome": "Meia", "preco": 10, "quantidade": 20, "tamanhos": ["P", "M", "G"]}

# 4. Calcular valor total em loja
valor_total = sum(produto["preco"] * produto["quantidade"] for produto in loja.values())

# 5. Introduzir ações dentro de funções
def atualizar_preco(dicionario, produto, novo_preco):
    if produto in dicionario:
        dicionario[produto]["preco"] = novo_preco

atualizar_preco(loja, "produto2", 120)

# Exibir resultados
print("Dicionário da loja:", loja)
print("Número total de itens:", num_itens)
print("Valor total em loja:", valor_total)
