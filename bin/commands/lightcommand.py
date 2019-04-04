from gpiozero import LED, PWMLED
from configreader import ConfigReader
import signal

class LightCommand:
    instance = None
    
    def __init__(self, mode):
        if not LightCommand.instance:
            LightCommand.instance = LightCommand.__LightCommand(mode)
        else:
            LightCommand.instance.mode = mode
    
    def execute(self):
        LightCommand.instance.mode[LightCommand.instance.mode]()

    class __LightCommand:
        def __init__(self, mode):
            config = ConfigReader()

            self.__light1 = LED(int(config.light1))
            self.__light2 = LED(int(config.light2))

            self.mode = mode
            self.directions = {
                "off": self.__lightsOff,
                "backward": self.__lightsBlink,
                "alternate": self.__lightsAlternate
            }

        def __lightsOff(self):
            self.__light1.off()
            self.__light2.off()

        def __lightsBlink(self):
            pass
            
        def __lightsAlternate(self):
            pass

        