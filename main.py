import pygame
from objetos import Objeto_Cenario

class Principal:

    def __init__(self, tamanho_x: int, tamanho_y: int, titulo: str) -> None:
        
        self.tela = pygame.display.set_mode([tamanho_x, tamanho_y])
        self.titulo = pygame.display.set_caption(titulo)
        self.rodando_game = True
        self.tela_start = Objeto_Cenario("assets/start.png", 0, 0)

    def desenhar(self) -> None:
        
        pass

    def verificar_se_fecha(self) -> None:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando_game = False

    def atualizar_tela(self) -> None:

        while self.rodando_game == True:
            self.desenhar()
            self.verificar_se_fecha()
            pygame.display.update()

game = Principal(360, 640, "BeeHoney")
game.atualizar_tela()
