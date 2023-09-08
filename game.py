import pygame
from objetos import Objeto_Cenario
from random import randrange

class Game:

    def __init__(self) -> None:
        
        self.bg = Objeto_Cenario("assets/bg.png", 0, 0) # background
        self.bg2 = Objeto_Cenario("assets/bg.png", 0, -640)
        self.muda_cena = False
        self.aranha = Objeto_Cenario("assets/spider1.png", randrange(0,300), -50)
        self.flor = Objeto_Cenario("assets/florwer1.png", randrange(0,300), -50)

    def desenhar(self, tela: pygame.surface.Surface) -> None:

        self.bg.desenhar_objeto(tela)
        self.bg2.desenhar_objeto(tela)
        self.aranha.desenhar_objeto(tela)
        self.flor.desenhar_objeto(tela)

    def atualizar_tela(self) -> None:

        self.mova_bg()
        self.aranha.anime("spider", 8, 4)
        self.flor.anime("florwer", 8, 2)
        self.mova_ahanhas()
        self.mova_flores()

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

    def mova_flores(self) -> None:

        self.flor.sprite.rect[1] += 5
        if self.flor.sprite.rect[1] >= 700:
            self.flor.sprite.kill()
            self.flor = Objeto_Cenario("assets/florwer1.png", randrange(0,300), -50)
