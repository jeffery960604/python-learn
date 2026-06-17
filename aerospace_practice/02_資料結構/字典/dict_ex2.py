flight_log = [
    {"time": 1, "altitude": 500, "velocity": 150},
    {"time": 2, "altitude": 1000, "velocity": 300},
    {"time": 3, "altitude": 1500, "velocity": 450}
]

# 法一：傳統迴圈
all_altitudes: list[int] = []
for record in flight_log:
    all_altitudes.append(record["altitude"])
print("傳統迴圈萃取的高度數據：", all_altitudes)

# 法二：一行搞定 (列表推導式)
fast_altitudes = [record["altitude"] for record in flight_log]
print("列表推導式萃取的高度數據：", fast_altitudes)

# 溫度轉換函數範例
def temperature_change_to_K(C: float | int | str) -> float:
    K = float(C) + 273.15
    return K

# 注意：這裡原本的 input 建議在呼叫時處理
try:
    user_input = 25 # 範例數值
    k_val = temperature_change_to_K(user_input)
    print(f'攝氏 {user_input} 度轉換為開氏溫標為 {k_val}K')
except ValueError:
    print("請輸入有效的數字")
