class Numbers:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        print(f'Object created with values: {self.a}, {self.b}, {self.c}, {self.d}')

    def __del__(self):
        print(f'Object with values {self.a}, {self.b}, {self.c}, {self.d} is destroyed')

    def average(self):
        return (self.a + self.b + self.c + self.d) / 4

    def maximum(self):
        return max(self.a, self.b, self.c, self.d)

    def __str__(self):
        return f'Numbers(a={self.a}, b={self.b}, c={self.c}, d={self.d})'


# Создание объектов класса
# Объект с константными значениями
numbers1 = Numbers(1, 2, 3, 4)
print(f'Average: {numbers1.average()}')
print(f'Maximum: {numbers1.maximum()}')
print(numbers1)

# Объект с введенными с клавиатуры значениями
a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))
c = int(input('Enter value for c: '))
d = int(input('Enter value for d: '))
numbers2 = Numbers(a, b, c, d)
print(f'Average: {numbers2.average()}')
print(f'Maximum: {numbers2.maximum()}')
print(numbers2)

