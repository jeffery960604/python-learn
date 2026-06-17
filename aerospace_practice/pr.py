#垂直起降無人機
battery=35 
rpm=8500
if(battery>=20 and rpm>=8000):
    print(True)
else:
    print('無法起飛')

#大氣壓力
p_start=101325
temp_deinc=0.0065
tenp_standar=288.15
h=3000
p=p_start*(1-(temp_deinc*h/tenp_standar)**5 )
print(p)




    