#Digitar um valor e ao final mostrar a tabuada desse valor.

#print("\n===== IMPRIMIR A TABUADA DO NUMERO DIGITADO =====")

#n1 = int(input("Informe um Numero e Mostre a Tabuada: "))   # digitar o Numero

#for i in range(1,11):
#    r = i * n1
#    linha =  (f"{n1} x {i}  = {r}")  
#    print( linha  )

# Digitar valor e dizer se é Par ou Impar.

#n = int(input("Entre com um Número: "))

#vlr = n % 2
#conec = ""
#if vlr == 1:
#   conec = "IMP" 
#print("O Número é + {conec} + PAR")

# digite 5 numeros e diga se é par ou impar

lista = []

for i in range(1,6):
        
        x = int(input(f"Digite o Numero: "))

        r =int(x) % 2

        
        if r == 1:
           sit = "IMPAR"
        elif r == 0:
           sit = "PAR"  
        
        print(f"O {i}º Numero é : {sit}")
      