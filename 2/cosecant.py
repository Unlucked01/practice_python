from trig_function import TrigFunction, math


class Cosecant(TrigFunction):
    def value(self):
        """Возвращает значение косеканса для self.x"""
        return 1 / math.sin(self.x)

    def derivative(self):
        """Возвращает производную косеканса"""
        return Cosecant(-math.cos(self.x) * self.value())

    def __str__(self):
        return f"Cosecant(x={self.x})"

