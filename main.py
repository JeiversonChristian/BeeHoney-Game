import pygame
from menu import Menu, GameOver
from game import Game

class Principal:

    def __init__(self, tamanho_x: int, tamanho_y: int, titulo: str) -> None:

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/bg.ogg")
        pygame.mixer.music.play(-1) # -1 faz repetir a músia em looping
        
        self.tela = pygame.display.set_mode([tamanho_x, tamanho_y])
        self.titulo = pygame.display.set_caption(titulo)
        self.rodando_game = True
        self.menu = Menu("assets/start.png")
        self.game = Game()
        self.gameover = GameOver("assets/gameover.png")
        self.fps = pygame.time.Clock()

    def desenhar(self) -> None:
        
        self.tela.fill([0,0,0])
        if self.menu.muda_cena == False:
            self.menu.desenhar(self.tela)
        elif self.game.muda_cena == False:
            self.game.desenhar(self.tela)
            self.game.atualizar_tela()
        elif self.gameover.muda_cena == False:
            self.gameover.desenhar(self.tela)
        else:
            self.menu.muda_cena = False
            self.game.muda_cena = False
            self.gameover.muda_cena = False
            self.game.abelha.vidas = 3
            self.game.abelha.pontos = 0

    def verificar_se_fecha(self, evento: pygame.event.Event) -> None:

        if evento.type == pygame.QUIT:
            self.rodando_game = False

    def verificar_eventos(self) -> None:
        for evento in pygame.event.get():
            self.verificar_se_fecha(evento)
            if self.menu.muda_cena == False:
                self.menu.verificar_se_apertou_enter(evento)
            elif self.game.muda_cena == False:
                self.game.abelha.mova_abelha(evento)
            else:
                self.gameover.verificar_se_apertou_enter(evento)

    def atualizar_tela(self) -> None:

        while self.rodando_game == True:
            self.fps.tick(30)
            self.desenhar()
            self.verificar_eventos()
            pygame.display.update()

game = Principal(360, 640, "BeeHoney")
game.atualizar_tela()
