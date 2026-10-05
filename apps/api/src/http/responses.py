from datetime import date, datetime
from flask import jsonify
from pydantic import ValidationError
from src.core.errors import ApiError

def to_jsonable(value):
    if isinstance(value, (datetime, date)) :
        return value.isoformat()
    if isinstance(value, dict):
        return {key: to_jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [to_jsonable(item) for item in value]
    return value

def register_error_handlers(app) -> None:
    @app.errorhandler(ApiError)
    def handle_api_error(error: ApiError):
        return jsonify({"error": error.code, "message": error.message}), error.status_code

    @app.errorhandler(ValidationError)
    def handle_validation_error(error: ValidationError):
        return jsonify({"error": "NOT_FOUND", "message": "Resource not found", "details": error.errors()}), 404

    @app.errorhandler(Exception)
    def handle_unexpected(error: Exception):
        app.logger.exception(error)
        return jsonify({"error": "INTERNAL_ERROR", "message": "Unexpected server error"}), 500
    