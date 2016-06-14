""" Composite

Component

Leaf
Composite

"""
class LogObject:
    def __init__(self):
        self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))

class MenuComponent(LogObject):
    def get_name        (self):                     pass
    def get_description (self):                     pass
    def get_price       (self):                     pass
    def is_vegetarian   (self):                     pass
    def print           (self):                     pass
    def add             (self, menu_component):     pass
    def remove          (self, menu_component):     pass
    def get_child       (self, index):              pass


class MenuItem(MenuComponent):
    def __init__(self, name, description, is_vegetarian, price):
        super().__init__()
        self.name           = name
        self.description    = description
        self.is_vegetarian  = is_vegetarian
        self.price          = price

    def get_name        (self):     return self.name
    def get_description (self):     return self.description
    def get_price       (self):     return self.price
    def get_vegetarian  (self):     return self.is_vegetarian
    def print           (self):            
        self.log.debug(self.get_name())
        if self.get_vegetarian(): self.log.debug('VEG')
        self.log.debug(self.get_price())
        self.log.debug(self.get_description())
        


class Menu(MenuComponent):
    def __init__(self, name, description):
        super().__init__()
        self.menu_components = []
        self.name           = name
        self.description    = description
    
    def get_name        (self):     return self.name
    def get_description (self):     return self.description
    
    def add             (self, menu_component):
        self.menu_components.append(menu_component)
        
    def remove          (self, menu_component):
        i = self.menu_components.index(menu_component)
        self.menu_components.pop(i)
        
    def get_child       (self, index):
        i = self.menu_components.index(menu_component)
        return self.menu_component[i]

    def print           (self):
        self.log.debug(self.get_name())
        self.log.debug(self.get_description())
        self.log.debug('----------------------------------------')
        for item in self.menu_components:
            item.print()

            

class Waitress(LogObject):
    def __init__(self, menus):
        self.menus = menus
        
    def print_menu(self):
        self.menus.print()
            
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
        mi = MenuItem('Test', 'This is a test', True, 23.00)
        m = Menu('Test', 'This is a test')
        m.add(mi)
        mi.print()
        m.print()
            
    def test_case_02(self): pass




# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))
