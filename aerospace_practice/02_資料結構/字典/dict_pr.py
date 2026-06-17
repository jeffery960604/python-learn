# 字典練習：篩選衛星傳回的原始數據
telemetry_data = [
    {"time": 1, "status": "Normal", "voltage": 12.5},
    {"time": 2, "status": "Warning", "voltage": 11.2},
    {"time": 3, "status": "Normal", "voltage": 12.4},
    {"time": 4, "status": "Critical", "voltage": 9.8},
    {"time": 5, "status": "Normal", "voltage": 12.6}
]

safe_voltages: list[float] = []
for record in telemetry_data:
    if record["status"] == "Normal":
        vol = record["voltage"]
        if isinstance(vol, (int, float)):
            safe_voltages.append(float(vol))

print("安全電壓名單 (狀態為 Normal)：", safe_voltages)


