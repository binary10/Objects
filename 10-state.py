"""
Created on Sun Jun 28 19:47:46 2015
Based on Head First Design Patterns book implementation in Java.
"""
import logging
import unittest 
import sys 

class State:
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
        self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))


    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
       pass

    def dispense(self):
       pass

    def refill(self):
        pass

    def toString(self):
        pass


class HasQuarterState(State):
    def insertQuarter(self):
        self.log.debug("You can't insert another quarter")

    def ejectQuarter(self):
        self.log.debug("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        self.log.debug("You turned...")
        self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        self.log.debug("No gumball dispensed")

    def refill(self):
        pass

    def __str__(self):
       return "waiting for turn of crank"


class NoQuarterState(State):
    def insertQuarter(self):
        self.log.debug("You inserted a quarter")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        self.log.debug("You haven't inserted a quarter")

    def turnCrank(self):
        self.log.debug("You turned, but there's no quarter")

    def dispense(self):
        self.log.debug("You need to pay first")

    def refill(self):
        pass

    def __str__(self):
        return "waiting for quarter"


class SoldOutState(State):
    def insertQuarter(self):
        self.log.debug("You can't insert a quarter, the machine is sold out")

    def ejectQuarter(self):
        self.log.debug("You can't eject, you haven't inserted a quarter yet")

    def turnCrank(self):
        self.log.debug("You turned, but there are no gumballs")

    def dispense(self):
        self.log.debug("No gumball dispensed")

    def refill(self):
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def __str__(self):
        return "sold out"


class SoldState(State):
    def insertQuarter(self):
        self.log.debug("Please wait, we're already giving you a gumball")

    def ejectQuarter(self):
        self.log.debug("Sorry, you already turned the crank")

    def turnCrank(self):
        self.log.debug("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if (self.gumballMachine.getCount() > 0):
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            self.log.debug("Oops, out of gumballs!")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

    def refill(self):
        pass

    def __str__(self):
        return "dispensing a gumball"


class GumballMachine:

    def __init__(self, numberGumballs):
        self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))
        self.count = numberGumballs
	

        self.soldOutState       = SoldOutState(self)
        self.noQuarterState     = NoQuarterState(self)
        self.hasQuarterState    = HasQuarterState(self)
        self.soldState          = SoldState(self)

        if (numberGumballs > 0):
            self.state = self.noQuarterState
        else:
             self.state = self.soldOutState

    # All operations that are delegated to the States
    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()

    def refill(self, count):
       self.count += count
       self.log.debug("The gumball machine was just refilled; it's new count is: " + str(self.count))
       self.state.refill()

    def releaseBall(self):
        self.log.debug("A gumball comes rolling out the slot...");
        if (self.count != 0):
            self.count = self.count - 1

    # Setter. Not necessary, but helpful if setting requires complex steps.
    def setState(self, state):
       self.state = state

    # Internal states/properties. Not necessary, but good practice if steps are complex.
    def getCount(self):
        return self.count

    def getState(self):
        return self.state

    def getSoldOutState(self):
        return self.soldOutState;


    def getNoQuarterState(self):
        return self.noQuarterState

    def getHasQuarterState(self):
        return self.hasQuarterState

    def getSoldState(self):
        return self.soldState

    # Magic Methods
    def __str__(self):
        s = "\nMighty Gumball, Inc."
        s += "\nJava-enabled Standing Gumball Model #2004"
        s += "\nInventory: " + str(self.count) + " gumball"
        if (self.count != 1):
            s += "s"
        s += "\n"
        s += "Machine is " + str(self.state) + "\n"
        return s

# Configure Log
class AppLog:
	def __init__(self):
		self.log = logging.getLogger(__name__)
		h = logging.StreamHandler(sys.stdout)
		f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		h.setFormatter(f)
		self.log.setLevel(logging.DEBUG)
		self.log.addHandler(h)

# Define tests
class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		self.log = AppLog().log
		self.gumballMachine = GumballMachine(2)

	def test_gumball_machine(self):
		self.log.debug(self.gumballMachine)
	
	def test_basic_purchase(self):
		self.gumballMachine.insertQuarter()
		self.gumballMachine.turnCrank()
		self.gumballMachine.insertQuarter()
		self.gumballMachine.turnCrank()
		self.log.debug(self.gumballMachine)

	def test_refill(self):
		self.gumballMachine.refill(5)
		self.gumballMachine.insertQuarter()
		self.gumballMachine.turnCrank()
		self.log.debug(self.gumballMachine)		

# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))

