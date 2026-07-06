# Criar codigo para verificar se foi digitado m ou f,
# e mostra por extenso
# se não existir digite Erica Hilton
from datetime import datetime
ano_atual = datetime.now().year

print("=============================")
print("====== QUAL O GENERO / ========")
print(f"========{ano_atual}==============")

C1 = input("Genero...............:").upper()

if C1 == "F":
    print("FEMININO")
elif C1 == "M":
    print("MASCULINO")
else:
    print("INDEFINIDO")

    
print(C1)
