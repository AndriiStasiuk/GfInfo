"""This module defines the service routing system."""

from sanic import Blueprint
from sanic.app import Sanic

from gw_info_api.constants import API_PREFIX
from gw_info_api.resources.smoke_resource import SmokeResources
from gw_info_api.resources.db_resource import DBResources
from gw_info_api.resources.transport_resource import TransportResources
from gw_info_api.resources.driver_resource import DriverResource


def load_api(app: Sanic) -> None:
    """...."""
    api_v1 = Blueprint("v1", url_prefix=API_PREFIX)

    api_v1.add_route(SmokeResources.as_view(), "/smoke", strict_slashes=False)
    api_v1.add_route(DBResources.as_view(), "/database", strict_slashes=False)
    api_v1.add_route(TransportResources.as_view(), "/transport", strict_slashes=False)
    api_v1.add_route(DriverResource.as_view(), "/driver", strict_slashes=False)

    app.blueprint(api_v1)
