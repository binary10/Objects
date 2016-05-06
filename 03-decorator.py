class Beverage():
		pass

class HouseBlend(Beverage):
	def __init__(self):
		pass
	
	def get_description(self):
		return 'I\'m a House Blend'
		
	def cost(self):
		print('House Blend: $2.75')
		return 2.75


class CondimentDecorator(Beverage):
	pass

class Milk(CondimentDecorator):
	def __init__(self,beverage):
		self.beverage = beverage

	def get_description(self):
		return self.beverage.get_description() + '\n' + 'I\'m Milk'
		
	def cost(self):
		print('Milk: $0.75')
		return self.beverage.cost() + 0.75
		
class Mocha(CondimentDecorator):
	def __init__(self,beverage):
		self.beverage = beverage
		self.description = 'I\'m Mocha\n'
	
	def get_description(self):
		return self.beverage.get_description() + '\n' + 'I\'m Mocha'

	def cost(self):
		print('Mocha: $0.80')
		return self.beverage.cost() + 0.80

class Test_Order():
	def run(self):
		bev = HouseBlend()
		bev = Milk(bev)
		bev = Mocha(bev)
		
		print(bev.cost())
		print(bev.get_description())
		
Test_Order().run()
