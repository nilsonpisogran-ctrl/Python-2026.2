# Imprima as tabuadas de 1 a 10
opcao = " "
n1 = 0
linha = 0
while True:
    #n1 = 0  
    for i in range(1,10):
        r = i
        n1 = i + 1
        print(f"\n===== TABUADA DO {i} =====")

        for i in range(1,11):
            r = i * n1
            linha =  (f"{n1} x {i}  = {r}")  
            print( linha  )

            while opcao not in ("S", "N"):
                opcao = input("Continua ? S ou N: ").upper()
                n1 = 0
                linha = 0

                if opcao == "N":
       
                    print("\nPrograma encerrado.")