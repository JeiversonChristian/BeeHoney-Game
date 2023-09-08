import pygame
from objetos import Objeto_Cenario

class Game:

    def __init__(self) -> None:
        
        self.bg = Objeto_Cenario("assets/bg.png", 0, 0) # background
        self.muda_cena = False

    def desenhar(self, tela: pygame.surface.Surface) -> None:

        self.bg.grupo.draw(tela)

    def atualizar_tela(self) -> None:

        pass
