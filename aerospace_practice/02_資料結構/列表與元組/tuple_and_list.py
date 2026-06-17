# 任務一：Tuple 的解包與 List 更新（飛行軌跡模擬）
# 我們有一架無人機出發時的三維座標，記錄在 Tuple 裡 (x, y, z)。
# 現在無人機收到指令，需要將高度（z 軸）提升 150 公尺，並將新的座標記錄為 List 以便後續不斷更新。

start_pos = (34.0, 12.5, 500.0)
print('起始點座標:', start_pos)

# 解包
x, y, z = start_pos

# 建立新的 List 並更新高度
current_pos = [x, y, z + 150]
print('更新後座標:', current_pos)
