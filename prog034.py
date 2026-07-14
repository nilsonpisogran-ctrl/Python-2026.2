senha_correta = "python123"
tentativas = 0
max_tentativa = 3
while tentativas < max_tentativa:
    tentativa = input(f"Digite a senha (tentativa {tentativas + 1} / {max_tentativa} ):")
    if tentativas == senha_correta:
        print("Acesso Permitido")
        break
    else:
        print("Senha Incorreta")
        tentativas += 1
else:
    print("Numero máximo de tentativa, aguarde 1 minuto e tente novamente")