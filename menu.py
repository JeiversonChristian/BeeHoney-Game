import pygame
from objetos import Objeto_Cenario

class Menu:

    def __init__(self) -> None:
        
        self.tela_start = Objeto_Cenario("assets/star.png", 0, 0)
        self.muda_cena = False

    def desenhar(self, tela: pygame.surface.Surface) -> None:

        self.tela_start.grupo.draw(tela)

    def verificar_se_apertou_tecla(self, evento: pygame.event.Event) -> None:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN: # Tecla Enter
                self.muda_cena = True