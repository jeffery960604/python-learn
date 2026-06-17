def divide_numbers():
    try:
        # 嘗試執行可能會發生錯誤的程式碼
        num1 = float(input("請輸入被除數: "))
        num2 = float(input("請輸入除數: "))
        
        result = num1 / num2
        
    except ValueError:
        # 當輸入不是數字時觸發
        print("錯誤：請輸入有效的數字！")
        
    except ZeroDivisionError:
        # 當除數為 0 時觸發
        print("錯誤：除數不能為零！")
        
    except Exception as e:
        # 捕捉其他所有類型的錯誤
        print(f"發生了未預期的錯誤: {e}")
        
    else:
        # 如果 try 區塊中的程式碼成功執行（沒出錯），則執行這裡
        print(f"計算結果是: {result}")
        
    finally:
        # 無論是否發生錯誤，最後都會執行這裡
        print("程式執行結束。")

if __name__ == "__main__":
    divide_numbers()
