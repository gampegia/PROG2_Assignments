"""
Prog 2
W01
P01 2.2 Person

Authors:
Gwendoline Vocat (Vocatgwe), Gian Gamper (Gampegia), Jonas Bratschi (Bratsjon)

Date: 08.03.2024
"""


class Person:
    """
    Represents a person with attributes for hair color and age.

    Attributes:
        hair_color (str): The hair color of the person.
        age (int): The age of the person.
    """

    def __init__(self, hair_color, age):
        """
        Initializes a new instance of the Person class.

        Args:
            hair_color (str): The hair color of the person.
            age (int): The age of the person.
        """
        self.hair_color = hair_color
        self.age = age

    def speak(self, message):
        """
        Prints a message spoken by the person.

        Args:
            message (str): The message to be spoken.
        """
        print(message)

    def get_older(self):
        """
        Increases the person's age by 1.
        """
        self.age += 1


# Creating instances of the Person class
p = Person('black', 25)  # A person with black hair and 25 years old
p2 = Person('blonde', 30)  # A person with blonde hair and 30 years old
p3 = Person('brown', 35)  # A person with brown hair and 35 years old

# Aging the first person by one year and having them speak
p.get_older()
p.speak('Hey there! My hair color is ' + p.hair_color + ' and I am ' + str(p.age) + ' years old in one year.')
