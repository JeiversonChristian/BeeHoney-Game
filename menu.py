import pygame
from objetos import Objeto_Cenario

class Menu:

    def __init__(self, caminho_img: str) -> None:
        
        self.tela_start = Objeto_Cenario(caminho_img, 0, 0)
        self.muda_cena = False

    def desenhar(self, tela: pygame.surface.Surface) -> None:

        self.tela_start.grupo.draw(tela)

    def verificar_se_apertou_enter(self, evento: pygame.event.Event) -> None:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN: # Tecla Enter
                self.muda_cena = True

class GameOver(Menu):

    def __init__(self, caminho_img: str) -> None:
        super().__init__(caminho_img)
                