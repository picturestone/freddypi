from commands.movecommand import MoveCommand

class Handler:
    def __init__(self):
        self.__map = {
            "move" : self.__createMoveCommand
        }

    def handle(self, commandRequest):
        commandName = commandRequest["command"]
        commandParameters = commandRequest["parameter"]

        factoryMethod = self.__map[commandName]
        command = factoryMethod(commandParameters)

        command.execute()

        print(command)


    def __createMoveCommand(self, parameterMap):
        direction = parameterMap["direction"]
        speed = parameterMap["speed"]
        moveCommand = MoveCommand(direction, speed)
        return moveCommand