class multifilter():

    def judge_half(pos, neg):
            return pos >= neg
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return pos > 0
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0
        # допускает элемент, если его допускают все функции (neg == 0)


    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge =judge
        self.index = 0
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self

    def __next__(self):
        self.pos = 0  # при каждой проверке нового числа обнуляем значения
        self.neg = 0

        if self.index < len(self.iterable):  # проходим по всему числам из диапазона
            self.index += 1  # увеличиваем индекс
            # здесь создаем обычный цикл for,
            # проходящий по внешним функциям mul
            # (а помним что они у нас означают funcs),
            # увеличиваем pos (true) or neg (false)
            for f in self.funcs:
                if f(self.iterable[self.index-1]) == True:
                    self.pos += 1
                else:
                    self.neg += 1
        # отправляем на проверку установленного фильтра judge c найденным кол-вом pos neg
            if self.judge(self.pos, self.neg):
                return self.iterable[self.index-1]
            # возвращаем число по индексу  - оно и будет показано при print
            else:
                return self.__next__()

        raise StopIteration
    # бросаем исключение которое останавливает итерацию


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]