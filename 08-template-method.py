"""
Created on Fri Jun 26 13:49:15 2015
Based on Head First Design Patterns book implementation in Java.
"""
import logging
import unittest 
import sys 

class CaffeineBeverage():
	def __init__(self):
		self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))
		
    # Template method
	def prepareRecipe(self):
		self.boilWater()
		self.brew()
		self.pourInCup()
		self.addCondiment()

	def boilWater(self):
		self.log.debug('Boiling water')
        
	def pourInCup(self):
		self.log.debug('Pouring in cup')
    
	def brew(self):
		pass
    
	def addCondiment(self):
		pass


class Coffee(CaffeineBeverage):
    def brew(self):
        self.log.debug('Putting grind in coffee pot')
        
    def addCondiment(self):
        self.log.debug('Adding milk and sugar')


class Tea(CaffeineBeverage):
    def brew(self):
        self.log.debug('Putting tea leaves in pot')
        
    def addCondiment(self):
        self.log.debug('Adding lemon and honey')

# Configure Log
class AppLog:
	def __init__(self):
		l = logging.getLogger(__name__)
		h = logging.StreamHandler(sys.stdout)
		f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		h.setFormatter(f)
		l.setLevel(logging.DEBUG)
		l.addHandler(h)

# Define tests
class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		self.log = AppLog()
		self.tea = Tea()
		self.coffee = Coffee()
	
	def test_templates(self):
        # Run
		self.tea.prepareRecipe()
		self.coffee.prepareRecipe()


# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))
