# 無回傳值無參數值的函數
def greeting():
    print('Python歡迎你')
    print('謝謝')
    
# 有回傳值有參數值的函數
def plus(x1,x2):    # x1, x2 參數值
    y = x1 + x2   
    return y        # y 回傳值

# print(plus(3,5))

# 多回傳值有參數值的函數
def add_mul(x1,x2):    # x1, x2 參數值
    y1 = x1 + x2
    y2 = x1*x2
    return y1 , y2       # y1 y2回傳值

# z1,z2 = add_mul(3,5)
# print(z1)
# print(z2)

#%%
def interest(interest_type,subject):
    print('我的興趣' + interest_type)
    print('在' + interest_type + '中,我最喜歡' + subject)
    print()

interest( subject = '歐洲',interest_type = '旅遊' )

def interest(interest_type, subject = '日本'):
    print('我的興趣' + interest_type)
    print('在' + interest_type + '中,我最喜歡' + subject)
    print()

interest('旅遊')


def guest_info(firstname,lastname,gender, middlename = ''):
    if gender == 'm':
        print(lastname + middlename + firstname +'先生您好')
    else:
        print(lastname + middlename + firstname +'小姐您好')


guest_info(firstname='展榮',lastname='康',gender='m')
guest_info('Ben','富蘭克林','m','Tom')

