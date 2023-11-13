from flask import jsonify, request
from . import consulta_bp
from sqlalchemy import inspect, desc, func, asc
from app import db
from app.consulta.models import Property, Status, StatusHistory 

@consulta_bp.route('/esquema', methods=['GET'])
def obtener_esquema():
    inspector = inspect(db.engine)
    tablas = inspector.get_table_names()
    esquema = {}

    for tabla in tablas:
        columnas = inspector.get_columns(tabla)
        esquema[tabla] = [{'name': columna['name'], 'type': str(columna['type'])} for columna in columnas]

    return jsonify(esquema)

@consulta_bp.route('/inmuebles', methods=['GET'])
def obtener_inmuebles():

    year = request.args.get('year')
    city = request.args.get('city')
    status = request.args.get('status')

    if status and status not in ["pre_venta", "en_venta", "vendido"]:
        return jsonify([])

    propertyQuery = Property.query

    if year:
        propertyQuery = propertyQuery.filter(Property.year == year)
    if city:
        propertyQuery = propertyQuery.filter(Property.city == city)

    inmuebles = propertyQuery.all()

    diccionario_inmuebles = {inmueble.id:
            {
            'id': inmueble.id,
            'address': inmueble.address,
            'city': inmueble.city,
            'price': inmueble.price,
            'description': inmueble.description,
            'year': inmueble.year,
            'status':'' 
            }
            for inmueble in inmuebles}


    query = (
    db.session.query(
        StatusHistory.property_id,
        Status.name.label('status_name')
    )
    .join(Status, StatusHistory.status_id == Status.id)
    .order_by(desc(StatusHistory.update_date))
    )

    statusHistoryQuery = query.all()

    for property_id, status_name in statusHistoryQuery:
        diccionario_inmuebles[property_id]['status'] = status_name

    status_query = ["pre_venta", "en_venta", "vendido"]
    resultado = list(diccionario_inmuebles.values())    
    resultado = [property for property in resultado if any(status_name in property.get("status") for status_name in status_query)]

    if status:
       resultado = [property for property in resultado if property.get("status") == status]

    return jsonify(resultado)