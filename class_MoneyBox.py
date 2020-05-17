class MoneyBox:
    def __init__(self, capacity): # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.count = 0

    def can_add(self, v): # True, если можно добавить v монет, False иначе
        if (self.count + v) <= self.capacity:
            return True
        else: return False

    def add(self, v): # положить v монет в копилку
        self.count += v

a = MoneyBox(250)
a.add(2)
print(a.count)