import uuid

from gw_info_api.constants import DB_URL
from gw_info_api.utils.logger import log
from models.models import db, TransportLocation


async def add_transport_location(transport_id: str, location: str, time):
    try:
        async with db.with_bind(DB_URL):
            await TransportLocation.create(
                id=uuid.uuid4(),
                transport_id=transport_id,
                location=location,
                date_of_state=time
            )
    except Exception:
        log.error(f"Can't add location({location}) of transport with id {transport_id}")
