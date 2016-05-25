import unittest
import logging
import sys

class LogObject:
    def __init__(self):
        self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))


class MallardDuck(LogObject):
    def quack(self):
        self.log.info('Honk honk!')


class DecoyDuck(LogObject):
    def quack(self):
        self.log.info('Qua qua!')


class RubberDuck(LogObject):
    def quack(self):
        self.log.info('Squeak squeak!')


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

    def test_case_01(self):
        from random import sample
        duck_type = ('picnic', 'hunting', 'bathtub')
        d = sample(duck_type, 1)
        print(d)
        duck = None
        if d == 'picnic':
            duck = MallardDuck()
        elif d == 'hunting':
            duck = DecoyDuck()
        elif d == 'bathtub':
            duck = RubberDuck()
        print(type(duck))
        
    def test_case_02(self):
        pass


# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))