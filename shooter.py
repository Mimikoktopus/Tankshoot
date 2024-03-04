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
Waehrung   = 0
Feinde     = []
Skinan     = 1
SkinanK    = 1
Equipv     = 0
Equipv2    = 0
Equipv3    = 0

#Bider, Sounds import
Fadenkreuz  = pygame.image.load("Fadenkreuz.png")
Hintergrund = pygame.image.load("Hintergrund.jpg")
Soldat      = pygame.image.load("Panzer.png")
Gameover    = pygame.image.load("Gameover.jpg")
FeindB      = pygame.image.load("Feind.png")
Panzer1     = pygame.image.load("PanzerUntersatz.png")
PanzerK1    = pygame.image.load("PanzerKanonenturm.png")
Panzer2     = pygame.image.load("Panzer2.png")
PanzerK2    = pygame.image.load("Panzer2K.png")
Panzer3     = pygame.image.load("Panzer3.png")
PanzerK3    = pygame.image.load("Panzer3K.png")
Schliessen  = pygame.image.load("Quit.png")
Back        = pygame.image.load("Back.png")
Buy1        = pygame.image.load("Buy1.png")
Buy2        = pygame.image.load("Buy2.png")
Equip       = pygame.image.load("Equip.png")
Equiped     = pygame.image.load("Equiped.png")
Startb      = pygame.image.load("Start.png")
Skinb       = pygame.image.load("Skins.png")
Skin1       = pygame.image.load("T72Skin.png")
Skin2       = pygame.image.load("Panzer2Skin.png")
Skin3       = pygame.image.load("Panzer3Skin.png")
Wonp        = pygame.image.load("win.jpg")
Schuss      = pygame.mixer.Sound("Schuss.mp3")
TodG        = pygame.mixer.Sound("TodG.mp3")
TodS        = pygame.mixer.Sound("TodS.mp3")
WonS        = pygame.mixer.Sound("WonS.mp3")
Music       = pygame.mixer.music.load("Music.mp3")
font        = pygame.font.SysFont(None, 50)

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
Start      = True
Skin       = False
Skin2A     = False
Skin3A     = False

