from flask  import Flask, request, jsonify
import requests
import geraChaveAcesso
from os import listdir
import json

app = Flask(__name__)

@app.route('/')
def raiz():
    return jsonify({"ConsultaNF":"Bem Vindo, Você pede possíveis notas, Eu te informo a nota certa!"})

@app.route('/consulta', methods=["POST"])
def main():
    dados = request.get_json()
    chaveAcessoArray = geraChaveAcesso.calculaDigitoVerificador(dados)
    print (chaveAcessoArray)

    for chave in (chaveAcessoArray):
        respostaDanfeOnline = consultanf(chave)
        return jsonify({
            "chaveValida": [
                respostaDanfeOnline.get("chave")
            ]
        })




def consultanf(chave):
    #consultando a nota fiscal.
    
    payload = {'chave': chave}
    headers = {
        'authority':'www.danfeonline.com.br',
        'method': 'POST',
        'path':'/key',
        'scheme':'https',
        'accept-encoding':'gzip, deflate, br',
        'origin':'https://www.danfeonline.com.br',
        'referer':'https://www.danfeonline.com.br/',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
        }

    response = requests.post("https://www.danfeonline.com.br/key", data=payload, headers=headers)
    
    # print(response.request.headers)
    # print(response.json())
    return response.json()
    
app.run(debug=True)