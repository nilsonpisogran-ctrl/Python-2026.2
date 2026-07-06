# fazer um sistema para validar o acesso a montanha russa
# A pessoa deve ser maior de 12 anos
# A pessoa deve ter um ingreso.
# analisa a idade do visitante e se ele tem ingresso
# mostrar 1: "Acesso liberado, divirta-se", se for maior de 12 anos e tem ingresso
# mostrar 2: " Voce tem ingresso mas não tem idade" 
# mostrar 3: "Acesso negado, é necessario ingresso"


nome=input("Digite Seu Nome.................: ")
idade=int(input("digite sua Idade................: "))
ingresso=input("Possui Ingresso? (S) ou (N)....: ").upper()
msg = ""
if idade > 11 and ingresso == "s":
    msg = "Acesso liberado, divirta-se"
elif idade < 12 and ingresso == "n":
    msg=" Voce tem ingresso mas não tem idade" 
else:
    msg="Acesso negado, é necessario ingresso"
    
print(msg)
