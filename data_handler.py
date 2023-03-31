class DataHandler:
    def __init__(self):
        self.websites = []
        self.usernames = []
        self.passwords = []

    def add_password(self, password_input):
        self.passwords.append(password_input)

    def add_website(self, website_input):
        self.websites.append(website_input)

    def add_username(self, username_input):
        self.usernames.append(username_input)

    def print_credentials(self):
        print(self.usernames)
        print(self.websites)
        print(self.passwords)
