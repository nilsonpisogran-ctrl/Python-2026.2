def saudar_User(x,y):
    print(f"Bem Vindo {sobrenome}, tudo Bem? seu nome é: {nome}")

def soma(v1,v2):
    return(v1 - v2)

def calpercent(x,per):
    return(x * per /100)

def tabuada():
    for n in range(1,10):
        for i in range(n,10):
            print(f" {n} x {i} = {i * n}")
    i = 1        
def situacao(x,y):
    idade = x - y

    if idade >= 18 and idade <= 65:
        print("Maior de Idade")
    elif idade < 18:
        print("Proibido paraMenores")
    elif idade > 65:
        print("Senhor IDOSO")

nome        = input("Digite seu Nome : ")
sobrenome   = input("Entre com ultimo Nome : ")
v1          = int(input("Digite ano Atual formato : 9999 : "))
v2          = int(input("Entre com Ano Nascimento no formato 9999 : "))
v3          = int(input("Entre com Valor para CAlculo de porcentagem : "))
v4          = int(input("Qual % Deseja? : "))

saudar_User(sobrenome, nome)
idade = soma(v1,v2)
print(f"Sua idade é: {idade}")
valor = calpercent(v3,v4)
situacao(v1,v2)
print(f"{valor} é {v4}% de {v3}")
tabuada()
