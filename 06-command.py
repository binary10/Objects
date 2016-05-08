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
        c.execute()

        
class MeowCommand:
    def __init__(self):
        pass
    def execute(self):  
        print('Meow meow!')
        
class BarkCommand:
    def __init__(self):
        pass
    def execute(self):
        print('Bark bark!')

class NullCommand:
    def __init__(self):
        pass
    def execute(self):
        pass