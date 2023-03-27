import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200

if __name__ == '__main__':
    screen = tkinter.Tk()
    screen.title("Password Manager")
    screen.config(padx=20, pady=20)
    canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    logo = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=logo)
    canvas.pack()

    screen.mainloop()
