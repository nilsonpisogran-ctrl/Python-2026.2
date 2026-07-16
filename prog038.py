# automatiza uma comanda de restaurante
def exibirnome(nome,cel):
    print(f"Olá {nome}, tudo Bem? seu numero é: {cel}")
    
# Teste Função
for i in range(5):
   exibirnome("Nilson Macedo", "21-964.449.770")
   exibirnome("Telles", "440")



produtos = ["Batata Frita", "Pastel", "Filé Aperitivo", "Torrada", "Franco Passarinho", "Chopp"]
total = 0
situacao = True
while situacao:

    n1 = int(input("Digite Código do Produto: "))

    if n1 == 0:
        situacao == False

        for i in range(1,n1):
            print(produtos[n1])
            print(f"Sub Total da Comanda: {total}")
            print(f"Total da Conta com 10% de Acréscimo {total * 1.1}")
            print(f"Total da Conta com 10% de Desconto {total * .90}")

    n2 = int(input("Digite Valor do Produto: "))

    total = total + n2

print(n1,n2,total)