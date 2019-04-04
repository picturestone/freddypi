from gpiozero import LED, PWMLED
from configreader import ConfigReader
import signal

class MoveCommand:
    instance = None
    
    def __init__(self, direction, speed):
        if not MoveCommand.instance:
            MoveCommand.instance = MoveCommand.__MoveCommand(direction, speed / 100)
        else:
            MoveCommand.instance.direction = direction
            MoveCommand.instance.speed = speed /100
    
    def execute(self):
        MoveCommand.instance.directions[MoveCommand.instance.direction]()

    class __MoveCommand:
        def __init__(self, direction, speed):
            config = ConfigReader()

            self.__leftForward = LED(int(config.leftMotorForwardPin))
            self.__leftBackward = LED(int(config.leftMotorBackwardPin))
            self.__leftEnable = PWMLED(int(config.leftMotorEnablePin))

            self.__rightForward = LED(int(config.rightMotorForwardPin))
            self.__rightBackward = LED(int(config.rightMotorBackwardPin))
            self.__rightEnable = PWMLED(int(config.rightMotorEnablePin))

            self.speed = speed
            self.direction = direction
            self.directions = {
                "forward": self.__moveForward,
                "backward": self.__moveBackward,
                "left": self.__moveLeft,
                "right": self.__moveRight,
                "stop": self.__stop
            }

        def __moveForward(self):
            self.__setLeftForward()
            self.__setRightForward()

        def __moveBackward(self):
            self.__setLeftBackward()
            self.__setRightBackward()

        def __moveLeft(self):
            self.__robot.right(speed=self.speed)

        def __moveRight(self):
            self.__robot.left(speed=self.speed)
        
        def __stop(self):
            self.__robot.stop()

        def __setLeftForward(self):
            self.__leftForward.on()
            self.__leftBackward.off()
            self.__leftEnable.value = self.speed

        def __setLeftBackward(self):
            self.__leftForward.off()
            self.__leftBackward.on()
            self.__leftEnable.value = self.speed

        def __setRightForward(self):
            self.__rightForward.on()
            self.__rightBackward.off()
            self.__rightEnable.value = self.speed

        def __setRightBackward(self):
            self.__rightForward.off()
            self.__rightBackward.on()
            self.__rightEnable.value = self.speed


    
    