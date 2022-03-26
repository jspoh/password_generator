# simple password generator with UI
# also allows you to copy generated password to clipboard

import random
import sys
import PySimpleGUI as sg
import pyperclip

print("Initializing program..")

sg.theme('DarkTeal9')
size = (20, 1)
in_size = (15, 1)

alphabet = "abcdefghijklmnopqrstuvwxyz"
symbol = "`~!@#$%^&*()_+-=[]\{}|;':\",./<>?"


class Password(object):
    def __init__(self):
        self.password = ""
        self.l_pass = []
        self.s_pass = []
        self.n_pass = []
        self.letters = 0
        self.symbols = 0
        self.numbers = 0

    def info(self):
        self.letters = int(values['letters'])
        self.symbols = int(values['symbols'])
        self.numbers = int(values['numbers'])

    def create_password(self):
        for i in range(self.letters):
            l = random.randint(0, len(alphabet) - 1)
            ul = random.randint(0, 1)
            if ul == 0:
                self.l_pass.append(alphabet[l])
            else:
                self.l_pass.append(alphabet[l].upper())

        for i in range(self.symbols):
            s = random.randint(0, len(symbol) - 1)
            self.s_pass.append(symbol[s])

        for i in range(self.numbers):
            n = random.randint(0, 9)
            self.n_pass.append(str(n))

        pw_list = self.l_pass + self.s_pass + self.n_pass
        random.shuffle(pw_list)

        for i in range(len(pw_list)):
            self.password += pw_list[i]

        self.check_password()
        return self.password

    def check_password(self):
        lowercase = 0
        uppercase = 0

        for i in range(len(self.password)):
            if self.password[i] in alphabet:
                lowercase += 1
            elif self.password[i] in alphabet.upper():
                uppercase += 1
        if lowercase == 0 or uppercase == 0:
            self.l_pass = []
            self.s_pass = []
            self.n_pass = []
            self.password = ""
            self.create_password()


pw = Password()


class Layout(object):
    def __init__(self):
        self.layoutz = None
        self.window = None
        self.password = ""

    def layout(self):
        self.layoutz = [
            [sg.Text("Number of letters:", size=size), sg.In(key='letters', size=in_size)],
            [sg.Text("Number of symbols:", size=size), sg.In(key='symbols', size=in_size)],
            [sg.Text("Number of numbers:", size=size), sg.In(key='numbers', size=in_size)],
            [sg.Text("")],
            [sg.Button("Generate password", size=(20, 2)), sg.Text("", size=(0, 3)), sg.Button("Done", size=(10, 2))],
            [sg.Text("Password:", size=(15, 1))],
            [sg.Output(size=(30, 1))],
            [sg.Text("")],
            [sg.Button("Copy to clipboard")]
        ]
        self.window = sg.Window("Password generator", self.layoutz)


layout = Layout()
layout.layout()

running = True
while running:
    layout.password = pw.password
    event, values = layout.window.read()

    if event == sg.WIN_CLOSED or event == "Done":
        sg.popup("Goodbye!", background_color='black', auto_close=True, auto_close_duration=1, button_type=5)
        print("Program terminated")
        sys.exit()
    if event == 'Copy to clipboard':
        if pw.password == "":
            sg.popup("        There is nothing to copy!", title="Alert!")
        else:
            pyperclip.copy(pw.password)
            sg.popup("Password copied to clipboard!", title="Done")
    if event == "Generate password":
        try:
            if int(values['letters']) <= 1:
                sg.popup("Letter count must be higher than 1!", title="Alert!")
            else:
                pw.password = ""
                pw.info()
                print(f"{pw.create_password()}")
                layout.password = pw.password

                pw.l_pass = []
                pw.s_pass = []
                pw.n_pass = []
        except ValueError:
            sg.popup("     Values must be a number!     ", title="Alert!")
