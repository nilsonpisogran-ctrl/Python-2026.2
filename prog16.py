# fazer um sistema para validar a participação do candidto, onde
# so é permitido inscritos com mais de 18 anos e genero masculino.
#  verificar se o candidato está "Apto" ou "Não Apto".

from datetime import datetime
ano_atual = datetime.now().year

nome = input("Digite Seu Nome.................: ")
genero = input("Digite genero [M] ou [F]......: ").upper()
datnasc = int(input("Ano do Seu Nascimento.......: "))

idade  = (ano_atual - datnasc)

sitacao = "NÃO Apto..."
if idade > 17 and genero == "M":
    situacao = "Apto p/ Serviço"
elif idade > 17 and genero != "M":
    situacao = "Não Apto"

print(f"{nome} Sua idade é: {idade} e sua situação é {situacao} para o serviço ")
