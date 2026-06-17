# 垂直起飛與大氣壓力計算
battery = 35 
rpm = 8500
if (battery >= 20 and rpm >= 8000):
    print(True)
else:
    print('無法起飛')

# 大氣壓力計算
p_start = 101325
temp_deinc = 0.0065
temp_standard = 288.15
h = 3000
p = p_start * (1 - (temp_deinc * h / temp_standard)**5)
print(f"在高度 {h}m 的大氣壓力為: {p}")
