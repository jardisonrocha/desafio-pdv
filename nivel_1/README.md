PDV - Sistema de Ponto de Venda

1. O que o código faz
O programa simula um sistema de Ponto de Venda (PDV), permitindo registrar compras, aplicar descontos de acordo com a idade do cliente e o valor restante da compra, e apresentar um resumo final das vendas.

2. Como o código funciona

1. O programa solicita a idade do cliente e o valor da compra.
2. Se o valor da compra for igual a zero, o programa encerra o registro.
3. Se a idade ou o valor forem negativos, apresenta uma mensagem de erro e solicita os dados novamente.
4. Se o cliente tiver 65 anos ou mais, recebe 20% de desconto sobre o valor original.
5. Após esse desconto, o programa verifica se o valor restante é maior que R$ 100,00. Se for, aplica mais 10%.
6. O programa exibe o valor final e guarda os dados de cada compra em uma lista usando `append()`.
7. Ao finalizar, utiliza `len()` para contar as compras e `sum()` para somar os valores brutos, os descontos e os valores finais.
8. Por último, exibe o resumo do dia.

3. Como executar

É necessário ter o Python instalado.

No terminal, dentro da pasta `nivel_1`, execute:
python pdv.py

Digite `0` no valor da compra para encerrar e visualizar o resumo.

4. Tabela de exemplos

| Caso | Idade | Valor original | Desconto | Valor final |
| 1 | 30 | R$ 50,00 | Sem desconto | R$ 50,00 |
| 2 | 70 | R$ 50,00 | 20% | R$ 40,00 |
| 3 | 30 | R$ 200,00 | 10% | R$ 180,00 |
| 4 | 70 | R$ 200,00 | 20% e mais 10% | R$ 144,00 |
| 5 | 70 | R$ 125,00 | 20%; sem desconto extra | R$ 100,00 |

Observação: o desconto extra de 10% só é aplicado se o valor após o desconto para idosos for maior que R$ 100,00.

5. Resumo final

O sistema automatiza o cálculo dos descontos e organiza as informações das compras, facilitando a conferência dos valores e a visualização do total de vendas do dia.
