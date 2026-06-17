#for 已知次數
for second in range(1,11):#十次
    altitude=50*second
    print(f'第{second}秒，高度為:{altitude}m')

#while 等待條件符合
fuel=100
while fuel>=0:
    print(f'燃料剩餘{fuel}%,引擎持續運作中')
    fuel-=20
print('燃料耗盡')

