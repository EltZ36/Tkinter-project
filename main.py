import tkinter as tk

window = tk.Tk()
welcome = tk.Button(text="Hello, What is your name?", fg="white", bg="black",width=20, height=10)
name = tk.Entry()
welcome.pack()
name.pack()

