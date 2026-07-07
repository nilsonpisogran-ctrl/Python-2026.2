# Digitar 2 valores e usando if verificar qual o maior

# git add "nomeprograma.py"
# git commit -m  "nomeprograma.py"
# git push -u origin main


#while True:

print("\n===== IMPRIMIR O MAIOR MUMERO DIGITADO =====")


n1 = int(input("Informe 1º Numero: "))
n2 = int(input("Informe 2º Numero: "))

if n1 > n2:
    print (f"{n1} é maior que {n2}")
elif n2 > n1:
    print (f"{n2} é maior que {n1}")

#while opcao not in ("S", "N"):
#        opcao = input("Digite apenas S ou N: ").upper()

#if opcao == "N":
#   break
print("\nPrograma encerrado.")

