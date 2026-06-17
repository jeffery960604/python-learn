# 一次讀取「整個檔案」所有內容
with open("flight_log.txt", "r") as file:
    content = file.read()
    print(content)

# 一行一行讀取（適合大型 log 檔）
with open("flight_log.txt", "r") as file:
    for line in file:
        print(line)  # 每次 print 一行
