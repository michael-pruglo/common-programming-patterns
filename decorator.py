#!/usr/bin/env python3


class Notifier:
    def send(self, message):
        print(message)

class BaseDecorator(Notifier):
    def __init__(self, notifier):
        super().__init__()
        self.wrappee = notifier
    def send(self, message):
        self.wrappee.send(message)

class SMSDecorator(BaseDecorator):
    def send(self, message):
        super().send(message)
        print(f"sending SMS '{message}'")
class FacebookDecorator(BaseDecorator):
    def send(self, message):
        super().send(message)
        print(f"sending Facebook msg '{message}'")
class SlackDecorator(BaseDecorator):
    def send(self, message):
        super().send(message)
        print(f"sending Slack msg '{message}'")

class Application:
    def __init__(self):
        self.notifier = None
    def set_notifier(self, notifier):
        self.notifier = notifier
    def on_important_news(self):
        assert self.notifier
        self.notifier.send("CEO organizes a meeting at 11am")


if __name__ == "__main__":
    app = Application()
    facebook_enabled = True
    sms_enabled = True

    stack = Notifier()
    if facebook_enabled:
        stack = FacebookDecorator(stack)
    if sms_enabled:
        stack = SMSDecorator(stack)

    app.set_notifier(stack)
    app.on_important_news()
