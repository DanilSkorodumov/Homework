import math  # Импортируем модуль math для математических операций, таких как вычисление площади и корня.


class Figure:
    sides_count = 0  # Количество сторон фигуры (по умолчанию 0 для базового класса)

    def __init__(self, color, *sides):
        self.__sides = []  # Инициализируем инкапсулированный атрибут для сторон
        self.__color = list(color)  # Сохраняем цвет в формате RGB как список
        self.filled = False  # Устанавливаем, закрашена ли фигура

        if not self.__is_valid_sides(*sides):  # Проверяем корректность переданных сторон
            self.__sides = [1] * self.sides_count  # Если некорректно, устанавливаем стороны по умолчанию
        else:
            self.__sides = list(sides)  # Иначе сохраняем переданные стороны

    def __is_valid_color(self, r, g, b):
        """Проверяет корректность переданных значений цвета."""
        return all(isinstance(x, int) and 0 <= x <= 255 for x in
                   (r, g, b))  # Проверяем, что все значения - целые числа в диапазоне от 0 до 255

    def set_color(self, r, g, b):
        """Устанавливает новый цвет, если он корректный."""
        if self.__is_valid_color(r, g, b):  # Проверяем корректность цвета
            self.__color = [r, g, b]  # Устанавливаем новый цвет
        # Если цвет некорректный, ничего не меняем

    def get_color(self):
        """Возвращает текущий цвет."""
        return self.__color  # Возвращаем список RGB цветов

    def __is_valid_sides(self, *new_sides):
        """Проверяет корректность сторон."""
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)
        # Проверяем количество сторон и что все стороны - положительные целые числа

    def get_sides(self):
        """Возвращает список сторон."""
        return self.__sides  # Возвращаем список сторон фигуры

    def set_sides(self, *new_sides):
        """Устанавливает новые стороны."""
        if self.__is_valid_sides(*new_sides):  # Проверяем корректность новых сторон
            self.__sides = list(new_sides)  # Устанавливаем новые стороны

    def __len__(self):
        """Возвращает периметр фигуры."""
        return sum(self.__sides)  # Возвращаем сумму всех сторон (периметр)


class Circle(Figure):
    sides_count = 1  # У круга одна сторона (длина окружности)

    def __init__(self, color, circumference):
        super().__init__(color)  # Вызываем конструктор родительского класса Figure

        if not isinstance(circumference, (int, float)) or circumference <= 0:  # Проверяем тип и значение окружности
            raise ValueError("Circumference must be a positive number.")  # Выбрасываем ошибку при некорректном значении

        self.__radius = circumference / (2 * math.pi)  # Рассчитываем радиус по длине окружности
        self.set_sides(circumference)  # Устанавливаем длину окружности как сторону

    def get_square(self):
        """Возвращает площадь круга."""
        return math.pi * (self.__radius ** 2)  # Площадь круга: π * r^2


class Triangle(Figure):
    sides_count = 3  # У треугольника три стороны

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)  # Вызываем конструктор родительского класса Figure с тремя сторонами

    def get_square(self):
        """Возвращает площадь треугольника по формуле Герона."""
        a, b, c = self.get_sides()  # Получаем стороны треугольника

        if not all(isinstance(side, (int, float)) and side > 0 for side in (a, b, c)):
            raise ValueError("All sides must be positive numbers.")  # Проверяем корректность сторон

        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Площадь по формуле Герона


class Cube(Figure):
    sides_count = 12  # У куба двенадцать рёбер

    def __init__(self, color, edge_length):
        super().__init__(color)  # Вызываем конструктор родительского класса Figure

        if not isinstance(edge_length, (int, float)) or edge_length <= 0:
            raise ValueError("Edge length must be a positive number.")
            # Проверяем тип и значение длины ребра

        self.set_sides(*[edge_length] * self.sides_count)
        # Устанавливаем все рёбра равными

    def get_volume(self):
        """Возвращает объём куба."""
        edge_length = self.get_sides()[0]  # Получаем длину ребра (все рёбра одинаковые)
        return edge_length ** 3  # Объём куба: a^3


# Пример использования классов
circle1 = Circle((200, 200, 100), 10)  # Создаем объект круга с цветом и длиной окружности
cube1 = Cube((222, 35, 130), 6)  # Создаем объект куба с цветом и длиной ребра

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменение цвета круга
print(circle1.get_color())  # Выводим текущий цвет круга: [55,66,77]
cube1.set_color(300, 70, 15)  # Попытка изменить цвет куба на некорректный
print(cube1.get_color())  # Выводим текущий цвет куба: [222,35,130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12)  # Попытка изменить стороны куба на некорректные
print(cube1.get_sides())  # Выводим текущие стороны куба: [6]*12
circle1.set_sides(15)  # Изменение стороны круга на новую длину окружности
print(circle1.get_sides())  # Выводим текущие стороны круга: [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # Выводим длину окружности: ~15.71

# Проверка объёма (куба):
print(cube1.get_volume())  # Выводим объём куба: ~216