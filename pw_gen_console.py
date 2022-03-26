# simple password generator

import random

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
        self.letters = int(input("Number of letters: "))
        self.symbols = int(input("Number of symbols: "))
        self.numbers = int(input("Number of numbers: "))

        if self.letters <= 1:
            print("Letter count must be higher than 1!")
            self.info()
        else:
            self.create_password()

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
        print(self.password)

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


pw = Password()
pw.info()
