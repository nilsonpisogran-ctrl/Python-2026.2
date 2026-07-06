# Criar codigo para usuario digitar um numero;
# 4 notas bimestrais;
# calcular media entre as 4 notas.
# printar a mensagem - " Sua media é : wmedia"
nome = input("Digite Seu Nome: ")
N1 = float(input("Nota primeira Prova  : " ))
N2 = float(input("Nota do trabalho     : " ))
N3 = float(input("Nota Segunda Prova   : " ))
N4 = float(input("Nota de participação : " ))
media = ( N1 + N2 + N3 + N4) /4
print(f"{nome} Sua nota final é: ", media)

if media > 5.9:
    print("Aprovado")
else:
    print("Reprovado")
    