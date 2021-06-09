import json
import uuid
from datetime import date, datetime, timezone
import asyncio

import asyncpg
from sanic.response import json as sanic_json
from sanic.views import HTTPMethodView

from gw_info_api.constants import DB_URL
from gw_info_api.utils.background_tasks import add_transport_location
from gw_info_api.utils.encoder import CustomEncoder
from models.models import db, Transport


class TransportResources(HTTPMethodView):
    """Class for creating all tables."""

    async def post(self, request):
        payload = json.loads(request.body.decode())
        async with db.with_bind(DB_URL):
            await Transport.create(
                id=uuid.uuid4(),
                car_plate=payload["car_plate"],
                driver_id=payload["driver_id"],
                model=payload["model"],
                color=payload["color"],
                birth=date(*map(int, payload["birth"].split("-"))),
                type=payload["type"],
                vin_code=payload["vin_code"],
                engine_type=payload["engine_type"],
                engine_capacity=payload["engine_capacity"],
                registration_date=date(*map(int, payload.get("registration_date").split("-"))) if payload.get(
                    "registration_date") else date.today(),
                active=payload.get("active", True),
            )
        return sanic_json({"message": "New transport was added"})

    async def get(self, request):
        time = datetime.now(timezone.utc).replace(tzinfo=None)
        connection = await asyncpg.connect(DB_URL)
        result = await connection.fetchrow(f"""
            SELECT
                   tr.id 
                 , tr.car_plate
                 , tr.model
                 , tr.color
                 , tr.birth
                 , tr.type
                 , tr.vin_code
                 , tr.engine_type
                 , tr.engine_capacity
                 , tr.registration_date
                 , d.first_name
                 , d.last_name
                 , d.middle_name
                 , d.birth
                 , d.driving_license_start
                 , d.driving_license_end
                 , d.driving_license_number
                 , d.categories
                 , f.description as fine_description
                 , f.start_date as fine_start_date
            FROM transport tr
            JOIN driver d on d.id = tr.driver_id
            LEFT JOIN fine f on tr.id = f.transport_id
            WHERE tr.car_plate = '{request.args['car_plate'][0]}'
            AND tr.active IS TRUE;
        """)
        transport_id = None
        if result:
            response = dict(result)
            transport_id = response.pop('id')
            is_hunt_out = await connection.fetchrow(f"""
                SELECT 1 FROM hunt_out
                WHERE transport_id = '{transport_id}'::uuid
                AND active IS TRUE;
            """
                                                    )
        await connection.close()

        if not result:
            return sanic_json({"message": "Not found"}, status=404)

        response["is_hunt_out"] = True if is_hunt_out else False

        if "location" in request.headers:
            asyncio.create_task(add_transport_location(transport_id, request.headers["location"], time))

        return sanic_json({"message": json.loads(json.dumps(response, cls=CustomEncoder))})
