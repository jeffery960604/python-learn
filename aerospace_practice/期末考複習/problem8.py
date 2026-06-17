'''Viewed class.py:1-72

`*看到你已經把剛剛學姊教的範例都照著打了一遍，我滿意地點點頭，推給你一張嶄新的考卷*`

哇！你不只聽，還把範例全部自己打了一遍，這個練習方式非常正確！讓我們來出一題讓你從零開始自己打造設計圖。

---

### 📝 物件導向初級任務：打造無人機控制台

**情境**：我們實驗室接到一個任務，要製作一套無人機管理系統。每一台無人機都有自己獨立的名字、電量與飛行高度。

**你的任務（請在 `class.py` 最下面繼續寫）**：

#### Step 1 - 畫設計圖 `class Drone`
定義一個 `class`，名字叫做 `Drone`。

#### Step 2 - 工廠初始化 `__init__`
讓這個 `Drone` 設計圖需要一個原物料：`drone_name`（無人機的名字）。
在 `__init__` 裡面設定三個屬性：
  - `self.name` = `drone_name`（貼上名字標籤）
  - `self.battery` = `100`（出廠時電量是滿的）
  - `self.altitude` = `0`（出廠時停在地面，高度為 0）

#### Step 3 - 定義兩個方法
**方法一 `takeoff(self, target_height)`**（起飛，需要一個「目標高度」的原物料）：
  - 如果 `self.battery` > 20：
    - 把 `self.altitude` 設定成 `target_height`
    - 扣掉 20 點電量 (`self.battery -= 20`)
    - 印出：`"[名字] 起飛成功！目前高度：[高度] 公尺，剩餘電量：[電量] %"`
  - 否則：
    - 印出：`"[名字] 電量不足，無法起飛！"`

**方法二 `status_report(self)`**（狀態回報，不需要原物料）：
  - 直接印出：`"=== [名字] 狀態回報 ==="`
  - 印出：`"高度：[高度] 公尺"`
  - 印出：`"電量：[電量] %"`

#### Step 4 - 量產兩台無人機
用你的 `Drone` 設計圖，打造兩台不同的無人機：
- 第一台叫做 `"破碎星塵"` (你取的那個超帥的名字！)
- 第二台叫做 `"追風者"`

#### Step 5 - 操控它們
1. 讓「破碎星塵」起飛到高度 `500` 公尺。
2. 讓「追風者」起飛到高度 `1000` 公尺。
3. 呼叫兩台無人機的 `status_report()` 看看它們的狀態。

---

`*用筆敲了敲桌子，提醒你幾個關鍵點*`

**學姊的小提醒**：
- 記得每個方法的括號裡，第一個都要寫 `self` 喔！
- 屬性要用 `self.xxx` 來存取，直接寫 `battery` Python 會找不到它是誰的。

寫好了叫我，我們一起看結果！加油加油！⚡'''

class Drone:
    def __init__(self, name) :
        self.name = name
        self.battery = 100
        self.altitude = 0

    def takeoff(self, target_height) :
        if self.battery > 20:
            self.altitude = target_height
            self.battery -=20
            print(f"{self.name} 起飛成功！目前高度：{target_height} 公尺，剩餘電量：{self.battery} %")
        else:
            print(f"{self.name} 電量不足，無法起飛！")

    def status_report(self) :
        print(f"=== {self.name} 狀態回報 ===")
        print(f"高度：{self.altitude} 公尺")
        print(f"電量：{self.battery} %")

drone01 = Drone('破碎星塵')
drone02 = Drone('追風者')

drone01.takeoff(100)