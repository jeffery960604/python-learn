'''📡 航太實驗室：空中防撞系統 (封包架構實戰)
第一步：建立封包與模組
請開一個全新的資料夾 problem7。
在 problem7 裡面，建立一個資料夾叫做 avionics。（這就是我們的封包 Package！）
在 avionics 資料夾裡面，建立一個 Python 檔案叫做 radar.py。（這就是我們的雷達模組 Module！）
第二步：在 radar.py 裡面打造防撞機器
在 radar.py 檔案裡，請定義一個函數：

函數名稱：detect_collision(my_alt, other_alt) (需要兩個原物料：我們的高度 my_alt，和另一架飛機的高度 other_alt)
內部邏輯： 計算兩架飛機的高度差：diff = abs(my_alt - other_alt) (註：abs() 是取絕對值，不管誰高誰低，算出來都是正數距離)。 如果 diff 小於 1000 呎：return "警告！高度差過小，有相撞風險！"
 如果 diff 大於等於 1000 呎：return "安全：維持安全隔離。"
第三步：建立飛航主電腦
回到 problem7 這個資料夾（也就是跟 avionics 資料夾放在同一個層級的地方）。
建立一個檔案叫做 flight_computer.py。
在裡面寫入跨封包叫貨的魔法語法：
python
# 從 avionics 資料夾裡面的 radar 檔案，拿出機器
from avionics.radar import detect_collision
測試系統： 我們的高度是 35000 呎，對面飛來一架高度 34500 呎的飛機。 請呼叫 detect_collision，把這兩個數字丟進去，用一個變數接住回傳值，並印出來看看系統是不是有發出警告。
*用筆在紙上畫出資料夾的樹狀圖給你看*

你的 problem7 完成後，長相應該會像這樣喔：

text
problem7/
├── flight_computer.py   (主電腦)
└── avionics/            (封包資料夾)
    └── radar.py         (雷達模組)
這就是業界最標準的封包分類法了。你試著把這套防撞系統架設起來，讓主電腦成功讀取雷達的資料吧！'''

from avionics.radar import detect_collision
test = detect_collision(35000,34500)
print(test)
