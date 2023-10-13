#!./venv/bin/python3

import proto.galaxy_pb2 as pb2
import proto.galaxy_pb2_grpc as pb2_grpc
import grpc
import json
import argparse


def get_coordinates():
    parser = argparse.ArgumentParser()
    parser.add_argument('coordinates', nargs='*', type=float)
    return parser.parse_args().coordinates


def get_ships(channel, coordinates: list[int]):
    stub = pb2_grpc.GalaxyStub(channel)
    for ship in stub.get_ships(pb2.GalacticPossition(pos=coordinates)):
        ship_dict = {
            "alignment": pb2.Ship.AlignmentType.Name(ship.alignment),
            "name": ship.name,
            "class_": pb2.Ship.ClassType.Name(ship.ship_class),
            "length": ship.length,
            "crew_size": ship.crew_size,
            "armed": ship.armed,
            "officers": [{
                "first_name": officer.first_name,
                "second_name": officer.second_name,
                "rank": officer.rank,
            } for officer in ship.officers if officer.first_name]
        }
        yield json.dumps(ship_dict, indent=2)


if __name__ == '__main__':
    coordinates = get_coordinates()
    try:
        assert len(coordinates) != 0
        with grpc.insecure_channel('localhost:50051') as channel:
            for ship in get_ships(channel, coordinates):
                print(ship)
    except:
        print('Сoordinates were not received.')
