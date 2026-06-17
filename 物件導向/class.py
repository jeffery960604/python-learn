#物件導向
class Pet:
    __name: str
    kind: str
    year: str

    def __init__(self, name: str, kind: str, year: int) -> None:
        self.__name = name
        self.kind = kind
        self.year = str(year) + '歲'
    def show_name(self):
        return self.__name

class Cat(Pet):
    color: str
    breed: str

    def __init__(self, name: str, year: int, color: str, breed: str) -> None:
        super().__init__(name, '貓', year)
        self.color = color
        self.breed = breed

my_Pet =Cat(name='小白', year=5, color='姆芋', breed='白底虎斑')

print(my_Pet.show_name())
#組合
class Engine:
    horsepower: int

    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower
    
    def sound(self):
        return '姆芋姆芋'
    
class Car:
    brand: str
    engine: Engine

    def __init__(self, brand: str, engine: Engine) -> None:
        self.brand = brand
        self.engine = engine
    
    def drive(self):
        return f"{self.brand} 發動了，引擎發出 {self.engine.sound()} 的聲音！"

#建立零組件
my_engine = Engine(500)
my_car = Car('姆芋車', my_engine)

print(my_car.drive())

#例外
try:
    pwd =input('請輸入密碼：')
except:
    print('輸入錯誤')
else:
    print('輸入正確')


class father():
    def __init__(self,name,year):
        self.name=name
        self.year=year
my_father =()



    

