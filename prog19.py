# 200 - "Sucesso!! Tudo certo com sua requisição"
# 400 - "Erro do Cliente: Requisição Mal formada"
# 401 - "403 (erro de Permissão: voce não tem acesso a esta pagina) "
# 404 - "Erro: Página não encontrada"
# 500 | 503 - Erro de servidor: Nosso Sistema está instavel no momento
# para código invalido = Código HTTP dsconhecido

#for i in range(10):

cod = input("Informe o Código: ")
   
match cod:
    case  "200": 
        print("Sucesso!! Tudo certo com sua requisição")
    case  "400": 
        print("Erro do Cliente: Requisição Mal formada")
    case  "401 | 403": 
        print("Erro de Permissão: voce não tem acesso a esta pagina")
    case  "404": 
        print("Erro: Página não encontrada")
    case  "500 | 503": 
        print("Erro de servidor: Nosso Sistema está instavel no momento")
    case _: 
        print("código invalido = Código HTTP dsconhecido")
   