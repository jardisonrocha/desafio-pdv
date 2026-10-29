
resumo = []
valorDesc = 0
ValorComDesc = 0

while True:
    IdadeDoCliente = int(input("Digite a idade do cliente: "))
    ValorDeCompra = float(input("Digite o valor da compra (Digite 0 para encerrar): RS "))

    if ValorDeCompra == 0:
        break

    if IdadeDoCliente < 0:
        print("A idade digitada não é permitida. Tente novamente!")
        continue

    if ValorDeCompra < 0:
        print("O valor da compra não é permitido. Tente novamente!")
        continue

    valorDesc = 0
    ValorComDesc = ValorDeCompra

    if IdadeDoCliente >= 65:
        valorDesc = ValorDeCompra * 0.20
        ValorComDesc = ValorDeCompra - valorDesc

    if ValorComDesc > 100:
        descontoExtra = ValorComDesc * 0.10
        valorDesc += descontoExtra
        ValorComDesc -= descontoExtra

    print(f"Valor Final: R${ValorComDesc:.2f}")

    resumo.append([ValorDeCompra, valorDesc, ValorComDesc])

print("====RESUMO DO DIA====\n")

quantidadeCompras = len(resumo)
totalBruto = sum(compras[0] for compras in resumo)
totalDesc = sum(compras[1] for compras in resumo)
totalFinal = sum(compras[2] for compras in resumo)

print(f"Quantidade de compras: {quantidadeCompras}")
print(f"Total bruto: R${totalBruto:.2f}")
print(f"Total de descontos: R${totalDesc:.2f}")
print(f"Total final: R${totalFinal:.2f}")
