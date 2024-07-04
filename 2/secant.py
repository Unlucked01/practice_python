from trig_function import TrigFunction, math


class Secant(TrigFunction):
    def value(self):
        """Возвращает значение секанса для self.x"""
        return 1 / math.cos(self.x)

    def derivative(self):
        """Возвращает производную секанса"""
        return Secant(math.tan(self.x) * self.value())

    def __str__(self):
        return f"Secant(x={self.x})"

