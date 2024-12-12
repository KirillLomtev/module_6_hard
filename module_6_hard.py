import math


class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__color = self.__is_valid_color(color)[0]
        self.__sides = sides if self.__is_valid_sides(sides) and all(isinstance(item, int) for item in sides) else self.sides_count*[1]
        self.filled = self.__is_valid_color(color)[1]

    def __is_valid_color(self, color):
        if all(isinstance(item, int) for item in color):
            if color[0] in range(0,256) and color[1] in range(0,256) and color[2] in range(0,256):
                return color, True
            else:
                return self.__color, False
        else:
            return 'Error', False

    def set_color(self,*color):
        self.__color = self.__is_valid_color(color)[0]
        self.filled = self.__is_valid_color(color)[1]

    def get_color(self):
        if all(isinstance(item, int) for item in self.__color):
            return list(self.__color)
        else:
            return self.__color

    def __is_valid_sides(self, sides):
        if all(isinstance(item, int) for item in sides):
            if len(sides) == self.sides_count:
                return True
            else:
                return False
        else:
            print(f"Ошибка ввода сторон у {self.__str__()}, все стороны взяты за 1")
            return "Error"

    def get_sides(self):
        if all(isinstance(item, int) for item in self.__sides):
            return list(self.__sides)
        else:
            return self.__sides


    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0]/(2*math.pi)

    def get_cquare(self):
        return 2*math.pi*self.__radius**2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_cquare(self):
        p = self.__len__()
        return math.sqrt(p*(p-self.get_sides()[0])*(p-self.get_sides()[1])*(p-self.get_sides()[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides*self.sides_count if len(sides)==1 and all(isinstance(item, int) for item in sides) else [1]*self.sides_count

    def get_sides(self):
        return list(self.__sides)

    def get_volume(self):
        return self.get_sides()[0]**3



circle1 = Circle((200, 200, 100), 10.1) # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)



# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится

print(circle1.get_color())

cube1.set_color(300.1, 70, 15) # Не изменится

print(cube1.get_color())



# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится

print(cube1.get_sides())

circle1.set_sides(15) # Изменится

print(circle1.get_sides())



# Проверка периметра (круга), это и есть длина:

print(len(circle1))


# Проверка объёма (куба):

print(cube1.get_volume())

