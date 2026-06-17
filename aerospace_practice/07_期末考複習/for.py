# 假設我們現在正在監測一台飛行器的馬赫數 (Mach number)
mach_number = 1.2

if mach_number < 0.8:
    print("目前是次音速飛行 (Subsonic)，氣流還算乖巧喔！")
elif 0.8 <= mach_number < 1.2:
    print("進入穿音速區 (Transonic) 了！注意震波的產生。")
elif 1.2 <= mach_number < 5.0:
    print("現在是超音速飛行 (Supersonic)！")
else:
    print("哇，超過馬赫 5 了，這是高超音速 (Hypersonic) 的領域呢！")

# 這裡有一個列表，裝著四個感測器的溫度（攝氏度）
sensor_temperatures = [350, 420, 390, 850]

# 用 for 迴圈把它們一個個拿出來檢查
for temp in sensor_temperatures:
    if temp > 800:
        print(f"警告！溫度 {temp} 度太高了，噴嘴可能會融毀！")
    else:
        print(f"溫度 {temp} 度，在安全範圍內。")

# 火箭發射倒數計時器
countdown = 5

while countdown > 0:
    print(f"T-minus {countdown} 秒...")
    # 每次執行完，把數字減 1
    countdown = countdown - 1

print("Ignition! 火箭升空啦 🚀")

temperatures = [350, 420, 390]

# 寫法一：叫它 t
for t in temperatures:
    print(t)

# 寫法二：叫它 data
for data in temperatures:
    print(data)

# 寫法三：就算叫它 pikachu 也會跑喔（雖然我們不建議這麼鬧啦😆）
for pikachu in temperatures:
    print(pikachu)
    



