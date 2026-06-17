# Python 巢狀迴圈：印星星系列 (Star Patterns)

# 1. 正三角形
# 特性：i 代表行數，每層印出的星星數量等於 i。
print("--- 正三角形 ---")
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print() # 換行
    i += 1

# 2. 倒三角形
# 特性：i 代表行數，從 5 開始倒數到 1。
print("\n--- 倒三角形 ---")
i = 5
while i >= 1:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print() # 換行
    i -= 1

# 3. 數值追蹤範例 (幫助理解 i 與 j 的關係)
# 這個範例會同時印出當時的 i 跟 j，讓您看清楚變化。
print("\n--- 數值追蹤範例 ---")
i = 1
while i <= 3:
    j = 1
    while j <= i:
        print(f"(i={i}, j={j})", end=" ")
        j += 1
    print()
    i += 1

