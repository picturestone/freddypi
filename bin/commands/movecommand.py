from gpiozero import Robot
from configreader import ConfigReader
import signal

class MoveCommand:
    instance = None
    
    def __init__(self, direction):
        if not MoveCommand.instance:
            instance = MoveCommand.__MoveCommand(direction)
            self.__execute()
        else:
            instance.__direction = direction
    
    def __execute(self):
        self.instance.__directions[self.instance.__direction]()

    class __MoveCommand:
        def __init__(self, direction):
            config = ConfigReader()
            self.__robot = Robot(
                left=(int(config.leftMotorForwardPin),int(config.leftMotorBackwardPin)), 
                right=(int(config.rightMotorForwardPin),int(config.rightMotorBackwardPin))
                )
            self.speed = 1
            self.direction = direction
            self.__directions = {
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

    
    