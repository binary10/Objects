import unittest
import logging
import sys

class Behavior:
    def __init__(self):
        self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))

# Fly
class FlyBehavior(Behavior):
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        self.log.debug('Flap flap flap!')

class FlyNoWay(FlyBehavior):
    def fly(self):
        self.log.debug('Tumble!')


# Quacks
class QuackBehavior(Behavior):
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        self.log.debug('Quack quack!')

class Squeak(QuackBehavior):
    def quack(self):
        self.log.debug('Squeak squeak!')

class MuteQuack(QuackBehavior):
    def quack(self):
        self.log.debug('Qua qua!')

class Gobble(QuackBehavior):
    def quack(self):
        self.log.debug('Gobble gobble!')

class Bird:
    def __init__(self):
        self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))


class Duck(Bird):
    def __init__(self):
        super().__init__()
        self.fly = FlyWithWings()
        self.quack = Quack()

    def performFly(self):
        self.fly.fly()

    def performQuack(self):
        self.quack.quack()


class RubberDuck(Bird):
    def __init__(self):
        super().__init__()
        self.fly = FlyNoWay()
        self.quack = Squeak()

    def performFly(self):
        self.fly.fly()

    def performQuack(self):
        self.quack.quack()


class MallardDuck(Bird):
    def __init__(self):
        super().__init__()
        self.fly = FlyNoWay()
        self.quack = Quack()

    def performFly(self):
        self.fly.fly()

    def performQuack(self):
        self.quack.quack()


class Turkey(Bird):
    def __init__(self):
        super().__init__()
        self.fly = FlyNoWay()
        self.quack = Gobble()

    def performFly(self):
        self.fly.fly()

    def performQuack(self):
        self.quack.quack()


class Penguin(Bird):
    def __init__(self):
        super().__init__()
        self.fly = FlyNoWay()
        self.quack = MuteQuack()

    def performFly(self):
        self.fly.fly()

    def performQuack(self):
        self.quack.quack()

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
        if not hasattr(cls, 'log'):
            cls.log = AppLog().log

    def test_case_01(self):
      p = Penguin()
      p.performQuack()
      p.performFly()

    def test_case_02(self):
      pass


# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))
