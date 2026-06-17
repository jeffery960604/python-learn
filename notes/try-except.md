---
type: note
tags:
  - 學科/python
status: active
created: 2026-05-22
---




在 Python 中，`try...except` 是用來做**「例外處理（Exception Handling）」**的機制。

簡單來說，它的功用就是：**「預防程式因為發生錯誤而崩潰（Crash），讓程式在遇到狀況時，還能優雅地處理並繼續執行。」**

---

### 🛡️ 生活化的比喻：寄送包裹
想像你是一個快遞員，你的任務是把包裹送到某個地址：
*   **`try` (嘗試)**：你按照預定路線開車去送貨（執行正常的程式碼）。
*   **`except` (例外/發生意外)**：結果前面道路施工（發生錯誤）！如果你沒有應變計畫，你可能就會傻在原地，甚至車子撞上去（程式崩潰）。但如果你有 `except` 計畫，你就會說：「如果遇到施工，我就改走替代道路。」（捕捉錯誤並處理它）。

---

### 1. 最基礎的用法：try 和 except
當你在程式碼中覺得「某段程式可能會報錯」時，就可以把它放進 `try` 區塊裡。

```python
try:
    # 這裡放「可能會出錯」的程式碼
    number = int(input("請輸入一個數字："))
    print(f"你輸入的數字是：{number}")

except:
    # 如果 try 裡面的程式碼發生錯誤，就會跳到這裡執行
    print("發生錯誤了！你輸入的不是數字喔！")

print("程式順利結束。")
```
**情境測試：**
*   如果你輸入 `10` 👉 程式正常印出 10，並印出「程式順利結束」。
*   如果你輸入 `蘋果` 👉 轉換成整數 `int("蘋果")` 會失敗。這時程式**不會崩潰報紅字**，而是會跳到 `except`，印出「發生錯誤了...」，然後繼續往下執行，印出「程式順利結束」。

---

### 2. 捕捉「特定」的錯誤
剛剛的寫法會把「所有」錯誤都抓起來，但實務上，不同的錯誤我們通常會想要有不同的處理方式。

常見的錯誤種類例如：
*   `ValueError`：傳入無效的值（例如把 "ABC" 轉成數字）。
*   `ZeroDivisionError`：除以零的錯誤。

```python
try:
    x = int(input("請輸入被除數: "))
    y = int(input("請輸入除數: "))
    result = x / y
    print(f"答案是: {result}")

except ValueError:
    print("格式錯誤：請輸入阿拉伯數字！")

except ZeroDivisionError:
    print("數學錯誤：除數不可以是 0！")

except Exception as e:
    # Exception 是所有錯誤的「老大哥」，這招可以用來捕捉前面沒涵蓋到的其他錯誤
    # "as e" 可以把系統真正的錯誤訊息存進變數 e 裡面印出來看
    print(f"發生了未知的錯誤：{e}")
```

---

### 3. 完整的四大天王：try / except / else / finally
除了 `try` 和 `except`，Python 還提供了另外兩個好用的區塊，組合起來就是最完整的錯誤處理機制：

*   **`try`**：測試這段程式碼是否會報錯。
*   **`except`**：如果報錯了，就執行這裡。
*   **`else`**：如果 **完全沒有報錯**，就會執行這裡。
*   **`finally`**：**不管有沒有報錯，最後都一定會執行這裡**（通常用來做「善後工作」，例如關閉檔案、斷開資料庫連線）。

```python
def divide_numbers(a, b):
    try:
        print("--- 開始執行計算 ---")
        result = a / b
        
    except ZeroDivisionError:
        print("❌ 錯誤：除數不能為零！")
        
    else:
        # 只有在 try 成功（沒發生例外）時才會執行
        print(f"✅ 計算成功！答案是 {result}")
        
    finally:
        # 無論成功或失敗，最後一定會執行
        print("--- 計算過程結束 ---\n")

# 測試看看
divide_numbers(10, 2)  # 正常情況
divide_numbers(10, 0)  # 發生錯誤的情況
```

**輸出結果會是這樣：**
```text
--- 開始執行計算 ---
✅ 計算成功！答案是 5.0
--- 計算過程結束 ---

--- 開始執行計算 ---
❌ 錯誤：除數不能為零！
--- 計算過程結束 ---
```

---

### 💡 總結與最佳實踐 (Best Practice)
1. **為什麼不用 if-else 就好？**
   有些錯誤很難用 `if-else` 事先檢查（例如網路突然斷線、你要讀取的檔案剛剛剛好被使用者刪除了）。`try...except` 是一種「先做了再說，出事了我再處理」的思維（在 Python 界被稱為 EAFP 原則：*Easier to ask for forgiveness than permission*，求原諒比求許可容易）。
2. **不要濫用空白的 `except:`**：
   盡量指定你要捕捉什麼錯誤（例如 `except ValueError:`），或者用 `except Exception as e:` 來知道究竟發生了什麼事。如果只寫一個 `except:`，它會把你按 `Ctrl+C` 想強制停止程式的指令也攔截下來，會讓除錯變得非常困難喔！

---
## 🔗 航線關聯 (Flight Link)
- **飛行控制台 MOC**：[[30_Projects/15_python/00_Python_MOC|💻 Python MOC]]
