# Desafio aplicativo de caixa de mercado
# Tabela de referencia
# 001 -> Arroz     R$ 4,00
# 002 -> Feijão    R$ 7,00
# 003 -> MACARRAO  R$ 5,00

arroz = 4
feijao= 7
macarrao = 5
total = 0
#num = 1
situacao = True
while situacao:

    n1 = int(input("Digite Código do Produto: "))
    
    if n1 == 0:
       print(f"Total dos Produto {total}")
       situacao = False
    elif n1 == 1:
        total = total + arroz
        print(f"Arroz : R$ 4,00")
    elif n1 == 2:
        total = total + feijao
        print(f"Feijão : R$ 7,00") 
    elif n1 == 3:
        total = total + macarrao
        print(f"Macarrão: R$ 5,00")

    print(f"Sub Total dos Produtos {total}")

    