""" Notes

* No variable should hold a reference to a concrete class.
* No class should derive from a concrete class.
* No method should override an implemented method of any
of its base classes.
"""


import unittest
import logging
import sys

class LogObject:
    def __init__(self):
        self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))

""" Duck Objects for No Pattern
"""
class MallardDuck(LogObject):
    def quack(self):
        self.log.info('Honk honk!')


class DecoyDuck(LogObject):
    def quack(self):
        self.log.info('Qua qua!')


class RubberDuck(LogObject):
    def quack(self):
        self.log.info('Squeak squeak!')



""" Pizza Simple Factory

What if we want to create NY and Chicago
style pizza? One way is to make a new version
of the SimplePizzaFactory and compose the store
with them. 

"""

class SimplePizzaFactory(LogObject):

    def create_pizza(self, type):
        pizza = None
        if type == 'cheese':
            pizza = CheesePizza()
        elif type == 'pepperoni':
            pizza = PepperoniPizza()
        elif type == 'clam':
            pizza = ClamPizza()
        elif type == 'veggie':
            pizza = VeggiePizza()
        
        return pizza


# Concrete pizza classes
class CheesePizza():
    pass
class PepperoniPizza():
    pass
class ClamPizza():
    pass
class VeggiePizza():
    pass



"""  Pizza Factory Method
"""
class PizzaStore(LogObject):
    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        
        # Tell the pizza to create itself 
        # (Then stop talking to your pizza)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
    # Abstract. Subclasses will implement.
    def create_pizza(self, pizza_type):
        return object()


class NYPizzaStore(PizzaStore):
    def create_pizza(self):
        pass
class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self):
        pass
class WashingtonPizzaStore(PizzaStore):
    def create_pizza(self):
        pass    

# NY Style
class NYStyleCheesePizza(Pizza):
    pass
class NYStylePepperoniPizza(Pizza):
    pass
class NYStyleClamPizza(Pizza):
    pass
class NYStyleVeggiePizza(Pizza):
    pass

# Chicago Style
class ChicagoStyleCheesePizza(Pizza):
    pass
class ChicagoStylePepperoniPizza(Pizza):
    pass
class ChicagoStyleClamPizza(Pizza):
    pass
class ChicagoStyleVeggiePizza(Pizza):
    pass

# Washington Style
class WashingtonStyleCheesePizza(Pizza):
    pass
class WashingtonStylePepperoniPizza(Pizza):
    pass
class WashingtonStyleClamPizza(Pizza):
    pass
class WashingtonStyleVeggiePizza(Pizza):
    pass


""" Abstract Factory
"""

class PizzaIngredientFactory(LogObject):
    def create_sauce(self):
        pass
    def create_dough(self):
        pass
    def create_cheese(self):
        pass
    def create_veggies(self):
        pass
    def create_pepperoni(self):
        pass
    def create_clams(self):
        pass

        
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_sauce(self):
        return MarinaraSauce()
    def create_dough(self):
        return ThinCrustDough()
    def create_cheese(self):
        return ReggianoCheese()
    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]
    def create_pepperoni(self):
        return SlicedPepperoni()
    def create_clams(self):
        return FreshClams()


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_sauce(self):
        return PlumTomatoSauce()
    def create_dough(self):
        return ThickCrustDough()
    def create_cheese(self):
        return MozzarellaCheese()
    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]
    def create_pepperoni(self):
        return SlicedPepperoni()
    def create_clams(self):
        return FreshClams()


# Ingredient Families
# NY
class FreshClams:
    pass
class MarinaraSauce:
    pass
class ThinCrustDough:
    pass
class ReggianoCheese:
    pass

# Chicago
class FrozenClams:
    pass
class PlumTomatoSauce:
    pass
class ThickCrustDough:
    pass
class MozzarellaCheese:
    pass

# California
class Calimari:
    pass
class BruschettaSauce:
    pass
class VeryThinCrust:
    pass
class GoatCheese:
    pass

    
# Shared
class SlicedPepperoni:
    pass
class Garlic:
    pass
class Onion:
    pass
class Mushroom:
    pass
class RedPepper:
    pass
    
######################################
# Pizza
######################################
class Pizza(LogObject):
    """
    name
    dough
    sauce
    toppings = []
    """
    
    def prepare(self):
        pass
    def bake(self):
        pass
    def cut(self):
        pass
    def box(self):
        pass
    def getName(self):
        return name
 

# Configure Log
class AppLog:
    class __AppLog:
        def __init__(self):
            self.log = logging.getLogger(__name__)
            h = logging.StreamHandler(sys.stdout)
            f = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
            h.setFormatter(f)
            self.log.setLevel(logging.DEBUG)
            self.log.addHandler(h)

    instance = None

    def __init__(self):
        if not AppLog.instance:
            AppLog.instance = self.__AppLog()


    def __getattr__(self, attr):
        return getattr(self.instance, attr)


# Define tests
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = AppLog().log

    def test_not_using_factory(self):
        from random import sample
        duck_type = ('picnic', 'hunting', 'bathtub')
        d = sample(duck_type, 1)

        duck = None
        if d == ['picnic']:
            duck = MallardDuck()
        elif d == ['hunting']:
            duck = DecoyDuck()
        elif d == ['bathtub']:
            duck = RubberDuck()
        self.log.debug(d)
        self.log.debug(type(duck))

    def test_simple_factory(self):
        s = SimplePizzaFactory()
        pizza = s.create_pizza('cheese')
        self.log.debug(type(pizza))

    def test_case_02(self):
        pass

# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))