from flask import jsonify, Flask, request

app = Flask(__name__)

catalogo = {
    201: {"Codigo": 201, "Producto": "Teclado mecánico RGB", "Precio": 45.00, "Stock": 12},
    202: {"Codigo": 202, "Producto": "Mouse inalámbrico", "Precio": 18.50, "Stock": 25},
    203: {"Codigo": 203, "Producto": "Monitor LED 24", "Precio": 165.00, "Stock": 8}
}

@app.get("/")
def inicio():
    return jsonify(
       {
            "mensaje": "Bienvendio usuario",
            "versión": "1.0",
            "endpoints": [
                "Get / Catalogo",
                "Get / Catalogo / <id>"
            ]      
       }
    )

@app.get("/catalogo")
def obtener_catalogo():
    return jsonify(list(catalogo.values()))

@app.get("/catalogo/<int:id>")
def obtener_producto_por_id(id):
    producto = catalogo.get(id)
    if producto: 
        return jsonify(producto)
    return jsonify({"error": "producto no encontrado :("}), 404

@app.post("/catalogo")
def agregar_producto():
    datos = request.get_json()

    if not datos or "Producto" not in datos or "Precio" not in datos or "Stock" not in datos:
        return jsonify({"error": "Faltan datos necesarios"}), 400
    
    nuevo_id = max(catalogo.keys(), default = 200) + 1

    nuevo_producto = {
        "Codigo": nuevo_id,
        "Producto": datos["Producto"],
        "Precio": datos["Precio"],
        "Stock": datos["Stock"]
    }
    catalogo[nuevo_id] = nuevo_producto
    return jsonify(nuevo_producto), 201

if __name__ == "__main__":
    app.run(debug = True)