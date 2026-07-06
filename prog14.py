# Criar codigo para digitar um numero de candidato
# e mostra o candidato
# se não existir digite voto nulo
from datetime import datetime
ano_atual = datetime.now().year

print("=============================")
print("====== URNA ELEITORAL========")
print(f"========{ano_atual}==============")

C1 = int(input("Digite Numero seu Candidato: "))

if C1 == 15:
    print("Juquinha")
elif C1 == 25:
    print("Luizinho")
elif C1 == 36:
    print("Aninha")
else:
    print("Voto Nulo")