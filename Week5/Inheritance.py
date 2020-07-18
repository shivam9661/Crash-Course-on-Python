class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


class Apple(Fruit):
    pass


class Grape(Fruit):
    pass


granny_smith = Apple('red', 'sweet')

carnelian = Grape('purple', 'sweet')

print(granny_smith.color, carnelian.color);


class Animal:
    sound = ""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print('my name is {},And i make sound of {}'.format(self.name, self.sound))


class Piglet(Animal):
    sound = 'Oink!'


hamlet = Piglet("Hamlet")
hamlet.speak()


class Cow(Animal):
    sound = 'Mooooo'

milky = Cow('Milky White')

milky.speak()
