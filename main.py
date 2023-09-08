import pygame
from objetos import Objeto_Cenario
from menu import Menu

class Principal:

    def __init__(self, tamanho_x: int, tamanho_y: int, titulo: str) -> None:
        
        self.tela = pygame.display.set_mode([tamanho_x, tamanho_y])
        self.titulo = pygame.display.set_caption(titulo)
        self.rodando_game = True
        self.menu = Menu()

    def desenhar(self) -> None:
        
        if self.menu.muda_cena == False:
            self.menu.desenhar(self.tela)

    def verificar_se_fecha(self, evento: pygame.event.Event) -> None:

        if evento.type == pygame.QUIT:
            self.rodando_game = False

    def eventos(self) -> None:
        for evento in pygame.event.get():
            self.verificar_se_fecha(evento)
            self.menu.verificar_se_apertou_enter(evento)

    def atualizar_tela(self) -> None:

        while self.rodando_game == True:
            self.desenhar()
            self.eventos()
            pygame.display.update()

game = Principal(360, 640, "BeeHoney")
game.atualizar_tela()
