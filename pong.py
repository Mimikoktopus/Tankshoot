import pygame
pygame.init()
pygame.font.init()

ORANGE    = ( 255, 140, 0)
ROT       = ( 255, 0, 0)
GRUEN     = ( 0, 255, 0)
SCHWARZ   = ( 0, 0, 0)
WEiSS     = ( 255, 255, 255)
BLAU      = ( 0, 0, 255)
GRAU      = ( 150, 150, 150)
SpielerA  = 190
SpielerB  = 190
BallX     = 320
Bally     = 240
BallXG    = 6
BallYG    = 3
SpielerAP = 0
SpielerBP = 0
window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
pygame.display.set_caption("Pong")

spielaktiv = True

while spielaktiv:
    window.fill(GRAU)
    rect = pygame.Rect(50, SpielerA, 6, 100)
    pygame.draw.rect(window, (ROT), rect)
    rect = pygame.Rect(550, SpielerB, 6, 100)
    pygame.draw.rect(window, (BLAU), rect)
    rect = pygame.Rect(317, 0, 6, 480)
    pygame.draw.rect(window, (WEiSS), rect)
    pygame.draw.circle(window, (GRUEN), (BallX, Bally), 10)
    pygame.display.flip()
    clock.tick(60)
    BallX = BallX + BallXG
    Bally = Bally + BallYG
    
    if BallX > 640:
        Font=pygame.font.SysFont('timesnewroman',  50)
        SpielerAPT = Font.render("PlayerA: " + str(SpielerAP), False, SCHWARZ)
        window.blit(SpielerAPT,(50, 50))
        SpielerAP = SpielerAP +1
        BallX     = 320
        Bally     = 240
    if BallX < 0:
        SpielerAP = SpielerBP +1
        BallX     = 320
        Bally     = 240
    if BallX > 543:
        if Bally > SpielerB:
            if Bally < SpielerB +100:
                BallXG = BallXG *-1
    if BallX < 63:
        if Bally > SpielerA:
            if Bally < SpielerA +100:
                BallXG = BallXG *-1
    if Bally > 477:
        BallYG = BallYG *-1
    if Bally < 3:
        BallYG = BallYG *-1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        SpielerA = SpielerA-5
    if keys[pygame.K_s]:
        SpielerA = SpielerA+5
    if keys[pygame.K_UP]:
        SpielerB = SpielerB-5
    if keys[pygame.K_DOWN]:
        SpielerB = SpielerB+5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False