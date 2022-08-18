# Drzwi, okna -> otwórz, zamknij
# Światło, -> włącz, wyłącz, natężenie
# Światło kolorowe -> włącz, wyłącz, natężenie, kolor(RGB)
# Czajnik, Kuchenka, Pralka, Zmywarka -> włącz, wyłącz, włącz za T czasu
# Telewizor, Radio -> włącz, wyłącz, ciszej, głośniej, kanał do przodu, kanał do tyłu, kanał X

# Każdy pokój ma mieć łatwą możliwość włączenia i wyłączenia wszystkich urządzeń w pokoju
# Ma istnieć możliwość zamknięcia domu (tzn. drzwi wejściowych i okien)
# Każde urządzenie ma unikalną nazwę (coś pokroju 0x2214AE32, można sobie wymyśleć)

import time


class Door:
    def __init__(self, door_name, type):
        self.name = door_name
        self.open = False
        self.type = type


class Window:
    def __init__(self, window_name):
        self.name = window_name
        self.open = False


class Lamp:
    def __init__(self, lamp_name):
        self.name = lamp_name
        self.on = False
        self.intensity = 0

    def change_intensity(self, intensity):
        if intensity >= 100:
            self.intensity = 100
        elif intensity <= 0:
            self.intensity = 0
        else:
            self.intensity = intensity
        return self
    
    def turn_on(self):
        self.on = True
        return self

    def turn_off(self):
        self.on = False
        return self


class LampRGB(Lamp):
    def __init__(self, lamp_name, intencity, on):
        super().__init__(lamp_name, intencity, on)
        self.color = (255, 255, 255)
    
    def change_intensity(self, intensity):
        return super().change_intensity(intensity)

    def change_color(self, R, G, B):
        self.color = (R, G, B)
        return self

    def turn_on(self):
        return super().turn_on()
    
    def turn_off(self):
        return super().turn_off()
        

class Device:
    def __init__(self, name, on = False):
        self.on = on
        self.name = name

    def turn_on(self):
        self.on = True
        return self

    def turn_off(self):
        self.on = False
        return self


class Device_AGD(Device):
    def __init__(self, name, on = False) -> None:
        super().__init__(name, on)

    def on_for_time(self, time_on):
        self.on()
        time.sleep(time_on * 60)
        self.off()
        return self

    def turn_on(self):
        return super().turn_on()
    
    def turn_off(self):
        return super().turn_off()


class Device_Entertaiment(Device):
    def __init__(self,name, on = False, volume = 50, channel = 1) -> None:
        super().__init__(name, on )
        self.volume = volume
        self.channel = channel
    
    def volume_up(self):
        self.volume += 1
        if self.volume >= 100:
            self.volume = 100
        return self

    def volume_down(self):
        self.volume -= 1
        if self.volume <= 0:
            self.volume = 0
        return self

    def change_volume(self, vol):
        if vol>= 100:
            self.volume = 100
        elif vol <= 0:
            self.volume = 0
        else:
            self.volume = vol
        return self

    def channel_up(self):
        self.channel += 1
        return self

    def channel_down(self):
        self.channel -= 1
        if self.channel <= 0:
            self.channel = 1
        return self

    def change_channel(self, x):
        self.channel = x
        if self.channel <= 0:
            self.channel = 1
        return self

    def turn_on(self):
        return super().turn_on()
    
    def turn_off(self):
        return super().turn_off()


class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.doors = []
        self.out_doors = []
        self.windows = []
        self.devices = []
        self.light = []
    
    def close(self):
        for door in self.out_doors:
            door.open = False
        for window in self.windows:
            window.open = False
        return self

    def open(self):
        for door in self.out_doors:
            door.open = True
        return self

    def turn_on(self):
        for device in self.devices:
            device.turn_on()
        for lamp in self.light:
            lamp.turn_on()
        for window in self.windows:
            window.open = True
        for door in self.out_doors:
            door.open = True
        for door in self.doors:
            door.open = True
        return self

    def turn_off(self):
        for device in self.devices:
            device.turn_off()
        for lamp in self.light:
            lamp.turn_off()
        for window in self.windows:
            window.open = False 
        for door in self.out_doors:
            door.open = False
        for door in self.doors:
            door.open = False
        return self

    def add_window(self, window):
        self.windows.append(window)
        return self

    def add_door(self, door):
        self.doors.append(door)
        return self
    
    def add_device(self, device):
        self.devices.append(device)       
        return self

    def add_lamp(self, lamp): 
        self.light.append(lamp)
        return self
    

class SmartHouse:
    def __init__(self):
        self.rooms = []

    def __str__(self):
        pass
        return f""

    def open(self):
        for room in self.rooms:
            room.open()
        return self

    def close(self):
        for room in self.rooms:
            room.close()
        return self

    def add_room(self, room):
        self.rooms.append(room)
        return self
     