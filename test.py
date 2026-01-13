import pygame;pygame.init();screen = pygame.display.set_mode((400, 300));clock = pygame.time.Clock()

# プレイヤーとブロックの設定
player = pygame.Rect(50, 50, 32, 32)
block = pygame.Rect(150, 100, 64, 64)
speed = 5

running = True
while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx = dy = 0
    if keys[pygame.K_LEFT]:
        dx = -speed
    if keys[pygame.K_RIGHT]:
        dx = speed
    if keys[pygame.K_UP]:
        dy = -speed
    if keys[pygame.K_DOWN]:
        dy = speed

    # 横移動の当たり判定
    player.x += dx
    if player.colliderect(block):
        player.x -= dx  # ぶつかったら戻す！

    # 縦移動の当たり判定
    player.y += dy
    if player.colliderect(block):
        player.y -= dy  # ぶつかったら戻す！

    # 描画
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), player)  # 青：プレイヤー
    pygame.draw.rect(screen, (255, 0, 0), block)   # 赤：ブロック
    pygame.display.flip()

pygame.quit()
