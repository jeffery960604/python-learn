'''🚀 航太實驗室終極任務：霍曼轉移任務控制台
第一步：打造軌道力學模組 (請在 problem6 資料夾建立新檔案 orbital_mechanics.py)
為了不讓複雜的數學公式模糊了 Python 的學習焦點，學姊已經幫你把「霍曼轉移 $\Delta v$ (速度變化量)」的數學公式寫好了。

任務：在 orbital_mechanics.py 裡，定義一個函數叫做 calculate_delta_v(r1, r2)。
把你需要的原物料 r1 (目前軌道半徑) 和 r2 (目標軌道半徑) 丟進去，然後把下面這段數學公式包進函數裡，並記得把最後算出來的 total_dv 給 return 出來。
python
# 這是要包在 calculate_delta_v 函數裡面的公式喔！
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
第二步：打造任務主控台 (在你的 main.py 裡面寫)
任務 1：從剛剛的 orbital_mechanics 模組中，import 你的那台計算機 calculate_delta_v。
任務 2：建立一個字典 mission_data，記錄我們太空船的現狀：
python
mission_data = {
    "current_radius": 6700,         # 目前停泊在半徑 6700 km 的低地軌道
    "fuel_capacity_dv": 2.5,        # 我們剩下的燃料，最多只能提供 2.5 km/s 的速度變化
    "target_orbits": [7000, 10000, 42164] # 長官給了三個候選目標軌道 (42164 是同步軌道喔)
}
任務 3 (核心組合技)： 使用 for 迴圈，把 target_orbits 裡面的三個目標軌道半徑，一個一個拿出來。
任務 4：在迴圈裡面，呼叫你進口來的 calculate_delta_v 計算機！ 把字典裡的 current_radius 當作 r1，把迴圈拿出來的目標軌道當作 r2，餵給計算機，並拿一個變數 req_dv 接住回傳的結果。
任務 5：拿算出來的 req_dv，去跟字典裡的 fuel_capacity_dv 做 if-else 比較：
如果 req_dv 小於等於燃料極限：印出 "目標軌道 [r2] km：燃料充足，需要 [req_dv] km/s，允許轉移！"
如果大於燃料極限：印出 "目標軌道 [r2] km：燃料不足！需要 [req_dv] km/s，任務駁回。"'''

from orbital_mechanics import calculate_delta_v

mission_data = {
    "current_radius": 6700,         # 目前停泊在半徑 6700 km 的低地軌道
    "fuel_capacity_dv": 2.5,        # 我們剩下的燃料，最多只能提供 2.5 km/s 的速度變化
    "target_orbits": [7000, 10000, 42164] # 長官給了三個候選目標軌道 (42164 是同步軌道喔)
}
r1 = mission_data["current_radius"]
for r2 in mission_data["target_orbits"]:
    req_dv = calculate_delta_v(r1,r2)
    if req_dv >= mission_data["fuel_capacity_dv"]:
        print(f"目標軌道 {r2} km：燃料不足！需要 {req_dv} km/s，任務駁回。")
    else:
        print(f"目標軌道 {r2} km：燃料充足，需要 {req_dv} km/s，允許轉移！")
