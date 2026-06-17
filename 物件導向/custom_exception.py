# 1. 定義自定義錯誤類別 (繼承 Exception)
class NegativeNumberError(Exception):
    """當輸入數字為負數時拋出的錯誤"""
    value: int
    message: str

    def __init__(self, value: int) -> None:
        self.value = value
        self.message = f"錯誤：不接受負數 ({value})，請輸入正數。"
        # 呼叫父類別的 __init__ 傳入訊息
        super().__init__(self.message)

def check_age(age: int) -> None:
    if age < 0:
        # 2. 使用 raise 主動拋出錯誤
        raise NegativeNumberError(age)
    elif age < 18:
        print("年齡判斷結果：未成年")
    else:
        print("年齡判斷結果：成年")

if __name__ == "__main__":
    print("--- 自定義錯誤示範 ---")
    try:
        input_val = input("請輸入您的年齡: ")
        age = int(input_val)
        check_age(age)
        
    except NegativeNumberError as e:
        # 3. 捕捉我們自定義的錯誤
        print(f"捕捉到自定義錯誤: {e}")
        
    except ValueError:
        print("錯誤：請輸入有效的整數數字。")
        
    finally:
        print("檢查結束。")
