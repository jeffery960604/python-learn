# list 範例：紀錄飛行高度歷史
altitude_history: list[int] = []  # 這是一個空的紀錄表

altitude_history.append(5000)
altitude_history.append(2500)
# 現在清單變成了 [5000, 2500]

h = 5000
h_list: list[float] = [float(h)]  # 把初始高度放進去

while h >= 10:
    h = h / 2
    h_list.append(h)  # 每次減半，就把新高度存進去

print(f"紀錄完成！共存了 {len(h_list)} 個數據點。")
print(f"前三個高度紀錄是：{h_list[:3]}") # 這是切片 (Slicing) 用法喔

# 假設你的 h_list 已經存好數據了
fifth_second_height = h_list[5]

print(f"探測器在第 5 秒時的高度是：{fifth_second_height:.2f} m")
