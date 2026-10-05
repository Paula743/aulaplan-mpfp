# Evidencia 01 de octubre de 2026
María Paula Flores Prieto  
Lenguajes Modernos de Programación

## 📁 Nuevas carpetas y archivos

```text
apps/
└── api/
    ├── src/
    │   ├── core/
    │   │   └── errors.py
    │   ├── firebase/
    │   │   └── client.py
    │   ├── http/
    │   │   ├── app.py
    │   │   ├── responses.py
    │   │   └── routes_health.py
    │   ├── repositories/
    │   │   └── base.py
    │   └── services/
    │       └── crud.py
    ├── dev.py
    └── main.py
```

La estructura mostrada conrresponde únicamente a los archivos agregados, algunas de las carpetas también son nuevas.

## 📄 Nuevo código

## Modificaciones a archivos ya existentes

### health_routes.py

El código existente se susutituyó por el siguiente:

```python
from flask import Blueprint, jsonify
health_bp = Blueprint("health", __name__)

@health_bp.get("/health")

def health():
    return (
        jsonify(
            {
                "status": "ok",
                "service": "aulaplan-api",
                "runtime": "python",
            }
        ), 
        200,
    )

```

### dev.py

El código existente se susutituyó por el siguiente:

```python
from src.http.app import create_app
 
app = create_app()

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True, 
    )
```

## Código en archivos nuevos

### errors.py

```python
class ApiError(Exception):
    def __init__(self, message: str, status_code: int = 400, code: str = "API_ERROR") -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.code = code
```

### client.py

```python
from functools import lru_cache
from google.cloud.firestore_v1 import Client
from firebase_admin import firestore

@lru_cache(maxsize=1)
def get_db() -> Client:
    return firestore.client()
```

### app.py

```python
from flask import Flask
from src.http.routes_health import health_bp
from src.http.responses import register_error_handlers

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["TESTING"] = testing
    register_error_handlers(app)
    app.register_blueprint(health_bp)
    return app
```

### responses.py

```python
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
```

### base.py

```python
from datetime import datetime, timezone
from typing import Any
from google.cloud.firestore_v1.base_query import FieldFilter
from src.core.errors import ApiError
from src.firebase.client import get_db

class FiresetoreRepository:
    def __init__(self, collection_name: str) -> None:
        self.collection_name = collection_name

    @property
    def collection(self):
        return get_db().collection(self.collection_name)

    def list(self, filters: dict[str, Any] | None = None) -> list[dict]:
        query = self.collection
        for key, value in (filters or {}).items():
            query = query.where(filter=FieldFilter(key, "==", value))

        result = []
        for snapshot in query.stream():
            row = snapshot.to_dict() or {}
            row["id"] = snapshot.id
            result.append(row)
        return result

    def get(self, document_id: str) -> dict:
        snapshot = self.collection.document(document_id).get()
        if not snapshot.exists:
            raise ApiError("Resource not found", 404, "NOT_FOUND")
        data = snapshot.to_dict() or {}
        data["id"] = snapshot.id
        return data

    def create(self, data: dict) -> dict:
        now = datetime.now(timezone.utc)
        document = self.collection.document()
        payload = {**data, "created_at": now, "updated_at": now}
        document.set(payload)
        return self.get(document.id)

    def update(self, document_id: str, data: dict) -> dict:
        self.get(document_id)
        payload = {**data, "updated_at": datetime.now(timezone.utc)}
        self.collection.document(document_id).update(payload)
        return self.get(document_id)

    def delete(self, document_id: str) -> None:
        self.get(document_id)
        self.collection.document(document_id).delete()

    def exists_by_field(self, field: str, value: Any, exclude_id: str | None = None) -> bool:
        query = self.collection.where(filter=FieldFilter(field, "==", value)).limit(2)
        for snapshot in query.stream():
            if snapshot.id != exclude_id:
                return True
        return False
```

### crud.py

```python
from typing import Type
from pydantic import BaseModel

from src.core.errors import ApiError
from src.repositories.base import FirestoreRepository


class CrudService:
    def __init__(
        self,
        repository: FirestoreRepository,
        create_schema: Type[BaseModel],
        update_schema: Type[BaseModel],
        unique_fields: tuple[str, ...] = (),
    ) -> None:
        self.repository = repository
        self.create_schema = create_schema
        self.update_schema = update_schema
        self.unique_fields = unique_fields

    def list(self, filters: dict | None = None) -> list[dict]:
        return self.repository.list(filters)

    def get(self, document_id: str) -> dict:
        return self.repository.get(document_id)

    def create(self, raw: dict) -> dict:
        model = self.create_schema.model_validate(raw)
        data = model.model_dump()
        self._assert_unique(data)
        return self.repository.create(data)

    def update(self, document_id: str, raw: dict) -> dict:
        model = self.update_schema.model_validate(raw)
        data = model.model_dump()
        self._assert_unique(data, document_id)
        return self.repository.update(document_id, data)

    def delete(self, document_id: str) -> None:
        self.repository.delete(document_id)

    def _assert_unique(self, data: dict, exclude_id: str | None = None) -> None:
        for field in self.unique_fields:
            if field in data and self.repository.exists_by_field(field, data[field], exclude_id):
                raise ApiError(f"{field} already exists", 409, "DUPLICATE_VALUE")
```

### main.py

```python
from firebase_admin import get_app, initialize_app
from firebase_functions import https_fn
from src.http.app import create_app

try:
    get_app()
except ValueError:
    initialize_app()

flask_app = create_app()

@https_fn.on_request(
    region="us-central1"
    cors=True,
)

def api(req: https_fn.Request) -> https_fn.Response:
    with flask_app.request_context(req.environ):
        return flask_app.full_dispatch_request()
```