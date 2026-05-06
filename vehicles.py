class Automobile:
    def __init__(self,make,modle,milage,price):
        self.__make = make 
        self.__modle = modle
        self.__milage = milage
        self.__price = price 

    def get_make(self):
        return self.__make
    
    def get_modle(self):
        return self.__modle
    
    def get_milage(self):
        return self.__milage
    
    def get_price(self):
        return self.__price
    
    def set_make(self,make):
        self.__make = make

    def set_modle(self,modle):
        self.__modle = modle
    
    def set_milage(self,milage):
        self.__milage = milage

    def set_price(self,price):
        self.__price = price

    