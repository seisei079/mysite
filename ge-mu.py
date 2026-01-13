import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('冒険')
tile_size = 32
map_data = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
]
ground = pygame.image.load('ground.png')
kusa = pygame.image.load('kusa.png')
akua = pygame.transform.scale(pygame.image.load('akua.png'), (20, 20))
akua_rect = akua.get_rect()
clock = pygame.time.Clock()
running = True
def can_move_rect(rect):
    idou = [
        (rect.left, rect.top), (rect.right -1, rect.top), (rect.left, rect.bottom -1), (rect.right -1, rect.bottom -1)
    ]
    for x, y in idou:
        tile_x = x // tile_size
        tile_y = y // tile_size
        if not (0 <= tile_x < len(map_data[0]) and 0 <= tile_y < len(map_data)):
            return False
        if map_data[tile_y][tile_x] != 0:
            return False
    return True
while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    new_x = akua_rect.x
    new_y = akua_rect.y
    if keys[pygame.K_LEFT]:
        new_x -= 5
    if keys[pygame.K_RIGHT]:
        new_x += 5
    if keys[pygame.K_UP]:
        new_y -= 5
    if keys[pygame.K_DOWN]:
        new_y += 5
    temp_rect = akua_rect.copy()
    temp_rect.x = new_x
    if can_move_rect(temp_rect):
        akua_rect.x = new_x
    temp_rect = akua_rect.copy()
    temp_rect.y = new_y
    if can_move_rect(temp_rect):
        akua_rect.y = new_y
    screen.fill((0, 0, 0))
    for y in range(len (map_data)):
        for x in range(len (map_data[0])):
            tile = map_data[y][x]
            pos = screen.blit(kusa, (x * tile_size, y * tile_size))
            if tile == 0:
                screen.blit(ground, pos)
            elif tile == 1:
                screen.blit(kusa, pos)
    screen.blit(akua, akua_rect)
    pygame.display.flip()
pygame.quit()
