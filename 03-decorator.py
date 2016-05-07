import logging
import sys

# Create Beverages
class Beverage():
	def __init__(self):
		self.log = logging.getLogger(__name__ + ':' + type(self).__name__)
		self.log.addHandler(logging.StreamHandler())
		self.log.setLevel(logging.INFO)

class HouseBlend(Beverage):
	def __init__(self):
		super().__init__()
	
	def get_description(self):
		return 'I\'m a House Blend'
		
	def cost(self):
		self.log.info('$2.75')
		return 2.75


# Create Condiments
class CondimentDecorator(Beverage):
	def __init__(self):
		self.log = logging.getLogger(__name__ + ':' + type(self).__name__)
		self.log.addHandler(logging.StreamHandler())
		self.log.setLevel(logging.INFO)

class Milk(CondimentDecorator):
	def __init__(self,beverage):
		super().__init__()
		self.beverage = beverage

	def get_description(self):
		return self.beverage.get_description() + '\n' + 'I\'m Milk'
		
	def cost(self):
		self.log.info('$0.75')
		return self.beverage.cost() + 0.75
		
class Mocha(CondimentDecorator):
	def __init__(self,beverage):
		super().__init__()
		self.beverage = beverage
		self.description = 'I\'m Mocha\n'
	
	def get_description(self):
		return self.beverage.get_description() + '\n' + 'I\'m Mocha'

	def cost(self):
		self.log.info('$0.80')
		return self.beverage.cost() + 0.80


# Test Classes
class Test_Order():
	def run(self):
		# Build a new coffee order
		bev = HouseBlend()
		bev = Milk(bev)
		bev = Mocha(bev)
		
		# Log the cost
		logging.info(bev.cost())


#if __name__=='__main__':
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
Test_Order().run()
