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