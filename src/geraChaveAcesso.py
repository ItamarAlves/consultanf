from datetime import datetime
import utils

def calculaDigitoVerificador(dados):
    #aqui monto a chave de 43 digitos. 
    #próximo passo, calcular o digito verificador.
    # O dígito verificador da chave de acesso da NF-e é baseado em um cálculo do módulo 11. O
    # módulo 11 de um número é calculado multiplicando-se cada algarismo pela sequência de
    # multiplicadores 2,3,4,5,6,7,8,9,2,3, ..., posicionados da direita para a esquerda.

    #A somatória dos resultados das ponderações dos algarismos é dividida por 11 e o DV (dígito
    #verificador) será a diferença entre o divisor (11) e o resto da divisão:
    #DV = 11 - (resto da divisão)
    codigoUf = dados.get("codigoUf")
    emissao = dados.get("dataEmissao")
    emissaoTemp = emissao
    cnpj = dados.get("cnpj")
    modelo = dados.get("modelo")
    serie = dados.get("serie")
    numeroNfInicio = dados.get("numeroNfInicio")
    numeroNfFinal = dados.get("numeroNfFinal")
    tipoEmissao = dados.get("tipoEmissao")
    codigoNumerico = dados.get("codigoNumerico")

    qtDias = utils.quantidadeDias(emissao, datetime.today())
    chaveAcessoArray = []
    for numeroNf in range(int(numeroNfInicio),int(numeroNfFinal)+1):

        emissao = emissaoTemp
        for dia in range(0, qtDias):
            dataEmissao = utils.addDay(emissao)
            emissao = utils.formatDate(dataEmissao)
            
            chave43 = codigoUf + emissao[0:5].replace('/', '') + cnpj + modelo + serie + utils.prencheNumeroNf(str(numeroNf)) + tipoEmissao + codigoNumerico
            
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
            chaveAcessoArray.append(chaveAcesso)
            # print(chaveAcesso)

    return chaveAcessoArray
