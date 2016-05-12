import logging
import sys
import unittest

# Create Beverages
class Beverage():
	def __init__(self):
		self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))

class HouseBlend(Beverage):
	def __init__(self):
		super().__init__()		# Use logger set up in abstract base class
	
	def get_description(self):
		return 'I\'m a House Blend'
		
	def cost(self):
		self.log.info('$2.75')
		return 2.75


# Create Condiments
class CondimentDecorator(Beverage):
	def __init__(self,beverage):
		super().__init__()
		self.beverage = beverage


class Milk(CondimentDecorator):
	def get_description(self):
		return self.beverage.get_description() + '\n' + 'I\'m Milk'
		
	def cost(self):
		self.log.info('$0.75')
		return self.beverage.cost() + 0.75
		
class Mocha(CondimentDecorator):
	def get_description(self):
		return self.beverage.get_description() + '\n' + 'I\'m Mocha'

	def cost(self):
		self.log.info('$0.80')
		return self.beverage.cost() + 0.80


# Configure Log
class AppLog:
	def __init__(self):
		self.log = logging.getLogger(__name__)
		h = logging.StreamHandler(sys.stdout)
		f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		h.setFormatter(f)
		self.log.setLevel(logging.DEBUG)
		self.log.addHandler(h)


# Define tests
class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		self.log = AppLog().log
		
		# Build a new coffee order
		self.bev = HouseBlend()
		self.bev = Milk(self.bev)
		self.bev = Mocha(self.bev)
	
	def test_decorator(self):
		self.log.debug(self.bev.cost())
		self.log.debug(self.bev.get_description())

# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))
