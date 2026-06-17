# pyright: reportImplicitRelativeImport=false
# main.py - 主程式執行入口
import physics_engine as pe # type: ignore
from constants import EARTH_RADIUS # type: ignore

def run_test():
    # 1. 準備數據：地球表面的位置 (即半徑 = 地球半徑)
    current_location = EARTH_RADIUS
    
    # 2. 呼叫函數
    v_escape = pe.calculate_escape_speed(current_location)
    
    # 3. 輸出結果
    if isinstance(v_escape, float):
        print(f"🌍 地球表面的逃逸速度約為：{v_escape:.2f} km/s")
        print(f"換算時速約為：{v_escape * 3600:.0f} km/h")
    else:
        print(v_escape)

if __name__ == "__main__":
    run_test()
