# 字典 (Dictionary) 的用途：貼標籤
drone_status: dict[str, str | int] = {
    "altitude": 5000,    # 高度 (m)
    "velocity": 340,     # 速度 (m/s)
    "battery": 85        # 電量 (%)
}

# 新增標籤
drone_status["temperature"] = -20
drone_status['mission'] = '探測'
print(f"無人機狀態: {drone_status}")

# 列表嵌套字典 (List of Dictionaries)
flight_log: list[dict[str, int]] = [] 
for sec in range(1, 4):
    current_status = {
        "time": sec,
        "altitude": sec * 500,
        "velocity": sec * 150
    }
    flight_log.append(current_status)

print("數據紀錄完成！")

# 讀取嵌套數據
target_record = flight_log[1]  
target_altitude = target_record["altitude"]
print(f"第 2 秒的高度是：{target_altitude} m")

# 批量處理
all_altitudes: list[int] = []
for record in flight_log:
    all_altitudes.append(record["altitude"])

print("萃取完成的高度數據：", all_altitudes)
