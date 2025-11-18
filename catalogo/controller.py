from flask import Blueprint, request, jsonify
from  model import *
import requests
import os

catalog_blueprint = Blueprint('catalog', __name__)

catalogs = {}

def verificar_user(user_id):
    USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://user_service:6000/users/')
    try:
        response = requests.get(f'{USER_SERVICE_URL}/users/{user_id}')
        return response.status_code == 200
    
    except requests.exceptions.RequestException as e:
        print("Erro ao conectar ao serviço de utilizadores", e)
        return False


@catalog_blueprint.route('/<int:catalog_id>', methods=['GET'])
def get_catalog(catalog_id):
    catalog = catalogs.get(catalog_id)
    if catalog:
        return jsonify(catalog.to_dict())
    return jsonify({'error': 'catalog not found'}), 404

@catalog_blueprint.route('/', methods=['POST'])
def create_catalog():
    catalog_data = request.json
    user_id = catalog_data['user_id']
    
    # Verifica se o user existe no serviço de utilizadores
    if not verificar_user(user_id):
        return jsonify({'error': 'User does not exist'}), 400
    
    # Cria o pedido se o user existir
    catalog = catalog(catalog_id=catalog_data['catalog_id'], user_id=user_id, catalog_details=catalog_data['catalog_details'])
    catalogs[catalog.catalog_id] = catalog
    return jsonify(catalog.to_dict()), 201