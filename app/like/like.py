from flask import jsonify
from . import like_bp

@like_bp.route('/like', methods=['GET'])
def get_inmuebles():
    # Aquí realizar consultas a la base de datos y formatear la respuesta.
    # Ejemplo:
    inmuebles = [{"id": 1, "direccion": "Calle 123", "estado": "pre_venta",} ]
    return jsonify(inmuebles)
