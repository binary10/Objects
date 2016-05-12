import logging
import unittest 
import sys

# Create main widget
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

# Define commands
class Command:
	def __init__(self):
		self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))

class MeowCommand(Command):
    def execute(self):  
        self.log.debug('Meow meow!')
    def undo(self):  
        self.log.debug('Woem woem!')
        
class BarkCommand(Command):
    def execute(self):
        self.log.debug('Bark bark!')
    def undo(self):  
        self.log.debug('Krab krab!')

class NullCommand(Command):
    def execute(self):
        pass
    def undo(self):  
        pass

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
		cls.log  = AppLog().log
		cls.r 	 = RemoteControl()
		cls.meow = MeowCommand()
		cls.bark = BarkCommand()
		cls.n	 = NullCommand()
	
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

# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))
