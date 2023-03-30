import tkinter
class Gui:
    CANVAS_WIDTH = 200
    CANVAS_HEIGHT = 200
    def __init__(self):
        self.screen = tkinter.Tk()
        self.screen.title("Password Manager")
        self.screen.config(padx=50, pady=50)

        self.canvas = tkinter.Canvas(width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        self.logo = tkinter.PhotoImage(file="logo.png")
        self.canvas.create_image(self.CANVAS_WIDTH / 2, self.CANVAS_HEIGHT / 2, image=self.logo)
        self.canvas.grid(column=1, row=0)

        self.website_label = tkinter.Label(text="Website:")
        self.website_label.grid(column=0, row=1)

        self.username_label = tkinter.Label(text="Email/Username:")
        self.username_label.grid(column=0, row=2)

        self.password_label = tkinter.Label(text="Password:")
        self.password_label.grid(column=0, row=3)

        self.website_input = tkinter.Entry()
        self.website_input.grid(column=1, row=1, columnspan=2, sticky="ew")
        self.website_input.focus()

        self.username_input = tkinter.Entry()
        self.username_input.grid(column=1, row=2, columnspan=2, sticky="ew")
        self.username_input.insert(0, "example@gmail.com")

        self.password_input = tkinter.Entry()
        self.password_input.grid(column=1, row=3, sticky="ew")

        self.generate_button = tkinter.Button(text="Generate Password")
        self.generate_button.grid(column=2, row=3)

        self.add_button = tkinter.Button(text="Add")
        self.add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

        self.screen.mainloop()

    def get_password(self):
        return self.password_input.get()

    def get_username(self):
        return self.username_input.get()

    def get_website(self):
        return self.website_input.get()



