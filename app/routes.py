from flask import Blueprint, jsonify, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return jsonify({"message": "Welcome to DevSecOps App", "status": "active"})

@main_bp.route('/api/data', methods=['POST'])
def process_data():
    data = request.json
    return jsonify({"received": data, "processed": True})