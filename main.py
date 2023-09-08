import pygame
from menu import Menu
from game import Game

class Principal:

    def __init__(self, tamanho_x: int, tamanho_y: int, titulo: str) -> None:
        
        self.tela = pygame.display.set_mode([tamanho_x, tamanho_y])
        self.titulo = pygame.display.set_caption(titulo)
        self.rodando_game = True
        self.menu = Menu()
        self.game = Game()
        self.fps = pygame.time.Clock()

    def desenhar(self) -> None:
        
        if self.menu.muda_cena == False:
            self.menu.desenhar(self.tela)
        elif self.game.muda_cena == False:
            self.game.desenhar(self.tela)
            self.game.atualizar_tela()

    def verificar_se_fecha(self, evento: pygame.event.Event) -> None:

        if evento.type == pygame.QUIT:
            self.rodando_game = False

    def verificar_eventos(self) -> None:
        for evento in pygame.event.get():
            self.verificar_se_fecha(evento)
            self.menu.verificar_se_apertou_enter(evento)
            self.game.abelha.mova_abelha(evento)

    def atualizar_tela(self) -> None:

        while self.rodando_game == True:
            self.fps.tick(30)
            self.desenhar()
            self.verificar_eventos()
            pygame.display.update()

game = Principal(360, 640, "BeeHoney")
game.atualizar_tela()
