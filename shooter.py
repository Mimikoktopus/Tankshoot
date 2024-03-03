#Import Blog
import pygame
import os
import pathlib
import math
import random
pygame.init()
os.chdir(pathlib.Path(__file__).parent.resolve())

#Variablen Blog
ORANGE     = ( 255, 140, 0)
ROT        = ( 255, 0, 0)
GRUEN      = ( 0, 255, 0)
SCHWARZ    = ( 0, 0, 0)
WEiSS      = ( 255, 255, 255)
BLAU       = ( 0, 0, 255)
GRAU       = ( 150, 150, 150)
infoObject = pygame.display.Info()
window     = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
PlayerX    = infoObject.current_w /2
PlayerY    = infoObject.current_h /2
PlayerR    = 0
Level      = 1
LevelF     = 5
Punkte     = 0
KugelX     = PlayerX
KugelY     = PlayerY
KugelXG    = 4
KugelYG    = 4
Highscore  = 0
Leben      = 100
Feinde     = []

#Bider, Sounds import
Fadenkreuz = pygame.image.load("Fadenkreuz.png")
Hintergrund= pygame.image.load("Hintergrund.jpg")
Soldat     = pygame.image.load("Panzer.png")
Gameover   = pygame.image.load("Gameover.jpg")
FeindB     = pygame.image.load("Feind.png")
Panzer     = pygame.image.load("PanzerUntersatz.png")
PanzerK    = pygame.image.load("PanzerKanonenturm.png")
Wonp       = pygame.image.load("win.jpg")
Schuss     = pygame.mixer.Sound("Schuss.mp3")
TodG       = pygame.mixer.Sound("TodG.mp3")
TodS       = pygame.mixer.Sound("TodS.mp3")
WonS       = pygame.mixer.Sound("WonS.mp3")
Music      = pygame.mixer.music.load("Music.mp3")
font       = pygame.font.SysFont(None, 50)

pygame.mixer.music.play(-1)
Hintergrund = pygame.transform.scale(Hintergrund,(infoObject.current_w, infoObject.current_h))
Gameover    = pygame.transform.scale(Gameover,(infoObject.current_w, infoObject.current_h))
Wonp        = pygame.transform.scale(Wonp,(infoObject.current_w, infoObject.current_h))


#Funktions Blog
def Feindreturn():
    global infoObject
    Seite  = random.randint(1,4)
    if Seite == 1:
        FeindY = -1000
        FeindX = random.randint(-1000,infoObject.current_w + 1000)
    if Seite == 2:
        FeindY = infoObject.current_w +1000
        FeindX = random.randint(-1000,infoObject.current_w + 1000)
    if Seite == 3:
        FeindX = -1000
        FeindY = random.randint(-1000,infoObject.current_h + 1000)
    if Seite == 4:
        FeindX = infoObject.current_h +1000
        FeindY = random.randint(-1000,infoObject.current_h + 1000)
    Feinde.append([FeindX, FeindY])
    if len(Feinde) < Level:
        Feindreturn()

clock = pygame.time.Clock()
pygame.display.set_caption("Pong")
66
pygame.mouse.set_visible(0)
Feindreturn()

spielaktiv = True
Kugelaktiv = False
GameoverS  = False
Win        = False
Esc        = False

