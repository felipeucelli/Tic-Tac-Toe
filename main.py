import tkinter


class Game:
    def __init__(self, master):
        self.root = master
        self.root.title('Tic Tac Toe')

        self.player_x = tkinter.StringVar()
        self.player_o = tkinter.StringVar()

        self.player_x.set('X')
        self.player_o.set('O')
        self.active = 0
        self._create_buttons()
        self._score()

    def reset_buttons(self):
        self.button_1['text'] = ''
        self.button_2['text'] = ''
        self.button_3['text'] = ''
        self.button_4['text'] = ''
        self.button_5['text'] = ''
        self.button_6['text'] = ''
        self.button_7['text'] = ''
        self.button_8['text'] = ''
        self.button_9['text'] = ''

        self.button_1.configure(state=tkinter.ACTIVE)
        self.button_2.configure(state=tkinter.ACTIVE)
        self.button_3.configure(state=tkinter.ACTIVE)
        self.button_4.configure(state=tkinter.ACTIVE)
        self.button_5.configure(state=tkinter.ACTIVE)
        self.button_6.configure(state=tkinter.ACTIVE)
        self.button_7.configure(state=tkinter.ACTIVE)
        self.button_8.configure(state=tkinter.ACTIVE)
        self.button_9.configure(state=tkinter.ACTIVE)

    def win_checker_x(self):

        # Linha 0
        if self.button_1['text'] == 'X' and self.button_2['text'] == 'X' and self.button_3['text'] == 'X':
            self.player_x_score['text'] += 1
            self.reset_buttons()

        # Linha 1
        if self.button_4['text'] == 'X' and self.button_5['text'] == 'X' and self.button_6['text'] == 'X':
            self.player_x_score['text'] += 1
            self.reset_buttons()

        # Linha 2
        if self.button_7['text'] == 'X' and self.button_8['text'] == 'X' and self.button_9['text'] == 'X':
            self.player_x_score['text'] += 1
            self.reset_buttons()

        # Coluna 0
        if self.button_1['text'] == 'X' and self.button_4['text'] == 'X' and self.button_7['text'] == 'X':
            self.player_x_score['text'] += 1
            self.reset_buttons()

        # Coluna 1
        if self.button_2['text'] == 'X' and self.button_5['text'] == 'X' and self.button_8['text'] == 'X':
            self.player_x_score['text'] += 1
            self.reset_buttons()

        # Coluna 2
        if self.button_3['text'] == 'X' and self.button_6['text'] == 'X' and self.button_9['text'] == 'X':
            self.player_x_score['text'] += 1
            self.reset_buttons()

        # Direita esquerda
        if self.button_1['text'] == 'X' and self.button_5['text'] == 'X' and self.button_9['text'] == 'X':
            self.player_x_score['text'] += 1
            self.reset_buttons()

        # Esquerda direita
        if self.button_3['text'] == 'X' and self.button_5['text'] == 'X' and self.button_7['text'] == 'X':
            self.player_x_score['text'] += 1
            self.reset_buttons()

    def win_checker_o(self):

        # Linha 0
        if self.button_1['text'] == 'O' and self.button_2['text'] == 'O' and self.button_3['text'] == 'O':
            self.player_o_score['text'] += 1
            self.reset_buttons()

        # Linha 1
        if self.button_4['text'] == 'O' and self.button_5['text'] == 'O' and self.button_6['text'] == 'O':
            self.player_o_score['text'] += 1
            self.reset_buttons()

        # Linha 2
        if self.button_7['text'] == 'O' and self.button_8['text'] == 'O' and self.button_9['text'] == 'O':
            self.player_o_score['text'] += 1
            self.reset_buttons()

        # Coluna 0
        if self.button_1['text'] == 'O' and self.button_4['text'] == 'O' and self.button_7['text'] == '0':
            self.player_o_score['text'] += 1
            self.reset_buttons()

        # Coluna 1
        if self.button_2['text'] == 'O' and self.button_5['text'] == 'O' and self.button_8['text'] == 'O':
            self.player_o_score['text'] += 1
            self.reset_buttons()

        # Coluna 2
        if self.button_3['text'] == 'O' and self.button_6['text'] == 'O' and self.button_9['text'] == 'O':
            self.player_o_score['text'] += 1
            self.reset_buttons()

        # Direita esquerda
        if self.button_1['text'] == 'O' and self.button_5['text'] == 'O' and self.button_9['text'] == 'O':
            self.player_o_score['text'] += 1
            self.reset_buttons()

        # Esquerda direita
        if self.button_3['text'] == 'O' and self.button_5['text'] == 'O' and self.button_7['text'] == 'O':
            self.player_o_score['text'] += 1
            self.reset_buttons()

    def select(self, button):
        if self.active == 0:
            button['text'] = self.player_x.get()
            button.configure(state=tkinter.DISABLED)
            self.active = 1
        else:
            button['text'] = self.player_o.get()
            button.configure(state=tkinter.DISABLED)
            self.active = 0
        self.win_checker_x()
        self.win_checker_o()

    def _score(self):
        self.player_x_score = tkinter.Label(self.root, font='Arial 10 bold', text=0)
        self.player_o_score = tkinter.Label(self.root, font='Arial 10 bold', text=0)

        self.player_x_score.grid(row=3, columnspan=3)
        self.player_o_score.grid(row=4, columnspan=3)

    def _create_buttons(self):
        self.button_1 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_2 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_3 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_4 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_5 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_6 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_7 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_8 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_9 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)

        self.button_1['command'] = lambda: self.select(self.button_1)
        self.button_2['command'] = lambda: self.select(self.button_2)
        self.button_3['command'] = lambda: self.select(self.button_3)
        self.button_4['command'] = lambda: self.select(self.button_4)
        self.button_5['command'] = lambda: self.select(self.button_5)
        self.button_6['command'] = lambda: self.select(self.button_6)
        self.button_7['command'] = lambda: self.select(self.button_7)
        self.button_8['command'] = lambda: self.select(self.button_8)
        self.button_9['command'] = lambda: self.select(self.button_9)

        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    main = tkinter.Tk()
    root = Game(main)
    root.start()
