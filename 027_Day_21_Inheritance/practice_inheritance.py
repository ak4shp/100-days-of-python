class Animal:
    def __init__(self) -> None:
        self.eyes = 2
        self.move_speed = 0

    def breathe(self):
        print("Inhale, exhale")

    def move(self):
        self.move_speed = 10
        print(f"Moving with speed of {self.move_speed}.")


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        self.hold_water = True

    def swim(self):
        self.move_speed = 30
        print(f"Swimming.. with speed of {self.move_speed}")

    def breathe(self):
        super().breathe()
        print("Breathe Inside water !")


jelly = Fish()
jelly.swim()
jelly.breathe()
print(jelly.eyes)
print(jelly.hold_water)
print("------------------")
dyla = Animal()
dyla.move()
dyla.breathe()