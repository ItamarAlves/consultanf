from flask import request
from datetime import datetime, timedelta

def calculaDigitoVerificador(dados):
    #aqui monto a chave de 43 digitos. 
    #próximo passo, calcular o digito verificador.
    # O dígito verificador da chave de acesso da NF-e é baseado em um cálculo do módulo 11. O
    # módulo 11 de um número é calculado multiplicando-se cada algarismo pela sequência de
    # multiplicadores 2,3,4,5,6,7,8,9,2,3, ..., posicionados da direita para a esquerda.

    #A somatória dos resultados das ponderações dos algarismos é dividida por 11 e o DV (dígito
    #verificador) será a diferença entre o divisor (11) e o resto da divisão:
    #DV = 11 - (resto da divisão)
    cUF = dados.get("cUF")
    emissao = dados.get("AAMM")
    cnpj = dados.get("CNPJ")
    mod = dados.get("mod")
    serie = dados.get("serie")
    nNF = dados.get("nNF")
    nNFFinal = dados.get("nNFFinal")
    tpEmis = dados.get("tpEmis")
    cNF = dados.get("cNF")

    chaveAcesso = ""
    for numeroNf in range(int(nNF),int(nNFFinal)):
        dataEmissao = addDay(emissao)
        emissao = formatDate(dataEmissao)
        chave43 = cUF + emissao[0:5].replace('/', '') + cnpj + mod + serie + prencheNumeroNf(str(numeroNf)) + tpEmis + cNF
        chaveAcesso = chave43

        indice = 2
        chave43 = chave43[::-1]
        soma = 0
        for i in range(len(chave43)):
            valorChaveAcessoSeparado = chave43[i:i+1]
            mult = int(valorChaveAcessoSeparado) * indice
            soma += mult

            indice += 1
            if (indice > 9):
                indice = 2    

        #próximo passo: Dividindo a somatória das ponderações por 11 teremos
        resto = soma % 11
        #Quando o resto da divisão for 0 (zero) ou 1 (um), o DV deverá ser igual a 0 (zero).
        dv = 11 - resto

        if ((resto <= 0 or resto == 1) or dv >= 10):
            dv = 0
                
        chaveAcesso = chaveAcesso + str(dv)
        print(chaveAcesso)

    return chaveAcesso


def addDay(data):
    data = parseDate(data)
    data = data + timedelta(days=1)
    return data

def parseDate(data):
    return datetime.strptime(data, "%d/%m/%Y")

def formatDate(data):
    return data.strftime('%d/%m/%Y')

def prencheNumeroNf(numero):
    size = 9 - len(numero)
    for i in range(0, size):
        numero = '0' + numero
    return numero