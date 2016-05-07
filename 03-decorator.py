import logging
import sys

class Beverage():
	def __init__(self):
		self.log = logging.getLogger(__name__)
		self.log.addHandler(logging.StreamHandler())
		self.log.setLevel(logging.INFO)


class HouseBlend(Beverage):
	def __init__(self):
		super().__init__()
	
	def get_description(self):
		return 'I\'m a House Blend'
		
	def cost(self):
		self.log.info('House Blend: $2.75')
		return 2.75


class CondimentDecorator(Beverage):
	def __init__(self):
		self.log = logging.getLogger(__name__)
		self.log.addHandler(logging.StreamHandler())
		self.log.setLevel(logging.INFO)


class Milk(CondimentDecorator):
	def __init__(self,beverage):
		super().__init__()
		self.beverage = beverage

	def get_description(self):
		return self.beverage.get_description() + '\n' + 'I\'m Milk'
		
	def cost(self):
		self.log.info('Milk: $0.75')
		return self.beverage.cost() + 0.75
		
class Mocha(CondimentDecorator):
	def __init__(self,beverage):
		super().__init__()
		self.beverage = beverage
		self.description = 'I\'m Mocha\n'
	
	def get_description(self):
		return self.beverage.get_description() + '\n' + 'I\'m Mocha'

	def cost(self):
		self.log.info('Mocha: $0.80')
		return self.beverage.cost() + 0.80

class Test_Order():
	
	def run(self):
		bev = HouseBlend()
		bev = Milk(bev)
		bev = Mocha(bev)
		
		print(bev.cost())
		print(bev.get_description())
		
#if __name__=='__main__':
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
Test_Order().run()
