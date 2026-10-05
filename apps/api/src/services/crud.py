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