#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Editor:
    text = ""
    backup = ""
    def get_selection(self):
        return self.text[:len(self.text)//2]
    def delete_selection(self):
        self.text = self.text[len(self.text)//2:]

class Application:
    clipboard = ""
    history = []
    def exec_command(self, command):
        if command.execute():
            self.history.append(command)


class Command(ABC):
    def __init__(self, app:Application, editor:Editor):
        self.app = app
        self.editor = editor
        self.backup = None

    @abstractmethod
    def execute(self):
        pass


class CopyCommand(Command):
    def execute(self):
        self.app.clipboard = self.editor.get_selection()
        return False

class CutCommand(Command):
    def execute(self):
        self.editor.backup = self.editor.text
        self.app.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True

class UndoCommand(Command):
    def execute(self):
        if self.editor.backup:
            self.editor.text = self.editor.backup
        return True


if __name__ == "__main__":
    app = Application()
    editor = Editor()
    editor.text = "a quick brown fox jumped over the lazy dog"

    def print_debug():
        print(f'editor: "{editor.text}"')
        print(f'clipboard: "{app.clipboard}"')
        print(f'command history: {app.history}')
        print()

    app.exec_command(CopyCommand(app, editor))
    print_debug()
    app.exec_command(CutCommand(app, editor))
    print_debug()
    app.exec_command(UndoCommand(app, editor))
    print_debug()
