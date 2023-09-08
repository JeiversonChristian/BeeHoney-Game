import pygame
from objetos import Objeto_Cenario

class Game:

    def __init__(self) -> None:
        
        self.bg = Objeto_Cenario("assets/bg.png", 0, 0) # background
        self.bg2 = Objeto_Cenario("assets/bg.png", 0, -640)
        self.muda_cena = False
        self.aranha = Objeto_Cenario("assets/spider1.png", 200, 200)

    def desenhar(self, tela: pygame.surface.Surface) -> None:

        self.bg.grupo.draw(tela)
        self.bg2.grupo.draw(tela)
        self.aranha.grupo.draw(tela)

    def atualizar_tela(self) -> None:

        self.mova_bg()
        self.aranha.anime()

    def mova_bg(self) -> None:

        self.bg.sprite.rect[1] += 1
        self.bg2.sprite.rect[1] += 1
        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640
