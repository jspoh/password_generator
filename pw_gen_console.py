# simple password generator
# console version in case you dont have PySimpleGUI / want to use this in browsers (colab.google maybe?)

import random
import sys
import pyperclip

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
        try:
            self.letters = int(input("Number of letters: "))
            self.symbols = int(input("Number of symbols: "))
            self.numbers = int(input("Number of numbers: "))
        except ValueError:
            print("Values must be a number!")
            self.info()

        if self.letters <= 1:
            print("Letter count must be higher than 1!")
            self.info()
        else:
            self.create_password()

    def create_password(self):
        self.l_pass = []
        self.s_pass = []
        self.n_pass = []
        self.password = ""
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
        print(f'''
Password: {self.password}''')
        pyperclip.copy(self.password)
        print('''Password successfully copied to clipboard
''')
        self.cont()

    def check_password(self):  # to ensure that there is at least 1 upper and lower case alphabet in the password
        lowercase = 0
        uppercase = 0

        for i in range(len(self.password)):
            if self.password[i] in alphabet:
                lowercase += 1
            elif self.password[i] in alphabet.upper():
                uppercase += 1
        if lowercase == 0 or uppercase == 0:
            self.create_password()

    def cont(self):
        contin = input("Would you like to generate another password? (y/n)\n").lower()
        if contin == "y":
            self.info()
        elif contin == "n":
            print("Alright, goodbye!")
            sys.exit()
        else:
            print("\nPlease enter a valid response! (y/n)")
            self.cont()

pw = Password()
pw.info()


# disregard this lol
# this is just another method to do this lol without the random.shuffle() function
#
# counter = 0
# while counter < letters+symbols+numbers:
#    choice = random.randint(1, 3)
#    if choice == 1:
#        if l_pass:
#            lc = random.randint(0, len(l_pass)-1)
#            password += l_pass[lc]
#            l_pass.remove(l_pass[lc])
#            counter += 1
#    elif choice == 2:
#        if s_pass:
#            ls = random.randint(0, len(s_pass) - 1)
#            password += s_pass[ls]
#            s_pass.remove(s_pass[ls])
#            counter += 1
#    else:
#        if n_pass:
#            ln = random.randint(0, len(n_pass)-1)
#            password += n_pass[ln]
#            n_pass.remove(n_pass[ln])
#            counter += 1
