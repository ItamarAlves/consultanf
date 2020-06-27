from flask  import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/')
def raiz():
    return jsonify({"r":"Hello, World!"})

@app.route('/consulta', methods=["POST"])
def main():
    dados = request.get_json();
    utils.calculaDigitoVerificador(dados);
    return jsonify(dados);


app.run(debug=True)