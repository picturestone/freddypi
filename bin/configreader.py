import configparser

class ConfigReader:
    instance = None
    def __init__(self):
        if not ConfigReader.instance: 
            instance = ConfigReader.__ConfigReader()
            self.leftMotorForwardPin = instance.leftMotorForwardPin
            self.leftMotorBackwardPin = instance.leftMotorBackwardPin
            self.leftMotorEnablePin = instance.leftMotorEnablePin
            self.rightMotorForwardPin = instance.rightMotorForwardPin
            self.rightMotorBackwardPin = instance.rightMotorBackwardPin
            self.rightMotorEnablePin = instance.rightMotorEnablePin
            self.ip = instance.ip
            self.port = instance.port

    class __ConfigReader: 

        def __init__(self):
            config = configparser.ConfigParser()
            config.read('config.ini')
            
            self.leftMotorForwardPin = config['MotorLeft']['forward']
            self.leftMotorBackwardPin = config['MotorLeft']['backward']
            self.leftMotorEnablePin = config['MotorLeft']['enable']
            self.rightMotorForwardPin = config['MotorRight']['forward']
            self.rightMotorBackwardPin = config['MotorRight']['backward']
            self.rightMotorEnablePin = config['MotorRight']['enable']
            self.ip = config['server']['ip']
            self.port = config['server']['port']

    

    



