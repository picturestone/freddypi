from gpiozero import Robot
from bin.configreader import ConfigReader
import signal

class MoveCommand:
    instance = None
    
    def __init__(self, direction, speed):
        if not MoveCommand.instance:
            instance = MoveCommand.__MoveCommand(direction, speed)
            self.__execute()
        else:
            instance.__direction = direction
            instance.__speed = speed
    
    def __execute(self):
        self.instance.__directions[self.instance.__direction]()

    class __MoveCommand:
        def __init__(self, direction, speed):
            config = ConfigReader()
            self.__robot = Robot(
                left=(config.leftMotorForwardPin,config.leftMotorBackwardPin), 
                right=(config.rightMotorForwardPin,config.rightMotorBackwardPin)
                )
            self.direction = direction
            self.speed = speed/100
            self.__directions = {
                "forward": self.__moveForward,
                "backward": self.__moveBackward,
                "left": self.__moveLeft,
                "right": self.__moveRight
            }

        def __moveForward(self):
            self.__robot.forward(speed=self.speed)

        def __moveBackward(self):
            self.__robot.backward(speed=self.speed)

        def __moveLeft(self):
            self.__robot.left(speed=self.speed)

        def __moveRight(self):
            self.__robot.right(speed=self.speed)

    
    