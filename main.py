class Person:
    #constructor - special ethod to initialize atributes
    def __init__(self, name, surname, age=None, gender=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def walk(self):
        print('Person', self.name, 'walking')

    def info(self):
        print('Person mame=', self.name, 'surname', self.surname,'age',self.age, 'gender=', self.gender)
