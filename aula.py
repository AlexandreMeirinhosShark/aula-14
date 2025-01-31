from tkinter import *

counter = 0
screen = Tk()
screen.title("Teste")
screen.geometry("500x500+750+250")
screen.wm_resizable(width=False, height=False)


def teste():
    print("ola")


def teste2():
    print('')


button = Button(screen, text="Clique aqui", command=teste2)
button.pack(pady=100)
button2 = Button(screen, text="Clique ali", command=teste)
button2.place(x=100, y=100)

labe = Label(screen, text=f"Número {counter}", font="Time 20 bold")
labe.place(width=150, height=30, x=100, y=150)

screen.mainloop()
