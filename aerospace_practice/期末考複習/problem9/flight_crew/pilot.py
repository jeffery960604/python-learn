class Pilot :
    def __init__(self, name , license_type):
        self.name = name 
        self.license_type = license_type
        self.flight_hours = 0
    def fly_mission(self, hours):
        self.flight_hours+=hours
        print(f'{self.name}')
    def get_report(self) :
        print("==== 飛行員報告 ====")
        print("姓名：[姓名]")
        print(f"總飛行時數：{self.flight_hours} 小時")
        if self.flight_hours >= 500:
            print("資歷：資深機師")
        elif self.flight_hours >= 100 :
            print("資歷：資深機師")
        else:
            print("資歷：飛行員")
        
        