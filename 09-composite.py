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

    def test_case_02(self):
        pancakeHouseMenu =  Menu("PANCAKE HOUSE MENU", "Breakfast")
        dinerMenu =  Menu("DINER MENU", "Lunch")
        cafeMenu =  Menu("CAFE MENU", "Dinner")
        dessertMenu =  Menu("DESSERT MENU", "Dessert of course!")
        coffeeMenu =  Menu("COFFEE MENU", "Stuff to go with your afternoon coffee")

        allMenus = Menu("ALL MENUS", "All menus combined")

        allMenus.add(pancakeHouseMenu)
        allMenus.add(dinerMenu)
        allMenus.add(cafeMenu)

        pancakeHouseMenu.add(MenuItem("K&B's Pancake Breakfast","Pancakes with scrambled eggs, and toast",True,2.99))
        pancakeHouseMenu.add(MenuItem("Regular Pancake Breakfast","Pancakes with fried eggs, sausage",False,2.99))
        pancakeHouseMenu.add(MenuItem("Blueberry Pancakes","Pancakes made with fresh blueberries, and blueberry syrup",True,3.49))
        pancakeHouseMenu.add(MenuItem("Waffles","Waffles, with your choice of blueberries or strawberries",True,3.59))

        dinerMenu.add(MenuItem("Vegetarian BLT","(Fakin') Bacon with lettuce & tomato on whole wheat",True,2.99))
        dinerMenu.add(MenuItem("BLT","Bacon with lettuce & tomato on whole wheat",False,2.99))
        dinerMenu.add(MenuItem("Soup of the day","A bowl of the soup of the day, with a side of potato salad",False,3.29))
        dinerMenu.add(MenuItem("Hotdog","A hot dog, with saurkraut, relish, onions, topped with cheese",False,3.05))
        dinerMenu.add(MenuItem("Steamed Veggies and Brown Rice","Steamed vegetables over brown rice",True,3.99))

        dinerMenu.add(MenuItem("Pasta","Spaghetti with Marinara Sauce, and a slice of sourdough bread",True,3.89))

        dinerMenu.add(dessertMenu)

        dessertMenu.add(MenuItem("Apple Pie","Apple pie with a flakey crust, topped with vanilla icecream",True,1.59))

        dessertMenu.add(MenuItem("Cheesecake","Creamy New York cheesecake, with a chocolate graham crust",True,1.99))
        dessertMenu.add(MenuItem("Sorbet","A scoop of raspberry and a scoop of lime",True,1.89))

        cafeMenu.add(MenuItem("Veggie Burger and Air Fries","Veggie burger on a whole wheat bun, lettuce, tomato, and fries",True,3.99))
        cafeMenu.add(MenuItem("Soup of the day","A cup of the soup of the day, with a side salad",False,3.69))
        cafeMenu.add(MenuItem("Burrito","A large burrito, with whole pinto beans, salsa, guacamole",True,4.29))

        cafeMenu.add(coffeeMenu)

        coffeeMenu.add(MenuItem("Coffee Cake","Crumbly cake topped with cinnamon and walnuts",True,1.59))
        coffeeMenu.add(MenuItem("Bagel","Flavors include sesame, poppyseed, cinnamon raisin, pumpkin",False,0.69))
        coffeeMenu.add(MenuItem("Biscotti","Three almond or hazelnut biscotti cookies",True,0.89))

        waitress = Waitress(allMenus)

        waitress.print_menu()



# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))
