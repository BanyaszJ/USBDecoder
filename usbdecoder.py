from random import randint as randint
from time import sleep as sleep

class UsbDataCreator():
    def __init__(self):
        pass

    def stream(self):
        self.sleep(1000)
        return self.create_bit_pairs()

    def create_bit_pairs(self):
        return [self.generate_dplus_bit(), self.generate_dminus_bit()]
        
    def generate_dplus_bit(self):
        return randint(0, 1)
        
    def generate_dminus_bit(self):
        return randint(0, 1)
        
    def sleep(self, time):
        sleep(time/1000) # in miliseconds
        
class UsbDataContainer():
    def __init__(self):
        self.data_list = [2]*40
        
    def get_usb_data(self):
        return self.data_list
        
    def add_item(self, data):
        self.data_list.insert(0, data)
        
    def remove_item(self):
        self.data_list.pop()
'''------------------------------------------------------------------------------------------------------------------------------------------'''

usb = UsbDataCreator()
usb_data = UsbDataContainer()


while True:
    # print(usb.stream())
    
    usb_data.add_item(usb.stream())
    print(usb_data.get_usb_data())
    
    