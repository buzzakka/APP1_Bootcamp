import proto.galaxy_pb2 as pb2, proto.galaxy_pb2_grpc as pb2_grpc
import random
from constants import *
from concurrent import futures
import grpc


class Galaxy(pb2_grpc.GalaxyServicer):
    def get_ships(self, request, context):
        print(f'Сoordinates: {request.pos}')
        return self.generate_ships()

    def generate_ships(self):

        for _ in range(random.randint(1, 10)):

            ship = pb2.Ship()
            ship.alignment = random.randint(0, 1)
            ship.name = random.choice(NAMES)            
            ship.ship_class = random.randint(0, 5)
            ship.length = random.uniform(80, 20000)
            ship.crew_size = random.randint(4, 500)
            ship.armed = random.choice([True, False])
            min_officers = 0 if ship.alignment == 'Enemy' else 1
            for _ in range(min_officers, 10):
                officer = ship.officers.add()
                officer.first_name = random.choice(FIRST_NAMES)
                officer.second_name = random.choice(SECOND_NAMES)
                officer.rank = random.choice(RANKS)
            yield ship


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GalaxyServicer_to_server(Galaxy(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started. Listening on port 50051.")
    server.start()
    server.wait_for_termination()


server()
