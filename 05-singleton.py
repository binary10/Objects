"""
AKA Highlander -- There can be only one
"""


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
	  pass
	
  def test_case_02(self):
	  pass


# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))
