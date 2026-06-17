'''📝 繼承與覆寫練習題
第一題：遺傳老爸的技能（純繼承，不覆寫）
任務：
定義一個 class Vehicle（交通工具），__init__ 接收一個 brand（品牌），方法 move(self) 印出 "[品牌] 正在移動..."。
定義一個 class Airplane(Vehicle)，繼承 Vehicle，再額外定義一個自己獨有的方法 fly(self)，印出 "[品牌] 正在高空飛行！"。
打造一個 Airplane 物件，品牌叫 "波音"，試著呼叫它的 move() 和 fly()，看看繼承來的 move() 有沒有用。
第二題：兒子改造老爸的技能（覆寫 Override）
任務：
沿用上面的 Vehicle（老爸）。
定義一個 class RocketShip(Vehicle)（火箭船），覆寫 move(self) 方法，讓它印出的內容改成 "[品牌] 點火發射！🚀 衝出大氣層！" 而不是原本的「正在移動」。
打造一個 RocketShip 物件，品牌叫 "SpaceX"，呼叫它的 move()，確認它印出的是覆寫後的版本。
第三題：保留老爸的精華，再加料（super() 的魔法）
任務：
沿用 Vehicle（老爸）。
定義一個 class ElectricPlane(Vehicle)（電動飛機）。
覆寫 __init__，讓電動飛機在初始化時，除了接收 brand 之外，還要接收 battery_range（電池續航里程）。
用 super().__init__(brand) 先讓老爸把 brand 屬性設定好。
再自己設定 self.battery_range = battery_range。
覆寫 move(self) 方法，用 super().move() 先讓老爸說一句「正在移動」，然後再加上自己的一行："電池續航：[battery_range] 公里，零排放飛行中 🌿"。
打造一個 ElectricPlane，品牌 "空中巴士"，續航 3000 公里，呼叫 move() 看看兩層輸出有沒有同時出現。'''
class vehicle:
    def __init__(self,brand) :
        self.brand = brand
    def move(self) :
        print(f'{self.brand}正在移動')
        
class airplane(vehicle) :
    def __init__(self,brand , wingSpan):
        super().__init__(brand)
        self.wingSpan = wingSpan
    def fly(self) :
        print(f'{self.brand}正在高空飛行')
        
test = airplane("姆芋",132)
test.move()
test.fly()

class ElectricPlane(vehicle):
    def __init__(self,brand , battery_range):
        super().__init__(brand)
        self.battery_range = battery_range
    def move(self,battery_range):
        super().move()
        print(f'電池續航{self.battery_range}公里')

test2 = ElectricPlane('空中巴士',45)
test2.move(45)





