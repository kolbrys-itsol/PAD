# zadanie 1
class Animal:

    def __init__(self, gender='Female', genus=None):
        self.isAlive = True
        self.gender = gender
        self.genus = genus

    def breed(self, partner):
        if self.gender == 'Female' and partner.gender == 'Male' and self.genus == partner.genus:
            if self.genus == 'Canis':
                return Dog()
            else:
                return Cat()
        else:
            raise Exception('attribute not found')

    @property
    def genus(self):
        return self._genus

    @genus.setter
    def genus(self, new_genus):
        if new_genus is None or new_genus == 'Canis' or new_genus == 'Felis':
            self._genus = new_genus
        else:
            raise Exception('Wrong genus type!')

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        if new_gender == 'Female' or new_gender == 'Male':
            self._gender = new_gender
        else:
            raise Exception('Wrong gender type!')


class Dog(Animal):
    def __init__(self, gender='Female', genus='Canis'):
        Animal.__init__(self, gender=gender, genus=genus)

    def woof(self):
        return "woof woof"

    @Animal.genus.setter
    def genus(self, new_genus):
        if new_genus == "Canis":
            self._genus = new_genus
        else:
            raise Exception('Dog can only be Canis')


class Cat(Animal):
    def __init__(self, gender='Female', genus='Felis'):
        Animal.__init__(self, gender=gender, genus=genus)

    def purr(self):
        return "purr"

    @Animal.genus.setter
    def genus(self, new_genus):
        if new_genus == "Felis":
            self._genus = new_genus
        else:
            raise Exception('Cat can only be Feline')


if __name__ == '__main__':
    test = Animal('Male', 'Canis')
    print(test.genus)
    print('======')
    test2 = Dog('Male')
    print(test2.woof())
    print('======')
    cat = Cat('Male')
    print(cat.purr())
    print('======')
    cat2 = Cat('Female')
    cat3 = cat2.breed(cat)
    print(cat3.genus)
    print(cat3.purr())


