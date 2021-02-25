from tkinter import *
from tkinter import ttk

class Hello:
    def __init__(self, master):

        self.myLabel = Label(master, text="Hello world!")
        self.myLabel.grid(row = 0, column = 0, columnspan = 2)
        self.myLabel.config(text="lhrferfbergfljeqw", wraplength = 150, justify = CENTER, foreground = "blue", background = "yellow"
                            , font = ("Courier", 18, "bold"))
        #logo = PhotoImage(file = "Path")
        #self.myLabel.config(image=logo)
        #self.mylabel.config(compund = "text", "center", "left")
        #mylabel.img = logo
        #mylabel.config(image =label.img)

        #samm_logo = logo.subsample(5, 5)
        #button.config(image = samll_logo)

        self.button = Button(master, text="Click me", command = self.text_mass)
        self.button.grid(row = 1, column = 0)
        self.button.invoke()
        self.b = ttk.Button(master, text="Click me to change", command = self.text_m)
        self.b.grid(row = 1, column = 1)
        self.b.state(["disabled"])
        self.b.state(["!disabled"])

        self.check = ttk.Checkbutton(master, text="Spam")
        self.check.grid(row = 3, column = 1)
        self.spam = StringVar()
        self.spam.set("SPAM!")
        self.check.config(variable = self.spam, onvalue = "it is there", offvalue = "It is gone!")

        self.rad = ttk.Radiobutton(master, text = "Iam hear")
        self.rad.grid(row = 3, column = 0)

        self.ent = ttk.Entry(master, width=30, justify = CENTER)
        self.ent.grid(row = 4)
        self.ent.get()
        self.ent.insert(0, "Enter your password")
        self.ent.config(show = "*")

        self.com = ttk.Combobox(master, textvariable = "month")
        self.com.grid(row = 5)
        self.com.config(values = ("Jan", "Feb"))

        self.sp = ttk.Spinbox(master, from_=1990, to = 2021, textvariable = "year")
        self.sp.grid(row = 6)






    def text_m(self):
        self.myLabel.config(text="You changed me!")

    def text_mass(self):
        self.myLabel.config(text="You changed me again!")


def main():
    root = Tk()
    app = Hello(root)
    root.geometry("500x600")
    root.mainloop()

if __name__== "__main__": main()