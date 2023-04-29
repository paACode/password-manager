import data_handler
import graphical_user_interface
import password_generator


def save_new_credentials():
    if gui.inputs_valid():
        credentials_handler.add_website(gui.get_website())
        credentials_handler.add_username(gui.get_username())
        credentials_handler.add_password(gui.get_password())

        if gui.popup_save_confirmation():
            credentials_handler.export_to_json()
        gui.clear_password_input()
        gui.clear_website_input()


def create_password():
    password_handler.reset_password()
    password_handler.set_password_rules()
    password_handler.generate_password()
    gui.clear_password_input()
    gui.password_input.insert(0, string=password_handler.get_password_as_string())


def search_credentials():
    credentials_handler.read_from_json()
    try:
        search_website = gui.get_website()
        index = credentials_handler.websites.index(search_website)

    except ValueError:
        graphical_user_interface.popup_website_not_found(website=search_website)
    else:
        website = credentials_handler.websites[index]
        password = credentials_handler.passwords[index]
        username = credentials_handler.usernames[index]
        graphical_user_interface.popup_found_credentials(found_website=website, found_username=username,
                                                         found_pw=password)


if __name__ == '__main__':
    gui = graphical_user_interface.PasswordManager()
    gui.add_logo_to_canvas()
    gui.set_layout()
    gui.set_default_behaviour()

    credentials_handler = data_handler.DataHandler()
    credentials_handler.read_from_json()

    password_handler = password_generator.PasswordGenerator()

    gui.add_button.configure(command=save_new_credentials)
    gui.generate_button.configure(command=create_password)
    gui.search_button.configure(command=search_credentials)
    #

    gui.screen.mainloop()
