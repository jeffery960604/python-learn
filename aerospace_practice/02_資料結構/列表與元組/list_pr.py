# list 練習題：模擬爬升日誌
h = 0
s = 0
flight_log: list[str] = []
while h < 3000:
    h += 600
    s += 1
    flight_log.append(f'第{s}秒 高度為{h}m')

print(f'記錄完成，日誌共有 {len(flight_log)} 筆數據。')
print(flight_log)
print(f'最後一筆索引值: {len(flight_log)-1}')
print(f'第 5 筆數據: {flight_log[4]}')
