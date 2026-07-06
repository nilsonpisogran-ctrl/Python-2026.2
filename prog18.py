# fazer um codigo que leia o cargo do funcionario
# e, de acordo com o cargo, mostrar o salario obedecendo a tabela abaixo
# caixa = 1500
# vendedor = 2400
# gerente = 4000
# calcule:
    # inss: 12% do salario
    # irrf: se salario maior que 2000, desconto 14%
    #       se salario <= 2000, desconto 8%
    # Salario Final: Salario - inss - irrf

#caixa=1500
#vendedor=2400
#gerente=4000

cargo=input("Digite Cargo....[caixa/vendedor/gerente].............: ").upper()

if cargo == "CAIXA":
   salario = 1500
elif cargo == "VENDEDOR":
     salario = 2400
elif cargo == "GERENTE":
    salario =  4000

inss=(salario * 12 ) / 100
fgts=(salario * 8 / 100)
irrf = 0
if salario > 2000 and salario < 4000:
    irrf = (salario * 8 /100)
elif salario > 2000:
    irrf = (salario * 14/100)

print(f"Seu Salario é {salario}, desconta {inss} de INSS e será depositado em seu FGTS {fgts}, e será descontado {irrf} de IRRF.")
