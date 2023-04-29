import tkinter
import tkinter.messagebox


def popup_empty_field():
    tkinter.messagebox.showerror(title="Oops", message=f"Please do not leave any fields empty")


def popup_website_not_found(website):
    tkinter.messagebox.showerror(title="Oops", message=f"Could not find \n"
                                                       f"'{website}'")


def popup_found_credentials(found_pw, found_website, found_username):
    tkinter.messagebox.showinfo(title="Search", message=f"Credentials found for {found_website}:"
                                                        f"\n username: {found_pw}"
                                                        f"\n password: {found_username}")


class PasswordManager:
    CANVAS_WIDTH = 200
    CANVAS_HEIGHT = 200

    def __init__(self):
        self.screen = tkinter.Tk()
        self.screen.title("Password Manager")
        self.canvas = tkinter.Canvas()
        self.logo = tkinter.PhotoImage(file="logo.png")
        self.website_label = tkinter.Label(text="Website:")
        self.username_label = tkinter.Label(text="Email/Username:")
        self.password_label = tkinter.Label(text="Password:")
        self.website_input = tkinter.Entry()
        self.username_input = tkinter.Entry()
        self.password_input = tkinter.Entry()
        self.generate_button = tkinter.Button(text="Generate Password")
        self.add_button = tkinter.Button(text="Add")
        self.search_button = tkinter.Button(text="Search")

    def add_logo_to_canvas(self):
        self.canvas.configure(width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        self.canvas.create_image(self.CANVAS_WIDTH / 2, self.CANVAS_HEIGHT / 2, image=self.logo)

    def set_default_behaviour(self):
        self.username_input.insert(0, "example@gmail.com")
        self.website_input.focus()

    def set_layout(self):
        self.screen.config(padx=50, pady=50)
        self.canvas.grid(column=1, row=0)
        self.website_label.grid(column=0, row=1)
        self.username_label.grid(column=0, row=2)
        self.password_label.grid(column=0, row=3)
        self.website_input.grid(column=1, row=1, sticky="ew")
        self.username_input.grid(column=1, row=2, columnspan=2, sticky="ew")
        self.password_input.grid(column=1, row=3, sticky="ew")
        self.generate_button.grid(column=2, row=3, sticky="ew")
        self.search_button.grid(column=2, row=1, sticky="ew")
        self.add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

    def get_password(self):
        return self.password_input.get()

    def get_username(self):
        return self.username_input.get()

    def get_website(self):
        return self.website_input.get()

    def clear_password_input(self):
        self.password_input.delete(0, tkinter.END)

    def clear_website_input(self):
        self.website_input.delete(0, tkinter.END)

    def popup_save_confirmation(self):
        is_confirmed = tkinter.messagebox.askokcancel(title=self.get_website(),
                                                      message=f"Credentials entered:"
                                                              f"\n username: {self.get_username()}"
                                                              f"\n password: {self.get_password()}"
                                                              f"\n Is this ok?")
        return is_confirmed

    def inputs_valid(self):
        if self.get_password() == "":
            popup_empty_field()
            return False
        elif self.get_username() == "":
            popup_empty_field()
            return False
        elif self.get_website() == "":
            popup_empty_field()
            return False
        return True
