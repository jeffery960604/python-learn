'''任務：跨檔案連線測試

請開一個全新的檔案，命名為 engine_room.py。 在這個檔案裡，定義一個簡單的函數：
python
def check_temperature():
    return "引擎溫度正常，維持在 850 度"
再開第二個新檔案，命名為 main_control.py（主控台）。
在主控台裡，使用 from engine_room import check_temperature。
呼叫 check_temperature()，拿變數接住它，並且印出來！'''

from engine_room import check_temperature
test = check_temperature()
print(test)