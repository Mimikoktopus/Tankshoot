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
KugelX     = PlayerX
KugelY     = PlayerY
KugelXG    = 4
KugelYG    = 4
Feinde     = [[30, 30]]

#Bider, Sounds import
Fadenkreuz = pygame.image.load("Fadenkreuz.png")
Hintergrund= pygame.image.load("Hintergrund.jpg")
Soldat     = pygame.image.load("Panzer.png")
FeindB      = pygame.image.load("Feind.png")
Schuss     = pygame.mixer.Sound("Schuss.mp3")
Hintergrund= pygame.transform.scale(Hintergrund,(infoObject.current_w, infoObject.current_h))

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
        FeindX = infoObject.current_h
        FeindY = random.randint(-1000,infoObject.current_h + 1000)
    Feinde.append([FeindX, FeindY])

clock = pygame.time.Clock()
pygame.display.set_caption("Pong")
66
pygame.mouse.set_visible(0)

spielaktiv = True
Kugelaktiv = False

while spielaktiv:
    window.fill(GRAU)
    MausP = pygame.mouse.get_pos()
    window.blit(Hintergrund, pygame.Rect(0, 0, 32, 32))
    if Kugelaktiv:
        pygame.draw.circle(window, (ORANGE), (KugelX, KugelY), 5)
        KugelX  = KugelX + KugelXG
        KugelY  = KugelY + KugelYG
    
    Px = MausP[0] - PlayerX
    Py = MausP[1] - PlayerY
    Soldatw2 = math.degrees (math.atan2 (-Py,Px))
    Soldatw =pygame.transform.rotate(Soldat, Soldatw2)
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
                Kugelaktiv = False
    FeindXA = FeindX - PlayerX
    FeindYA = FeindY - PlayerY
    FeindA  = math.sqrt(FeindXA ** 2 + FeindYA ** 2)
    if FeindA < 80:
        spielaktiv = False    # Player Hitbox
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
        PlayerY = PlayerY-10
    if keys[pygame.K_s]:
        PlayerY = PlayerY+10
    if keys[pygame.K_a]:
        PlayerX = PlayerX-10
    if keys[pygame.K_d]:
        PlayerX = PlayerX+10
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