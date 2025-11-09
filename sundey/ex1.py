from abc import ABC ,abstractmethod
class Engine:
    def __init__(self,fuel_type:str,horsepower :int):
        self.fuel_type=fuel_type
        self.horsepower=horsepower

class Vehicle(ABC):
    def __init__(self,license_plate:str,year:str):
        self.__license_plate=license_plate  
        self.__year=year
    
    def get_year(self):
        return self.__year
    
    def get_license_plate(self):
        return self.__license_plate
    
    def set_year(self,new_year):
        self.__year=new_year

    def set_license_plate(self,license_plate):
        self.__license_plate=license_plate

    @abstractmethod
    def calculate_annual_tax (self):
        pass






