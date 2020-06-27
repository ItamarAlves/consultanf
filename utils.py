from flask import request

def calculaDigitoVerificador(dados):
    cUF = dados.get("cUF")
    emissao = dados.get("AAMM").replace('/', '')
    emissao = emissao[0:4]
    cnpj = dados.get("CNPJ")
    mod = dados.get("mod")
    serie = dados.get("serie")
    nNF = dados.get("nNF")
    nNFFinal = dados.get("nNFFinal")
    tpEmis = dados.get("tpEmis")
    cNF = dados.get("cNF")

    #aqui monto a chave de 43 digitos. 
    chave43 = cUF + emissao + cnpj + mod + serie + nNF + tpEmis + cNF
    chaveAcesso = chave43
    #próximo passo, calcular o digito verificador.
    # O dígito verificador da chave de acesso da NF-e é baseado em um cálculo do módulo 11. O
    # módulo 11 de um número é calculado multiplicando-se cada algarismo pela sequência de
    # multiplicadores 2,3,4,5,6,7,8,9,2,3, ..., posicionados da direita para a esquerda.

    #A somatória dos resultados das ponderações dos algarismos é dividida por 11 e o DV (dígito
    #verificador) será a diferença entre o divisor (11) e o resto da divisão:
    #DV = 11 - (resto da divisão)

    indice = 2
    multiplicador = [2,3,4,5,6,7,8,9]
    chave43 = chave43[::-1]
    soma = 0
    for i in range(len(chave43)):
        valorChaveAcessoSeparado = chave43[i:i+1]
        mult = int(valorChaveAcessoSeparado) * indice
        soma += mult
        #print(int(valorChaveAcessoSeparado))
        #print(" * ")
        #print(indice)

        foiUltimo = True
        for multplica in multiplicador:
            if (multplica > indice and foiUltimo != False):
                indice = multplica
                foiUltimo = False

    #próximo passo: Dividindo a somatória das ponderações por 11 teremos
    resto = soma % 11
    #Quando o resto da divisão for 0 (zero) ou 1 (um), o DV deverá ser igual a 0 (zero).
    if (resto == 0 or resto == 1):
        dv = 0

    dv = 11 - resto
    chaveAcesso = chaveAcesso + str(dv)
    print(chaveAcesso)

    return ""
