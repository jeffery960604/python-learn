---
type: note
tags:
  - 學科/python
status: active
created: 2026-05-22
---




延續我們上一個「收納工具箱」的比喻：
*   **函數（`def`）**：是一件件單終的工具（例如：十字起子、一字起子）。
*   **模組（`.py` 檔案）**：是裝滿同類工具的「抽屜」（例如：螺絲起子抽屜）。

那麼，如果你的抽屜越來越多，桌子放不下了怎麼辦？
這時候你就需要買一個**「大層架（資料夾）」**，把這些抽屜有系統地收納進去。

這個「大層架（資料夾）」在 Python 裡就稱為 **「套件」或「封包」（Package）**。
*(註：在台灣的 Python 社群中，Package 最常見的翻譯是「套件」，但指的都是同一個東西！)*

---

### 第一步：如何建立一個套件 (Package)？

建立套件非常簡單，只要**建立一個資料夾**，然後把相關的 `.py` 檔案丟進去就可以了。但有一個非常重要的「通關密語」！

請看以下的檔案結構範例：

```text
我的專案資料夾/
 │
 ├── main.py               <-- 你的主程式
 │
 └── my_tools/             <-- 建立一個資料夾 (這就是套件！)
      │
      ├── __init__.py      <-- 💥關鍵：身分證檔案！
      ├── math_tools.py    <-- 數學模組
      └── text_tools.py    <-- 文字處理模組
```

**🧙‍♂️ 魔法檔案：`__init__.py` 是做什麼用的？**
當 Python 看到一個資料夾時，它怎麼知道這是一般的資料夾，還是可以用來寫程式的「套件」？
只要你在資料夾裡新增一個名為 `__init__.py` 的檔案（裡面可以是**完全空白**的），就等於發了一張身分證給這個資料夾，告訴 Python：「嘿！這是一個 Python 套件，請讓我可以在程式裡引入它！」
*(雖然 Python 3.3 之後不強制規定要有這個檔案，但加上去是業界標準的最佳習慣！)*

---

### 第二步：如何在程式中使用套件裡的東西？

現在，你的主程式 `main.py` 想要呼叫 `my_tools` 資料夾裡面的 `math_tools.py` 的函數，寫法會多加一個「點（`.`）」，就像是在指路徑一樣：**`資料夾名稱.檔案名稱`**。

📁 **`main.py` (主程式)**

#### 寫法 A：完整路徑引入 (連名帶姓)
```python
# 告訴 Python：進入 my_tools 資料夾，拿出 math_tools
import my_tools.math_tools

# 使用時也必須連名帶姓
result = my_tools.math_tools.add(10, 5)
print(result)
```
*缺點：名字太長了，打字會打到崩潰！*

#### 寫法 B：精準引入 (最推薦！⭐)
```python
# 語法：from 資料夾.檔案 import 函數名稱
from my_tools.math_tools import add

# 拿出來之後，直接用就可以了！
result = add(10, 5)
print(result)
```

#### 寫法 C：引入整個模組，幫它取個短名字
```python
from my_tools import math_tools as mt

result = mt.add(10, 5)
print(result)
```

---

### 第三步：大開眼界！全世界的套件任用 (pip)

自己寫套件（資料夾）用來整理程式碼很棒，但 Python 最強大的地方在於：**網路上有全世界頂尖工程師寫好的幾十萬個免費套件！**

這就像是一個超級龐大的「線上工具大賣場」，只要你想要什麼功能，幾乎都找得到：
*   想寫網路爬蟲抓資料？有 `requests` 套件。
*   想做資料分析、畫圖？有 `pandas` 和 `matplotlib` 套件。
*   想做人工智慧？有 `PyTorch` 或 `TensorFlow` 套件。

**如何下載別人的套件？**
我們不需自己慢慢下載資料夾，只要打開你的電腦終端機（Terminal / 命令提示字元），使用 Python 內建的送貨員 `pip` 指令：

```bash
# 在終端機輸入以下指令來安裝套件 (例如安裝 requests)
pip install requests
```

安裝好之後，你在你的 `main.py` 裡面就可以直接 `import` 來用，完全不需要管它存在電腦的哪個資料夾裡，Python 會自動幫你找到它！

```python
import requests

# 輕鬆用別人寫好的工具，抓取網頁資料！
response = requests.get("https://www.google.com")
print(response.status_code)
```

### 總結
1. **模組 (Module)**：一個 `.py` 檔案。
2. **套件 (Package)**：一個裝滿 `.py` 檔案的資料夾（裡面通常會有個空白的 `__init__.py`）。
3. **引入語法**：用 `from 資料夾.檔案 import 函數` 就能跨資料夾拿工具。
4. **第三方套件**：透過 `pip install 套件名稱`，你可以把全世界寫好的神級工具箱下載到你的電腦裡直接使用！

---
## 🔗 航線關聯 (Flight Link)
- **飛行控制台 MOC**：[[30_Projects/15_python/00_Python_MOC|💻 Python MOC]]
