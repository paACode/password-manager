import pandas
import os
import json

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

    def read_from_json(self):
        try:
            with open("credentials.json", "r") as credentials_file:
                credentials_list = json.load(credentials_file)
        except FileNotFoundError:
            with open("credentials.json", "w"):
                print("empty credentials.json created")
        except json.JSONDecodeError:
            pass

        else:
            self.websites = [entry["website"] for entry in credentials_list]
            self.passwords = [entry["password"] for entry in credentials_list]
            self.usernames = [entry["username"] for entry in credentials_list]




    def export_to_csv(self):
        credentials = self.export_as_dataframe()
        credentials.to_csv("credentials.csv")

    def export_to_json(self):
        credentials_df = self.export_as_dataframe()
        credentials_json = credentials_df.to_json(orient= "records")
        credentials_json_parsed = json.loads(credentials_json)
        with open("credentials.json", "w") as credentials_file:
            json.dump(credentials_json_parsed, credentials_file, indent=4)




    def print_credentials(self):
        print(self.usernames)
        print(self.websites)
        print(self.passwords)

    def clear(self):
        self.websites.clear()
        self.usernames.clear()
        self.passwords.clear()
