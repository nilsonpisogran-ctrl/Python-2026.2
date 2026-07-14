#desenvolver código para digitar peso e altura
# e ao final mostrar o IMC
# IMC = peso x altura ao quadrado
peso = float(input("Digite Peso: " ))
altura = float(input("Digite Altura: "))
IMC = peso / (altura **2) 
print(f"IMC é: {IMC:.2f}")