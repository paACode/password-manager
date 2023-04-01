import pandas
import os

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


    def export_as_dataframe(self):
        dataframe = pandas.DataFrame()
        dataframe["website"] = self.websites
        dataframe["username"] = self.usernames
        dataframe["password"] = self.passwords
        return dataframe

    def read_from_csv(self):
        if os.path.isfile("credentials.csv"):
            dataframe = pandas.read_csv("credentials.csv")
            self.websites = dataframe["website"].tolist()
            self.passwords = dataframe["password"].tolist()
            self.usernames = dataframe["username"].tolist()

    def export_to_csv(self):
        credentials = self.export_as_dataframe()
        credentials.to_csv("credentials.csv")

    def print_credentials(self):
        print(self.usernames)
        print(self.websites)
        print(self.passwords)
    def clear(self):
        self.websites.clear()
        self.usernames.clear()
        self.passwords.clear()

