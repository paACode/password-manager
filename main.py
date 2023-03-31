import tkinter
import pandas

import data_handler
import graphical_user_interface


def save_credentials():
    credentials_handler.add_website(gui.website_input.get())
    credentials_handler.add_password(gui.password_input.get())
    credentials_handler.add_username(gui.username_input.get())
    credentials_handler.print_credentials()


if __name__ == '__main__':
    gui = graphical_user_interface.PasswordManager()
    gui.add_logo_to_canvas()
    gui.set_layout()
    gui.set_default_behaviour()

    credentials_handler = data_handler.DataHandler()

    gui.add_button.configure(command=save_credentials)

    gui.screen.mainloop()
