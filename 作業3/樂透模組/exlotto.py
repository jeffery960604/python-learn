# ==========================================================
# 課程名稱：程式設計 Python 
# 作業編號：HW03
# 學生姓名：陳登翔 
# 學號：11450062A
# 撰寫日期：2026-05-21
# 程式功能簡述：樂透模組
# ==========================================================
import random
from typing import List

def lotto(n: int, m: int) -> List[int]:
    """
    從 1 到 n 個數字中隨機抽取 m 個不重複的數字。
    
    :param n: 數字的最大範圍 (1 到 n)
    :param m: 抽取的數字數量
    :return: 包含 m 個隨機抽取的數字之列表 (未排序)
    """
    if m > n:
        raise ValueError("抽取的數量 m 不能大於範圍 n")
    if n < 1 or m < 1:
        raise ValueError("範圍 n 和數量 m 必須是大於 0 的整數")
        
    return random.sample(range(1, n + 1), m)