while spielaktiv:
    if Esc == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                   spielaktiv = False
        MausP = pygame.mouse.get_pos()
        FadenkreuzP = pygame.Rect(MausP[0]-16, MausP[1]-16, 32, 32)
        window.blit(Fadenkreuz, FadenkreuzP)
        if Punkte > Highscore :
            Highscore = Punkte
        SpielerAText = font.render("Kills : " + str(Punkte), True, pygame.Color('white'))
        window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width(), 30))
        SpielerAText = font.render("Level : " + str(Level), True, pygame.Color('white'))
        window.blit(SpielerAText, (30 , 30))
        SpielerAText = font.render("Highscore : " + str(Highscore), True, pygame.Color('white'))
        window.blit(SpielerAText, (infoObject.current_w /2 -SpielerAText.get_width()/2, infoObject.current_h-100 -SpielerAText.get_height()/2))
        pygame.display.flip()
        clock.tick(60)
        window.blit(Wonp, pygame.Rect(0, 0, infoObject.current_h, infoObject.current_w))
        keys  = pygame.key.get_pressed()

    else:
        if Win == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    spielaktiv = False
            MausP = pygame.mouse.get_pos()
            FadenkreuzP = pygame.Rect(MausP[0]-16, MausP[1]-16, 32, 32)
            window.blit(Fadenkreuz, FadenkreuzP)
            if Punkte > Highscore :
                Highscore = Punkte
            SpielerAText = font.render("Kills : " + str(Punkte), True, pygame.Color('white'))
            window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width(), 30))
            SpielerAText = font.render("Level : " + str(Level), True, pygame.Color('white'))
            window.blit(SpielerAText, (30 , 30))
            SpielerAText = font.render("Highscore : " + str(Highscore), True, pygame.Color('white'))
            window.blit(SpielerAText, (infoObject.current_w /2 -SpielerAText.get_width()/2, infoObject.current_h-100 -SpielerAText.get_height()/2))
            pygame.display.flip()
            clock.tick(60)
            window.blit(Wonp, pygame.Rect(0, 0, infoObject.current_h, infoObject.current_w))
            keys  = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                spielaktiv = False 
            if keys[pygame.K_RETURN]:
                LevelF = Level*5
                Feinde = []
                Feindreturn()
                PlayerX = infoObject.current_w /2
                PlayerY = infoObject.current_h /2
                Win = False
                PlayerR = 0
                Leben   = 100
        else:
            if GameoverS == False:
                if LevelF <= 0:
                    pygame.mixer.Sound.play(WonS)
                    Level += 1
                    Win = True
                window.fill(GRAU)
                MausP = pygame.mouse.get_pos()
                window.blit(Hintergrund, pygame.Rect(0, 0, 32, 32))
                if Kugelaktiv:
                    pygame.draw.circle(window, (ORANGE), (KugelX, KugelY), 5)
                    KugelX  = KugelX + KugelXG
                    KugelY  = KugelY + KugelYG
                
                Soldatw =pygame.transform.rotate(Panzer, PlayerR)
                window.blit(Soldatw, (PlayerX - Soldatw.get_width()/2, PlayerY - Soldatw.get_height()/2))
                
                Px = MausP[0] - PlayerX
                Py = MausP[1] - PlayerY
                Soldatw2 = math.degrees (math.atan2 (-Py,Px))
                Soldatw =pygame.transform.rotate(PanzerK, Soldatw2)
                window.blit(Soldatw, (PlayerX - Soldatw.get_width()/2, PlayerY - Soldatw.get_height()/2))
                
                for Feind in Feinde:
                    Fx = PlayerX - Feind[0]
                    Fy = PlayerY - Feind[1]
                    Feindw2 = math.degrees (math.atan2 (-Fy,Fx))
                    Feindw =pygame.transform.rotate(FeindB, Feindw2)
                    window.blit(Feindw, (Feind[0] - FeindB.get_width()/2, Feind[1] - FeindB.get_height()/2))

                
                FadenkreuzP = pygame.Rect(MausP[0]-16, MausP[1]-16, 32, 32)
                window.blit(Fadenkreuz, FadenkreuzP)
                #rect = pygame.Rect(infoObject.current_w /4, infoObject.current_h /4, infoObject.current_w /2, 50)
                #pygame.draw.rect(window, (SCHWARZ), rect)
                SpielerAText = font.render("Kills : " + str(Punkte), True, pygame.Color('white'))
                window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width(), 30))
                SpielerAText = font.render("Level : " + str(Level), True, pygame.Color('white'))
                window.blit(SpielerAText, (30 , 30))
                rect = pygame.Rect(infoObject.current_w /2 - 200, 30, Leben*4, 30)
                pygame.draw.rect(window, (ROT), rect)
                SpielerAText = font.render("Health: "+ str(Leben), True, pygame.Color('white'))
                window.blit(SpielerAText, (infoObject.current_h -SpielerAText.get_width() , 30))
                pygame.display.flip()
                clock.tick(60)

                for Feind in Feinde:  
                    FeindX = Feind[0]
                    FeindY = Feind[1]
                    FeindXG = (FeindX-PlayerX)/100
                    FeindYG = (FeindY-PlayerY)/100  
                    divisor = abs(FeindXG)
                    if abs(FeindYG) > divisor:
                        divisor = abs(FeindYG)
                    FeindYG  = FeindYG/divisor
                    FeindXG  = FeindXG/divisor  
                    FeindYG  = FeindYG * -5
                    FeindXG  = FeindXG * -5
                    Feind[0]   = FeindX + FeindXG
                    Feind[1]   = FeindY + FeindYG
                    FeindXA = FeindX - PlayerX
                    FeindYA = FeindY - PlayerY
                    FeindA  = math.sqrt(FeindXA ** 2 + FeindYA ** 2)
                    if FeindA < 80:
                        Leben   -= 1      # Player Hitbox
                    if Leben <= 0:
                        GameoverS = True    
                        pygame.mixer.Sound.play(TodS)

                if Kugelaktiv :
                    for i in range(len(Feinde)):
                        Feind   = Feinde[i]   
                        FeindX  = Feind[0]
                        FeindY  = Feind[1]
                        FeindXA = FeindX - KugelX
                        FeindYA = FeindY - KugelY
                        FeindA  = math.sqrt(FeindXA ** 2 + FeindYA ** 2)
                        if FeindA < 35 :
                            del Feinde[i]
                            Feindreturn()   # Feind Hitbox
                            Punkte += 1
                            pygame.mixer.Sound.play(TodG)
                            LevelF -= 1
                            Kugelaktiv = False
                if KugelX < 0 :
                    Kugelaktiv = False
                if KugelY < 0 :
                    Kugelaktiv = False
                if KugelX > infoObject.current_w :
                    Kugelaktiv = False
                if KugelY > infoObject.current_h :
                    Kugelaktiv = False    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        spielaktiv = False 
                keys  = pygame.key.get_pressed()
                mouse = pygame.mouse.get_pressed()
                if keys[pygame.K_w]:
                    PlayerX += math.cos(math.radians(-PlayerR))*7
                    PlayerY += math.sin(math.radians(-PlayerR))*7
                if keys[pygame.K_s]:
                    PlayerX += math.cos(math.radians(-PlayerR))*-7
                    PlayerY += math.sin(math.radians(-PlayerR))*-7
                if keys[pygame.K_a]:
                    PlayerR = PlayerR +3
                if keys[pygame.K_d]:
                    PlayerR = PlayerR -3
                if keys[pygame.K_ESCAPE]:
                    spielaktiv = False
                if mouse[0] and (not Kugelaktiv):
                    Kugelaktiv = True
                    pygame.mixer.Sound.play(Schuss)
                    KugelX    = PlayerX
                    KugelY    = PlayerY
                    KugelXG = (MausP[0]-PlayerX)/100
                    KugelYG = (MausP[1]-PlayerY)/100  
                    divisor = abs(KugelXG)
                    if abs(KugelYG) > divisor:
                        divisor = abs(KugelYG)
                    KugelYG = KugelYG/divisor
                    KugelXG = KugelXG/divisor  
                    KugelYG = KugelYG * 10
                    KugelXG = KugelXG * 10 
                if PlayerX < 20 :
                    PlayerX = 20
                if PlayerY < 20 :
                    PlayerY = 20
                if PlayerX > infoObject.current_w -20 :
                    PlayerX = infoObject.current_w -20
                if PlayerY > infoObject.current_h -20 :
                    PlayerY = infoObject.current_h-20
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        spielaktiv = False
                MausP = pygame.mouse.get_pos()
                FadenkreuzP = pygame.Rect(MausP[0]-16, MausP[1]-16, 32, 32)
                window.blit(Fadenkreuz, FadenkreuzP)
                if Punkte > Highscore :
                    Highscore = Punkte
                SpielerAText = font.render("Kills : " + str(Punkte), True, pygame.Color('white'))
                window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width(), 30))
                SpielerAText = font.render("Level : " + str(Level), True, pygame.Color('white'))
                window.blit(SpielerAText, (30 , 30))
                SpielerAText = font.render("Highscore : " + str(Highscore), True, pygame.Color('white'))
                window.blit(SpielerAText, (infoObject.current_w /2 -SpielerAText.get_width()/2, infoObject.current_h/2 -SpielerAText.get_height()/2))
                pygame.display.flip()
                clock.tick(60)
                window.blit(Gameover, pygame.Rect(0, 0, infoObject.current_h, infoObject.current_w))
                Leben = 100
                keys  = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    spielaktiv = False 
                if keys[pygame.K_RETURN]:
                    Punkte    = 0
                    LevelF    = 5
                    Level     = 1
                    Feinde    = []
                    Feindreturn()
                    PlayerX   = infoObject.current_w /2
                    PlayerY   = infoObject.current_h /2
                    GameoverS = False
                    PlayerR   = 0