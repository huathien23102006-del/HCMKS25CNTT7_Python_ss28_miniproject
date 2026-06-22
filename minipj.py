class BaseVehicle:
    def __init__(self, license_plate):
        self.__odometer = 0
        self.license_plate = license_plate
    
    @property
    def odometer(self):
        return self.__odometer

    def calculate_efficiency(self):
        pass
    
    def drive(self, distance):
        if distance > 0:
            self.__odometer += distance
        else:
            print("Lỗi! số km phải lớn hơn 0")
    
    def __lt__(self, other):
        if isinstance(other, BaseVehicle):
            return self.odometer < other.odometer
    
    @staticmethod
    def validate_license_plate(plate):
        return (len(plate) == 9 and palte.startswith("29"))

class ElectricBus(BaseVehicle):
    def calculate_efficiency(self):
        result = 100 - (self.odometer * 0.005)

        if result < 50:
            return 50.0
        
        return result

class AutonomousFeature:
    def calculate_efficiency(self):
        return 95.0

class RoboBus(ElectricBus, AutonomousFeature):
    def calculate_efficiency(self):
        electric_bus = ElectricBus.calculate_efficiency(self)
        autonomous_feature = AutonomousFeature.calculate_efficiency(self)
        return (electric_bus + autonomous_feature) / 2
def main():
    current_vehicle = None
    while True:
        print("""
        ===== SMART TRANSIT MENU =====
        1. Khởi tạo & Đăng ký xe lai RoboBus mới
        2. Giả lập vận hành & kiểm tra hiệu suất 
        """)

        choice = input("Chọn chức năng(1-2): ")
        match choice:
            case "1":
                plate = input("Nhập biển số xe (9 kí tự, bắt đầu bằng 29): ")
                if BaseVehicle.validate_license_plate(plate):
                    current_vehicle = RoboBus(plate)
                    print("[Thành công]: Khởi tạo phương tiện RoboBus thành công!")
                    print("[MRO Architecture]: " + "->" .join(cls.__name__ for cls in RoboBus.__mro__))
                else:
                    print("[Lỗi]: Biển số không hợp lệ!")
            case "2":
                if current_vehicle is None:
                    print("[Lỗi]: Chưa có xe!")
                    continue
                try:
                    distance = float(input("Nhập số km di chuyển mới phát sinh: "))
                    current_vehicle.drive(distance)
                    print("[Thành công]: Cập nhật lộ trình xe chạy thành công.")
                    print("Tổng quãng đường:",current_vehicle.odometer,"km")
                    print("Hiệu suất tiêu thụ:",current_vehicle.calculate_efficiency(),"%")
                except ValueError as e:
                    print(e)

            case "3":
                break

            case _:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()


