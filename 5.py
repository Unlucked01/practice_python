import numpy as np
import matplotlib.pyplot as plt


def calculate_function(a, b, c, d, f, g, x_values):
    return np.exp(np.sin(a * x_values ** 2 + b * x_values + c)) + d * np.cos(f * x_values + g)


def main():
    # Определение тестовых данных
    default_params = {
        "a": 1.0,
        "b": 1.0,
        "c": 0.0,
        "d": 1.0,
        "f": 1.0,
        "g": 0.0,
        "x_min": -10.0,
        "x_max": 10.0,
        "num_points": 1000,
        "color": "blue",
        "background_color": "white",
        "plot_type": "line",
        "line_width": 2.0
    }

    use_defaults = input("Использовать тестовые данные по умолчанию? (y/n): ").lower() == 'y'

    if use_defaults:
        a = default_params["a"]
        b = default_params["b"]
        c = default_params["c"]
        d = default_params["d"]
        f = default_params["f"]
        g = default_params["g"]
        x_min = default_params["x_min"]
        x_max = default_params["x_max"]
        num_points = default_params["num_points"]
        color = default_params["color"]
        background_color = default_params["background_color"]
        plot_type = default_params["plot_type"]
        line_width = default_params["line_width"]
    else:
        # Ввод параметров функции
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))
        d = float(input("Введите коэффициент d: "))
        f = float(input("Введите коэффициент f: "))
        g = float(input("Введите коэффициент g: "))

        # Ввод диапазона и количества точек
        x_min = float(input("Введите минимальное значение x: "))
        x_max = float(input("Введите максимальное значение x: "))
        num_points = int(input("Введите количество точек: "))

        # Ввод параметров для графика
        color = input("Введите цвет графика (например, 'blue', 'green'): ")
        background_color = input("Введите цвет фона (например, 'white', 'black'): ")
        plot_type = input("Введите тип графика ('line' для линий, 'dot' для точек): ")
        line_width = float(input("Введите толщину линии (если выбран тип 'line'): "))

    # Генерация значений x и y
    x_values = np.linspace(x_min, x_max, num_points)
    y_values = calculate_function(a, b, c, d, f, g, x_values)

    # Определение масштаба по оси y
    y_min = y_values.min()
    y_max = y_values.max()

    # Создание графика
    fig, ax = plt.subplots()
    ax.set_facecolor(background_color)

    if plot_type == 'line':
        ax.plot(x_values, y_values, color=color, linewidth=line_width)
    elif plot_type == 'dot':
        ax.plot(x_values, y_values, 'o', color=color)

    # Настройка осей
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

    # Установка пределов для осей
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])

    plt.show()


if __name__ == "__main__":
    main()