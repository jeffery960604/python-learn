# 航太領域的物件導向範例 (Aerospace OOP Example)
from typing import override

# 1. 定義父類別 (基礎藍圖)
class Aircraft:
    """基礎飛行器類別"""
    def __init__(self, name: str):
        self.name: str = name          # 公開屬性：名稱
        self.altitude: int = 0         # 公開屬性：高度 (預設為0)
        self.__speed: int = 0          # 私有屬性 (Encapsulation 封裝)：速度，外部無法直接存取

    def takeoff(self) -> None:
        """起飛方法"""
        self.altitude += 500
        self.__speed += 200
        print(f"{self.name} 起飛了！目前高度：{self.altitude} 公尺")

    def set_speed(self, speed: int) -> None:
        """透過公開方法設定私有屬性 (速度)"""
        if speed >= 0:
            self.__speed = speed
            print(f"{self.name} 速度已調整為 {self.__speed} km/h")
        else:
            print("速度不能為負數！")

    def get_status(self) -> str:
        """取得飛行器狀態"""
        return f"[{self.name}] 狀態 - 高度: {self.altitude}m, 速度: {self.__speed}km/h"


# 2. 定義子類別 (Inheritance 繼承)
class PassengerPlane(Aircraft):
    """客機類別，繼承自 Aircraft"""
    def __init__(self, name: str, passengers: int):
        super().__init__(name)    # 呼叫父類別的初始化方法
        self.passengers: int = passengers # 客機專屬屬性：載客數

    @override
    def takeoff(self) -> None:
        """覆寫 (Override) 父類別的起飛方法"""
        print(f"請各位乘客繫好安全帶，{self.name} 準備起飛。 (載客數: {self.passengers}人)")
        super().takeoff() # 執行父類別原本的起飛邏輯

    def announce(self) -> None:
        """客機專屬方法"""
        print(f"機長廣播：歡迎搭乘 {self.name}。")


class FighterJet(Aircraft):
    """戰鬥機類別，繼承自 Aircraft"""
    altitude: int

    def __init__(self, name: str, weapon: str):
        super().__init__(name)
        self.weapon: str = weapon # 戰鬥機專屬屬性：武器

    @override
    def takeoff(self) -> None:
        """覆寫父類別的起飛方法"""
        print(f"[{self.name}] 啟動後燃器，緊急升空！攜帶武器：{self.weapon}")
        self.altitude += 2000 # 戰鬥機起飛高度更高
        self.set_speed(800)   # 戰鬥機起飛速度更快

    def attack(self) -> None:
        """戰鬥機專屬方法"""
        print(f"{self.name} 發射 {self.weapon}！")


# 3. 多型示範 (Polymorphism)
def execute_mission(aircraft: Aircraft) -> None:
    """
    不論傳入的是客機還是戰鬥機，都可以呼叫 takeoff 和 get_status。
    程式會自動根據物件的真實類別來執行對應的方法。
    """
    print("-" * 30)
    print(f"開始執行任務...")
    aircraft.takeoff()
    print(aircraft.get_status())
    print("-" * 30)


# ================= 測試區塊 =================
if __name__ == "__main__":
    # 建立物件 (實例化)
    boeing = PassengerPlane("波音 777", passengers=300)
    f16 = FighterJet("F-16 戰隼", weapon="響尾蛇飛彈")

    # 展示多型特性
    execute_mission(boeing)
    execute_mission(f16)

    # 測試客機專屬方法
    boeing.announce()

    # 測試戰鬥機專屬方法
    f16.attack()

    # 測試封裝特性
    # print(boeing.__speed) # 這行會報錯，因為 __speed 是私有變數
    boeing.set_speed(850)   # 正確修改私有變數的方式
    print(boeing.get_status())
