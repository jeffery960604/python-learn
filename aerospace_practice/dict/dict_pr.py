# 衛星傳回來的原始數據 (List of Dictionaries)
telemetry_data = [
    {"time": 1, "status": "Normal", "voltage": 12.5},
    {"time": 2, "status": "Warning", "voltage": 11.2},
    {"time": 3, "status": "Normal", "voltage": 12.4},
    {"time": 4, "status": "Critical", "voltage": 9.8},
    {"time": 5, "status": "Normal", "voltage": 12.6}
]
safe_voltages=[]
for record in telemetry_data:
    if record["status"]=="Normal":
        sV=record["voltage"]
        safe_voltages.append(sV)
print("安全電壓名單：", safe_voltages)

    