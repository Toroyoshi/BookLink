from flask import Blueprint, request, jsonify
from  model import Loan
import requests
import os

loan_blueprint = Blueprint('loan', __name__)

loans = {}

def verificar_user(user_id):
    USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://user_service:6000/users/')
    try:
        response = requests.get(f'{USER_SERVICE_URL}/users/{user_id}')
        return response.status_code == 200
    
    except requests.exceptions.RequestException as e:
        print("Erro ao conectar ao serviço de utilizadores", e)
        return False


@loan_blueprint.route('/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    loan = loans.get(loan_id)
    if loan:
        return jsonify(loan.to_dict())
    return jsonify({'error': 'loan not found'}), 404

@loan_blueprint.route('/', methods=['POST'])
def create_loan():
    loan_data = request.json
    user_id = loan_data['user_id']
    
    # Verifica se o user existe no serviço de utilizadores
    if not verificar_user(user_id):
        return jsonify({'error': 'User does not exist'}), 400
    
    # Cria o pedido se o user existir
    loan = loan(loan_id=loan_data['loan_id'], user_id=user_id, product_details=loan_data['product_details'])
    loans[loan.loan_id] = loan
    return jsonify(loan.to_dict()), 201