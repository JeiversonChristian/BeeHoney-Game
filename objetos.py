import pygame

class Objeto_Cenario:

    def __init__(self, caminho_img: str, pos_x: int, pos_y: int) -> None:
        
        self.grupo = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.grupo)
        self.sprite.image = pygame.image.load(caminho_img)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = pos_x
        self.sprite.rect[1] = pos_y
        self.frame = 1
        self.tick = 0

    def desenhar_objeto(self, tela: pygame.surface.Surface) -> None:
        
        self.grupo.draw(tela)

    def anime(self, nome_imagem: str, tick_max: int, frame_max: int) -> None:
        self.tick += 1
        if self.tick >= tick_max:
            self.tick = 0
            self.frame += 1
        if self.frame > frame_max:
            self.frame = 1
        self.sprite.image = pygame.image.load("assets/"+nome_imagem+str(self.frame)+".png")
        