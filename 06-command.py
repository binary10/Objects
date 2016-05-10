import unittest 
import sys

class RemoteControl:
    def __init__(self):
        self.stack = []
        self.command = None
    def setCommand(self, command):
        self.command = command
    def executeCommand(self):
        self.command.execute()
        self.stack.append(self.command)
    def undoCommand(self):
        c = self.stack.pop()
        c.undo()

        
class MeowCommand:
    def __init__(self):
        pass
    def execute(self):  
        print('Meow meow!')
    def undo(self):  
        print('Woem woem!')
        
class BarkCommand:
    def __init__(self):
        pass
    def execute(self):
        print('Bark bark!')
    def undo(self):  
        print('Krab krab!')

class NullCommand:
    def __init__(self):
        pass
    def execute(self):
        pass
    def undo(self):  
        pass

class Test(unittest.TestCase):
	def setUp(self):
		self.r = RemoteControl()
		self.meow = MeowCommand()
		self.bark = BarkCommand()
		self.n	 = NullCommand()
	
	def test_commands(self):
		# Run
		self.r.setCommand(self.meow)
		self.r.executeCommand()
		self.r.setCommand(self.bark)
		self.r.executeCommand()
		self.r.setCommand(self.n)
		self.r.executeCommand()
		self.r.undoCommand()
		self.r.undoCommand()
		self.r.undoCommand()


runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))
