#批量讀取法一
# 這是我們從黑盒子拿出來的火箭飛行日誌 (List of Dictionaries)
flight_log = [
    {"time": 1, "altitude": 500, "velocity": 150},
    {"time": 2, "altitude": 1000, "velocity": 300},
    {"time": 3, "altitude": 1500, "velocity": 450}
]

# 1. 準備一個專門裝「高度」的空串列
all_altitudes = []

# 2. 開始批量處理！
for record in flight_log:
    # 這裡的 record，就是每一圈抽出來的「單張報告(字典)」喔！
    
    # 3. 讀取標籤為 "altitude" 的資料
    current_h = record["altitude"]
    
    # 4. 把這個數字存進我們的新箱子裡
    all_altitudes.append(current_h)

print("萃取完成的高度數據：", all_altitudes)
# 輸出結果會是整齊的：[500, 1000, 1500]

#法二
# 一行搞定批量萃取！
fast_altitudes = [record["altitude"] for record in flight_log]

print("魔法萃取的高度數據：", fast_altitudes)


def temperature_change(C):
    K=C+273.15
    return K

f=temperature_change(input('請輸入溫度'))
print(f'轉換為華氏{f}')