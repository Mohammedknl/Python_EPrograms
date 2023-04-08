class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("An animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("The dog barks.")


class Cat(Animal):
    def speak(self):
        print("The cat meows.")


animal = Animal("Unknown")
animal.speak()

dog = Dog("Buddy")
dog.speak()

cat = Cat("Luna")
cat.speak()

