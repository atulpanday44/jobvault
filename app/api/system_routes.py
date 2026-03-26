from flask import Blueprint, jsonify, request

# Create the Blueprint for system routes
system_routes = Blueprint('system_routes', __name__)

# Health check endpoint
@system_routes.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': '2026-03-26 08:23:17'}), 200

# Job fetch trigger endpoint
@system_routes.route('/fetch_job', methods=['POST'])
def fetch_job():
    job_id = request.json.get('job_id')
    if not job_id:
        return jsonify({'error': 'job_id is required'}), 400
    # Implement logic to fetch the job based on job_id
    # For now, we will just return a mock job response
    return jsonify({'job_id': job_id, 'status': 'fetched'}), 200
