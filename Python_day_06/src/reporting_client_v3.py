#!./venv/bin/python3

from sqlalchemy import MetaData, String, Integer, Column, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, Session
import sqlalchemy
import json
import grpc
import argparse
from reporting_client import get_ships
from reporting_client_v2 import is_correct_ship

OFFICERS_TABLE_NAME = 'officers'
SHIPS_TABLE_NAME = 'ships'

metadata = MetaData()
engine = sqlalchemy.create_engine("postgresql://localhost/ex_03")

Base = declarative_base()


class Officer(Base):
    __tablename__ = OFFICERS_TABLE_NAME
    id = Column(Integer(), primary_key=True)
    ship_id = Column(ForeignKey(SHIPS_TABLE_NAME + '.id'))
    first_name = Column(String(30))
    second_name = Column(String(30))
    rank = Column(String(30))


class Ship(Base):
    __tablename__ = SHIPS_TABLE_NAME
    id = Column(Integer(), primary_key=True)
    alignment = Column(String(5), nullable=False)
    name = Column(String(30), nullable=False)
    class_ = Column(String(11), nullable=False)
    length = Column(Float(), nullable=False)
    crew_size = Column(Integer(), nullable=False)
    armed = Column(Boolean(), nullable=False)


Base.metadata.create_all(engine)


def add_to_table(ship):
    data = json.loads(ship)
    if not is_dublicate(data):
        session = Session(bind=engine)
        new_ship = Ship(
            alignment=data['alignment'],
            name=data['name'],
            class_=data['class_'],
            length=data['length'],
            crew_size=data['crew_size'],
            armed=data['armed']
        )
        session.add(new_ship)
        session.commit()
        session.refresh(new_ship)
        for officer in data['officers']:
            new_officer = Officer(
                ship_id=new_ship.id,
                first_name=officer['first_name'],
                second_name=officer['second_name'],
                rank=officer['rank']
            )
            session.add(new_officer)
        session.commit()


def is_dublicate(ship):
    session = Session(bind=engine)
    ships_with_the_same_name = session.query(
        Ship).filter(Ship.name == ship['name'])
    for sh in ships_with_the_same_name:
        result_flag = False
        officers_in_the_ship = session.query(
            Officer).filter(Officer.ship_id == sh.id)
        officers_list = []
        for officer in officers_in_the_ship:
            officers_list.append({"first_name": officer.first_name,
                                 "second_name": officer.second_name, "rank": officer.rank})
        for officer in ship['officers']:
            if officer not in officers_list:
                result_flag = False
                break
            else:
                result_flag = True
        if result_flag:
            return True
    return False


def find_traitors():
    session = Session(bind=engine)
    ally_officers = get_officers_db('Ally')
    ally_officers_list = officer_to_dict_list(ally_officers)
    enemy_officers = get_officers_db('Enemy')
    enemy_officers_list = officer_to_dict_list(enemy_officers)
    traitors_list = []
    for officer in ally_officers_list:
        if officer in enemy_officers_list and officer not in traitors_list:
            traitors_list.append(officer)
    print(traitors_list)


def get_officers_db(alignment):
    session = Session(bind=engine)
    return session.query(
        Officer.first_name,
        Officer.second_name,
        Officer.rank, Ship.alignment
    ).join(Ship).filter(Ship.alignment == alignment).all()


def officer_to_dict_list(officers_db):
    return [
        {
            "first_name": officer.first_name,
            "second_name": officer.second_name,
            "rank": officer.rank
        } for officer in officers_db
    ]


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=[
                        'scan', 'traitors'], help='Choose a command')
    parser.add_argument('scan', type=float, nargs='*')

    args = parser.parse_args()

    if args.command == 'scan':
        assert args.scan
    return args


if __name__ == '__main__':
    try:
        args = parser()
        with grpc.insecure_channel('localhost:50051') as channel:
            if args.command == 'scan':
                for ship in get_ships(channel, args.scan):
                    if is_correct_ship(ship):
                        print(ship)
                        add_to_table(ship)
            else:
                find_traitors()
    except AssertionError:
        print('Сoordinates were not received.')
