# -*- coding: utf-8 -*-

# @autor: Felipe Ucelli
# @github: github.com/felipeucelli

# Built-in
from tkinter import Tk

# Módulo próprio
from lib.game import Game

if __name__ == '__main__':
    main = Tk()
    root = Game(main)
    root.start()
