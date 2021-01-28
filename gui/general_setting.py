from tkinter import LabelFrame, IntVar, DoubleVar, StringVar, Label, Entry, Button, RAISED, SUNKEN
from typing import List


LOG_SOURCE: str = "GUI_SETTINGS"


class SettingField:
    def __init__(self, root: LabelFrame, name: str, variable_value: any = 0, variable_type: str = "string",
                 row: int = 0, column: int = 0):
        self.name: str = name
        self.variable_type: str = variable_type
        if variable_type is "int":
            self.old_variable: IntVar = IntVar(value=int(variable_value))
            self.variable: IntVar = IntVar(value=int(variable_value))
        elif variable_type is "float":
            self.old_variable: DoubleVar = DoubleVar(value=float(variable_value))
            self.variable: DoubleVar = DoubleVar(value=float(variable_value))
        else:
            self.old_variable: StringVar = StringVar(value=str(variable_value))
            self.variable: StringVar = StringVar(value=str(variable_value))
        self.label: Label = Label(root, text=name)
        self.label.grid(row=row, column=column)
        self.variable_field: Label = Label(root, textvariable=self.variable)
        self.variable_field.grid(row=row, column=column + 1)

    def set(self, value: any):
        if self.variable_type is "int":
            self.old_variable.set(int(value))
            self.variable.set(int(value))
        elif self.variable_type is "float":
            self.old_variable.set(float(value))
            self.variable.set(float(value))
        else:
            self.old_variable.set(str(value))
            self.variable.set(str(value))

    def get(self) -> any:
        try:
            if self.variable_type is "int":
                return int(self.variable.get())
            elif self.variable_type is "float":
                return float(self.variable.get())
            else:
                return str(self.variable.get())
        except ValueError:
            self.variable.set(self.old_variable.get())
            print("[%s] wrong value entered.. using old one." % LOG_SOURCE)
            if self.variable_type is "int":
                return int(self.variable.get())
            elif self.variable_type is "float":
                return float(self.variable.get())
            else:
                return str(self.variable.get())


class SettingEntry:
    def __init__(self, root: LabelFrame, name: str, variable_value: any = 0, variable_type: str = "string",
                 row: int = 0, column: int = 0):
        self.name: str = name
        self.variable_type: str = variable_type
        self.old_variable: StringVar = StringVar(value=str(variable_value))
        self.variable: StringVar = StringVar(value=str(variable_value))
        self.label: Label = Label(root, text=name)
        self.label.grid(row=row, column=column)
        self.variable_entry: Entry = Entry(root, width=5, textvariable=self.variable)
        self.variable_entry.grid(row=row, column=column + 1)

    def set(self, value: any):
        if self.variable_type is "int":
            self.old_variable.set(int(value))
            self.variable.set(int(value))
        elif self.variable_type is "float":
            self.old_variable.set(float(value))
            self.variable.set(float(value))
        else:
            self.old_variable.set(str(value))
            self.variable.set(str(value))

    def get(self) -> any:
        try:
            if self.variable_type is "int":
                return int(self.variable.get())
            elif self.variable_type is "float":
                return float(self.variable.get())
            else:
                return str(self.variable.get())
        except ValueError:
            self.variable.set(self.old_variable.get())
            print("[%s] wrong value entered.. using old one." % LOG_SOURCE)
            if self.variable_type is "int":
                return int(self.variable.get())
            elif self.variable_type is "float":
                return float(self.variable.get())
            else:
                return str(self.variable.get())


class RadioButtons:
    def __init__(self, root: LabelFrame, names: List[str], shared_variable: IntVar, command, option: str,
                 sub_option: str, row: int = 0, column: int = 0, width: int = 15, height: int = 1):
        self.root: LabelFrame = root
        self.row: int = row
        self.column: int = column
        self.width: int = width
        self.height: int = height
        self.names: List[str] = names
        self.option: str = option
        self.sub_option: str = sub_option
        self.variable: IntVar = shared_variable
        self.command = command
        self.buttons: List[Button] = []
        self.set_buttons(names)
        self.press(0)

    def press(self, button_id: int):
        self.set(button_id)
        for i, button in enumerate(self.buttons):
            if i is not button_id:
                button.config(relief=RAISED)
            else:
                button.config(relief=SUNKEN)
        self.command(self.option, self.sub_option, self.variable.get())

    def set(self, value: any):
        self.variable.set(int(value))

    def get(self) -> any:
        return int(self.variable.get())

    def set_buttons(self, button_names: List[str]):
        if self.buttons:
            for button in self.buttons:
                button.destroy()

        self.buttons = []
        self.names = button_names
        for i, name in enumerate(self.names):
            def generate_press_function(current_index: int):
                def press_function():
                    self.press(current_index)

                return press_function

            new_button: Button = Button(self.root, text=name, width=self.width, height=self.height,
                                        command=generate_press_function(i))
            new_button.grid(row=self.row + i, column=self.column)
            self.buttons.append(new_button)