"""This module contains basic classes for configuring service and test if service is available."""

from sanic.response import json
from sanic.views import HTTPMethodView

from gw_info_api.utils.logger import log


class SmokeResources(HTTPMethodView):
    """Class for checking if service is available."""

    async def get(self, *_, **__):
        await log.info("Service is available")
        return json({"message": "OK"})
