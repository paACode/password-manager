import tkinter
import pandas
import gui


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

website_list = []
username_list = []
password_list = []


# credentials = {
#     "website": ["hello"],
#     "username": [],
#     "password": []
# }

# credentials_dataframe = pandas.DataFrame.from_dict(credentials)
# print(credentials_dataframe.website)

def get_credentials(gui):
    print(bla)
    print(gui.get_password(), gui.get_website(), gui.get_username())


# ---------------------------- UI SETUP ------------------------------- #

if __name__ == '__main__':
    gui = gui.Gui()
    print(gui.get_username())
    gui.add_button.configure(command= get_credentials)
