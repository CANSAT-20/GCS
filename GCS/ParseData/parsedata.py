import traceback
import sys
from decimal import Decimal

class Parse:
    def __init__(self):
        self.model = 0

    def get_altitude(self, data):
        x = data.split(",")
        a = Decimal(x[3])
        return a

    def get_gps_latitude(self, data):
        x = data.split(",")
        a = Decimal(x[8])
        return a

    def get_gps_longitude(self, data):
        x = data.split(",")
        a = Decimal(x[9])
        return a

    def get_gps_altitude(self, data):
        x = data.split(",")
        a = Decimal(x[10])
        return a
