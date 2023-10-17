#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_on(self): pass
    @abstractmethod
    def turn_on(self): pass
    @abstractmethod
    def turn_off(self): pass
    @abstractmethod
    def get_volume(self): pass
    @abstractmethod
    def set_volume(self, val): pass
    @abstractmethod
    def get_channel(self): pass
    @abstractmethod
    def set_channel(self, val): pass

class Tv(Device):
    def is_on(self): pass
    def turn_on(self): print("turning tv on")
    def turn_off(self): pass
    def get_volume(self): pass
    def set_volume(self, val): pass
    def get_channel(self): pass
    def set_channel(self, val): pass

class Radio(Device):
    def is_on(self): pass
    def turn_on(self): pass
    def turn_off(self): pass
    def get_volume(self): pass
    def set_volume(self, val): print(f"setting radio volume to {val}")
    def get_channel(self): pass
    def set_channel(self, val): pass


class RemoteControl:
    def __init__(self, device:Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_on():
            self.device.turn_off()
        else:
            self.device.turn_on()
    def volume_up(self):
        self.device.set_volume(self.device.get_volume()+10)
    def volume_down(self):
        self.device.set_volume(self.device.get_volume()-10)
    def channel_up(self):
        self.device.set_channel(self.device.get_channel()+1)
    def channel_down(self):
        self.device.set_channel(self.device.get_channel()-1)

class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)


if __name__ == "__main__":
    tv = Tv()
    tv_remote = RemoteControl(tv)
    tv_remote.toggle_power()

    radio = Radio()
    radio_remote = AdvancedRemoteControl(radio)
    radio_remote.mute()
