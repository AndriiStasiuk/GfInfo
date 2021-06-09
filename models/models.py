from gino import Gino
from sqlalchemy.dialects.postgresql import UUID, ARRAY

db = Gino()


class Driver(db.Model):
    __tablename__ = "driver"

    id = db.Column(UUID, primary_key=True)
    first_name = db.Column(db.String(length=100))
    last_name = db.Column(db.String(length=100))
    middle_name = db.Column(db.String(length=100))
    birth = db.Column(db.Date())
    driving_license_start = db.Column(db.Date())
    driving_license_end = db.Column(db.Date())
    driving_license_number = db.Column(db.String(length=100))
    categories = db.Column(ARRAY(db.String))


class Fine(db.Model):
    __tablename__ = "fine"

    id = db.Column(UUID, primary_key=True)
    transport_id = db.Column(UUID)
    start_date = db.Column(db.Date())
    description = db.Column(db.String(length=1000))
    active = db.Column(db.Boolean())


class HuntOut(db.Model):
    __tablename__ = "hunt_out"

    id = db.Column(UUID, primary_key=True)
    transport_id = db.Column(UUID)
    start_date = db.Column(db.String(length=100))
    active = db.Column(db.Boolean())


class Transport(db.Model):
    __tablename__ = "transport"

    id = db.Column(UUID, primary_key=True)
    car_plate = db.Column(db.String(length=50), index=True)
    driver_id = db.Column(UUID)
    model = db.Column(db.String(length=100))
    color = db.Column(db.String(length=100))
    birth = db.Column(db.Date())
    type = db.Column(db.Integer())
    vin_code = db.Column(db.String(length=17))
    engine_type = db.Column(db.Integer())
    engine_capacity = db.Column(db.Float())
    registration_date = db.Column(db.Date())
    active = db.Column(db.Boolean())


class TransportLocation(db.Model):
    __tablename__ = "transport_location"

    id = db.Column(UUID, primary_key=True)
    transport_id = db.Column(UUID)
    location = db.Column(db.String(length=100))
    date_of_state = db.Column(db.DateTime())
