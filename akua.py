import pygame;pygame.init();w,h=500,500;screen=pygame.display.set_mode((w,h));pygame.display.set_caption('アクア')
run=True
while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            run=False
    screen.fill()
    pygame.display.flip
pygame.quit()