class Null:
    """ 
    Null objects always and reliably "do nothing." 
    https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch05s24.html
    """

    def __init__(self, *args, **kwargs): pass
    def __call__(self, *args, **kwargs): return self
    def __repr__(self): return "Null(  )"
    def __nonzero__(self): return 0

    def __getattr__(self, name): return self
    def __setattr__(self, name, value): return self
    def __delattr__(self, name): return self

    

"""
def compute(x, y):
    try: "lots of computation here to return some appropriate object"
    except SomeError: return Null(  )

for x in xs:
    for y in ys:
        compute(x, y).somemethod(y, x)
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
