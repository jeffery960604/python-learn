# Python for 迴圈基礎：重複做 N 次

# 1. 最基本的：重複做 5 次
# 使用 range(5) 就會從 0 開始，做到 4，總共 5 次。
print("--- 重複做 5 次 ---")
for i in range(5):
    print("這是一行重複的文字")

# 2. 認識變數 i
# 在 for i in range(5) 中，i 會依序變成 0, 1, 2, 3, 4。
print("\n--- 看看變數 i 的變化 ---")
for i in range(5):
    print(f"現在 i 的值是：{i}")

# 3. 指定範圍：從 1 數到 5
# range(1, 6) 表示從 1 開始，到 6 之前（也就是 5）結束。
print("\n--- 從 1 數到 5 ---")
for i in range(1, 6):
    print(f"數到：{i}")

# 4. 指定間隔：每次加 2
# range(0, 11, 2) 表示從 0 開始，每次加 2，直到 11 之前。
print("\n--- 每次加 2 的計數 ---")
for i in range(0, 11, 2):
    print(f"目前 i 是：{i}")

# 5. 倒著數：每次減 1
# range(5, 0, -1) 表示從 5 開始，每次減 1，到 0 之前（也就是 1）結束。
print("\n--- 倒著數 5 到 1 ---")
for i in range(5, 0, -1):
    print(f"數到：{i}")

# 6. 累加計算 (Total)：算 1 到 10 的總和
# 定義一個初始變數 total = 0
total = 0

# range() 函式一個很重要的特性：「包含起始值，但不包含結束值」（含頭不含尾）。
for i in range(1, 11):
    total = total + i # 每次把 index 加進去

print(f"\n--- 1 到 10 的總和是：{total} ---")



