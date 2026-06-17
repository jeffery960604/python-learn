# Python 讀取檔案教學範例 (已修正路徑問題)
import os

# =====================================================================
# 💡 為什麼會報錯？
# 因為你的終端機「工作目錄」是在 "/Users/xiang/Documents/python learning"，
# 但你的 sample.txt 卻是放在子資料夾「資料存取」裡面。
# 
# 解決方法：我們可以使用 os.path 動態取得「目前 Python 檔所在的資料夾」，
# 再去組合出 sample.txt 的路徑，這樣不論你在哪裡執行這個程式都不會報錯！
# =====================================================================

# 1. 取得目前 main.py 所在的絕對路徑資料夾
base_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 組合出 sample.txt 的正確絕對路徑
file_path = os.path.join(base_dir, "sample.txt")

print(f"目前讀取的檔案路徑為：{file_path}\n")

# ==========================================
# 方法 1：一次讀取整個檔案內容 (適合小檔案)
# ==========================================
print("--- 方法 1: 一次讀取全部內容 ---")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)


# ==========================================
# 方法 2：逐行讀取 (最推薦！適合大檔案，省記憶體)
# ==========================================
print("\n--- 方法 2: 逐行讀取 (用 for 迴圈) ---")
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


# ==========================================
# 方法 3：讀取所有行並存成列表 (List)
# ==========================================
print("\n--- 方法 3: 讀取所有行並存成 List ---")
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("讀取出來的列表：", lines)
    print("第二行的內容是：", lines[1].strip())

