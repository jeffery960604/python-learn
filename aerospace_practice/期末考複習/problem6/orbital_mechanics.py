def calculate_delta_v(r1, r2):
     # 地球標準重力參數 (km^3/s^2)
    mu = 398600  
    
    # 計算轉移軌道半長軸
    a = (r1 + r2) / 2
    
    # 第一段加速 (離開原軌道)
    v1 = (mu / r1) ** 0.5
    vt1 = (mu * (2/r1 - 1/a)) ** 0.5
    dv1 = abs(vt1 - v1)
    
    # 第二段加速 (進入目標軌道)
    v2 = (mu / r2) ** 0.5
    vt2 = (mu * (2/r2 - 1/a)) ** 0.5
    dv2 = abs(vt2 - v2)
    
    # 總共需要的速度變化量 (Delta-V)
    total_dv = dv1 + dv2
    return(total_dv)
