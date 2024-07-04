import math


class TrigFunction:
    def __init__(self, x):
        self.x = x  # Переменная, для которой вычисляется значение функции

    def value(self):
        """Метод для получения значения функции. Должен быть переопределен в наследниках."""
        raise NotImplementedError("This method should be overridden in subclasses")

    def derivative(self):
        """Метод для получения производной функции. Должен быть переопределен в наследниках."""
        raise NotImplementedError("This method should be overridden in subclasses")

    def __str__(self):
        return f"TrigFunction(x={self.x})"
