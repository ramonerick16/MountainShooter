#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH , WIN_HEIGHT
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT ))

    def run(self):
        menu = Menu(self.window)  # Cria o menu uma única vez
        menu.run()  # Inicia a lógica do menu

        while True:
            pass  # O 'pass' deve estar com 8 espaços (ou 2 tabs) de recuo

''