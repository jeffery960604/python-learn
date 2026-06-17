# for 迴圈與 while 迴圈範例

# for 迴圈：已知次數 (例如固定時間間隔)
print("--- for 迴圈 (模擬定時回傳高度) ---")
for second in range(1, 11):
    altitude = 50 * second
    print(f'第 {second} 秒，高度為: {altitude}m')

# while 迴圈：等待條件符合 (例如監控燃料)
print("\n--- while 迴圈 (模擬燃料監控) ---")
fuel = 100
while fuel >= 0:
    print(f'燃料剩餘 {fuel}%，引擎持續運作中')
    fuel -= 20
print('燃料耗盡')
