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

class Abelha(Objeto_Cenario):

    def __init__(self, caminho_img: str, pos_x: int, pos_y: int) -> None:
        super().__init__(caminho_img, pos_x, pos_y)

        pygame.mixer.init()
        self.som_pts = pygame.mixer.Sound("sounds/score.ogg") # sound -> musica curta | Music -> musica grande
        self.som_bateu = pygame.mixer.Sound("sounds/bateu.ogg")
        
        self.vidas = 3
        self.pontos = 0
        
    def mova_abelha(self, evento: pygame.event.Event) -> None:

        if evento.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - self.sprite.image.get_width()/2
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - self.sprite.image.get_height()/2

    def testar_colisao(self, grupo: pygame.sprite.Group, nome: str) -> None:

        nome = nome
        colidiu = pygame.sprite.spritecollide(self.sprite, grupo, True) 
        if nome == "flor" and colidiu:
            self.pontos += 1
            self.som_pts.play()
        elif nome == "aranha" and colidiu:
            self.vidas -= 1
            self.som_bateu.play()
 
class Texto:

    def __init__(self, tamanho_texto: int, texto: str) -> None:
        
        pygame.font.init()
        self.fonte = pygame.font.SysFont("Arial bold", tamanho_texto)
        self.render = self.fonte.render(texto, False, (255,255,255))

    def desenhar(self, tela: pygame.surface.Surface, x: int, y: int) -> None:
        
        tela.blit(self.render, (x,y))

    def atualizar(self, texto: str) -> None:

        self.render = self.fonte.render(texto, False, (255,255,255))
