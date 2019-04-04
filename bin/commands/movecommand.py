from gpiozero import Robot
from configreader import ConfigReader
import signal

class MoveCommand:
    instance = None
    
    def __init__(self, direction):
        if not MoveCommand.instance:
            self.instance = MoveCommand.__MoveCommand(direction)
        else:
            self.instance.direction = direction
    
    def execute(self):
        self.instance.directions[self.instance.direction]()

    class __MoveCommand:
        def __init__(self, direction):
            config = ConfigReader()
            self.__robot = Robot(
                left=(int(config.leftMotorForwardPin),int(config.leftMotorBackwardPin)), 
                right=(int(config.rightMotorForwardPin),int(config.rightMotorBackwardPin))
                )
            self.speed = 1
            self.direction = direction
            self.directions = {
                "forward": self.__moveForward,
                "backward": self.__moveBackward,
                "left": self.__moveLeft,
                "right": self.__moveRight,
                "stop": self.__stop
            }

        def __moveForward(self):
            self.__robot.forward(speed=self.speed)

        def __moveBackward(self):
            self.__robot.backward(speed=self.speed)

        def __moveLeft(self):
            self.__robot.left(speed=self.speed)

        def __moveRight(self):
            self.__robot.right(speed=self.speed)
        
        def __stop(self):
            self.__robot.stop()

    
    