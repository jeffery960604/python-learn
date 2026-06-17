# while 迴圈練習：探測器墜落模擬
h = 5000
s = 0
print(f"初始高度: {h}m")
while h >= 10:
    h = h / 2
    s += 1
    print(f'第 {s} 秒，高度減半為 {h:.2f}m')

print(f"模擬結束，共經過 {s} 秒後高度低於 10m")
