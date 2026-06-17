---
type: note
tags:
  - 學科/python
status: active
created: 2026-05-22
---


---
### 💡 最白話的解釋：`self` 就是「我自己」

在英文裡，self 就是「自己」的意思。
當你在類別（設計圖）裡面寫程式時，因為**「物件根本還沒被創造出來」**，你不知道未來這個物件會叫 `my_car`、`your_car` 還是 `car_a`。

所以，在設計圖裡面，我們統一用 `self` 來代稱**「未來那個被創造出來的物件本人」**。
在設計圖裡寫 `self.name = "小明"`，翻譯成白話文就是：**「我自己的名字叫做小明」**。

---

### 🏧 情境比喻：銀行的 ATM 提款機

想像「銀行帳戶」是一個類別（設計圖），裡面有一個「存款」的方法。
今天，**小明**和**小華**各自去開戶，產生了兩個不同的物件：

```python
class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name  # 我自己的名字
        self.balance = balance        # 我自己的餘額

    # 存款的動作
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner_name} 存了 {amount} 元，目前餘額：{self.balance}")
```

現在，小明和小華要去存錢了：
```python
ming_account = BankAccount("小明", 1000)
hua_account = BankAccount("小華", 5000)

ming_account.deposit(500)  # 小明存 500
```

**🔥 這裡是最核心的問題：**
當你執行 `ming_account.deposit(500)` 的時候，程式怎麼知道這 500 元是要加進「小明」的餘額，而不是加進「小華」的餘額？畢竟大家都是共用同一個 `deposit` 方法啊！

**🔑 答案就是 `self`！**
當你呼叫 `ming_account.deposit(500)` 時，Python 在背後偷偷做了一件「偷天換日」的事情。

Python 其實把程式碼翻譯成了這樣：
👉 `BankAccount.deposit(ming_account, 500)`

也就是說，**Python 自動把 `ming_account` 這個物件，當作「第一個參數」塞進了方法裡！**

我們回頭看定義：
`def deposit(self, amount):`
*   第一個位置 `self`，接到了 `ming_account`。
*   第二個位置 `amount`，接到了 `500`。

所以在這個瞬間，方法裡面的 `self.balance`，指的就是 `ming_account.balance`（小明的餘額）。它就不會去改到小華的錢了！

這就像是你去 ATM 存錢，你必須**「插入你自己的提款卡 (self)」**，ATM 才知道要操作誰的帳戶。

---

### 🆚 比較：有寫 self 跟沒寫 self 有什麼差別？

如果在設計圖裡面，我們不用 `self` 會發生什麼事？

**❌ 錯誤示範（沒有用 self）：**
```python
class Student:
    def __init__(self, name):
        # 這裡只是創造了一個「暫時的變數」，方法執行完就消失了！
        student_name = name  

    def say_hi(self):
        # 這裡會報錯！因為它找不到 student_name 是什麼
        print(f"大家好，我是 {student_name}") 

# 測試
mike = Student("麥克")
mike.say_hi()  # 崩潰報錯！
```

**✅ 正確示範（使用 self）：**
```python
class Student:
    def __init__(self, name):
        # 加上 self.，這就像是用奇異筆把名字「寫在這個學生的額頭上」
        # 這個資料會跟著這個物件一輩子！
        self.student_name = name  

    def say_hi(self):
        # 加上 self.，代表「去讀取我自己額頭上的名字」
        print(f"大家好，我是 {self.student_name}") 

# 測試
mike = Student("麥克")
mike.say_hi()  # 成功印出：大家好，我是 麥克
```

---

### 總結 3 個關於 self 的必備觀念：

1. **它是代名詞**：在設計圖裡，`self` 就代表「未來正在執行動作的那個物件**本人**」。
2. **用來貼標籤**：`self.屬性` 就像是拿標籤貼在物件身上，確保資料會緊緊跟著這個物件，而不會在函數結束後就消失。
3. **強制規定**：在 Python 裡，類別裡面的每一個「方法（函數）」，小括號裡面的**第一個參數永遠必須是 `self`**（這是一個鐵規則）。

你可以把 `self` 想成是去醫院看病時填的**「初診資料表」**。醫生（方法）要看病時，必須先拿到你的資料表（`self`），才知道你是誰、過去有什麼病史（屬性），然後才能對「你」進行治療（動作）。

這樣解釋有讓 `self` 的形象具體一點了嗎？如果還是覺得哪邊怪怪的，隨時跟我說！

---
## 🔗 航線關聯 (Flight Link)
- **飛行控制台 MOC**：[[30_Projects/15_python/00_Python_MOC|💻 Python MOC]]
