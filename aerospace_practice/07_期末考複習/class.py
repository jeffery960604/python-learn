# 1. 畫設計圖 (Class 名稱習慣字首大寫)
class Spacecraft:
    
    # 2. 初始化工廠：當工廠在打造新飛機的「那一瞬間」，要先設定什麼？
    # __init__ 是一個特殊的魔法函數，self 代表「正在被打造的那架飛機本人」
    def __init__(self, name_tag):
        # 設定這架飛機的屬性 (變數)
        self.name = name_tag  # 給飛機貼上名字標籤
        self.fuel = 100       # 剛出廠時油箱是滿的 100
        
    # 3. 定義飛機可以做什麼 (方法)
    # 記得括號裡一定要寫 self，飛機才知道是「自己」要起飛！
    def launch(self):
        if self.fuel >= 20:
            print(f"{self.name} 點火起飛！🚀")
            self.fuel -= 20   # 扣掉自己的油
        else:
            print(f"{self.name} 燃料不足，無法起飛...")

# ====================================================

# 4. 開始量產實體物件 (Object)！
# 照著 Spacecraft 這張設計圖，打造一台叫做「阿波羅號」的飛機
ship_1 = Spacecraft("阿波羅號")

# 再打造另一台完全獨立的飛機「獵鷹號」
ship_2 = Spacecraft("獵鷹號")

# 5. 操作實體物件 (呼叫方法)
ship_1.launch()  # 阿波羅號起飛！


# 老爸設計圖 (基礎飛機)
class Airplane:
    def __init__(self, name):
        self.name = name
        
    def fly(self):
        print(f"{self.name} 正在平穩地飛行...")

# ---------------------------------------------

# 兒子設計圖 (戰鬥機)。括號裡寫 (Airplane) 代表繼承老爸
class FighterJet(Airplane):
    
    # 兒子自己獨有的新功能！老爸不會這招。
    def fire_missile(self):
        print(f"{self.name} 發射了空對空飛彈！咻——💥")

# 測試看看：
my_fighter = FighterJet("F-22 猛禽")
my_fighter.fly()          # 兒子自動學會了老爸的 fly()！
my_fighter.fire_missile() # 兒子還會自己獨門的絕招！

class FighterJet(Airplane):
    
    # 兒子決定覆寫 (Override) 老爸的飛行動態
    def fly(self):
        # 1. 先用 super() 請老爸把基礎的引擎啟動 (保留老爸的功能)
        super().fly()  
        
        # 2. 然後加上兒子自己加碼的超音速功能！
        print(f"{self.name} 開啟後燃器，進入超音速模式！🚀🚀🚀")

# 測試看看：
my_fighter = FighterJet("F-35 閃電")
my_fighter.fly()
# 螢幕會印出：
# F-35 閃電 正在平穩地飛行... (老爸的)
# F-35 閃電 開啟後燃器，進入超音速模式！🚀🚀🚀 (兒子加碼的)

