from flask import Blueprint, request, jsonify

user_routes = Blueprint('user_routes', __name__)

# Sample criteria data; in real implementation, this would likely come from a database
criteria_data = []
alerts_data = []

@user_routes.route('/criteria', methods=['POST'])
def create_criteria():
    new_criteria = request.json  # expects JSON data
    criteria_data.append(new_criteria)
    return jsonify(new_criteria), 201

@user_routes.route('/criteria', methods=['GET'])
def get_criteria():
    return jsonify(criteria_data), 200

@user_routes.route('/alerts', methods=['POST'])
def create_alert():
    new_alert = request.json  # expects JSON data
    alerts_data.append(new_alert)
    return jsonify(new_alert), 201

@user_routes.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts_data), 200
