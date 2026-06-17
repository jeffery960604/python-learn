# 裝滿東西的工具箱
toolbox = ["扳手", "螺絲", "膠水"]

# 我要拿第一個東西 (Python 是從 0 開始數喔！)
print(toolbox[0])  # 印出：扳手

# 新增一個零件到最後面
toolbox.append("螺旋槳") 


# 台北的經緯度 (緯度, 經度)
taipei_coords = (25.03, 121.56)

# 你可以讀取它
print(taipei_coords[0]) # 印出：25.03

# 但是如果你試圖修改它... 💥 錯誤！
# taipei_coords[0] = 26.0  <-- Python 會直接賞你紅字！


# F-16 戰鬥機的規格
f16_specs = {
    "model": "F-16",
    "top_speed": "馬赫 2.0",
    "weight_kg": 19200
}

# 用「標籤」來查資料
print(f16_specs["top_speed"]) # 印出：馬赫 2.0

# 隨時可以新增新的標籤跟資料
f16_specs["engine"] = "渦輪扇發動機"
