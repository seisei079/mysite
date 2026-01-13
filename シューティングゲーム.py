import pygame;pygame.init();W,H=600,600;screen=pygame.display.set_mode((W,H));pygame.display.set_caption('シューティングゲーム');clock=pygame.time.Clock();buruki=pygame.image.load('buru-ki-.png');buruki_rect=buruki.get_rect()
running = True
while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()
    dx=dy=0
    if keys[pygame.K_LEFT]:dx-=5
    if keys[pygame.K_RIGHT]:dx+=5
    if keys[pygame.K_UP]:dy-=5
    if keys[pygame.K_DOWN]:dy+=5
    screen.fill((0,0,0));screen.blit(buruki,buruki_rect);pygame.display.flip()
pygame.quit()

