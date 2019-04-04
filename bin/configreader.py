import configparser

class ConfigReader:
    instance = None
    def __init__(self):
        if not ConfigReader.instance: 
            instance = ConfigReader.__ConfigReader()
            self.leftMotorForwardPin = instance.leftMotorForwardPin
            self.leftMotorBackwardPin = instance.leftMotorBackwardPin
            self.rightMotorForwardPin = instance.rightMotorForwardPin
            self.rightMotorBackwardPin = instance.rightMotorBackwardPin
            self.ip = instance.ip
            self.port = instance.port

    class __ConfigReader: 

        def __init__(self):
            config = configparser.ConfigParser()
            config.read('config.ini')
            
            self.leftMotorForwardPin = config['MotorLeft']['forward']
            self.leftMotorBackwardPin = config['MotorLeft']['backward']
            self.rightMotorForwardPin = config['MotorRight']['forward']
            self.rightMotorBackwardPin = config['MotorRight']['backward']
            self.ip = config['server']['ip']
            self.port = config['server']['port']

    

    