while spielaktiv:
    if Skinan == 1:
        Skina   = Panzer1
        Equipv  = Equiped
        Equipv2 = Equip
        Equipv3 = Equip
        SkinG   = 10
    if SkinanK == 1:
        SkinaK = PanzerK1
    if Skinan == 2:
        Skina   = Panzer2
        Equipv2 = Equiped
        Equipv  = Equip
        Equipv3 = Equip
        SkinG   = 15
    if SkinanK == 2:
        SkinaK = PanzerK2
    if Skinan == 3:
        Skina   = Panzer3
        Equipv3 = Equiped
        Equipv2 = Equip
        Equipv  = Equip
        SkinG   = 25
    if SkinanK == 3:
        SkinaK = PanzerK3
    
    if Skin == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spielaktiv = False
        window.blit(Back, (30, 80))
        window.blit(Equipv, (100, infoObject.current_h/2 +199 +30))
        window.blit(Skin1, (60, infoObject.current_h/2))
        window.blit(Skin2, (60 +411 +60, infoObject.current_h/2))
        window.blit(Skin3, (60 +411 +411 +80, infoObject.current_h/2))
        if Skin2A == False:
            window.blit(Buy1, (100 +411 +100, infoObject.current_h/2 +199 +40))
        else:
            window.blit(Equipv2, (100 +411 +100, infoObject.current_h/2 +199 +40))
        MausP = pygame.mouse.get_pos()
        FadenkreuzP = pygame.Rect(MausP[0]-16, MausP[1]-16, 32, 32)
        window.blit(Fadenkreuz, FadenkreuzP)
        if Punkte > Highscore :
            Highscore = Punkte
        SpielerAText = font.render("Kills : " + str(Punkte), True, pygame.Color('white'))
        window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width(), 30))
        SpielerAText = font.render("Level : " + str(Level), True, pygame.Color('white'))
        window.blit(SpielerAText, (30 , 30))
        SpielerAText = font.render("Coins : " + str(Waehrung), True, pygame.Color('white'))
        window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width() , 60))
        pygame.display.flip()
        clock.tick(60)
        window.blit(Hintergrund, pygame.Rect(0, 0, infoObject.current_h, infoObject.current_w))
        keys  = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if mouse[0] and MausP[0] > 30 :
            if MausP[0] < 30 + 330:
                if MausP[1] > 80 and MausP[1] < 80 +150:
                    Skin = False
        if mouse[0] and MausP[0] > 100 :
            if MausP[0] < 100 + 200:
                if MausP[1] > infoObject.current_h/2 +199 +30 and MausP[1] < infoObject.current_h/2 +199 +230:
                    Skinan  = 1
                    SkinanK = 1

        if Skin3A == False:
            if Waehrung >= 40:
                if mouse[0] and MausP[0] > 200+411 :
                    if MausP[0] < 611 + 127:
                        if MausP[1] > infoObject.current_h/2 +199 +40 and MausP[1] < infoObject.current_h/2 +199 +240:
                            Skin2A = True
                            Waehrung -= 20

        else:
            if mouse[0] and MausP[0] > 200+411 :
                if MausP[0] < 611 + 200:
                    if MausP[1] > infoObject.current_h/2 +199 +40 and MausP[1] < infoObject.current_h/2 +199 +240:
                        Skinan  = 2
                        SkinanK = 2
        if Skin2A == False:
            if Waehrung >= 20:
                if mouse[0] and MausP[0] > 200+411 :
                    if MausP[0] < 611 + 127:
                        if MausP[1] > infoObject.current_h/2 +199 +40 and MausP[1] < infoObject.current_h/2 +199 +240:
                            Skin2A = True
                            Waehrung -= 20

        else:
            if mouse[0] and MausP[0] > 200+411 :
                if MausP[0] < 611 + 200:
                    if MausP[1] > infoObject.current_h/2 +199 +40 and MausP[1] < infoObject.current_h/2 +199 +240:
                        Skinan  = 2
                        SkinanK = 2
    else:
        if Start == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    spielaktiv = False
            window.blit(Schliessen, (infoObject.current_w/2 -232, infoObject.current_h/4 ))
            window.blit(Startb, (infoObject.current_w/2 -165, infoObject.current_h/2 ))
            window.blit(Skinb, (infoObject.current_w/2 -145, infoObject.current_h/4*3 ))
            MausP = pygame.mouse.get_pos()
            FadenkreuzP = pygame.Rect(MausP[0]-16, MausP[1]-16, 32, 32)
            window.blit(Fadenkreuz, FadenkreuzP)
            if Punkte > Highscore :
                Highscore = Punkte
            SpielerAText = font.render("Kills : " + str(Punkte), True, pygame.Color('white'))
            window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width(), 30))
            SpielerAText = font.render("Level : " + str(Level), True, pygame.Color('white'))
            window.blit(SpielerAText, (30 , 30))
            SpielerAText = font.render("Coins : " + str(Waehrung), True, pygame.Color('white'))
            window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width() , 60))
            pygame.display.flip()
            clock.tick(60)
            window.blit(Hintergrund, pygame.Rect(0, 0, infoObject.current_h, infoObject.current_w))
            keys  = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pressed()
            if mouse[0] and MausP[0] > infoObject.current_w/2 - 230:
                if MausP[0] < infoObject.current_w/2 + 230:
                    if MausP[1] > infoObject.current_h/4 and MausP[1] < infoObject.current_h/4 +146:
                        spielaktiv = False
            if mouse[0] and MausP[0] > infoObject.current_w/2 - 165:
                if MausP[0] < infoObject.current_w/2 + 165:
                    if MausP[1] > infoObject.current_h/2 and MausP[1] < infoObject.current_h/2 +130:
                        Start = False
            if mouse[0] and MausP[0] > infoObject.current_w/2 - 145:
                if MausP[0] < infoObject.current_w/2 + 145:
                    if MausP[1] > infoObject.current_h/4*3 and MausP[1] < infoObject.current_h/4*3 +130:
                        Skin = True            
        else:
            if Esc == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        spielaktiv = False
                window.blit(Schliessen, (infoObject.current_w/2 -230, infoObject.current_h/4 ))
                window.blit(Back, (infoObject.current_w/2 -145, infoObject.current_h/2 ))
                window.blit(Skinb, (infoObject.current_w/2 -145, infoObject.current_h/4*3 ))
                MausP = pygame.mouse.get_pos()
                FadenkreuzP = pygame.Rect(MausP[0]-16, MausP[1]-16, 32, 32)
                window.blit(Fadenkreuz, FadenkreuzP)
                if Punkte > Highscore :
                    Highscore = Punkte
                SpielerAText = font.render("Kills : " + str(Punkte), True, pygame.Color('white'))
                window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width(), 30))
                SpielerAText = font.render("Level : " + str(Level), True, pygame.Color('white'))
                window.blit(SpielerAText, (30 , 30))
                SpielerAText = font.render("Coins : " + str(Waehrung), True, pygame.Color('white'))
                window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width() , 60))
                pygame.display.flip()
                clock.tick(60)
                window.blit(Hintergrund, pygame.Rect(0, 0, infoObject.current_h, infoObject.current_w))
                keys  = pygame.key.get_pressed()
                mouse = pygame.mouse.get_pressed()
                if mouse[0] and MausP[0] > infoObject.current_w/2 - 230:
                    if MausP[0] < infoObject.current_w/2 + 230:
                        if MausP[1] > infoObject.current_h/4 and MausP[1] < infoObject.current_h/4 +146:
                            spielaktiv = False
                if mouse[0] and MausP[0] > infoObject.current_w/2 - 165:
                    if MausP[0] < infoObject.current_w/2 + 165:
                        if MausP[1] > infoObject.current_h/2 and MausP[1] < infoObject.current_h/2 +150:
                            Esc = False
                if mouse[0] and MausP[0] > infoObject.current_w/2 - 145:
                    if MausP[0] < infoObject.current_w/2 + 145:
                        if MausP[1] > infoObject.current_h/4*3 and MausP[1] < infoObject.current_h/4*3 +130:
                            Skin = True

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
                    SpielerAText = font.render("Coins : " + str(Waehrung), True, pygame.Color('white'))
                    window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width() , 60))
                    pygame.display.flip()
                    clock.tick(60)
                    window.blit(Wonp, pygame.Rect(0, 0, infoObject.current_h, infoObject.current_w))
                    keys  = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        Esc = True 
                    if keys[pygame.K_RETURN]:
                        LevelF = Level*5
                        Feinde = []
                        Feindreturn()
                        PlayerX = infoObject.current_w /2
                        PlayerY = infoObject.current_h /2
                        Win = False
                        PlayerR = 0
                        if Skinan == 1:
                            Leben = 100
                        else:
                            Leben = 150
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
                        
                        Soldatw =pygame.transform.rotate(Skina, PlayerR)
                        window.blit(Soldatw, (PlayerX - Soldatw.get_width()/2, PlayerY - Soldatw.get_height()/2))
                        
                        Px = MausP[0] - PlayerX
                        Py = MausP[1] - PlayerY
                        Soldatw2 = math.degrees (math.atan2 (-Py,Px))
                        Soldatw  = pygame.transform.rotate(SkinaK, Soldatw2)
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
                        SpielerAText = font.render("Coins : " + str(Waehrung), True, pygame.Color('white'))
                        window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width() , 60))
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
                            FeindYG  = FeindYG / divisor
                            FeindXG  = FeindXG / divisor  
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
                                    Waehrung += 1
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
                            Esc = True
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
                            KugelYG = KugelYG * SkinG
                            KugelXG = KugelXG * SkinG 
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
                        SpielerAText = font.render("Coins : " + str(Waehrung), True, pygame.Color('white'))
                        window.blit(SpielerAText, (infoObject.current_w -30 -SpielerAText.get_width() , 60))
                        SpielerAText = font.render("Highscore : " + str(Highscore), True, pygame.Color('white'))
                        window.blit(SpielerAText, (infoObject.current_w /2 -SpielerAText.get_width()/2, infoObject.current_h/2 -SpielerAText.get_height()/2))
                        pygame.display.flip()
                        clock.tick(60)
                        window.blit(Gameover, pygame.Rect(0, 0, infoObject.current_h, infoObject.current_w))
                        keys  = pygame.key.get_pressed()
                        if keys[pygame.K_ESCAPE]:
                            Esc       = True 
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
                            if Skinan == 1:
                                Leben = 100
                            else:
                                Leben = 150