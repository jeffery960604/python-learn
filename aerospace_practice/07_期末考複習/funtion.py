# 打造一台叫做 calculate_thrust (計算推力) 的機器
# 括號裡面的 mass 和 acceleration，是機器需要的「原物料 (參數)」
def calculate_thrust(mass, acceleration):
    
    # 機器內部的運作邏輯
    thrust = mass * acceleration
    
    # 【超級重要】return (回傳值)
    # 這代表機器處理完之後，把「成品 (thrust)」吐出來交給你
    return thrust

# 呼叫機器！把 500 (質量) 和 9.8 (加速度) 丟進去
# 並且拿一個箱子 (my_result) 去接機器吐出來的成品 (return 的東西)
my_result = calculate_thrust(500, 9.8)

print(f"計算出來的推力是：{my_result} 牛頓")


