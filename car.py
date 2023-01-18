from abc import ABC, abstractmethod
from serviceable import Serviceable

class Car(Serviceable,ABC):
    def __init__(self,engine, battery, last_service_date):
        # self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
