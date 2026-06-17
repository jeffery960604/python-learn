#字典的用途是貼標籤
drone_data = [5000, 340, 85]
#字典
# 無人機的遙測數據 (Telemetry Data)
drone_status = {
    "altitude": 5000,    # 高度 (m)
    "velocity": 340,     # 速度 (m/s)
    "battery": 85        # 電量 (%)
}
# 新增一個標籤叫 "temperature"，並賦予數值 -20
drone_status["temperature"] = -20
#新增一個
drone_status['mission']='探測'
print(drone_status)
#套殼
# 1. 先準備一個空的串列（打開黑盒子）
flight_log = [] 

# 2. 用迴圈模擬火箭飛行了 3 秒
for sec in range(1, 4):
    
    # 每一秒，感測器都會生成一個新的「字典（數據表單）」
    current_status = {
        "time": sec,                 # 時間標籤
        "altitude": sec * 500,       # 高度標籤 (假設每秒上升 500m)
        "velocity": sec * 150        # 速度標籤 (假設每秒加速 150m/s)
    }
    
    # 3. 關鍵步驟：把這張字典表單「套（附加）」進去串列裡！
    flight_log.append(current_status)

print("數據紀錄完成！")

#拿出來

# 步驟一：先從大盒子(List)裡抽出第 2 秒的那張表單 (索引值為 1)
target_record = flight_log[1]  
# 這時候 target_record 是一個字典：{'time': 2, 'altitude': 1000, 'velocity': 300}

# 步驟二：再從這張表單(Dictionary)上，看 "altitude" 這個標籤的值
target_altitude = target_record["altitude"]

# 🚀 工程師的「縮寫」終極絕招（兩步合併成一步）：
fast_query = flight_log[1]["altitude"]
print(f"第 2 秒的高度是：{fast_query} m")

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