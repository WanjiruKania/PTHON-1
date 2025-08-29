#INHERITANCE

class vehicle:
    def __init__(self, num_wheels, weight):
        self.num_wheels = num_wheels
        self.weight= weight

        def start(start):
            print("startng engine")

            def stop(self):
                print("stopping vehicle")
    
class car(vehicle):
    def open_trunk(self):
        print("opening trunk")

my_car = car(4, 5000)
my_car.start()
my_car.open_trunk()
