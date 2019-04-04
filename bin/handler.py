from commands.movecommand import MoveCommand
from commands.testcommand import TestCommand
from configreader import ConfigReader

class Handler:
    def __init__(self):
        self.__map = {
            "move" : self.__createMoveCommand,
            "test" : self.__createTestCommand
        }

    def handle(self, commandRequest):
        commandName = commandRequest["command"]
        commandParameters = commandRequest["parameter"]

        factoryMethod = self.__map[commandName]
        command = factoryMethod(commandParameters)

        command.execute()


    def __createMoveCommand(self, parameterMap):
        direction = parameterMap["direction"]
        moveCommand = MoveCommand(direction)
        return moveCommand

    def __createTestCommand(self, parameterMap):
        message = parameterMap["message"]
        testCommand = TestCommand(message)
        return testCommand