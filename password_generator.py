# Password Generator Project
import random
import pyperclip

class PasswordGenerator:

    def __init__(self):
        self.seed_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.seed_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.seed_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        self.nr_letters = None
        self.nr_symbols = None
        self.nr_numbers = None
        self.password_list = []

    def set_password_rules(self, letters=10, numbers=4, symbols=4, *args):
        self.nr_letters = letters
        self.nr_symbols = symbols
        self.nr_numbers = numbers

    def generate_password(self):
        password_letters = [random.choice(self.seed_letters) for letter in range(self.nr_letters)]
        symbol_letters = [random.choice(self.seed_symbols) for symbol in range(self.nr_symbols)]
        number_letters = [random.choice(self.seed_numbers) for number in range(self.nr_numbers)]
        self.password_list = password_letters + symbol_letters + number_letters
        # for letter in range(self.nr_letters):
        #     self.password_list.append(random.choice(self.seed_letters))
        # for symbol in range(self.nr_symbols):
        #     self.password_list.append(random.choice(self.seed_symbols))
        # for number in range(self.nr_numbers):
        #     self.password_list.append(random.choice(self.seed_numbers))
        random.shuffle(self.password_list)
        pyperclip.copy(self.get_password_as_string())

    def get_password_as_string(self):
        password = ""
        for char in self.password_list:
            password += char
        return password

    def reset_password(self):
        self.password_list.clear()
