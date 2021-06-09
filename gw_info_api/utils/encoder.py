import json
from uuid import UUID
import datetime


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        elif isinstance(obj, datetime.date):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
