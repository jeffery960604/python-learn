# pyright: reportImplicitRelativeImport=false
# physics_engine.py - 物理計算引擎模組
import math
from constants import MU_EARTH # type: ignore

def calculate_escape_speed(radius: float) -> float | str:
    """
    計算給定半徑位置的逃逸速度。
    """
    # 邏輯保護：半徑不能為 0 或負數
    if radius <= 0:
        return "錯誤：半徑必須大於 0 喔！"
    
    # 核心公式：sqrt(2 * mu / r)
    result = math.sqrt(2 * MU_EARTH / radius)
    return result
