carros = {}
for i in range (2):
    marca  = input("MARCA  : ")
    modelo = input("MODELO : ")
    ano    = input("ANO : ")
    valor  = int(input("Valor : "))
    
    carros[marca] = modelo, ano, valor
   
    for i in range(1,2):
        print(f"Relatorio Completo : {carros}")









          
