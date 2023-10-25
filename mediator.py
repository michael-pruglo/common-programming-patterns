#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event): pass

class Component(ABC):
    def __init__(self, dialog):
        self.dialog = dialog
    def show(self):
        print(f"displaying {self}")
    def hide(self):
        print(f"hiding {self}")

class Button(Component):
    def click(self):
        self.dialog.notify(self, "click")

class TextBox(Component):
    pass

class CheckBox(Component):
    checked = False
    def toggle(self):
        evnt = "uncheck" if self.checked else "check"
        self.checked = not self.checked
        self.dialog.notify(self, evnt)


class AuthDialog(Mediator):
    def __init__(self):
        self.title = ""
        self.login_not_reg_chkbx = CheckBox(self)
        self.login_username = TextBox(self)
        self.login_password = TextBox(self)
        self.reg_username = TextBox(self)
        self.reg_password = TextBox(self)
        self.reg_email = TextBox(self)
        self.ok_btn = Button(self)
        self.cancel_btn = Button(self)

    def notify(self, sender, event):
        if sender == self.login_not_reg_chkbx:
            if event == "check":
                self.title = "Log In"
                self.login_username.show()
                self.login_password.show()
                self.reg_username.hide()
                self.reg_password.hide()
                self.reg_email.hide()
            else:
                self.title = "Register"
                self.login_username.hide()
                self.login_password.hide()
                self.reg_username.show()
                self.reg_password.show()
                self.reg_email.show()
        elif sender == self.ok_btn and event == "click":
            print("checking credentials...")


if __name__ == "__main__":
    auth = AuthDialog()
    auth.login_not_reg_chkbx.toggle()
    auth.ok_btn.click()
