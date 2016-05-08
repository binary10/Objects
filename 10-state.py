# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:47:46 2015

Based on Head First Design Patterns book implementation in Java.

@author: dankow01
"""

class State:
    def __init__(self, gumballMachine):
        self.gumballMachine = None

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
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You can't insert another quarter")

    def ejectQuarter(self):
        print("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        print("You turned...")
        self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        pass

    def __str__(self):
       return "waiting for turn of crank"

# https://www.youtube.com/watch?v=CGzk2O9QhB8
class NoQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You inserted a quarter")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        print("You haven't inserted a quarter")

    def turnCrank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")

    def refill(self):
        pass

    def __str__(self):
        return "waiting for quarter"

class SoldOutState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def ejectQuarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def turnCrank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def __str__(self):
        return "sold out"


class SoldState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")

    def ejectQuarter(self):
        print("Sorry, you already turned the crank")

    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if (self.gumballMachine.getCount() > 0):
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumballs!")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

    def refill(self):
        pass

    def __str__(self):
        return "dispensing a gumball"


class GumballMachine:

    def __init__(self, numberGumballs):
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
       print("The gumball machine was just refilled; it's new count is: " + str(self.count))
       self.state.refill()

    def releaseBall(self):
        print("A gumball comes rolling out the slot...");
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
        s += "\nPython-enabled Standing Gumball Model #2004"
        s += "\nInventory: " + str(self.count) + " gumball"
        if (self.count != 1):
            s += "s"
        s += "\n"
        s += "Machine is " + str(self.state) + "\n"
        return s

# Test classes
class Test_Gumball():
	def run(self):
	    gumballMachine = GumballMachine(2)
	
	    print(gumballMachine)
	
	    gumballMachine.insertQuarter()
	    gumballMachine.turnCrank()
	
	    print(gumballMachine)
	
	    gumballMachine.insertQuarter()
	    gumballMachine.turnCrank()
	    gumballMachine.insertQuarter()
	    gumballMachine.turnCrank()
	
	    gumballMachine.refill(5)
	    gumballMachine.insertQuarter()
	    gumballMachine.turnCrank()
	
	    print(gumballMachine)
	   
Test_Gumball().run()
