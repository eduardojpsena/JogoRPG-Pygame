import pygame, sys, random
from time import sleep

##>>>>>>INICIALIZADOR<<<<<<##
pygame.init()
pygame.font.init()

##>>>>>>VARiÁVEIS<<<<<<##
##Screnn
largura = 800
altura = 600
tela = 0
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Monarch of Gods")
##Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
fundo = (0, 0, 0)
##Posição personagem
x = 385
y = 550
##Vida
lifepersonagem = 50
liferainha = 200
lifetouro = 50

##>>>>>>CARREGAMENTO DE IMAGENS<<<<<<##
##Personagem MC
charright = ['imagens/charprincipal/direita/direita0.png', 'imagens/charprincipal/direita/direita1.png',
             'imagens/charprincipal/direita/direita2.png', 'imagens/charprincipal/direita/direita3.png',
             'imagens/charprincipal/direita/direita4.png', 'imagens/charprincipal/direita/direita5.png',
             'imagens/charprincipal/direita/direita6.png', 'imagens/charprincipal/direita/direita7.png',
             ]
charleft = ['imagens/charprincipal/esquerda/esquerda0.png', 'imagens/charprincipal/esquerda/esquerda1.png',
            'imagens/charprincipal/esquerda/esquerda2.png', 'imagens/charprincipal/esquerda/esquerda3.png',
            'imagens/charprincipal/esquerda/esquerda4.png', 'imagens/charprincipal/esquerda/esquerda5.png',
            'imagens/charprincipal/esquerda/esquerda6.png', 'imagens/charprincipal/esquerda/esquerda7.png',
            ]
chardown = ['imagens/charprincipal/frente/frente0.png', 'imagens/charprincipal/frente/frente1.png',
            'imagens/charprincipal/frente/frente2.png', 'imagens/charprincipal/frente/frente3.png',
            'imagens/charprincipal/frente/frente4.png', 'imagens/charprincipal/frente/frente5.png',
            'imagens/charprincipal/frente/frente6.png', 'imagens/charprincipal/frente/frente7.png',
            ]
charup = ['imagens/charprincipal/tras/tras0.png', 'imagens/charprincipal/tras/tras1.png',
          'imagens/charprincipal/tras/tras2.png', 'imagens/charprincipal/tras/tras3.png',
          'imagens/charprincipal/tras/tras4.png', 'imagens/charprincipal/tras/tras5.png',
          'imagens/charprincipal/tras/tras6.png', 'imagens/charprincipal/tras/tras7.png',
          ]
person = pygame.image.load(chardown[0]).convert_alpha()

##Inimigo Rainha
enemirainhaup = ['imagens/EnemiRainha/cima1.png', 'imagens/EnemiRainha/cima2.png',
                 'imagens/EnemiRainha/cima3.png', 'imagens/EnemiRainha/cima4.png',
                 'imagens/EnemiRainha/cima5.png', 'imagens/EnemiRainha/cima6.png',
                 'imagens/EnemiRainha/cima7.png', 'imagens/EnemiRainha/cima8.png',
                 ]
enemirainhadown = ['imagens/EnemiRainha/frente1.png', 'imagens/EnemiRainha/frente2.png',
                   'imagens/EnemiRainha/frente3.png', 'imagens/EnemiRainha/frente4.png',
                   'imagens/EnemiRainha/frente5.png', 'imagens/EnemiRainha/frente6.png',
                   'imagens/EnemiRainha/frente7.png', 'imagens/EnemiRainha/frente8.png',
                   ]
enemirainharight = ['imagens/EnemiRainha/direita1.png', 'imagens/EnemiRainha/direita2.png',
                    'imagens/EnemiRainha/direita3.png', 'imagens/EnemiRainha/direita4.png',
                    'imagens/EnemiRainha/direita5.png', 'imagens/EnemiRainha/direita6.png',
                    'imagens/EnemiRainha/direita7.png', 'imagens/EnemiRainha/direita8.png',
                    ]
enemirainhaleft = ['imagens/EnemiRainha/esquerda1.png', 'imagens/EnemiRainha/esquerda2.png',
                   'imagens/EnemiRainha/esquerda3.png', 'imagens/EnemiRainha/esquerda4.png',
                   'imagens/EnemiRainha/esquerda5.png', 'imagens/EnemiRainha/esquerda6.png',
                   'imagens/EnemiRainha/esquerda7.png', 'imagens/EnemiRainha/esquerda8.png',
                   ]
enemirainha = pygame.image.load(enemirainhadown[0]).convert_alpha()

##Inimigo Touro
enemietouright = ['imagens/EnemiTouro/Dir1.png', 'imagens/EnemiTouro/Dir2.png',
                  'imagens/EnemiTouro/Dir3.png', 'imagens/EnemiTouro/Dir4.png',
                  'imagens/EnemiTouro/Dir1.png', 'imagens/EnemiTouro/Dir2.png',
                  'imagens/EnemiTouro/Dir3.png', 'imagens/EnemiTouro/Dir4.png'
                  ]
