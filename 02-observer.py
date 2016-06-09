""" Observer
Loose coupling is powerful. Strive for loosely coupled objects that interact.
Many changes can take place with no adverse consequences.
* The only thing a subject knows is about a shared interface
* Observers can be added at any time during runtime
* New types of observers can be added without changes to the subject
"""

class LogObject:
    def __init__(self):
        self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))


# Concrete Subject
class WeatherData(LogObject):
    def __init__(self):
        self.observers      = []
        self.temperature    = None
        self.humidity       = None
        self.pressure       = None

    def register_observer(self, observer):
        self.observers.append(observer)
        
    def remove_observer(self, observer):
        self.observers.pop(self.observers.index(observer))
        
    def notify_observers(self):
        for observer in self.observers:
            observer.update([self.get_temperature(), self.get_humidity(), self.get_pressure()])
    
    def measurements_changed(self):
        self.notify_observers()
            
    def get_temperature(self):  return self.temperature
    def get_humidity(self):     return self.humidity
    def get_pressure(self):     return self.pressure

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature    = temperature
        self.humidity       = humidity   
        self.pressure       = pressure   
        self.measurements_changed()

        

# Observers
# Implements: Observer - update(), DisplayElement - display()
class CurrentConditionsDisplay(LogObject):
    def update(self, event_args):   self.log.debug(' '.join([str(v) for v in event_args]))
    def display(self):                            pass

class StatisticsDisplay(LogObject):
    def update(self, event_args):   self.log.debug(' '.join([str(v) for v in event_args]))
    def display(self):                            pass

class ThirdPartyDisplay(LogObject):
    def update(self, event_args):   self.log.debug(' '.join([str(v) for v in event_args]))
    def display(self):                            pass

class ForecastDisplay(LogObject):
    def update(self, event_args):   self.log.debug(' '.join([str(v) for v in event_args]))
    def display(self):                            pass



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
      w = WeatherData()
      w.register_observer(CurrentConditionsDisplay())
      w.register_observer(StatisticsDisplay())
      w.register_observer(ThirdPartyDisplay())
      w.register_observer(ForecastDisplay())
      w.notify_observers()
      
    def test_case_02(self):
      pass


# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))
