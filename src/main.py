from flask  import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/')
def raiz():
    return jsonify({"ConsultaNF":"Bem Vindo, Você pede possíveis notas, Eu te informo a nota certa!"})

@app.route('/consulta', methods=["POST"])
def main():
    dados = request.get_json()
    chaveAcesso = utils.calculaDigitoVerificador(dados)
    return jsonify({"chaveAcesso": chaveAcesso})


app.run(debug=True)