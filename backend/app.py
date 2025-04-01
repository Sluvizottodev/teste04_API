from flask import Flask, request, jsonify
from services.operadoras_service import OperadorasService

app = Flask(__name__)
service = OperadorasService('operadoras.csv')

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo', '')
    resultados = service.buscar_operadoras(termo)
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)