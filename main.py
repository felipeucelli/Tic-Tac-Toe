import tkinter

root = tkinter.Tk()

player_x = tkinter.StringVar()
player_o = tkinter.StringVar()

player_x.set('X')
player_o.set('O')


def create_buttons():
    button_1 = tkinter.Button(root, text=' ', width=10, height=4)
    button_2 = tkinter.Button(root, text=' ', width=10, height=4)
    button_3 = tkinter.Button(root, text=' ', width=10, height=4)
    button_4 = tkinter.Button(root, text=' ', width=10, height=4)
    button_5 = tkinter.Button(root, text=' ', width=10, height=4)
    button_6 = tkinter.Button(root, text=' ', width=10, height=4)
    button_7 = tkinter.Button(root, text=' ', width=10, height=4)
    button_8 = tkinter.Button(root, text=' ', width=10, height=4)
    button_9 = tkinter.Button(root, text=' ', width=10, height=4)

    button_1.grid(row=0, column=0)
    button_2.grid(row=0, column=1)
    button_3.grid(row=0, column=2)
    button_4.grid(row=1, column=0)
    button_5.grid(row=1, column=1)
    button_6.grid(row=1, column=2)
    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)


create_buttons()

root.mainloop()
