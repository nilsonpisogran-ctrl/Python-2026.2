# Data 10/07/2026
# Cria codigo, para ler nome de 4 alunos com 3 notas;
# Calcular a media e verificar situação
# Situação: Media >= 7 = Aprovado
#           Media >=5 ou <=6 = Recuperação
#           Media < 5 = Reprovado

#for i in range(4): 
 #   aluno = input("Nome do Aluno ")
 #   nt01  = int(input("Primeira Nota: "))
 #   nt02  = int(input("Segunda Nota: "))
 #   nt03  = int(input("Terceira Nota : "))

 #   media = (nt01 + nt02 + nt03) / 3

  #  match True:
  #      case _ if media < 5:
  #          print("REPROVADO")

   #     case _ if media >= 7:
   #         print("APROVADO")

    #    case _ if media >= 5 and media < 7:
    #       print("RECUPERAÇÃO")
    #       print("Sua Média é:", media)
    

# ************************************
nome = ""
lista = ""
for i in range (10):

    nome = nome+str(i)

    nome = input("Entre com nome do produto: ")

    lista = lista + " " + nome
    lista = [lista]

    print(lista)

x = input("Digite o Produto : ")

for x in lista:
    if x in lista:
        print("Produto encontrado", x)

        