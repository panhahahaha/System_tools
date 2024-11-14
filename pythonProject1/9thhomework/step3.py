class Car:
    # 构造方法，用于初始化汽车的私有属性
    def __init__(self, brand, model, displacement, acceleration_time):
        self.__brand = brand  # 品牌
        self.__model = model  # 型号
        self.__displacement = displacement  # 排量
        self.__acceleration_time = acceleration_time  # 百公里加速时间

    # 输出汽车的私有属性
    def print_car_info(self):
        print(f"Brand: {self.__brand}")
        print(f"Model: {self.__model}")
        print(f"Displacement: {self.__displacement}L")
        print(f"Acceleration Time (0-100 km/h): {self.__acceleration_time}s")

    # 根据百公里加速时间分级
    def get_acceleration_grade(self):
        if self.__acceleration_time < 5:
            return "Excellent"
        elif self.__acceleration_time < 7:
            return "Good"
        elif self.__acceleration_time < 10:
            return "Average"
        else:
            return "Below Average"


# 创建汽车实例
car1 = Car("Tesla", "Model S", 2.0, 3.2)
car2 = Car("BMW", "M4", 3.0, 4.1)
car3 = Car("Toyota", "Corolla", 1.8, 9.0)

# 输出汽车信息
print("Car 1 Information:")
car1.print_car_info()
print(f"Acceleration Grade: {car1.get_acceleration_grade()}")
print()

print("Car 2 Information:")
car2.print_car_info()
print(f"Acceleration Grade: {car2.get_acceleration_grade()}")
print()

print("Car 3 Information:")
car3.print_car_info()
print(f"Acceleration Grade: {car3.get_acceleration_grade()}")
