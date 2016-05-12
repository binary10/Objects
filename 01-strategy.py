class Duck:
    pass
    
class MallardDuck:
    pass

class Turkey:
    pass

class FlyBehavior:
    pass
    
class QuackBehavior:
    pass


# Configure Log
class AppLog:
	def __init__(self):
		self.log = logging.getLogger(__name__)
		h = logging.StreamHandler(sys.stdout)
		f = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
		h.setFormatter(f)
		self.log.setLevel(logging.DEBUG)
		self.log.addHandler(h)


# Define tests
class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.log = AppLog().log

	def test_case_01(self):
	  pass
	
  def test_case_02(self):
	  pass


# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))
