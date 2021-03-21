# -*- coding: utf-8 -*-

# @autor: Felipe Ucelli
# @github: github.com/felipeucelli

# Built-in
import tkinter


class Game:
    """
    Classe responsável pela criação da interface e controle do game
    """
    def __init__(self, master):
        self.root = master
        self.root.title('Tic Tac Toe')

        # Instânciação do valor dos players
        # Player_X
        self.player_x = tkinter.StringVar()

        # Player_O
        self.player_o = tkinter.StringVar()

        # Seta o valor de cada player
        # Player_X
        self.player_x.set('X')

        # Player_O
        self.player_o.set('O')

        # Seta o primeiro player: 0 == X, 1 == O
        self.active = 0

        # Funções de inicialização
        self._create_buttons()
        self.load_default_color()
        self._score()

    def reset_buttons(self):
        """
        Responsável por carregar as configurações padrões dos inputs
        :return:
        """

        # Seta o valor nos inputs
        self.button_1['text'] = ''
        self.button_2['text'] = ''
        self.button_3['text'] = ''
        self.button_4['text'] = ''
        self.button_5['text'] = ''
        self.button_6['text'] = ''
        self.button_7['text'] = ''
        self.button_8['text'] = ''
        self.button_9['text'] = ''

        # Seta o estado dos inputs
        self.button_1.configure(state=tkinter.ACTIVE)
        self.button_2.configure(state=tkinter.ACTIVE)
        self.button_3.configure(state=tkinter.ACTIVE)
        self.button_4.configure(state=tkinter.ACTIVE)
        self.button_5.configure(state=tkinter.ACTIVE)
        self.button_6.configure(state=tkinter.ACTIVE)
        self.button_7.configure(state=tkinter.ACTIVE)
        self.button_8.configure(state=tkinter.ACTIVE)
        self.button_9.configure(state=tkinter.ACTIVE)

        # Seta o estado do botão "again"
        self.again.configure(state=tkinter.DISABLED)

        # Carrega as configurações padrões de background color
        self.load_default_color()

    def disable_buttons(self):
        """
        Responsável por desativar os inputs
        :return:
        """
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
        """
        Seta os valores padrões de background color
        :return:
        """
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
        """
        Responsável por alterar o background color em caso de vitória
        :return:
        """
        btn_1['bg'] = '#007700'
        btn_2['bg'] = '#007700'
        btn_3['bg'] = '#007700'

    def win_checker_x(self):
        """
        Responsável por verificar uma possível vitória no player_X
        :return:
        """

        # Linha 0
        if self.button_1['text'] == 'X' and self.button_2['text'] == 'X' and self.button_3['text'] == 'X':

            # Incrementa um ponto para o player_X
            self.player_x_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_1, self.button_2, self.button_3)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Linha 1
        if self.button_4['text'] == 'X' and self.button_5['text'] == 'X' and self.button_6['text'] == 'X':

            # Incrementa um ponto para o player_X
            self.player_x_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_4, self.button_5, self.button_6)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Linha 2
        if self.button_7['text'] == 'X' and self.button_8['text'] == 'X' and self.button_9['text'] == 'X':

            # Incrementa um ponto para o player_X
            self.player_x_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_7, self.button_8, self.button_9)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 0
        if self.button_1['text'] == 'X' and self.button_4['text'] == 'X' and self.button_7['text'] == 'X':

            # Incrementa um ponto para o player_X
            self.player_x_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_1, self.button_4, self.button_7)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 1
        if self.button_2['text'] == 'X' and self.button_5['text'] == 'X' and self.button_8['text'] == 'X':

            # Incrementa um ponto para o player_X
            self.player_x_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_2, self.button_5, self.button_8)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 2
        if self.button_3['text'] == 'X' and self.button_6['text'] == 'X' and self.button_9['text'] == 'X':

            # Incrementa um ponto para o player_X
            self.player_x_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_3, self.button_6, self.button_9)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Direita esquerda
        if self.button_1['text'] == 'X' and self.button_5['text'] == 'X' and self.button_9['text'] == 'X':

            # Incrementa um ponto para o player_X
            self.player_x_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_1, self.button_5, self.button_9)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Esquerda direita
        if self.button_3['text'] == 'X' and self.button_5['text'] == 'X' and self.button_7['text'] == 'X':

            # Incrementa um ponto para o player_X
            self.player_x_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_3, self.button_5, self.button_7)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

    def win_checker_o(self):
        """
        Responsável por verificar uma possível vitória no player_O
        :return:
        """

        # Linha 0
        if self.button_1['text'] == 'O' and self.button_2['text'] == 'O' and self.button_3['text'] == 'O':

            # Incrementa um ponto para o player_O
            self.player_o_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_1, self.button_2, self.button_3)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Linha 1
        if self.button_4['text'] == 'O' and self.button_5['text'] == 'O' and self.button_6['text'] == 'O':

            # Incrementa um ponto para o player_O
            self.player_o_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_4, self.button_5, self.button_6)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Linha 2
        if self.button_7['text'] == 'O' and self.button_8['text'] == 'O' and self.button_9['text'] == 'O':

            # Incrementa um ponto para o player_O
            self.player_o_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_7, self.button_8, self.button_9)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 0
        if self.button_1['text'] == 'O' and self.button_4['text'] == 'O' and self.button_7['text'] == '0':

            # Incrementa um ponto para o player_O
            self.player_o_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_1, self.button_5, self.button_7)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 1
        if self.button_2['text'] == 'O' and self.button_5['text'] == 'O' and self.button_8['text'] == 'O':

            # Incrementa um ponto para o player_O
            self.player_o_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_2, self.button_5, self.button_8)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Coluna 2
        if self.button_3['text'] == 'O' and self.button_6['text'] == 'O' and self.button_9['text'] == 'O':

            # Incrementa um ponto para o player_O
            self.player_o_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_3, self.button_6, self.button_9)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Direita esquerda
        if self.button_1['text'] == 'O' and self.button_5['text'] == 'O' and self.button_9['text'] == 'O':

            # Incrementa um ponto para o player_O
            self.player_o_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_1, self.button_5, self.button_9)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

        # Esquerda direita
        if self.button_3['text'] == 'O' and self.button_5['text'] == 'O' and self.button_7['text'] == 'O':

            # Incrementa um ponto para o player_O
            self.player_o_score['text'] += 1

            # Altera o background color
            self.win_change_color(self.button_3, self.button_5, self.button_7)

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

    def full_buttons_checker(self):
        """
        Responsável por veficar se todos os inputs já foram ativados
        :return:
        """
        if self.button_1['text'] != '' and self.button_2['text'] != '' and self.button_3['text'] != '' and \
                self.button_4['text'] != '' and self.button_5['text'] != '' and self.button_6['text'] != '' and \
                self.button_7['text'] != '' and self.button_8['text'] != '' and self.button_9['text'] != '':

            # Desativa os inputs
            self.disable_buttons()

            # Ativa o botão "again"
            self.again.configure(state=tkinter.ACTIVE)

    def restart_score(self):
        """
        Responsável por reiniciar os pontos
        :return:
        """

        # Reinicia os pontos do player_X
        self.player_x_score['text'] = 0

        # Reinicia os pontos do player_O
        self.player_o_score['text'] = 0

        # Reinicia o input
        self.reset_buttons()

    def select(self, button):
        """
        Responsável por adicionar um valor no input
        :param button: input selecionado
        :return:
        """

        # Verifica se o input está livre para receber algum valor
        if button['text'] == '':

            # Verifica qual player está ativo: 0 == X, 1 == O
            if self.active == 0:

                # Seta o player_X no input selecionado
                button['text'] = self.player_x.get()

                # Seta o player_O como próximo jogador
                self.active = 1
            else:

                # Seta o player_O no input selecionado
                button['text'] = self.player_o.get()

                # Seta o player_X como próximo jogador
                self.active = 0

            # Verifica se o player_X obteve uma vitória
            self.win_checker_x()

            # Verifica se o player_O obteve uma vitória
            self.win_checker_o()

            # Verifica se todos os input foram selecionados e nenhum player obteve vitória
            self.full_buttons_checker()

    def _score(self):
        """
        Responsável por criar o layout de pontos
        :return:
        """

        # Seta o nome do player
        player_x = tkinter.Label(self.root, font='Arial 10 bold', text='PLAYER X:')
        player_o = tkinter.Label(self.root, font='Arial 10 bold', text='PLAYER O:')

        # Seta os pontos do player
        self.player_x_score = tkinter.Label(self.root, font='Arial 10 bold', text=0)
        self.player_o_score = tkinter.Label(self.root, font='Arial 10 bold', text=0)

        # Distribuição dos layers com o gerenciador de layout grid()
        player_x.grid(row=3, column=0)
        player_o.grid(row=4, column=0)
        self.player_x_score.grid(row=3, column=1)
        self.player_o_score.grid(row=4, column=1)

    def _create_buttons(self):
        """
        Responsável pela criação dos inputs e dos botões
        :return:
        """

        # Instânciação dos botões "again" e "reset"
        self.again = tkinter.Button(self.root, font='Arial 10 bold', text='AGAIN')
        self.again.configure(state=tkinter.DISABLED)
        self.restart = tkinter.Button(self.root, font='Arial 10 bold', text='RESET')

        # Instânciação dos inputs
        # Linha 0
        self.button_1 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_2 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_3 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)

        # Linha 1
        self.button_4 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_5 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_6 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)

        # Linha 2
        self.button_7 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_8 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)
        self.button_9 = tkinter.Button(self.root, font='Arial 20 bold', text='', width=5, height=2)

        # Adição de funcionalidade para os inputs
        # Linha 0
        self.button_1['command'] = lambda: self.select(self.button_1)
        self.button_2['command'] = lambda: self.select(self.button_2)
        self.button_3['command'] = lambda: self.select(self.button_3)

        # Linha 1
        self.button_4['command'] = lambda: self.select(self.button_4)
        self.button_5['command'] = lambda: self.select(self.button_5)
        self.button_6['command'] = lambda: self.select(self.button_6)

        # Linha 2
        self.button_7['command'] = lambda: self.select(self.button_7)
        self.button_8['command'] = lambda: self.select(self.button_8)
        self.button_9['command'] = lambda: self.select(self.button_9)

        # Adição de funcionalidade para o botão "again"
        # Linha 3
        self.again['command'] = lambda: self.reset_buttons()

        # Adição de funcionalidade para o botão "reset"
        # Linha 4
        self.restart['command'] = lambda: self.restart_score()

        # Distribuição dos inputs e botões com o gerenciador de layout grid()
        # Linha 0
        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)

        # Linha 1
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)

        # Linha 2
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)

        # Linha 3
        self.again.grid(row=3, column=2)

        # Linha 4
        self.restart.grid(row=4, column=2)

    def start(self):
        """
        Responsável por iniciar a aplicação
        :return:
        """
        self.root.mainloop()
