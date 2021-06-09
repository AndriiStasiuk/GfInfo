import json
import uuid
from datetime import date

from sanic.response import json as sanic_json
from sanic.views import HTTPMethodView

from gw_info_api.constants import DB_URL
from models.models import db, Driver


class DriverResource(HTTPMethodView):
    """Class for creating all tables."""

    async def post(self, request):
        payload = json.loads(request.body.decode())
        async with db.with_bind(DB_URL):
            await Driver.create(
                id=uuid.uuid4(),
                first_name=payload["first_name"],
                last_name=payload["last_name"],
                middle_name=payload["middle_name"],
                birth=date(*map(int, payload["birth"].split("-"))),
                driving_license_start=date(*map(int, payload["driving_license_start"].split("-"))),
                driving_license_end=date(*map(int, payload["driving_license_start"].split("-"))),
                driving_license_number=payload["driving_license_number"],
                categories=payload["categories"],
            )
        return sanic_json({"message": "New driver was added"})
