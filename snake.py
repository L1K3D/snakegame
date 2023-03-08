import pygame
import random
pygame.init()

###===VALORES DE CORES E DIMENSÕES DE DISPLAY=====###
verde = (34, 139, 34)
azul = (0, 0, 205)
castanho = (222, 184, 135)
vermelho = (255, 0, 0)

dimensoes = (600, 600)

###=====VALORES INICIAIS=====###
x = 300
y = 300

d = 20

lista_cobra = [[x, y]]

dx = 0
dy = 0

x_comida = round(random.randrange(0, 600 - d) / 20) * 20
y_comida = round(random.randrange(0, 600 - d) / 20) * 20

fontes = pygame.font.SysFont("EVOGRIA", 35)

###=====VALORES DE DISPLAY=====###
tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake Game')

tela.fill(verde)

clock = pygame.time.Clock()

###=====FUNÇÕES DE FUNCIONAMENTO=====###
def desenha_cobra(lista_cobra): #$#APARCEIMENTO DA COBRA NA TELA#$#
    tela.fill(verde)
    for unidade in lista_cobra:
        pygame.draw.rect(tela, azul, [unidade[0], unidade[1], d, d])

def mover_cobra(dx, dy, lista_cobra): #$#MOVIMENTAÇÃO DA COBRA#$#
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d
    
    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]

    return dx, dy, lista_cobra

def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra): #$#DEFINE A AREA DA COMIDA E SUA CONDIÇÃO DE APARECIMENTO#$#
    
    head = lista_cobra[-1]

    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])
        x_comida = round(random.randrange(0, 600 - d) / 20) * 20
        y_comida = round(random.randrange(0, 600 - d) / 20) * 20

    pygame.draw.rect(tela, castanho, [x_comida, y_comida, d, d])
    return x_comida, y_comida, lista_cobra

def verifica_parede(lista_cobra): #$#CASO A COBRA CHEGUE NA BORDA DA TELA, O JOGADOR PERDE#$#
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]
    
    if x not in range(600) or y not in range(600):
        raise Exception

def verifica_mordeu_cobra(lista_cobra): #$#CASO A COBRA PASSE POR CIMA DO PROPRIO CORPO, O JOGADOR PERDE#$#
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()

    del corpo[-1]
    for x, y in corpo:
        if x == head[0] and y == head[1]:
            raise Exception

def atualizar_pontos(lista_cobra):
    pts = str(len(lista_cobra))
    score = fontes.render("PTS: " + pts, True, vermelho)
    tela.blit(score, [0, 0])

###=====SISTEMA DE LOOP=====###
while True:
    pygame.display.update()
    desenha_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(dx, dy, x_comida, y_comida, lista_cobra)
    verifica_parede(lista_cobra)
    verifica_mordeu_cobra(lista_cobra)
    atualizar_pontos(lista_cobra)
    print(lista_cobra)
    clock.tick(12) #$#DEFINE A VELOCIDADE DA COBRA#$#