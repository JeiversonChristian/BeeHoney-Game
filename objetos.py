import pygame

class Objeto_Cenario:

    def __init__(self, caminho_img: str, pos_x: int, pos_y: int) -> None:
        
        self.grupo = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.grupo)
        self.sprite.imagem = pygame.image.load(caminho_img)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = pos_x
        self.sprite.rect[1] = pos_y

    def desenhar(self, tela: pygame.surface.Surface):
        
        self.grupo.draw(tela)