'''
📝 學姊的 Python 飛行測驗 (第四彈：打造自動化加工機)
第一題：引擎啟動程序 (最基本的函數，不需原物料，只有 print)

情境：每次啟動引擎都要做一連串的檢查，我們把它寫成一個自動化按鈕。
任務：
定義一個函數叫做 start_engine()。
在函數裡面，依序印出三行字："1. 檢查燃料閥..."、"2. 啟動點火裝置..."、"3. 引擎啟動成功！"。
函數定義好之後，在最外面呼叫這個函數一次，看看這三行字有沒有印出來。
'''
def start_engine() :
    print("1. 檢查燃料閥...")
    print("2. 啟動點火裝置...")
    print("3. 引擎啟動成功！")
start_engine()

'''第二題：燃油需求計算機 (需要原物料，並且把成品 return 給你)

情境：機長需要知道飛這趟航線要加多少油。
任務：
定義一個函數叫做 calculate_fuel(distance, efficiency)。它需要兩個原物料：distance (飛行距離) 和 efficiency (燃油效率，也就是一單位燃料能飛多遠)。
在函數裡計算需要的油量：公式是 需要油量 = 距離 / 燃油效率。
使用 return 把算出來的結果吐出來。
呼叫這個函數，把距離設為 1000 (公里)，效率設為 5。
拿一個變數去接它吐出來的結果（例如 result = ...），然後把結果印出來看是不是 200。
'''

def calculate_fuel(distance, efficiency):
    result = distance/efficiency
    return(result)

result = calculate_fuel(1000,5)
print(result)

'''第三題：飛航高度廣播員 (結合判斷式與 return)

情境：我們需要一個自動廣播員，根據飛機的高度來決定廣播內容。
任務：
定義一個函數叫做 check_altitude(height)。
在函數裡面寫一個 if-else 判斷式：
如果 height 大於等於 10000，return 字串 "已到達巡航高度，可以解開安全帶"。
如果 height 小於 10000，return 字串 "飛機爬升中，請繫好安全帶"。
呼叫這個函數，分別餵給它 12000 和 5000 這兩個數字，用變數接住回傳值，並把廣播內容印出來。
'''
def check_altitude(height):
    if height >= 10000:
        result_1 = "已到達巡航高度，可以解開安全帶"
        return(result_1)
    else:
        result_2 = "飛機爬升中，請繫好安全帶"
        return(result_2)

test1 = check_altitude(12000)
print(test1)
test2 = check_altitude(5000)
print(test2)



