class Vehicle:
    __COLOR_VARIANTS = ['blue','red','green','white','black']

    def  __init__(self,owner,model,color,engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель:{self.__model}"

    def get_horsepower(self):
        return f"Мощность:{self.__engine_power}"

    def get_color(self):
        return f"Цвет:{self.__color}"

    def get_owner(self):
        return f"Владелец:{self.owner}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(self.get_owner())

    def set_color(self,new_color):
        if new_color.lower() in map(str.lower,self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}" )


class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5

    def __init__(self,owner,model,color,engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        super().__init__(owner,model,color,engine_power)



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()