class Engine():
    def __init__(self,horsepower):
        self.horsepower =horsepower

class Car():
    def __init__(self,brand,engine):
        self.brand =brand
        self.engine =engine

my_engine =Engine(120)
my_car =Car('honda',my_engine)

