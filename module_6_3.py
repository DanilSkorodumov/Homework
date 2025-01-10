import random
class Animal():
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self,speed):
        self._cords = [0,0,0]
        self.speed = speed

    def move(self,dx,dy,dz):
        new_x = self._cords [0] + dx * self.speed
        new_y = self._cords [1] + dy * self.speed
        new_z = self._cords [2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i cant't dive :(")
        else:
            self._cords = [new_x,new_y,new_z]

    def get_cords(self):
        print(f'X: {self._cords[0]},Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peacful:)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        num_of_eggs = random.randint(1,4)
        print (f"Here are(is) {num_of_eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self,dz):
        new_z = self._cords[2] - abs ( dz )  * 0.5 * self.speed
        self._cords[2] = max ( new_z , 0 )

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal,Bird,AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self,speed):
        super().__init__(speed)
    def speak(self):
        print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()