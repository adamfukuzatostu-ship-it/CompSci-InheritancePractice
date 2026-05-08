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


class Car(Automobile):
    def __init__(self, make, modle, milage, price,doors):
        super().__init__(make, modle, milage, price)
        self.__doors = doors 

    def get_doors(self):
        return self.__doors

    def set_doors(self,doors):
        self.__doors = doors

class Trucks(Automobile):
    def __init__(self, make, modle, milage, price,drive_type):
        super().__init__(make, modle, milage, price)
        self.__drive_type = drive_type

    def get_drive_type(self):
        return self.__drive_type
    
    def set_drive_type(self,drive_type):
        self.__drive_type = drive_type

class SUV(Automobile):
    def __init__(self, make, modle, milage, price,passanger_capacity):
        super().__init__(make, modle, milage, price)
        self.__passanger_capacity = passanger_capacity

    def get_passanger_capacity(self):
        return self.__passanger_capacity
    
    def set_passanger_capacity(self,passanger_capacity):
        self.__passanger_capacity = passanger_capacity   