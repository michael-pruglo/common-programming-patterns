#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Listener(ABC):
    @abstractmethod
    def update(self, data): pass

class EventManager:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, listener):
        if event_type not in self.listeners.keys():
            self.listeners[event_type] = []
        if listener not in self.listeners[event_type]:
            self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        assert event_type in self.listeners.keys()
        self.listeners[event_type].remove(listener)

    def notify(self, event_type, data):
        assert event_type in self.listeners.keys()
        for listener in self.listeners[event_type]:
            listener.update(data)

class LoggingListener(Listener):
    def update(self, filename):
        print(f"log updates to {filename}")

class EmailAlertListener(Listener):
    def update(self, filename):
        print(f"email on update to {filename}")

class Editor:
    def __init__(self):
        self.events = EventManager()
        self.file = ""

    def open_file(self, path):
        print(f"open file {path}")
        self.file = path
        self.events.notify("open", path)

    def save_file(self):
        print(f"saving file {self.file}")
        self.events.notify("save", self.file)


if __name__ == "__main__":
    editor = Editor()
    logger = LoggingListener()
    editor.events.subscribe("open", logger)
    email_alert = EmailAlertListener()
    editor.events.subscribe("save", email_alert)

    editor.open_file("input.txt")
    editor.save_file()
