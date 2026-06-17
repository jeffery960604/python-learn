def detect_collision(my_alt, other_alt):
    diff = abs(my_alt - other_alt)
    if diff<=1000 :
        return("警告！高度差過小，有相撞風險！")
    else :
        return("安全：維持安全隔離")
