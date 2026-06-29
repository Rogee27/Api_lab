from flask import jsonify, Flask, request

app = Flask(__name__)

catalogo = {
    201: {"Codigo": 201, "Producto": "Teclado mecánico RGB", "Precio": 45.00, "Stock": 12, "Categoria": "Teclados"},
    202: {"Codigo": 202, "Producto": "Mouse inalámbrico", "Precio": 18.50, "Stock": 25, "Categoria": "Mouse"},
    203: {"Codigo": 203, "Producto": "Monitor LED 24", "Precio": 165.00, "Stock": 8, "Categoria": "Monitores"}
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

    if not datos or "Producto" not in datos or "Precio" not in datos or "Stock" not in datos or "Categoria" not in datos:
        return jsonify({"error": "Faltan datos necesarios"}), 400
    
    if datos["Precio"] < 0 :
        return jsonify({"error": "El Precio no puede ser negativo"}), 400
    
    if datos["Stock"] < 0 :
        return jsonify({"error": "El Stock no puede ser negativo"}), 400
    
    nuevo_id = max(catalogo.keys(), default = 200) + 1

    nuevo_producto = {
        "Codigo": nuevo_id,
        "Producto": datos["Producto"],
        "Precio": datos["Precio"],
        "Stock": datos["Stock"],
        "Categoria": datos["Categoria"]
    }
    catalogo[nuevo_id] = nuevo_producto
    return jsonify(nuevo_producto)

@app.put("/catalogo/<int:id>")
def actualizar_producto(id):
    producto = catalogo.get(id)
    if not producto:
        return jsonify({"error": "producto no encontrado :(" }), 404
    datos_nuevos = request.get_json()

    if not datos_nuevos:
        return jsonify({"error": "no hay datos nuevos :(" }), 400
    
    if "Precio" in datos_nuevos:
        producto["Precio"] = datos_nuevos["Precio"]

    if "Stock" in datos_nuevos:
        producto["Stock"] = datos_nuevos["Stock"]    
    
    return jsonify(producto), 200 

@app.delete("/catalogo/<int:id>") 

def eliminar_producto(id):
    if id in catalogo:
        del catalogo[id]
        return jsonify({"Mensaje": "Producto eliminado correctamente"}), 200
    return jsonify({"error": "Producto no encontrado :("}), 404


if __name__ == "__main__":
    app.run(debug = True)