'''第一題：燃料消耗模擬器 (單純 while 迴圈)

情境：我們要模擬引擎消耗燃料的過程，直到沒油為止。
任務：
設定一個變數 fuel = 50。
寫一個 while 迴圈，條件是「當 fuel 大於 0 的時候」。
在迴圈裡面，印出 "引擎運轉中，剩餘燃料：[目前的油量] 單位"。
印完之後，把 fuel 減去 15（代表消耗了燃料）。
當迴圈結束（沒油了），在迴圈外面印出 "警告：燃料耗盡，引擎熄火！"。'''

fuel = 50
while fuel >= 0:
    print(f"引擎運轉中，剩餘燃料：{fuel} 單位")
    fuel=fuel-15
    print(f"剩餘燃料{fuel}")
print("警告：燃料耗盡，引擎熄火！")

'''第二題：飛航緊急代碼查詢器 (單純 Dictionary 讀取)

情境：飛行員遇到緊急狀況時，會在雷達上打出特定的四位數代碼。我們要寫一個程式來翻譯這些代碼。
任務：
建立一個字典，裡面裝著三個代碼：
python
squawk_codes = {
    "7500": "劫機",
    "7600": "無線電通訊故障",
    "7700": "緊急狀況"
}
設定一個變數 signal = "7700"（假設我們收到這個訊號）。
請利用 signal 去字典裡面查出對應的文字，並印出 "塔台收到代碼 7700，代表發生了：[你查到的文字]"。
'''
signal = "7700"
squawk_codes = {
    "7500": "劫機",
    "7600": "無線電通訊故障",
    "7700": "緊急狀況"
}
print(f"塔台收到代碼{signal}，代表發生了：{squawk_codes[signal]}")

'''第三題：無人機探勘任務 (終極結合題：while 裡面操作 Dictionary)

情境：我們有一台無人機，字典裡記錄了它的名字和電量。只要還有電，它就會持續探勘。
任務：
建立一個字典：
python
drone = {
    "name": "探路者號",
    "battery": 30
}
寫一個 while 迴圈，條件是「當 drone 的 "battery" 大於 0 時」。(提示：條件可以寫 while drone["battery"] > 0:)
在迴圈裡面印出："[無人機的名字] 正在探勘，目前電量：[無人機的電量] %"。
印完之後，把 drone["battery"] 扣掉 10。
迴圈結束後，印出 "[無人機的名字] 電量耗盡，任務結束。"。
'''
drone = {
    "name": "破碎星塵",
    "battery": 30
}
while drone["battery"] > 0 :
    print(f'目前電量{drone["battery"]}')
    drone["battery"] = drone["battery"] - 10
print(f'{drone["name"]}電量耗盡,任務結束')

'''第四題：太空船子系統中控台

情境：一艘太空船有非常多子系統（例如引擎、維生系統、導航）。我們把這些系統的狀態，全部收納在一個大型的嵌套字典裡。
任務：
建立這個大字典（你可以直接複製貼上這段）：
python
spacecraft = {
    "engine": {
        "status": "OK",
        "temperature": 850
    },
    "life_support": {
        "status": "Warning",
        "oxygen_level": 15
    },
    "navigation": {
        "status": "OK",
        "satellites_connected": 8
    }
}
讀取任務：艦長想知道引擎的溫度。請利用中括號，把 engine 裡面的 temperature 讀出來，並印出 "目前引擎溫度為：[溫度] 度"。
修改任務：維生系統的氧氣濃度太低了！請把 life_support 裡面的 oxygen_level 修改為 21。
新增任務：工程師剛剛修好了通訊模組。請在 spacecraft 這個大字典裡，新增一個標籤叫做 "communication"，它的數值也是一個小字典：{"status": "OK", "signal": 100}。
最後，把整個 spacecraft 印出來，看看是不是都更新成功了。

'''
spacecraft = {
    "engine": {
        "status": "OK",
        "temperature": 850
    },
    "life_support": {
        "status": "Warning",
        "oxygen_level": 15
    },
    "navigation": {
        "status": "OK",
        "satellites_connected": 8
    }
}
print(spacecraft["engine"]["temperature"])
# 第一道門打開後，緊接著打開第二道門
spacecraft["life_support"]["oxygen_level"] = 21
spacecraft.update({
    "communication":{"status": "OK", "signal": 100
    }
})
print(spacecraft)
