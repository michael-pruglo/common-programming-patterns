#!/usr/bin/env python3

from abc import ABC, abstractmethod

user_role = "average Joe"

class State(ABC):
    def __init__(self, document) -> None:
        self.document = document
    @abstractmethod
    def render(self): pass
    @abstractmethod
    def publish(self): pass

class Draft(State):
    def render(self):
        if user_role=="author" or user_role=="admin":
            print(self.document.text)
        else:
            print(f"error trying to render draft: access denied")
    def publish(self):
        if user_role=="author":
            self.document.change_state(Moderation(self.document))
            print("draft moved to moderation")
        elif user_role=="admin":
            self.document.change_state(Published(self.document))
            print("draft published by an admin")
        else:
            print("not enough privileges to publish the draft")

class Moderation(State):
    def render(self):
        print(f"note: this is a pre-published version: {self.document.text}")
    def publish(self):
        if user_role=="admin":
            self.document.change_state(Published(self.document))
            print("moderation passed, publishing")
        else:
            print("not enough priviledges to publish moderated content")

class Published(State):
    def render(self):
        print(self.document.text)
    def publish(self):
        pass

class Document:
    def __init__(self):
        self.change_state(Draft(self))
        self.text = "Lorem ipsum"
    def render(self):
        self.state.render()
    def publish(self):
        self.state.publish()
    def change_state(self, state):
        self.state = state


if __name__ == "__main__":
    article = Document()
    article.render()
    article.publish()
    user_role = "author"
    article.render()
    article.publish()
    article.publish()
    user_role = "admin"
    article.publish()
    article.render()
