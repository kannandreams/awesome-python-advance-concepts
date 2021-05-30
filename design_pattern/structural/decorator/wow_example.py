from abc import ABC, abstractmethod


class INoodles(object):

    def get_ingredients(self):
        pass

    def get_cost(self):
        pass

    def get_service_tax(self):
        return self.get_cost() * 1.00

class IRice(object):

    def get_ingredients(self):
        pass

    def get_cost(self):
        pass

    def get_service_tax(self):
        return self.get_cost() * 1.00


class RiceNoodles(INoodles):
    def get_ingredients(self):
        return 'RiceNoodles'

    def get_cost(self):
        return 5.00

class EggNoodles(INoodles):
    def get_ingredients(self):
        return 'EggNoodles'

    def get_cost(self):
        return 5.00

class WhiteRice(IRice):
    def get_ingredients(self):
        return 'WhiteRice'

    def get_cost(self):
        return 5.00

class INoodlesDecorator(INoodles):
    def __init__(self, decorated_noodle):
        self.decorated_noodle = decorated_noodle

    def get_cost(self):
        return self.decorated_noodle.get_cost()

    def get_ingredients(self):
        return self.decorated_noodle.get_ingredients()

class IRiceDecorator(IRice):
    def __init__(self, decorated_noodle):
        self.decorated_rice = decorated_rice

    def get_cost(self):
        return self.decorated_rice.get_cost()

    def get_ingredients(self):
        return self.decorated_rice.get_ingredients()

class VegMix(INoodlesDecorator):

    def __init__(self, decorated_noodle):
        INoodlesDecorator.__init__(self, decorated_noodle)

    def get_cost(self):
        return self.decorated_noodle.get_cost()

    def get_ingredients(self):
        return self.decorated_noodle.get_ingredients() + ', Vegetables'


class Chicken(INoodlesDecorator):

    def __init__(self, decorated_noodle):
        INoodlesDecorator.__init__(self, decorated_noodle)

    def get_cost(self):
        return self.decorated_noodle.get_cost() + 0.5

    def get_ingredients(self):
        return self.decorated_noodle.get_ingredients() + ', Chicken'


class Tofu(INoodlesDecorator):

    def __init__(self, decorated_noodle):
        INoodlesDecorator.__init__(self, decorated_noodle)

    def get_cost(self):
        return self.decorated_noodle.get_cost() + 0.35

    def get_ingredients(self):
        return self.decorated_noodle.get_ingredients() + ', Tofu'


if __name__ == '__main__':
    mynoodle = EggNoodles()

    print('Ingredients: ' + mynoodle.get_ingredients() + '; Cost: ' +
          str(mynoodle.get_cost())+'; sales tax = '+str(mynoodle.get_service_tax()))

    mynoodle = VegMix(mynoodle)
    print('Ingredients: '+mynoodle.get_ingredients() +
          '; Cost: '+str(mynoodle.get_cost())+'; sales tax = '+str(mynoodle.get_service_tax()))

    mynoodle = Chicken(mynoodle)
    print('Ingredients: '+mynoodle.get_ingredients() +
        '; Cost: '+str(mynoodle.get_cost())+'; sales tax = '+str(mynoodle.get_service_tax()))

    mynoodle = Tofu(mynoodle)
    print('Ingredients: '+mynoodle.get_ingredients() +
        '; Cost: '+str(mynoodle.get_cost())+'; sales tax = '+str(mynoodle.get_service_tax()))
