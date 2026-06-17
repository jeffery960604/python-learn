---
type: note
tags:
  - 學科/python
status: active
created: 2026-05-22
---




當你的程式越寫越長，如果把幾十個、甚至上百個 `def` 函數全都塞在同一個檔案裡，程式碼就會像一張凌亂的書桌，不僅很難找東西，還很容易出錯。

這時候，我們就會使用**「模組化（Modularization）」**的技巧。

### 📦 生活化的比喻：收納工具箱
*   **單一檔案**：把螺絲起子、鐵鎚、扳手全部丟在同一個大箱子裡。
*   **模組化（多檔案）**：你買了一個有好幾層的工具箱。第一層（檔案A）專門放「數學計算工具」，第二層（檔案B）專門放「處理文字工具」。需要用的時候，只要**「拉開特定的抽屜（Import）」**，拿出工具來用就好了。

在 Python 裡，**每一個 `.py` 檔案就是一個「模組（Module）」**。

---

### 第一步：建立你的工具箱（建立模組檔案）

假設我們現在要寫一個計算機程式。我們新增一個檔案，命名為 `math_tools.py`，專門把數學相關的 `def` 放進去。

📁 **`math_tools.py` (數學工具箱)**
```python
# 這是我們自訂的模組檔案

def add(a, b):
    """這是一個加法函數"""
    return a + b

def multiply(a, b):
    """這是一個乘法函數"""
    return a * b

def calculate_bmi(weight, height_cm):
    """計算 BMI 的函數"""
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)
```
*寫好之後就存檔，這個檔案就像是一個準備好的工具箱。*

---

### 第二步：在主程式中把工具箱拿來用（Import 引入）

現在，我們新增另一個檔案（通常是程式的起點），命名為 `main.py`。**這兩個檔案必須放在同一個資料夾裡**。

📁 **`main.py` (主程式)**
```python
# 告訴 Python：我要把剛剛寫好的 math_tools 模組拿進來用
import math_tools

print("歡迎來到我的超級計算機！")

# 使用方式：模組名稱.函數名稱()
result_add = math_tools.add(10, 5)
print(f"10 + 5 = {result_add}")

my_bmi = math_tools.calculate_bmi(70, 175)
print(f"你的 BMI 是：{my_bmi}")
```

---

### 💡 必學技巧：三種常見 of `import` 方式

根據你的需求，拉開抽屜（引入模組）的方式有三種：

#### 1. 整箱拿過來 (基礎用法)
```python
import math_tools

# 每次使用都要指名道姓（工具箱名.工具名）
math_tools.multiply(3, 4) 
```

#### 2. 只拿我需要的工具 (最常用！)
如果你覺得每次都要打 `math_tools.` 很麻煩，而且你只需要用到加法，可以這樣寫：
```python
# 從 math_tools 裡面，單獨把 add 和 multiply 拿出來
from math_tools import add, multiply

# 拿出來之後，就可以直接當作自己的函數來用，不用加前綴！
print(add(10, 5)) 
print(multiply(3, 4))
```

#### 3. 幫工具箱取綽號 (Alias)
有時候檔案名稱太長（例如 `data_processing_tools.py`），你可以幫它取個短一點的縮寫：
```python
import math_tools as mt

# 現在 mt 就代表 math_tools
print(mt.add(10, 5))
```
*(備註：如果你學到後來，看到大家寫 `import pandas as pd` 或 `import numpy as np`，就是用了這個技巧！)*

---

### 🛡️ 進階防護：`if __name__ == "__main__":` 是什麼？

當你把程式拆成好幾個檔案時，一定會遇到一個情況：你想要在 `math_tools.py` 裡面**偷偷測試**一下函數有沒有寫錯，但又**不希望**別人 `import` 它的時候，測試碼也被執行。

**錯誤示範（沒有防護）：**
```python
# math_tools.py
def add(a, b):
    return a + b

# 你自己在檔案底下寫了測試
print("測試一下：", add(1, 1)) 
```
如果這樣寫，當別人在 `main.py` 寫下 `import math_tools` 的瞬間，他的螢幕上就會莫名其妙印出「測試一下： 2」。

**正確解法（加上防禦機制）：**
請利用 Python 內建的魔法變數 `__name__`：

```python
# math_tools.py
def add(a, b):
    return a + b

# 加上這行通關密語！
if __name__ == "__main__":
    # 這裡面的程式碼，只有當你「直接點擊/執行這個檔案」時才會運作
    # 如果這個檔案是被別人 import 拿去當工具箱的，這裡面的程式就不會執行！
    print("這是我偷偷做的測試：", add(1, 1))
```

### 總結
1. **分檔**：把性質相近的 `def` 寫在同一個 `.py` 檔裡（例如處理時間的寫一個檔、處理爬蟲的寫一個檔）。
2. **引入**：在主程式中用 `import 檔名` 或 `from 檔名 import 函數` 把大腦組合起來。
3. **管理**：用 `if __name__ == "__main__":` 來隔離測試程式碼與工具模組。

這樣一來，你的主程式 `main.py` 可能只剩下短短的 20 行，但背後卻呼叫了成千上萬行被分門別類整理好的模組，這就是軟體工程的魔法！

---
## 🔗 航線關聯 (Flight Link)
- **飛行控制台 MOC**：[[30_Projects/15_python/00_Python_MOC|💻 Python MOC]]
