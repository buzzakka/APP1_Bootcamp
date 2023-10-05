import threading
from time import sleep

class Screwdriver:

    def __init__(self, id):
        self.id = id
        self.lock = threading.Lock()

    def pick_up(self):
        sleep(0.3)
        self.lock.acquire()

    def put_down(self):
        sleep(0.3)
        self.lock.release()


class Doctor(threading.Thread):

    def __init__(self, id, left_screwdriver, right_screwdriver):
        super().__init__()
        self.id = id
        self.left_screwdriver = left_screwdriver
        self.right_screwdriver = right_screwdriver

    def run(self):
        first_screwdriver, second_screwdriver = sorted([self.left_screwdriver, self.right_screwdriver], key=lambda x: x.id)
        first_screwdriver.pick_up()
        second_screwdriver.pick_up()
        sleep(0.6)
        print(f'Doctor {self.id}: BLAST!')
        second_screwdriver.put_down()
        first_screwdriver.put_down()

if __name__ == '__main__':
    doctor_num = 5
    screwdrivers = [Screwdriver(i) for i in range(doctor_num)]
    doctors = [Doctor(9 + id, screwdrivers[id], screwdrivers[(id + 1) % doctor_num]) for id in range(doctor_num)]
    
    for doctor in doctors:
        doctor.start()
    
    for doctor in doctors:
        doctor.join()
