"""estoque={   "tomate": [ 1000, 2.30],
            "alface": [ 500, 0.45],
			"batata": [ 2001, 1.20],
			"feijão": [ 100, 1.50] }

venda = [ ["tomate", 5], ["batata", 10], ["alface",5] ]
total = 0
print("Vendas:\n")

for operação in venda:
    produto, quantidade = operação 
    preço = estoque[produto][1] 
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
		(produto, quantidade,preço,custo))
    estoque[produto][0] -= quantidade 
    total+=custo
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])"""

estoque = {"tomate": [1000, 2.30],"alface": [500, 0.45],
        "batata": [2001, 1.20],"feijão": [100, 1.50]}

total = 0

for produto in estoque:
    print(produto, "- Preço:", estoque[produto][1], "- Quantidade:", estoque[produto][0])

while True:
    produto = input("Digite o nome do produto que deseja comprar (ou 'fim' para encerrar): ")

    if produto == "fim":
        break

    if produto not in estoque:
        print("Produto não encontrado. Tente novamente.")
        continue

    quantidade = int(input("Digite a quantidade que deseja comprar: "))

    if quantidade > estoque[produto][0]:
        print("Não temos essa quantidade em estoque.")
        continue

    preço = estoque[produto][1]
    custo = preço * quantidade
    estoque[produto][0] -= quantidade
    total += custo

    print("Você comprou", quantidade, produto, "por R$", custo)

    continuar = input("Deseja comprar mais alguma coisa? (sim/não): ")
    if continuar.lower() != "sim":
        break

print("Total da compra: R$", total)
print("\nNobo estoque:")

for produto in estoque:
    print(produto, "- Quantidade:", estoque[produto][0], "- Preço:", estoque[produto][1])