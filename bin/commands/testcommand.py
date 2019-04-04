class TestCommand:
    instance = None
    
    def __init__(self, message):
        if not TestCommand.instance:
            TestCommand.instance = TestCommand.__TestCommand(message)
        else:
            TestCommand.instance.message = message
    
    def execute(self):
        for i in range(0,4):
            print(TestCommand.instance.message)
        

    class __TestCommand:
        def __init__(self, message):
            self.message = message

        def __talk(self):
            print(self.message)
