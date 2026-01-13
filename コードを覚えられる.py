import pygame
import sys
import random
import time

pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("コードの順番を覚えよう！")
clock = pygame.time.Clock()

# 日本語対応フォント（環境に合わせて変更してね）
font_path = "C:/Windows/Fonts/meiryo.ttc"
font = pygame.font.Font(font_path, 28)
small_font = pygame.font.Font(font_path, 22)

# 正しいコードと説明
code_steps = [
    ("import pygame", "Pygameライブラリを読み込む"),
    ("pygame.init()", "Pygameを初期化する"),
    ("screen = pygame.display.set_mode((800, 600))", "画面サイズを設定する"),
    ("pygame.display.set_caption('ゲーム')", "ウィンドウのタイトルを設定する"),
    ("clock = pygame.time.Clock()", "時間管理のためのClockを作る"),
    ("while True:", "ゲームループを開始する"),
    ("    for event in pygame.event.get():", "イベントをチェックする"),
    ("        if event.type == pygame.QUIT:", "終了イベントを確認する"),
    ("            pygame.quit(); sys.exit()", "ゲームを終了する")
]

# ランダムに並べてボタンを作成
shuffled = random.sample(code_steps, len(code_steps))
buttons = []
for i, (text, desc) in enumerate(shuffled):
    rect = pygame.Rect(50, 50 + i * 65, 900, 55)
    buttons.append({"text": text, "desc": desc, "rect": rect})

clicked = []
message = ""
start_time = time.time()
end_time = None

# メインループ
while True:
    screen.fill((240, 250, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not end_time:
            for btn in buttons:
                if btn["rect"].collidepoint(event.pos) and btn["text"] not in [c["text"] for c in clicked]:
                    clicked.append(btn)
                    correct = code_steps[:len(clicked)]
                    if [c["text"] for c in clicked] != [c[0] for c in correct]:
                        message = "ちがうよ〜！やりなおし！"
                        clicked = []
                        start_time = time.time()
                    elif len(clicked) == len(code_steps):
                        end_time = time.time()
                        message = f"ぜんぶ正解！すごい！🎉（{round(end_time - start_time, 2)}秒）"

    # ボタン描画
    for btn in buttons:
        color = (180, 220, 255) if btn in clicked else (255, 255, 255)
        pygame.draw.rect(screen, color, btn["rect"])
        pygame.draw.rect(screen, (0, 0, 0), btn["rect"], 2)
        txt = font.render(btn["text"], True, (0, 0, 0))
        desc = small_font.render(btn["desc"], True, (80, 80, 80))
        screen.blit(txt, (btn["rect"].x + 10, btn["rect"].y + 5))
        screen.blit(desc, (btn["rect"].x + 10, btn["rect"].y + 30))

    # メッセージ表示
    if message:
        msg = font.render(message, True, (0, 100, 0))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT - 60))

    # タイマー表示
    if not end_time:
        now = time.time()
        timer_text = f"タイム：{round(now - start_time, 2)} 秒"
    else:
        timer_text = f"クリアタイム：{round(end_time - start_time, 2)} 秒"
    timer = font.render(timer_text, True, (0, 0, 0))
    screen.blit(timer, (WIDTH - 300, 10))

    pygame.display.flip()
    clock.tick(60)
