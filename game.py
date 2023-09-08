import pygame
from objetos import Objeto_Cenario
from random import randrange

class Game:

    def __init__(self) -> None:
        
        self.bg = Objeto_Cenario("assets/bg.png", 0, 0) # background
        self.bg2 = Objeto_Cenario("assets/bg.png", 0, -640)
        self.muda_cena = False
        self.aranha = Objeto_Cenario("assets/spider1.png", randrange(0,300), -50)

    def desenhar(self, tela: pygame.surface.Surface) -> None:

        self.bg.grupo.draw(tela)
        self.bg2.grupo.draw(tela)
        self.aranha.grupo.draw(tela)

    def atualizar_tela(self) -> None:

        self.mova_bg()
        self.aranha.anime()
        self.mova_ahanhas()

    def mova_bg(self) -> None:

        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4
        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def mova_ahanhas(self) -> None:

        self.aranha.sprite.rect[1] += 10
        if self.aranha.sprite.rect[1] >= 700:
            self.aranha.sprite.kill()
            self.aranha = Objeto_Cenario("assets/spider1.png", randrange(0,300), -50)
