# tuple 範例：物理常數與高度紀錄
# tuple 是不能變動的資料

# 物理常數
mars_physics = (3.721, 3389.5) # (重力加速度 m/s^2, 行星半徑 km)

# tuple unpacking (解包)
g, radius = mars_physics
print('系統初始化')
print(f"目標行星重力設定為: {g} m/s^2")
print(f"目標行星半徑設定為: {radius} km")

altitude_log: list[float] = []
print("\n【引擎點火，開始爬升】")
# 模擬前 3 秒的爬升過程
altitude_log.append(150.5)  # 第 1 秒
altitude_log.append(320.8)  # 第 2 秒
altitude_log.append(500.0)  # 第 3 秒

print(f"目前的飛行高度紀錄：{altitude_log}")
print(f"現在的最新高度是：{altitude_log[-1]} m")

# ==========================================
# 3. Tuple 的防護機制測試
# ==========================================
# 如果有粗心的工程師想偷偷把火星重力改成地球重力：
# mars_physics[0] = 9.81  
# (如果你把上面這行的 '#' 拿掉，Python 會立刻賞你一個紅色報錯)
