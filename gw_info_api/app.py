"""Module which execute needed operations before server start and after server stop."""

from sanic.app import Sanic
from sanic_cors import CORS
from gw_info_api.configurations import DevConfig

from gw_info_api.api_v1 import load_api
from gw_info_api.constants import SERVICE_NAME

app = Sanic(SERVICE_NAME)
app.config.from_object(DevConfig)

cors = CORS(
    app,
    resources={r"*": {"origin": "*"}},
    expose_headers=[
        "Link, X-Pagination-Current-Page",
        "X-Pagination-Per-Page",
        "X-Pagination-Total-Count",
        "X-Client",
        "Authorization",
        "Content-Type",
        "X-Filename",
    ],
)

load_api(app)
