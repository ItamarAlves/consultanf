from datetime import datetime, timedelta

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

def quantidadeDias(dataInicial, dataFinal):
    qtDias = abs((parseDate(dataInicial) - dataFinal).days)
    return qtDias