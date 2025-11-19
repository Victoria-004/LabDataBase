from flask import Blueprint, Response, jsonify
import json
from app.my_project.rescuers.service.rescuer_service import RescuerService

calls_bp = Blueprint('calls_bp', __name__, url_prefix='/calls')

rescuer_service = RescuerService()

@calls_bp.route('/<int:call_id>/rescuers', methods=['GET'])
def get_rescuers_for_call(call_id):
    rescuers = rescuer_service.get_rescuers_by_call_id(call_id)

    response_json = json.dumps(rescuers, ensure_ascii=False)
    return Response(response_json, content_type='application/json; charset=utf-8')