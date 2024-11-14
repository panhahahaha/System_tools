import winsound
class Clock:
    id = None  # 字符串
    price = None  # 浮点数

    def ring(self):
        winsound.Beep(2000, 3000)
clock1 = Clock()
clock1.id = "01010"
clock1.price = 10.8
clock1.ring()
print(clock1.id,clock1.price)
clock2 = Clock()
clock2.id = "02020"
clock2.price = 12.8
clock2.ring()
print(clock2.id,clock2.price)