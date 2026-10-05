from functools import lru_cache
from google.cloud.firestore_v1 import Client
from firebase_admin import firestore

@lru_cache(maxsize=1)
def get_db() -> Client:
    return firestore.client()