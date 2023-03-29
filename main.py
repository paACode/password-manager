import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200


if __name__ == '__main__':
    screen = tkinter.Tk()
    screen.title("Password Manager")
    screen.config(padx=50, pady=50)
    canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    logo = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=logo)
    canvas.grid(column=1, row=0)

    website_label = tkinter.Label(text="Website:")
    website_label.grid(column=0,row=1)
    username_label = tkinter.Label(text="Email/Username:")
    username_label.grid(column=0, row=2)
    password_label = tkinter.Label(text="Password:")
    password_label.grid(column=0, row=3)
    website_input = tkinter.Entry()
    website_input.grid(column=1, row=1, columnspan=2, sticky="w")
    username_input = tkinter.Entry()
    username_input.grid(column=1, row=2, columnspan=2, sticky="w")
    password_input = tkinter.Entry()
    password_input.grid(column=1, row=3, sticky="w")
    generate_button = tkinter.Button(text="Generate Password")
    generate_button.grid(column=2, row=3)
    add_button = tkinter.Button(text="Add")
    add_button.grid(column=1, row=4)

    screen.mainloop()
