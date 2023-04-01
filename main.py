import data_handler
import graphical_user_interface


def save_new_credentials():
    credentials_handler.add_website(gui.website_input.get())
    credentials_handler.add_password(gui.password_input.get())
    credentials_handler.add_username(gui.username_input.get())
    credentials_handler.export_to_csv()

    gui.clear_password_input()
    gui.clear_website_input()




if __name__ == '__main__':
    gui = graphical_user_interface.PasswordManager()
    gui.add_logo_to_canvas()
    gui.set_layout()
    gui.set_default_behaviour()

    credentials_handler = data_handler.DataHandler()
    credentials_handler.read_from_csv()
    credentials_handler.print_credentials()
    gui.add_button.configure(command=save_new_credentials)

    gui.screen.mainloop()
