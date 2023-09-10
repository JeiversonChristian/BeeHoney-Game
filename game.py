import pygame
from objetos import Objeto_Cenario, Abelha, Texto
from random import randrange

class Game:

    def __init__(self) -> None:
        
        self.bg = Objeto_Cenario("assets/bg.png", 0, 0) # background
        self.bg2 = Objeto_Cenario("assets/bg.png", 0, -640)
        self.muda_cena = False
        self.aranha = Objeto_Cenario("assets/spider1.png", randrange(0,300), -50)
        self.flor = Objeto_Cenario("assets/florwer1.png", randrange(0,300), -50)
        self.abelha = Abelha("assets/bee1.png", 150, 600)
        self.texto_pontuacao = Texto(120, "0")
        self.texto_vidas = Texto(60, "3")

    def desenhar(self, tela: pygame.surface.Surface) -> None:

        self.bg.desenhar_objeto(tela)
        self.bg2.desenhar_objeto(tela)
        self.aranha.desenhar_objeto(tela)
        self.flor.desenhar_objeto(tela)
        self.abelha.desenhar_objeto(tela)
        self.texto_pontuacao.desenhar(tela,160,50)
        self.texto_vidas.desenhar(tela,50,50)

    def atualizar_tela(self) -> None:

        self.mova_bg()
        self.aranha.anime("spider", 8, 4)
        self.mova_ahanhas()
        self.flor.anime("florwer", 8, 2)
        self.mova_flores()
        self.abelha.anime("bee", 2, 4)
        self.abelha.testar_colisao(self.aranha.grupo, "aranha")
        self.abelha.testar_colisao(self.flor.grupo, "flor") 
        self.game_over()
        self.texto_pontuacao.atualizar(str(self.abelha.pontos)) 
        self.texto_vidas.atualizar(str(self.abelha.vidas))   
        
    def mova_bg(self) -> None:

        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4
        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def mova_ahanhas(self) -> None:

        self.aranha.sprite.rect[1] += 10
        if self.aranha.sprite.rect[1] >= 700:
            self.aranha.sprite.kill()
            self.aranha = Objeto_Cenario("assets/spider1.png", randrange(0,300), -50)

    def mova_flores(self) -> None:

        self.flor.sprite.rect[1] += 5
        if self.flor.sprite.rect[1] >= 700:
            self.flor.sprite.kill()
            self.flor = Objeto_Cenario("assets/florwer1.png", randrange(0,300), -50)

    def game_over(self) -> None:
        if self.abelha.vidas <= 0:
            self.muda_cena = True