enemietouleft = ['imagens/EnemiTouro/Esq1.png', 'imagens/EnemiTouro/Esq2.png',
                 'imagens/EnemiTouro/Esq3.png', 'imagens/EnemiTouro/Esq4.png',
                 'imagens/EnemiTouro/Esq1.png', 'imagens/EnemiTouro/Esq2.png',
                 'imagens/EnemiTouro/Esq3.png', 'imagens/EnemiTouro/Esq4.png'
                 ]
enemitouro = pygame.image.load(enemietouright[0]).convert_alpha()

##Inimigo Dragão
enemidrag = ['imagens/EnemiDrag/parado.png','imagens/EnemiDrag/parado.png',
             'imagens/EnemiDrag/frente1.png', 'imagens/EnemiDrag/frente1.png',
             'imagens/EnemiDrag/frente2.png', 'imagens/EnemiDrag/frente2.png',
             'imagens/EnemiDrag/frente3.png', 'imagens/EnemiDrag/frente3.png']
enemidragao = pygame.image.load(enemidrag[0]).convert_alpha()

##NPCs
npccastelo = ['imagens/NPC/npc1.png', 'imagens/NPC/npc2.png', 'imagens/NPC/npc3.png',
              'imagens/NPC/npc4.png', 'imagens/NPC/npc5.png', 'imagens/NPC/npc6.png',
              'imagens/NPC/npc7.png']
npcsc1 = pygame.image.load(npccastelo[0]).convert_alpha()
npcsc2 = pygame.image.load(npccastelo[1]).convert_alpha()
npcsc3 = pygame.image.load(npccastelo[2]).convert_alpha()
npcsc4 = pygame.image.load(npccastelo[3]).convert_alpha()
npcsc5 = pygame.image.load(npccastelo[4]).convert_alpha()
npcsc6 = pygame.image.load(npccastelo[5]).convert_alpha()
npcsc7 = pygame.image.load(npccastelo[6]).convert_alpha()
npcaleatorio1 = pygame.image.load('imagens/NPC/npcfora1/parado.png').convert_alpha()
npcaleatorio2 = pygame.image.load('imagens/NPC/npcfora2/parado.png').convert_alpha()
npccavaleiro = pygame.image.load('imagens/NPC/npccavaleiro/parado.png').convert_alpha()
npcfreira = pygame.image.load('imagens/NPC/npcfreira/parado.png').convert_alpha()
npcpadre = pygame.image.load('imagens/NPC/npcpadre/parado.png').convert_alpha()

##Ataques Personagem
boladefogo = ['imagens/magia/boladefogo.png']
fogosagrado = ['imagens/magia/fogosagrado.png']
magia = pygame.image.load(boladefogo[0]).convert_alpha()

##Ataques Inimigos
magiarainha = pygame.image.load('imagens/magia/magiarainha.png').convert_alpha()
ataquetouro = pygame.image.load('imagens/magia/ataquetouro.png').convert_alpha()

##Background
bgmenu = pygame.image.load("imagens/mapas/menuselecao.png").convert()
bgseta = pygame.image.load("imagens/mapas/menuseta.png").convert_alpha()
bghistoria = pygame.image.load("imagens/mapas/bghistoria.png").convert()
bgcastelo = pygame.image.load("imagens/mapas/dentrocastelo.png").convert()
bgcidade1 = pygame.image.load("imagens/mapas/mapacidadetop.png").convert()
bgcidade2 = pygame.image.load("imagens/mapas/mapacidadedown.png").convert()
bgmundo = pygame.image.load("imagens/mapas/mundo.png").convert()
bgcastelorainha = pygame.image.load("imagens/mapas/castelorainha.png").convert()
bgendgame = pygame.image.load("imagens/mapas/endgame.png").convert()
bggameover = pygame.image.load("imagens/mapas/gameover.png").convert()
##Caixa de Texto (Pergaminho topo)
caixadetexto = pygame.image.load('imagens/mapas/pergaminhomsg.png').convert_alpha()
textx = 100; texty = 100
fonte = pygame.font.SysFont(("Harrington"), 15, bold=1)
text = fonte.render('', 1, black)
text2 = fonte.render('', 1, black)

##Itens
armadurasagrada = pygame.image.load('imagens/itens/armaduradivina.png').convert_alpha()
cajadosagrado = pygame.image.load('imagens/itens/cajadosagrado.png').convert_alpha()
iconecajado = pygame.image.load('imagens/itens/cajadosagradoitem.png').convert_alpha()
itemchar = []

##>>>>>>FUNÇÕES<<<<<<##
##Funcao Andar
andar = -1
def walk():
    global andar
    andar += 1
    if andar < 8:
        return andar
    else:
        andar = 0
        return andar

##Função area travada
def areatrav(topx, topy, rightx, righty, passos):
    global x; global y;

    if x == (topx) and (topy) <= y <= (righty):
        x -= passos
    if y == (righty) and (topx) <= x <= (rightx):
        y += passos
    if x == (rightx) and (topy) <= y <= (righty):
        x += passos
    if y == (topy) and (topx) <= x <= (rightx):
        y -= passos
    return

##Classe projetil
class projetil(object):
    def __init__(self, x, y, radius, facing, ataque):
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = facing
        self.ataque = ataque
        self.velocidade = 10 * facing

    def draw(self, screen):
        screen.blit(self.ataque, (int(self.x), int(self.y)))
        pygame.display.update()

