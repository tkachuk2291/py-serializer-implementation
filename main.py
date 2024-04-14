from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from car.serializers import CarSerializer
from car.models import Car
import io


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    content = JSONRenderer().render(serializer.data)
    return content


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    instance = serializer.save()
    return instance
