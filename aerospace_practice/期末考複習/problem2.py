'''第一題：單雙數航班 (算術運算子 % 與判斷式)

情境：我們要判斷今天的航班編號是單數還是雙數。如果編號除以 2 餘數是 0，就是雙數。
任務：設定變數 flight_num = 777。用 % 運算子判斷它除以 2 的餘數。如果是 0，印出 "這是雙數航班"；不然就印出 ㄌ。'''

flight_num = 777
end=(flight_num%2)
if end == 0:
    print("這是雙數航班")
else:
    print("這是單數航班")

'''第二題：太空艙載貨單 (List 新增元素)

情境：我們要準備發射物資到太空站。一開始載貨單是空的。
任務：
建立一個空的列表 cargo = []。
使用 .append() 語法，依序把 "太陽能板" 和 "冷凍披薩" 加進列表裡。
把整個 cargo 列表印出來看看裝了什麼。
'''
cargo = []
cargo.append("太陽能板")
cargo.append("冷凍披薩")
print(cargo)

'''第三題：人造衛星軌道 (Tuple 讀取)

情境：人造衛星的 (X, Y, Z) 三維座標是不可以隨便被竄改的，所以我們用 Tuple 存。
任務：有一個 Tuple 叫做 satellite_pos = (35000, 12000, 850)。請用中括號 [] 讀取並印出它的 Z 座標 (第三個數字)。(提示：記得 Python 是從 0 開始數的喔！)'''

satellite_pos = (35000, 12000, 850)
print(satellite_pos[2])

'''第四題：發動機監控儀表板 (Dictionary 讀取與修改)

情境：我們有一個字典記錄了發動機的當前狀態。
任務：
python
engine_status = {
    "model": "Raptor",
    "thrust": 2000,
    "temperature": 300
}
測試中溫度升高了！請把 "temperature" 的數值改成 850。
我們需要加裝一個新感測器。請在字典裡新增一個標籤 "pressure"，並設定它的數值為 150。
最後把整個 engine_status 字典印出來檢查。
'''
engine_status = {
    "model": "Raptor",
    "thrust": 2000,
    "temperature": 300
}
engine_status["temperature"]=850
engine_status["pressure"]=150
print(engine_status)
'''
第四題.update版
'''
engine_status = {
    "model": "Raptor",
    "thrust": 2000,
    "temperature": 300
}
engine_status.update({
    "temperature":850,
    "pressure":150  
})
print(engine_status)
'''
第五題：超音速過濾器 (綜合題：List + 比較運算子 + for 迴圈 + if)

情境：我們測量了 4 台飛行器的時速（單位：公尺/秒）。音速大約是 340 m/s。
任務： 有一組數據 speeds = [250, 400, 310, 800]。 請用 for 迴圈把數字一個一個拿出來：
如果大於 340，印出 "時速 [數字]：突破音障！"。
如果小於或等於 340，印出 "時速 [數字]：次音速飛行。"。
'''
speeds = [250, 400, 310, 800]
for speed in speeds :
    if speed >=340:
        print(f"時速{speed}：突破音障！")
    else :
        print(f"時速{speed}：次音速飛行！")

