class Person:
    def __init__(self, hair_color, age): 
        self.hair_color = hair_color
        self.age = age

    def speak(self, message):
        print(message)

    def get_older(self):
        self.age += 1

p = Person('black', 25)
p2 = Person('blonde', 30)
p3 = Person('brown', 35)

p.get_older()
p.speak('Hey there! My hair color is ' + p.hair_color + ' and I am ' + str(p.age) + ' years old in one year.')