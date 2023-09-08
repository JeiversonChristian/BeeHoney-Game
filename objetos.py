import pygame

class Objeto_Cenario:

    def __init__(self, caminho_img: str, pos_x: int, pos_y: int) -> None:
        
        self.imagem = pygame.image.load(caminho_img)
        self.pos_x = pos_x
        self.pos_y = pos_y

    def desenhar(self, tela: pygame.surface.Surface):
        
        tela.blit(self.imagem, self.pos_x, self.pos_y)