from sanic.response import json
from sanic.views import HTTPMethodView

from gw_info_api.constants import DB_URL
from models.models import db


class DBResources(HTTPMethodView):
    """Class for creating all tables."""

    async def post(self, _):
        try:
            async with db.with_bind(DB_URL):
                await db.gino.create_all()
        except Exception:
            return json({"message": "already exists"})
        return json({"message": "Created"})
