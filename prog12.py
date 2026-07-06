# Criar codigo para usuario digitar o ano nascimento;
# e o sistema calcule a idade.
# se idade maior que 18, mostrar "maior de Idade"
# senaõ - " menor de idade"
nome = input("Digite Seu Nome: ")
wdataatual = 2026
wdatanasc = float(input("Ano do Seu Nascimento........: " ))
widade    = wdataatual - wdatanasc
print(f"{nome} Sua idade é: ", widade)

if widade >= 18:
    print("Maior de Idade")
else:
    print("Menor de Idade, Vaza")