## Tela 0 = menu
##Musica de fundo
if tela == 0:
    pygame.mixer.music.load('musicas/menu.mp3')
    pygame.mixer.music.play(-1)

setax = 260
setay = 435

while tela == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
##Chamando a tela
    screen.blit(bgmenu, (0, 0))
    screen.blit(bgseta, pygame.rect.Rect(setax, setay, 0, 0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        setay = 495
    if pressed[pygame.K_UP]:
        setay = 435
        bgmenu = pygame.image.load("imagens/mapas/menuselecao.png").convert()
        pygame.display.update()
    if pressed[pygame.K_RETURN]:
##Chamando nova tela
        if setay == 435:
            pygame.time.delay(100)
            tela = 1
        if setay == 495:
            bgmenu = pygame.image.load("imagens/mapas/creditos.png").convert_alpha()
            pygame.display.update()
##Atualização display e delay
    pygame.display.update()
    pygame.time.delay(50)

##Tela 1 = Historia

historiay = 440

while tela == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                tela = 2
##Chamando a tela
    screen.blit(bghistoria, (0, 0))
    pressed = pygame.key.get_pressed()

##Atualização display e delay
    pygame.display.update()
    pygame.time.delay(50)

##Tela 2 = Castelo reunião
#Musica de fundo
if tela == 2:
    pygame.mixer.music.load('musicas/caminhada.mp3')
    pygame.mixer.music.play(-1)

sleep(0.5)
c = 0
while tela == 2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                c += 1
##Chamando a Tela
    screen.blit(bgcastelo, (0, 0))  ##Background
    screen.blit(npcsc1, pygame.rect.Rect(385, 85, 0, 0))  ##NPC1
    screen.blit(npcsc2, pygame.rect.Rect(290, 200, 0, 0))  ##NPC2
    screen.blit(npcsc3, pygame.rect.Rect(290, 280, 0, 0))  ##NPC3
    screen.blit(npcsc4, pygame.rect.Rect(290, 350, 0, 0))  ##NPC4
    screen.blit(npcsc5, pygame.rect.Rect(490, 200, 0, 0))  ##NPC5
    screen.blit(npcsc6, pygame.rect.Rect(485, 280, 0, 0))  ##NPC6
    screen.blit(npcsc7, pygame.rect.Rect(490, 350, 0, 0))  ##NPC7
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem
    #screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
    #screen.blit(text, pygame.rect.Rect(textx, texty, 0, 0))  ##Texto NPCS
##Vida Personagem
    pygame.draw.rect(screen, red, [x - 10, y - 10, 50, 2], 4)
    lifeMC = pygame.draw.rect(screen, green, [x - 10, y - 10, lifepersonagem, 2], 4)

    ##Movimento personagem
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_s]:
        y += 4
        person = pygame.image.load(chardown[walk()]).convert_alpha()
    if pressed[pygame.K_w]:
        y -= 4
        person = pygame.image.load(charup[walk()]).convert_alpha()
    if pressed[pygame.K_d]:
        x += 4
        person = pygame.image.load(charright[walk()]).convert_alpha()
    if pressed[pygame.K_a]:
        x -= 4
        person = pygame.image.load(charleft[walk()]).convert_alpha()
##Conversa geral
    if c == 0:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Bradock: Meu Rei, Liante chegou!', 1, black)
        screen.blit(text, pygame.rect.Rect(250, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 1:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Bradock: Meu Rei, Liante chegou!', 1, black)
        screen.blit(text, pygame.rect.Rect(250, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 2:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Rei Prili: Vou direto ao assunto, chegou a hora...', 1, black)
        screen.blit(text, pygame.rect.Rect(250, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 3:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Rei Prili: Você deve partir agora e aproveitar a oportunidade...', 1, black)
        screen.blit(text, pygame.rect.Rect(250, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 4:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Liante: Preciso saber dos detalhes!', 1, black)
        screen.blit(text, pygame.rect.Rect(250, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 5:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Rei Prili: A Rainha Parasita moveu seu exercito para o reino espiritual', 1, black)
        screen.blit(text, pygame.rect.Rect(200, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 6:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Rei Prili: Nesse momento ela está sozinha no seu castelo...', 1, black)
        screen.blit(text, pygame.rect.Rect(250, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 7:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Liante: Pois bem, não vou perder essa oportunidade, partirei agora', 1, black)
        screen.blit(text, pygame.rect.Rect(210, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
##Conversa por aproximação
    if x == 409 and 80 < y < 90 or x == 385 and y == 98 or x == 361 and 80 < y < 90:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Rei Prili: Você deve tomar cuidado Liante.', 1, black)
        screen.blit(text, pygame.rect.Rect(210, 33, 0, 0))  ##Texto NPCS
    if x == 265 and y == 202 or x == 293 and y == 218:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Josuah: Você é nossa ultima esperança', 1, black)
        screen.blit(text, pygame.rect.Rect(210, 33, 0, 0))  ##Texto NPCS
    if x == 265 and y == 278 or x == 293 and y == 294:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Mathias: Os sete exercitos foram para o reino esperitual', 1, black)
        screen.blit(text, pygame.rect.Rect(210, 33, 0, 0))  ##Texto NPCS
    if x == 265 and y == 354 or x == 289 and y == 374:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Henry: Arranca a cabeça dessa maldita', 1, black)
        screen.blit(text, pygame.rect.Rect(210, 33, 0, 0))  ##Texto NPCS
    if x == 493 and y == 362 or x == 509 and y == 346:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Bradock: Se você vencer, podemos salvar o reino', 1, black)
        screen.blit(text, pygame.rect.Rect(210, 33, 0, 0))  ##Texto NPCS
    if x == 497 and y == 290 or 509 <= x < 513 and y == 278:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Malford: Você é o melhor mago do nosso reino', 1, black)
        screen.blit(text, pygame.rect.Rect(210, 33, 0, 0))  ##Texto NPCS
    if x == 493 and y == 218 or x == 509 and y == 206:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Jessy: Nossa estrela do Orgulho', 1, black)
        screen.blit(text, pygame.rect.Rect(210, 33, 0, 0))  ##Texto NPCS

    ##Areas travadas
    #Bordas
    if x < 32:
        x += 4
    if y < 0:
        y += 4
    if x > 750:
        x -= 4
    if y > 533 and x > 430 or y > 533 and x < 350:
        y -= 4
    #Objetos
    areatrav(297, 110, 477, 370, 4) #mesa
    areatrav(30, 2, 77, 42, 4) #estatuaup1
    areatrav(689, 2, 755, 46, 4) #estatuaup2
    areatrav(30, 466, 93, 540, 4) #estatuadown1
    areatrav(685, 470, 755, 540, 4) #estatuadown2
    areatrav(365, 42, 405, 94, 4) #Rei
    areatrav(269, 162, 305, 214, 4) #Npcs
    areatrav(269, 242, 305, 290, 4)
    areatrav(269, 318, 305, 370, 4)
    areatrav(465, 158, 505, 214, 4)
    areatrav(465, 242, 505, 286, 4)
    areatrav(465, 318, 505, 358, 4)
##Chamando nova tela
    if y > 565 and 350 < x < 430:
        tela = 3
##Atualização display e delay
    pygame.display.update()
    pygame.time.delay(50)
    #print(f'x={x} y={y}') #Coordenada personagem

##Tela 3 = Pátio Castelo top

x = 369; y = 189
sleep(0.5)
itemarm = 1
aparecerarm = 0
c = 0
while tela == 3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                c += 1
##Chamando a tela
    screen.blit(bgcidade1, (0, 0))  ##Background
    screen.blit(npcaleatorio1, pygame.rect.Rect(193, 413, 0, 0))
    screen.blit(npcaleatorio2, pygame.rect.Rect(589, 413, 0, 0))
    screen.blit(npcpadre, pygame.rect.Rect(373, 433, 0, 0))
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem
    if aparecerarm == 1:
        screen.blit(armadurasagrada, pygame.rect.Rect(50, 550, 0, 0))
        if len(itemchar) == 0:
            itemchar.append('ArmaduraSagrada')
            c = 2
##Vida Personagem
    pygame.draw.rect(screen, red, [x - 10, y - 10, 50, 2], 4)
    lifeMC = pygame.draw.rect(screen, green, [x - 10, y - 10, lifepersonagem, 2], 4)

##Movimento Personagem
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_s]:
        y += 4
        person = pygame.image.load(chardown[walk()]).convert_alpha()
    if pressed[pygame.K_w]:
        y -= 4
        person = pygame.image.load(charup[walk()]).convert_alpha()
    if pressed[pygame.K_d]:
        x += 4
        person = pygame.image.load(charright[walk()]).convert_alpha()
    if pressed[pygame.K_a]:
        x -= 4
        person = pygame.image.load(charleft[walk()]).convert_alpha()

##Conversa por aproximação
    if x == 217 and 392 < y < 430 or 190 < x < 204 and y == 433 or x == 173 and 392 < y < 430:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Cameron: Este armadura irá te ajudar nas batalhas, contem poder divino', 1, black)
        screen.blit(text, pygame.rect.Rect(190, 33, 0, 0))  ##Texto NPCS
        if itemarm == 1:
            itemarm -= 1
            aparecerarm += 1
    if x == 569 and 392 < y < 430 or 586 < x < 600 and y == 433 or x == 613 and 392 < y < 430:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Paul: Ouvi falar que A "Estrela da Avareza" foi para o reino espiritual', 1, black)
        screen.blit(text, pygame.rect.Rect(200, 33, 0, 0))  ##Texto NPCS
    if x == 365 and 445 < y < 450 or x == 405 and 445 < y < 450:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Padre Gabriel: Gula vai te ajudar nessa batalha', 1, black)
        screen.blit(text, pygame.rect.Rect(210, 33, 0, 0))  ##Texto NPCS
##Mensagem automatica
    if c == 2:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 300, 0, 0))  ##Caixa de texto
        text = fonte.render('ARMADURA SAGRADA ADQUIRIDA', 1, black)
        screen.blit(text, pygame.rect.Rect(300, 320, 0, 0))
        text2 = fonte.render('Efeito: Reduz dano sofrido                 enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(300, 340, 0, 0))
##Areas travadas
    #Bordas
    if x < 32:
        x += 4
    if y < 0:
        y += 4
    if x > 750:
        x -= 4
    #Objetos
    areatrav(180, 81, 261, 169, 4) #Torres
    areatrav(501, 81, 585, 169, 4)
    areatrav(213, 0, 345, 157, 4) #Castelo
    areatrav(405, 0, 537, 157, 4)
    areatrav(105, 0, 669, 57, 4)  #Muros
    areatrav(41, 29, 85, 185, 4)
    areatrav(685, 37, 725, 181, 4)
    areatrav(105, 193, 337, 249, 4)
    areatrav(409, 193, 669, 245, 4)
    areatrav(30, 0, 97, 77, 4) #Torres
    areatrav(665, 0, 745, 81, 4)
    areatrav(30, 173, 105, 273, 4)
    areatrav(669, 177, 749, 273, 4)
    areatrav(30, 229, 129, 313, 4) #Arvores
    areatrav(669, 253, 749, 350, 4)
    areatrav(89, 257, 269, 389, 4) #Barraca
    areatrav(501, 257, 685, 389, 4)
    areatrav(105, 0, 669, 57, 4) #Muros
    areatrav(41, 29, 85, 185, 4)
    areatrav(685, 37, 725, 181, 4)
    areatrav(117, 193, 337, 249, 4)
    areatrav(409, 193, 669, 245, 4)
    areatrav(265, 453, 509, 600, 4) #Monumento
    areatrav(693, 465, 752, 600, 4) #Arvores
    areatrav(30, 453, 89, 600, 4)
    areatrav(340, 61, 405, 125, 4)
    areatrav(177, 390, 213, 429, 4)
    areatrav(573, 390, 609, 429, 4)
    areatrav(369, 397, 401, 459, 4)

##Chamando nova tela
    if y > 560 and 85 < x < 269 or y > 560 and 489 < x < 693:
        tela = 4
##Atualização display e delay
    pygame.display.update()
    pygame.time.delay(50)
    #print(f'x={x} y={y}') #Coordenada personagem

##Tela 4 = Pátio Castelo down

x = 385; y = 53
sleep(0.5)

while tela == 4:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
##Chamando a tela
    screen.blit(bgcidade2, (0, 0))  ##Background
    screen.blit(npcfreira, pygame.rect.Rect(329, 177, 0, 0))  ##Freira
    screen.blit(npccavaleiro, pygame.rect.Rect(445, 421, 0, 0))  ##Estrela da Inveja
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem
    if 'ArmaduraSagrada' in itemchar:
        screen.blit(armadurasagrada, pygame.rect.Rect(50, 550, 0, 0))

##Vida Personagem
    pygame.draw.rect(screen, red, [x - 10, y - 10, 50, 2], 4)
    lifeMC = pygame.draw.rect(screen, green, [x - 10, y - 10, 50, 2], 4)

##Movimento Personagem
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_s]:
        y += 4
        person = pygame.image.load(chardown[walk()]).convert_alpha()
    if pressed[pygame.K_w]:
        y -= 4
        person = pygame.image.load(charup[walk()]).convert_alpha()
    if pressed[pygame.K_d]:
        x += 4
        person = pygame.image.load(charright[walk()]).convert_alpha()
    if pressed[pygame.K_a]:
        x -= 4
        person = pygame.image.load(charleft[walk()]).convert_alpha()
##Conversa por aproximação
    if x == 313 and 177 < y < 197 or 326 < x < 340 and y == 205 or x == 361 and 177 < y < 197:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Yanna: Estarei rezando por você', 1, black)
        screen.blit(text, pygame.rect.Rect(200, 33, 0, 0))  ##Texto NPCS
    if x == 437 and 405 < y < 437 or 455 < x < 467 and y == 453 or x == 473 and 405 < y < 437:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Estrela da Inveja: Também estou indo ao reino espiritual, tenha cuidado', 1, black)
        screen.blit(text, pygame.rect.Rect(200, 33, 0, 0))  ##Texto NPCS

##Areas travadas
    #Bordas
    if x < 32:
        x += 4
    if y < 0:
        y += 4
    if x > 750:
        x -= 4
    if y > 533 and x > 430 or y > 533 and x < 350:
        y -= 4
    #Objetos
    areatrav(30, 0, 85, 81, 4) #Arvores
    areatrav(689, 0, 755, 61, 4)
    areatrav(269, 0, 498, 33, 4) #Monumento
    areatrav(30, 129, 201, 169, 4) #Casas esquerda
    areatrav(30, 181, 201, 221, 4)
    areatrav(30, 225, 201, 265, 4)
    areatrav(30, 281, 201, 317, 4)
    areatrav(30, 329, 201, 261, 4)
    areatrav(30, 373, 201, 413, 4)
    areatrav(569, 129, 755, 169, 4) #Casas direita
    areatrav(569, 181, 755, 221, 4)
    areatrav(569, 225, 755, 265, 4)
    areatrav(569, 281, 755, 317, 4)
    areatrav(569, 329, 755, 261, 4)
    areatrav(569, 373, 755, 413, 4)
    areatrav(317, 141, 357, 201, 4)
    areatrav(441, 385, 469, 449, 4)
##Chamando nova tela
    if y > 565 and 350 < x < 430:
        tela = 5
##Atualização display e delay
    pygame.display.update()
    pygame.time.delay(50)
    #print(f'x={x} y={y}') #Coordenada personagem

# Tela 5 = Mundo
##Musica de fundo
if tela == 5:
    pygame.mixer.music.load('musicas/mundoaberto.mp3')
    pygame.mixer.music.play(-1)

x = 617; y = 473
sleep(0.5)

while tela == 5:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
##Chamando a tela
    screen.blit(bgmundo, (0, 0))  ##Background
    screen.blit(enemidragao, pygame.rect.Rect(197, 149, 0, 0))  ##Dragão
    screen.blit(npccavaleiro, pygame.rect.Rect(509, 265, 0, 0))  ##Estrela da inveja
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem
    if 'ArmaduraSagrada' in itemchar:
        screen.blit(armadurasagrada, pygame.rect.Rect(50, 550, 0, 0))
##Vida Personagem
    pygame.draw.rect(screen, red, [x - 10, y - 10, 50, 2], 4)
    lifeMC = pygame.draw.rect(screen, green, [x - 10, y - 10, 50, 2], 4)

##Movimento Personagem
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_s]:
        y += 4
        person = pygame.image.load(chardown[walk()]).convert_alpha()
    if pressed[pygame.K_w]:
        y -= 4
        person = pygame.image.load(charup[walk()]).convert_alpha()
    if pressed[pygame.K_d]:
        x += 4
        person = pygame.image.load(charright[walk()]).convert_alpha()
    if pressed[pygame.K_a]:
        x -= 4
        person = pygame.image.load(charleft[walk()]).convert_alpha()

##Conversa por aproximação
    if x == 497 and 257 < y < 285 or 509 < x < 529 and y == 297 or x == 541 and 261 < y < 289:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Estrela da Inveja: Você deve matar o guarda Minotauro e pegar o cajado', 1, black)
        screen.blit(text, pygame.rect.Rect(190, 28, 0, 0))  ##Texto NPCS
        text2 = fonte.render('sagrado para derrotar a rainha, é a única maneira de ferir ela de verdade.', 1, black)
        screen.blit(text2, pygame.rect.Rect(190, 40, 0, 0))  ##Texto NPCS
    if tela == 5:
        enemidragao = pygame.image.load(enemidrag[walk()]).convert_alpha()

    ##Areas travadas
    #Bordas
    if x < 10:
        x += 4
    if y < 0:
        y += 4
    if x > 760:
        x -= 4
    if y > 550:
        y -= 4
    #Objetos
    areatrav(0, 125, 97, 197, 4) #Rios
    areatrav(77, 85, 129, 241, 4)
    areatrav(125, 241, 249, 309, 4)
    areatrav(141, 305, 217, 421, 4)
    areatrav(215, 420, 289, 497, 4)
    areatrav(285, 495, 373, 561, 4)
    areatrav(637, 61, 760, 193, 4)
    areatrav(161, 0, 509, 45, 4)
    areatrav(429, 0, 593, 81, 4)
    areatrav(653, 0, 760, 77, 4)
    areatrav(533, 357, 760, 413, 4) #Pedras
    areatrav(405, 489, 760, 550, 4)
    areatrav(341, 421, 465, 501, 4)
    areatrav(197, 125, 309, 181, 4) #Dragão
    areatrav(501, 229, 537, 293, 4) #Estrela da inveja
##Chamando nova tela
    if y < 21 and 597 < x < 649:
        tela = 6
##Atualização display e delay
    pygame.display.update()
    pygame.time.delay(50)
    #print(f'x={x} y={y}') #Coordenada personagem

# Tela 6 = Castelo Rainha
##Musica de fundo
if tela == 6:
    pygame.mixer.music.load('musicas/batalhafinal.mp3')
    pygame.mixer.music.play(-1)
##Posição MC
x = 385; y = 540
##Posição Rainha
xrainha = 400
yrainha = 65
rainhacimay = 70
rainhacimax = 200
rainhabaixox = 600
rainhabaixoy = 150

##Posição Touro
xtouro = 600
ytouro = 270
tourocimax = 100
tourocimay = 270
tourobaixox = 700
tourobaixoy = 275

sleep(0.5)
c = 0
bullets = []
bulletsrainha = []
bulletstouro = []
composition = ['personagem', 'rainha', 'touro']
aparecercaj = 0
danomagia = 2
danoinimigo = 20
while tela == 6:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                c += 1
    pygame.display.update()
##Chamando a tela
    quadradorainha = pygame.draw.rect(screen, white, [xrainha, yrainha, 36, 47], 1)
    quadradotouro = pygame.draw.rect(screen, white, [xtouro + 5, ytouro, 42, 47], 1)
    quadradopersonagem = pygame.draw.rect(screen, white, [x, y, 33, 47], 1)
    screen.blit(bgcastelorainha, (0, 0))  ##Background
    if 'rainha' in composition:
        screen.blit(enemirainha, pygame.rect.Rect(xrainha, yrainha, 0, 0))
        pygame.draw.rect(screen, red, [300, 20, 200, 20])
        life = pygame.draw.rect(screen, green, [300, 20, liferainha, 20])
    if 'touro' in composition:
        screen.blit(enemitouro, pygame.rect.Rect(xtouro, ytouro, 0, 0))
        pygame.draw.rect(screen, red, [xtouro - 10, ytouro - 10, 50, 2], 4)
        life2 = pygame.draw.rect(screen, green, [xtouro - 10, ytouro - 10, lifetouro, 2], 4)
        if lifetouro <= 0:
            composition.remove('touro')
    if 'personagem' in composition:
        screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem
        pygame.draw.rect(screen, red, [x - 10, y - 10, 50, 2], 4)
        lifeMC = pygame.draw.rect(screen, green, [x - 10, y - 10, lifepersonagem, 2], 4)
##Chamar itens e aparecer drop
    if 'ArmaduraSagrada' in itemchar:
        screen.blit(armadurasagrada, pygame.rect.Rect(40, 550, 0, 0))
        danoinimigo = 10
    if 'touro' not in composition:
        xcaj = xtouro
        ycaj = ytouro
        screen.blit(cajadosagrado, pygame.rect.Rect(xcaj, ycaj, 0, 0))
        if (xcaj + 30) >= x >= xcaj and (ycaj + 30) >= y >= ycaj and 'CajadoSagrado' not in itemchar:
            itemchar.append('CajadoSagrado')
            aparecercaj += 1
            c = 10
    if aparecercaj == 1:
        cajadosagrado = pygame.image.load('imagens/mapas/setavazio.png').convert_alpha()
        screen.blit(iconecajado, pygame.rect.Rect(73, 550, 0, 0))
        magia = pygame.image.load(fogosagrado[0]).convert_alpha()
        danomagia = 15
##Movimento Personagem
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_s]:
        y += 6
        person = pygame.image.load(chardown[walk()]).convert_alpha()
    if pressed[pygame.K_w]:
        y -= 6
        person = pygame.image.load(charup[walk()]).convert_alpha()
    if pressed[pygame.K_d]:
        x += 6
        person = pygame.image.load(charright[walk()]).convert_alpha()
    if pressed[pygame.K_a]:
        x -= 6
        person = pygame.image.load(charleft[walk()]).convert_alpha()
##Ataque personagem
    if pressed[pygame.K_SPACE]:
        if len(bullets) < 2:
            bullets.append(projetil(x, y, 6, -1.5, magia))
            sleep(0.1)
    for bullet in bullets:
        bullet.draw(screen)
        if bullet.y - bullet.radius < quadradorainha[1] + quadradorainha[3] and bullet.y - bullet.radius > quadradorainha[1]:
            if bullet.x + bullet.radius > quadradorainha[0] and bullet.x - bullet.radius < quadradorainha[0] + quadradorainha[2]:
                bullets.pop(bullets.index((bullet)))
                liferainha -= danomagia
        if 'touro' in composition:
            if bullet.y - bullet.radius < quadradotouro[1] + quadradotouro[3] and bullet.y - bullet.radius > quadradotouro[1]:
                if bullet.x + bullet.radius > quadradotouro[0] and bullet.x - bullet.radius < quadradotouro[0] + quadradotouro[2]:
                    bullets.pop(bullets.index((bullet)))
                    lifetouro -= 10
        if bullet.y < 600 and bullet.y > 0:
            bullet.y += bullet.velocidade
        else:
            bullets.pop(bullets.index(bullet))
        pygame.display.update()
##Ataque rainha
    if c >= 7 and 'rainha' in composition and not c == 10:
        if random.randint(0, 6) == 1:
            if len(bulletsrainha) < 4:
                bulletsrainha.append(projetil(xrainha+5, yrainha+10, 6, 1.2, magiarainha))
        for bulletr in bulletsrainha:
            bulletr.draw(screen)
            if bulletr.y - bulletr.radius < quadradopersonagem[1] + quadradopersonagem[3] and bulletr.y - bulletr.radius > quadradopersonagem[1]:
                if bulletr.x + bulletr.radius > quadradopersonagem[0] and bulletr.x - bulletr.radius < quadradopersonagem[0] + quadradopersonagem[2]:
                    bulletsrainha.pop(bulletsrainha.index((bulletr)))
                    lifepersonagem -= danoinimigo
            if bulletr.y < 600 and bulletr.y > 0:
                bulletr.y += bulletr.velocidade
            else:
                bulletsrainha.pop(bulletsrainha.index(bulletr))
##Ataque touro
    if c >= 7 and 'touro' in composition and not c == 10:
        if random.randint(0, 6) == 1:
            if len(bulletstouro) < 3:
                bulletstouro.append(projetil(xtouro+5, ytouro+10, 6, 1.2, ataquetouro))
        for bullett in bulletstouro:
            bullett.draw(screen)
            if bullett.y - bullett.radius < quadradopersonagem[1] + quadradopersonagem[3] and bullett.y - bullett.radius > quadradopersonagem[1]:
                if bullett.x + bullett.radius > quadradopersonagem[0] and bullett.x - bullett.radius < quadradopersonagem[0] + quadradopersonagem[2]:
                    bulletstouro.pop(bulletstouro.index((bullett)))
                    lifepersonagem -= danoinimigo
            if bullett.y < 600 and bullett.y > 0:
                bullett.y += bullett.velocidade
            else:
                bulletstouro.pop(bulletstouro.index(bullett))
            pygame.display.update()

##Conversa geral
    if c == 0:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('RainhaParasita: Humano maldito, você acha que pode me vencer?!', 1, black)
        screen.blit(text, pygame.rect.Rect(200, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 1:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('RainhaParasita: Humano maldito, você acha que pode me vencer?', 1, black)
        screen.blit(text, pygame.rect.Rect(200, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 2:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('RainhaParasita: Você não tem nenhuma chance...', 1, black)
        screen.blit(text, pygame.rect.Rect(190, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 3:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('RainhaParasita: Vou destruir toda sua raça.', 1, black)
        screen.blit(text, pygame.rect.Rect(200, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 4:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Liante: Seus dias de terror acabam aqui maldita...', 1, black)
        screen.blit(text, pygame.rect.Rect(200, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 5:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('Liante: Com o poder do Orgulho, irei te pulverizar.', 1, black)
        screen.blit(text, pygame.rect.Rect(200, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 6:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 0, 0, 0))  ##Caixa de texto
        text = fonte.render('RainhaParasita: Tente se puder.', 1, black)
        screen.blit(text, pygame.rect.Rect(200, 33, 0, 0))  ##Texto NPCS
        text2 = fonte.render('Enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(678, 52, 0, 0))  ##Texto NPCS
    if c == 10:
        screen.blit(caixadetexto, pygame.rect.Rect(0, 300, 0, 0))  ##Caixa de texto
        text = fonte.render('CAJADO SAGRADO ADQUIRIDO', 1, black)
        screen.blit(text, pygame.rect.Rect(300, 320, 0, 0))
        text2 = fonte.render('Efeito: Dano magico aumentado               enter...', 1, black)
        screen.blit(text2, pygame.rect.Rect(300, 340, 0, 0))
    if c >= 7 and not c == 10:
##Movimento Rainha
        if yrainha > rainhacimay and xrainha == rainhabaixox:
            pygame.display.update()
            yrainha -= 5
            enemirainha = pygame.image.load(enemirainhaup[walk()]).convert_alpha()
        elif yrainha == rainhacimay and xrainha > rainhacimax:
            pygame.display.update()
            xrainha -= 5
            enemirainha = pygame.image.load(enemirainhaleft[walk()]).convert_alpha()
        elif yrainha <= rainhabaixoy and xrainha < rainhabaixox:
            pygame.display.update()
            yrainha += 5
            enemirainha = pygame.image.load(enemirainhadown[walk()]).convert_alpha()
        elif yrainha > rainhabaixoy and xrainha >= rainhacimax:
            pygame.display.update()
            xrainha += 5
            enemirainha = pygame.image.load(enemirainharight[walk()]).convert_alpha()

##Movimento Touro
    if c >= 7 and 'touro' in composition:
        if ytouro > tourocimay and xtouro == tourobaixox:
            pygame.display.update()
            ytouro -= 4
            enemitouro = pygame.image.load(enemietouleft[walk()]).convert_alpha()
        elif ytouro == tourocimay and xtouro > tourocimax:
            pygame.display.update()
            xtouro -= 4
            enemitouro = pygame.image.load(enemietouleft[walk()]).convert_alpha()
        elif ytouro <= tourobaixoy and xtouro < tourobaixox:
            pygame.display.update()
            ytouro += 4
            enemitouro = pygame.image.load(enemietouright[walk()]).convert_alpha()
        elif ytouro > tourobaixoy and xtouro >= tourocimax:
            pygame.display.update()
            xtouro += 4
            enemitouro = pygame.image.load(enemietouright[walk()]).convert_alpha()

##Areas travadas
    #Bordas
    if x < 57:
        x += 6
    if y < 2:
        y += 6
    if x > 713:
        x -= 6
    if y > 550:
        y -= 6
    #Objetos
    areatrav(245, 1, 309, 44, 6) #Pilares
    areatrav(469, 1, 521, 44, 6)
    areatrav(55, 4, 161, 64, 6) #Gargulas
    areatrav(593, 4, 713, 68, 6)
    areatrav(89, 132, 137, 204, 6) #Buracos
    areatrav(89, 474, 141, 510, 6)
    areatrav(557, 444, 620, 516, 6)
    areatrav(617, 404, 697, 448, 6)

##Chamando nova tela
    if liferainha <= 0:
        tela = 'endgame'
    if lifepersonagem <= 0:
        tela = 'gameover'
##Atualização display e delay
    pygame.display.update()
    pygame.time.delay(40)
    #print(f'x={x} y={y}') #Coordenada personagem
##Musica de fundo
if tela == 'gameover' or tela == 'endgame':
    pygame.mixer.music.load('musicas/menu.mp3')
    pygame.mixer.music.play(-1)

while tela == 'gameover':
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                quit()
##Chamando a tela
    screen.blit(bggameover, (0, 0))
    pygame.display.update()
while tela == 'endgame':
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                quit()
##Chamando a tela
    screen.blit(bgendgame, (0, 0))
    pygame.display.update()
