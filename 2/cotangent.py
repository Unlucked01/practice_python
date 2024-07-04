from trig_function import TrigFunction, math


class Cotangent(TrigFunction):
    def value(self):
        """Возвращает значение котангенса для self.x"""
        return 1 / math.tan(self.x)

    def derivative(self):
        """Возвращает производную котангенса"""
        return Cotangent(-1 / math.sin(self.x) ** 2)

    def __str__(self):
        return f"Cotangent(x={self.x})"

