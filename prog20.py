# Digitar 2 numeros e mostra o menu abaixo
# Escolha a Opção
# ("1 - Somar")
# ("2 - Subtrair")
# ("3 - Multiplicar")
# ("4 - Dividir")

#for i in range(10):

n1 = int(input("Informe 1º Numero: "))
n2 = int(input("Informe 2º Numero: "))

print ("1 - Somar")
print ("2 - Subtrair")
print ("3 - Multiplicar")
print ("4 - Dividir")

cod=input("Digite Opçao: ")


match cod:
    case  1: 
        print(f" A Soma de {n1} + [n2] é {n1 + n2}" )
    case  2:
        print(f" A Diferença de {n1} + [n2] é {n1 - n2}" ) 
    case  3: 
        print(f" A Multiplicaçã de {n1} + [n2] é {n1 * n2}" ) 
    case  4:
        print(f" A Divisão de {n1} + [n2] é {n1 / n2}" ) 
        