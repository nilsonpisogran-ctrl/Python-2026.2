# usando while, escreva o código que some os numeros 
# ao serem digitados.
# o programa para ao digitar 0 (zero)
n2 = 0
num = 1
while num != 0:

    n1 =  int(input("Digite o Nome: "))
    
    if n1 == 0:
       print("Saindo Laço While...")
       break

    n2 = n2 + n1
    print(n2)