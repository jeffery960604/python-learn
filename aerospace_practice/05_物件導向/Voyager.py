# 定義基礎類別 (Base Class)：太空探測器
class SpaceProbe:
    def __init__(self, name, launch_year):
        self.name = name                 # 探測器名稱
        self.launch_year = launch_year   # 發射年份
        self.is_active = True            # 運作狀態（預設為運作中）

    def transmit_signal(self):
        """模擬探測器傳送訊號回地球"""
        if self.is_active:
            print(f"[{self.name}] 正在向深空網路 (DSN) 傳送訊號...")
        else:
            print(f"[{self.name}] 失去聯繫，無法傳送訊號。")

    def shutdown(self):
        """關閉探測器"""
        self.is_active = False
        print(f"[{self.name}] 系統已關閉。")


# 定義子類別 (Derived Class)：旅行者號探測器，繼承自 SpaceProbe
class VoyagerProbe(SpaceProbe):
    def __init__(self, name, launch_year, distance_au, gold_record_included=True):
        # 使用 super() 呼叫父類別的初始化方法
        super().__init__(name, launch_year)
        
        # 旅行者號特有的屬性
        self.distance_au = distance_au   # 距離地球的距離（天文單位 AU）
        self.gold_record_included = gold_record_included # 是否攜帶黃金唱片
        self.instruments_on = True       # 科學儀器是否開啟

    def update_distance(self, new_distance):
        """更新探測器與地球的距離"""
        self.distance_au = new_distance
        print(f"[{self.name}] 距離已更新：距離地球 {self.distance_au} AU (天文單位)。")

    def toggle_instruments(self, state):
        """為了節省電力，開啟或關閉科學儀器"""
        self.instruments_on = state
        status = "開啟" if state else "關閉"
        print(f"[{self.name}] 為了節省核電池 (RTG) 電力，科學儀器已{status}。")

    def display_status(self):
        """顯示旅行者號的當前狀態"""
        print("-" * 30)
        print(f"探測器名稱：{self.name}")
        print(f"發射年份：{self.launch_year}")
        print(f"目前距離：{self.distance_au} AU")
        print(f"黃金唱片：{'有攜帶' if self.gold_record_included else '未攜帶'}")
        print(f"儀器狀態：{'運作中' if self.instruments_on else '已關閉休眠'}")
        print("-" * 30)


# ==========================================
# 實際演練：建立物件 (Objects) 與呼叫方法
# ==========================================

if __name__ == "__main__":
    # 建立 Voyager 1 物件 (發射於 1977 年，目前距離超過 162 AU)
    voyager_1 = VoyagerProbe(name="旅行者 1 號", launch_year=1977, distance_au=162.5)
    
    # 建立 Voyager 2 物件 (發射於 1977 年，目前距離超過 136 AU)
    voyager_2 = VoyagerProbe(name="旅行者 2 號", launch_year=1977, distance_au=136.2)

    # 1. 顯示初始狀態
    voyager_1.display_status()
    voyager_2.display_status()

    # 2. 呼叫繼承自父類別的方法
    voyager_1.transmit_signal()

    # 3. 呼叫子類別特有的方法 (更新距離)
    voyager_1.update_distance(163.0)
    voyager_2.update_distance(136.5)

    # 4. 模擬電力衰減，關閉旅行者 2 號的某些儀器
    voyager_2.toggle_instruments(False)

    # 5. 再次查看旅行者 2 號的狀態
    voyager_2.display_status()