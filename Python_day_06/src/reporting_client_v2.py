import proto.galaxy_pb2 as pb2, proto.galaxy_pb2_grpc as pb2_grpc
from reporting_client import get_ships, get_coordinates
import grpc
from pydantic import BaseModel, ValidationError, model_validator

class Officer(BaseModel):
    first_name: str = None
    second_name: str = None
    rank: str = None

class Ship(BaseModel):
    alignment: str
    name: str
    class_: str
    length: float
    crew_size: int
    armed: bool
    officers: list[Officer]
    
    @model_validator(mode='after')
    def check_model(self) -> 'Ship':
        if (
            (self.class_ == 'Corvette' and 80 <= self.length <= 250 and 4 <= self.crew_size <= 10) or
            (self.class_ == 'Frigate' and 300 <= self.length <= 600 and 10 <= self.crew_size <= 15 and self.alignment == 'Ally') or
            (self.class_ == 'Cruiser' and 500 <= self.length <= 1000 and 15 <= self.crew_size <= 30) or
            (self.class_ == 'Destroyer' and 800 <= self.length <= 2000 and 50 <= self.crew_size <= 80 and self.alignment == 'Ally') or
            (self.class_ == 'Carrier' and 1000 <= self.length <= 4000 and 120 <= self.crew_size <= 250 and not self.armed) or
            (self.class_ == 'Dreadnought' and 5000 <= self.length <= 20000 and 300 <= self.crew_size <= 500)
        ) and not (self.name == 'Unknown' and self.alignment == 'Ally'):
            return self
        else:
            raise ValueError()

def is_correct_ship(ship) -> bool:
    try:
        Ship.model_validate_json(ship)
        return True
    except ValidationError as e:
        # print(e.json())
        return False


if __name__ == '__main__':
    coordinates = get_coordinates()
    try:
        assert len(coordinates) != 0
        with grpc.insecure_channel('localhost:50051') as channel:
            for ship in get_ships(channel, coordinates):
                if is_correct_ship(ship):
                    print(ship)
    except:
        print('Сoordinates were not received.')