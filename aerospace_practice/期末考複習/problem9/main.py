'''Edited problem8.py
Viewed problem8.py:41-81

`*看到你把所有問題全部修好，我激動地拍了桌子，眼睛亮晶晶*`

你修得完美無缺！每個小細節都到位了，把 `while` 換成 `if`、`self.name` 用對位置、`f-string` 的 f 也補好了。你現在的物件導向基礎已經相當扎實了！

那我們就來出終極進化版：**把 Class 放進封包裡，從另一個主程式呼叫它！**

---

### 🚀 航太終極整合任務：飛行員管理系統

**目標架構**：
```text
problem9/
├── main.py               (主程式，你的指揮中心)
└── flight_crew/          (封包，飛行員資料庫)
    └── pilot.py          (模組，飛行員設計圖放在這裡)
```

---

#### Step 1：在 `flight_crew/pilot.py` 裡打造飛行員設計圖

定義一個 `class Pilot`，初始化需要兩個原料：`name`（姓名）和 `license_type`（執照種類）。
在 `__init__` 裡設定三個屬性：
- `self.name` = 傳進來的名字
- `self.license` = 傳進來的執照種類
- `self.flight_hours` = `0`（出廠時飛行時數為 0）

再定義兩個方法：

**方法一 `fly_mission(self, hours)`**（執行任務，需要飛幾小時）：
- 把 `hours` 累加進 `self.flight_hours`
- 印出：`"[姓名] 完成任務，累積飛行時數：[總時數] 小時"`

**方法二 `get_report(self)`**（出具飛行報告）：
- 印出：`"==== 飛行員報告 ===="`
- 印出：`"姓名：[姓名]"`
- 印出：`"執照類型：[執照種類]"`
- 印出：`"總飛行時數：[時數] 小時"`
- 根據飛行時數，判斷資歷：
  - 時數 ≥ 1000：印出 `"資歷：資深機師 ✈️"`
  - 時數 ≥ 500：印出 `"資歷：熟練飛行員"`
  - 否則：印出 `"資歷：菜鳥新人 🐣"`

---

#### Step 2：在 `main.py` 裡建立指揮中心

從封包匯入設計圖：
```python
from flight_crew.pilot import Pilot
```

然後：
1. 打造兩個飛行員物件：
   - 第一位：名字 `"陳志明"`，執照 `"民航機師"`
   - 第二位：名字 `"林雅婷"`，執照 `"戰鬥機飛行員"`
2. 讓陳志明執行三次任務：分別飛 `300`、`400`、`350` 小時。
3. 讓林雅婷執行兩次任務：分別飛 `600`、`200` 小時。
4. 最後分別呼叫兩人的 `get_report()`，看看誰是資深機師！

---

`*把這份任務書鄭重地交到你手上*`

這題有兩個層面的挑戰：**先在 `pilot.py` 裡把 Class 寫完，再在 `main.py` 裡 import 它來用。**
先從 `pilot.py` 開始下手，寫好了再切換到 `main.py`。有任何卡關的地方隨時叫我喔！'''

from flight_crew.pilot import Pilot

name01 = Pilot("陳志明" , "民航機師")
name02 = Pilot("林雅婷" , "戰鬥機飛行員")

name01.fly_mission(300)
name01.fly_mission(400)
name01.fly_mission(350)

name02.fly_mission(600)
name02.fly_mission(200)

name01.get_report()
name02.get_report()
