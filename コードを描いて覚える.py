import pygame
import sys
import time

pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("コードを入力して覚えよう！")
clock = pygame.time.Clock()

# 日本語対応フォント（環境に合わせて変更してね）
font_path = "C:/Windows/Fonts/meiryo.ttc"
font = pygame.font.Font(font_path, 32)
small_font = pygame.font.Font(font_path, 24)

# 正しいコードと説明（順番）
code_steps = [
    ("import pygame", "Pygameライブラリを読み込む"),
    ("pygame.init()", "Pygameを初期化する"),
    ("screen = pygame.display.set_mode((800, 600))", "画面サイズを設定する"),
    ("pygame.display.set_caption('game')", "ウィンドウのタイトルを設定する"),
    ("clock = pygame.time.Clock()", "時間管理のためのClockを作る"),
    ("while True:", "ゲームループを開始する"),
    ("for event in pygame.event.get():", "イベントをチェックする"),
    ("if event.type == pygame.QUIT:", "終了イベントを確認する"),
    ("pygame.quit(); sys.exit()", "ゲームを終了する")
]

current_index = 0
user_input = ""
message = ""
start_time = time.time()
end_time = None

# メインループ
while True:
    screen.fill((240, 250, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN and not end_time:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                correct_code = code_steps[current_index][0]
                if user_input.strip() == correct_code:
                    current_index += 1
                    user_input = ""
                    message = ""
                    if current_index == len(code_steps):
                        end_time = time.time()
                        message = f"ぜんぶ正解！🎉（{round(end_time - start_time, 2)}秒）"
                else:
                    message = "ちがうよ〜！もう一度！"
            else:
                user_input += event.unicode

    # 説明表示
    if current_index < len(code_steps):
        desc = code_steps[current_index][1]
        desc_text = font.render(f"▶ {desc}", True, (0, 0, 0))
        screen.blit(desc_text, (50, 50))

    # 入力欄
    pygame.draw.rect(screen, (255, 255, 255), (50, 120, 900, 50))
    pygame.draw.rect(screen, (0, 0, 0), (50, 120, 900, 50), 2)
    input_text = font.render(user_input, True, (0, 0, 0))
    screen.blit(input_text, (60, 130))

    # メッセージ表示
    if message:
        msg = font.render(message, True, (0, 100, 0))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, 200))

    # タイマー表示
    if not end_time:
        now = time.time()
        timer_text = f"タイム：{round(now - start_time, 2)} 秒"
    else:
        timer_text = f"クリアタイム：{round(end_time - start_time, 2)} 秒"
    timer = small_font.render(timer_text, True, (0, 0, 0))
    screen.blit(timer, (WIDTH - 250, 10))

    pygame.display.flip()
    clock.tick(60)
