""" Adapter

If it walks like a duck and quacks like a duck...
then it might be a Turkey wrapped with a Duck adapter.
"""
import unittest
import logging
import sys

class LogObject:
    def __init__(self):
        self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))


class Duck(LogObject):
    def quack(self):
        pass
    def fly(self):
        pass

class MallardDuck(Duck):
    def quack(self):
        self.log.debug('Quack')
    def fly(self):
        self.log.debug('I\'m flying')

class Turkey(LogObject):
    def gobble(self):
        pass
    def fly(self):
        pass

    class WildTurkey(LogObject):
        def gobble(self):
            self.log.debug('Gobble gobble')
        def fly(self):
            self.log.debug('I\'m flying a short distance')


class TurkeyAdapter(LogObject):
    """ Convert a Turkey to a Duck """
    def __init__(self, turkey):
        super().__init__()
        self.turkey = turkey
    def quack(self):
        self.turkey.gobble()
    def fly(self):
        for i in range(5): self.turkey.fly()

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
      turkey = WildTurkey()
      turk = TurkeyAdapter(turkey)
      turk.quack()
      turk.fly()

    def test_case_02(self):
        pass


# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))

