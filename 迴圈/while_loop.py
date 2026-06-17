# Python while 迴圈語法與範例教學

# 1. 基本語法
# 當條件為 True 時，會持續執行區塊內的程式碼。
print("--- 基本 while 迴圈 ---")
count = 1
while count <= 5:
    print(f"目前計數：{count}")
    count += 1

# 2. 無窮迴圈與 break
# break 用於提早跳出整個迴圈。
print("\n--- break 的用法 ---")
while True:
    # try...except 是一個「例外處理」結構，目的是讓程式在出錯時也不會直接當機。
    try:
        # [try 區塊]：這裡是我們「嘗試」要執行的內容。
        # 在此模擬等待特定條件（例如使用者輸入或系統重連）。
        print("迴圈進行中... (在這裡按 Ctrl + C 可以看到效果)")
        
        # 為了展示效果，我們手動執行 break 否則真的會變無窮迴圈
        break 
        
    except KeyboardInterrupt:
        # [except 區塊]：這裡是「案發現場」。
        # 當使用者在終端機按下鍵盤的 [Ctrl + C] 組合鍵時，會觸發 KeyboardInterrupt。
        # 在這裡執行 break，可以讓我們「優雅地」結束，而不會在螢幕噴出一長串紅色的報錯。
        print("\n[系統]: 已偵測到您手動中斷程式，準備安全結束...")
        break

# 3. continue 的用法
# continue 用於跳過本次循環，直接進入下一次判定。
print("\n--- continue 的用法 (印出 1-10 之間的偶數) ---")
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue # 如果是奇數，跳過後面的程式碼
    # f-string 語法：開頭加上 f，就可以在大括號 { } 內直接放入變數，非常方便！
    print(f"偶數：{i}")

# 4. while 與 else
# else 區塊會在迴圈「正常完成」（即沒有被 break 中斷）後執行。
print("\n--- while 與 else ---")
n = 3
while n > 0:
    print(f"倒數：{n}")
    n -= 1
else:
    print("倒數結束！")

# 5. 常見應用：輸入驗證範例
# while True:
#     pw = input("請輸入密碼：")
#     if pw == "1234":
#         print("登入成功")
#         break
#     else:
#         print("密碼錯誤，請重試")

import random
target =random.randint(1,100)
guess = 0
tries = 0
while guess != target:
    guess = int(input("請輸入猜測的數字："))
    tries += 1
    if guess < target:
        print("太小了，再試一次")
    elif guess > target:
        print("太大了，再試一次")
    else:
        print("恭喜你猜對了！")
        print(f"你總共猜了 {tries} 次")

# 7. 巢狀迴圈 (Nested Loop)
# 迴圈裡面還有一個迴圈。外層迴圈每執行一次，內層迴圈就會完整跑完一輪。
print("\n--- 巢狀迴圈：座標產生器 (2x3 網格) ---")
row = 1
while row <= 2:      # 外層迴圈控制「列」
    col = 1
    while col <= 3:  # 內層迴圈控制「行」
        print(f"(r:{row}, c:{col})", end=" ")
        col += 1
    print()          # 內層跑完後換行
    row += 1

# 8. 經典練習：巢狀迴圈印星星 (已移至 star_patterns.py)
# 請參考 `star_patterns.py` 查看詳細的三角形與數值追蹤範例。

# 9. 巢狀迴圈：印出九九乘法表
# 橫排 (i) 代表乘數，直排 (j) 代表被乘數。
print("\n--- 九九乘法表 ---")
i = 1
while i <= 9:        # 控制外層：從 1 跑到 9
    j = 1
    while j <= 9:    # 控制內層：每一排也要跑 1 到 9
        print(f"{i}x{j}={i*j:2}", end="  ") # :2 是為了對齊，保留兩位空間
        j += 1
    print()          # 跑完一整排後換行
    i += 1
