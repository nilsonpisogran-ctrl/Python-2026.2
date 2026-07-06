# Criar codigo para usuario digitar o ano nascimento;
# e o sistema calcule a idade.
# se idade maior que 18, mostrar "maior de Idade"
# senaõ - " menor de idade"
from datetime import datetime
ano_atual = datetime.now().year
nome = input("Digite Seu Nome: ")
wano_atual = ano_atual
wdatanasc = float(input("Ano do Seu Nascimento........: " ))
widade    = wano_atual - wdatanasc
print(f"{nome} Sua idade é: ", widade)

if widade > 17 and widade < 65:
    print("Melhor Idade")
elif widade > 65:
    print("Idoso")
elif widade >= 18:
    print("Maior de idade")
else:
    print("Menor de Idade, Vaza")