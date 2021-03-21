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
        self.load_default_color()
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

        self.again.configure(state=tkinter.DISABLED)

        self.load_default_color()

    def disable_buttons(self):
        self.button_1.configure(state=tkinter.DISABLED)
        self.button_2.configure(state=tkinter.DISABLED)
        self.button_3.configure(state=tkinter.DISABLED)
        self.button_4.configure(state=tkinter.DISABLED)
        self.button_5.configure(state=tkinter.DISABLED)
        self.button_6.configure(state=tkinter.DISABLED)
        self.button_7.configure(state=tkinter.DISABLED)
        self.button_8.configure(state=tkinter.DISABLED)
        self.button_9.configure(state=tkinter.DISABLED)

    def load_default_color(self):
        self.button_1['bg'] = '#efefef'
        self.button_2['bg'] = '#efefef'
        self.button_3['bg'] = '#efefef'
        self.button_4['bg'] = '#efefef'
        self.button_5['bg'] = '#efefef'
        self.button_6['bg'] = '#efefef'
        self.button_7['bg'] = '#efefef'
        self.button_8['bg'] = '#efefef'
        self.button_9['bg'] = '#efefef'

    @staticmethod
    def win_change_color(btn_1, btn_2, btn_3):
        btn_1['bg'] = '#007700'
        btn_2['bg'] = '#007700'
        btn_3['bg'] = '#007700'

    def win_checker_x(self):

        # Linha 0
        if self.button_1['text'] == 'X' and self.button_2['text'] == 'X' and self.button_3['text'] == 'X':
            self.player_x_score['text'] += 1
            self.win_change_color(self.button_1, self.button_2, self.button_3)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Linha 1
        if self.button_4['text'] == 'X' and self.button_5['text'] == 'X' and self.button_6['text'] == 'X':
            self.player_x_score['text'] += 1
            self.win_change_color(self.button_4, self.button_5, self.button_6)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Linha 2
        if self.button_7['text'] == 'X' and self.button_8['text'] == 'X' and self.button_9['text'] == 'X':
            self.player_x_score['text'] += 1
            self.win_change_color(self.button_7, self.button_8, self.button_9)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 0
        if self.button_1['text'] == 'X' and self.button_4['text'] == 'X' and self.button_7['text'] == 'X':
            self.player_x_score['text'] += 1
            self.win_change_color(self.button_1, self.button_4, self.button_7)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 1
        if self.button_2['text'] == 'X' and self.button_5['text'] == 'X' and self.button_8['text'] == 'X':
            self.player_x_score['text'] += 1
            self.win_change_color(self.button_2, self.button_5, self.button_8)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 2
        if self.button_3['text'] == 'X' and self.button_6['text'] == 'X' and self.button_9['text'] == 'X':
            self.player_x_score['text'] += 1
            self.win_change_color(self.button_3, self.button_6, self.button_9)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Direita esquerda
        if self.button_1['text'] == 'X' and self.button_5['text'] == 'X' and self.button_9['text'] == 'X':
            self.player_x_score['text'] += 1
            self.win_change_color(self.button_1, self.button_5, self.button_9)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Esquerda direita
        if self.button_3['text'] == 'X' and self.button_5['text'] == 'X' and self.button_7['text'] == 'X':
            self.player_x_score['text'] += 1
            self.win_change_color(self.button_3, self.button_5, self.button_7)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

    def win_checker_o(self):

        # Linha 0
        if self.button_1['text'] == 'O' and self.button_2['text'] == 'O' and self.button_3['text'] == 'O':
            self.player_o_score['text'] += 1
            self.win_change_color(self.button_1, self.button_2, self.button_3)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Linha 1
        if self.button_4['text'] == 'O' and self.button_5['text'] == 'O' and self.button_6['text'] == 'O':
            self.player_o_score['text'] += 1
            self.win_change_color(self.button_4, self.button_5, self.button_6)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Linha 2
        if self.button_7['text'] == 'O' and self.button_8['text'] == 'O' and self.button_9['text'] == 'O':
            self.player_o_score['text'] += 1
            self.win_change_color(self.button_7, self.button_8, self.button_9)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 0
        if self.button_1['text'] == 'O' and self.button_4['text'] == 'O' and self.button_7['text'] == '0':
            self.player_o_score['text'] += 1
            self.win_change_color(self.button_1, self.button_5, self.button_7)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 1
        if self.button_2['text'] == 'O' and self.button_5['text'] == 'O' and self.button_8['text'] == 'O':
            self.player_o_score['text'] += 1
            self.win_change_color(self.button_2, self.button_5, self.button_8)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 2
        if self.button_3['text'] == 'O' and self.button_6['text'] == 'O' and self.button_9['text'] == 'O':
            self.player_o_score['text'] += 1
            self.win_change_color(self.button_3, self.button_6, self.button_9)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Direita esquerda
        if self.button_1['text'] == 'O' and self.button_5['text'] == 'O' and self.button_9['text'] == 'O':
            self.player_o_score['text'] += 1
            self.win_change_color(self.button_1, self.button_5, self.button_9)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

        # Esquerda direita
        if self.button_3['text'] == 'O' and self.button_5['text'] == 'O' and self.button_7['text'] == 'O':
            self.player_o_score['text'] += 1
            self.win_change_color(self.button_3, self.button_5, self.button_7)
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

    def full_buttons_checker(self):
        if self.button_1['text'] != '' and self.button_2['text'] != '' and self.button_3['text'] != '' and \
                self.button_4['text'] != '' and self.button_5['text'] != '' and self.button_6['text'] != '' and \
                self.button_7['text'] != '' and self.button_8['text'] != '' and self.button_9['text'] != '':
            self.disable_buttons()
            self.again.configure(state=tkinter.ACTIVE)

    def restart_score(self):
        self.player_x_score['text'] = 0
        self.player_o_score['text'] = 0
        self.reset_buttons()

    def select(self, button):
        if button['text'] == '':
            if self.active == 0:
                button['text'] = self.player_x.get()
                self.active = 1
            else:
                button['text'] = self.player_o.get()
                self.active = 0
            self.win_checker_x()
            self.win_checker_o()
            self.full_buttons_checker()

    def _score(self):
        player_x = tkinter.Label(self.root, font='Arial 10 bold', text='PLAYER X:')
        player_o = tkinter.Label(self.root, font='Arial 10 bold', text='PLAYER O:')

        self.player_x_score = tkinter.Label(self.root, font='Arial 10 bold', text=0)
        self.player_o_score = tkinter.Label(self.root, font='Arial 10 bold', text=0)

        player_x.grid(row=3, column=0)
        player_o.grid(row=4, column=0)
        self.player_x_score.grid(row=3, column=1)
        self.player_o_score.grid(row=4, column=1)

    def _create_buttons(self):
        self.again = tkinter.Button(self.root, font='Arial 10 bold', text='AGAIN')
        self.again.configure(state=tkinter.DISABLED)

        self.restart = tkinter.Button(self.root, font='Arial 10 bold', text='RESET')

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

        self.again['command'] = lambda: self.reset_buttons()
        self.restart['command'] = lambda: self.restart_score()

        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)

        self.again.grid(row=3, column=2)
        self.restart.grid(row=4, column=2)

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    main = tkinter.Tk()
    root = Game(main)
    root.start()
