import pygame
import random
import sys

pygame.init()

# 画面サイズと初期設定
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("鬼ごっこゲーム")
clock = pygame.time.Clock()

# フォントと色
font = pygame.font.SysFont(None, 40)
WHITE = (255, 255, 255)

# プレイヤーと敵の初期設定
x, y = 300, 220
speed = 10
enemy_x, enemy_y = 100, 100
enemy_speed = 3
hp = 3
invincible = 0

# スコア
score = 0
time_counter = 0
score_interval = 60  # 1秒ごとにスコア加算

# 回復アイテムの設定
item_img = pygame.image.load('ringo.png')
item_img = pygame.transform.scale(item_img, (50, 50))
item_x = random.randint(100, 1100)
item_y = random.randint(100, 800)
item_visible = True
item_timer = 0
item_interval = 600 # 約5秒ごとに出現

# 画像読み込み
player_img = pygame.image.load("inuinu.png")
player_img = pygame.transform.scale(player_img, (100, 100))
enemy_img = pygame.image.load("nekoneko.png")
enemy_img = pygame.transform.scale(enemy_img, (100, 100))

running = True
while running:
    screen.fill(WHITE)

    # プレイヤーの当たり判定
    player_rect = pygame.Rect(x - 20, y - 20, 40, 40)

    # アイテムの出現タイマー処理
    item_timer += 1
    if item_timer >= item_interval:
        item_timer = 0
        item_visible = not item_visible
        if item_visible:
            item_x = random.randint(100, 1100)
            item_y = random.randint(100, 800)

    # アイテムの当たり判定と描画
    if item_visible:
        item_rect = pygame.Rect(item_x, item_y, 50, 50)
        if player_rect.colliderect(item_rect):
            if hp < 3:
                hp += 1
                print(f"回復！HP: {hp}")
            item_visible = False
            item_timer = 0
        screen.blit(item_img, (item_x, item_y))

    # スコア加算
    time_counter += 1
    if time_counter >= score_interval:
        score += 1
        time_counter = 0

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # プレイヤーの移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed

    # 敵の移動（プレイヤーを追いかける）
    if enemy_x < x:
        enemy_x += enemy_speed
    elif enemy_x > x:
        enemy_x -= enemy_speed
    if enemy_y < y:
        enemy_y += enemy_speed
    elif enemy_y > y:
        enemy_y -= enemy_speed

    # 敵の当たり判定
    enemy_rect = pygame.Rect(enemy_x - 20, enemy_y - 20, 40, 40)

    # 無敵時間カウント
    if invincible > 0:
        invincible -= 1

    # 敵との当たり判定
    if player_rect.colliderect(enemy_rect) and invincible == 0:
        hp -= 1
        print(f"ダメージ！HP: {hp}")
        invincible = 60
        if hp <= 0:
            print("ゲームオーバー！💥")
            pygame.time.delay(1000)
            running = False

    # 描画
    screen.blit(player_img, (x - 20, y - 20))
    screen.blit(enemy_img, (enemy_x - 20, enemy_y - 20))

    # HPとスコア表示
    hp_text = font.render(f"HP: {hp}", True, (0, 0, 0))
    screen.blit(hp_text, (10, 10))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
