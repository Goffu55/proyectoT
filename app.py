from flask import Flask, jsonify, request

app = Flask(__name__)

from clientes import usuarios

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

@app.route('/test')
def getusuarios():
    return jsonify({"usuarios": usuarios, "message": "Produc's List"})

@app.route('/test/<string:alphanumeric>')
def getProduct(alphanumeric):
    usuariosFound = [usuario for usuario in usuarios if usuario['alphanumeric'] == alphanumeric]
    if (len(usuariosFound)> 0):
        return jsonify({"usuario": usuariosFound[0]})
    return jsonify({"message": "usuario not found"})

@app.route('/test', methods=['POST'])
def addusuario():
    # print(request.json)
    # return 'recieved'
    new_usuario = {
        "name": request.json['name'],
        "phone": request.json['phone'],
        "email": request.json['email'],
        "address": request.json['address'],
        "postalZip": request.json['postalZip'],
        "region": request.json['region'],
        "country": request.json['country'],
        "list": request.json['list'],
        "text": request.json['text'],
        "numberrange": request.json['numberrange'],
        "currency": request.json['currency'],
        "alphanumeric": request.json['alphanumeric']
    }
    usuarios.append(new_usuario)
    return jsonify({"message": "Product Added Succesfully", "usuarios": usuarios})

@app.route('/test/<string:alphanumeric>', methods=['PUT'])
def editusuarios(alphanumeric):
    usuariosFound = [usuario for usuario in usuarios if usuario['alphanumeric'] == alphanumeric]
    if (len(usuariosFound) > 0):
        usuariosFound[0]['name'] = request.json['name']
        usuariosFound[0]['phone'] = request.json['phone']
        usuariosFound[0]['email'] = request.json['email']
        usuariosFound[0]['address'] = request.json['address']
        usuariosFound[0]['postalZip'] = request.json['postalZip']
        usuariosFound[0]['region'] = request.json['region']
        usuariosFound[0]['country'] = request.json['country']
        usuariosFound[0]['text'] = request.json['text']
        usuariosFound[0]['list'] = request.json['list']
        usuariosFound[0]['numberrange'] = request.json['numberrange']
        usuariosFound[0]['currency'] = request.json['list']

        return jsonify({
            "message": "Product Updated",
            "product": usuariosFound[0]
        })
    return jsonify({"message": "Product not found"})

@app.route('/test/<string:alphanumeric>', methods=['DELETE'])
def deleteProduct(alphanumeric):
    usuariosFound = [usuario for usuario in usuarios if usuario['alphanumeric'] == alphanumeric]
    if (len(usuariosFound) > 0):
        usuarios.remove(usuariosFound[0])
        return jsonify({
            "message": "Product deleted",
            "usuarios": usuarios
        })
    return jsonify({"message": "Product not found"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)