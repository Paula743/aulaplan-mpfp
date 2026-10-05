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