## Criar codigo para usuario digitar um numero;
# 4 notas bimestrais;
# calcular media entre as 4 notas.
# printar a mensagem - " Sua media é : wmedia"

def media_notas(n1,n2,n3,n4):
    media = ( N1 + N2 + N3 + N4) /4
    if media <= 4:
        situacao = "REPROVADO"
    elif media >= 5 and media <= 6:
        situacao = "EM RECUPERAÇÃO"
    elif media >=7:
        situacao = "APROVADO"
    print(f"Sua Media Final foi {media} e voce está : " + situacao)

    
N1 = float(input("Nota primeira Prova  : " ))
N2 = float(input("Nota do trabalho     : " ))
N3 = float(input("Nota Segunda Prova   : " ))
N4 = float(input("Nota de participação : " ))

media_notas(N1,N2,N3,N4)