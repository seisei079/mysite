import tkinter
import tkinter.messagebox

key = ''
def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ''

mx = 1
my = 1
yuka = 0
moving = False

def smooth_move(dx, dy, steps=10):
    def step(count=0):
        if count < steps:
            canvas.move('MYCHR', dx / steps, dy / steps)
            root.after(20, step, count + 1)
        else:
            # 足あとを描く
            canvas.create_rectangle(mx*80, my*80, mx*80+79, my*80+79, fill='pink', width=0)
            canvas.tag_lower("all")
            canvas.tag_raise('MYCHR')
            global moving
            moving = False
    step()

def main_proc():
    global mx, my, moving, yuka
    if not moving:
        dx, dy = 0, 0
        if key == 'Up' and maze[my-1][mx] == 0:
            dy = -80
            my -= 1
        elif key == 'Down' and maze[my+1][mx] == 0:
            dy = 80
            my += 1
        elif key == 'Left' and maze[my][mx-1] == 0:
            dx = -80
            mx -= 1
        elif key == 'Right' and maze[my][mx+1] == 0:
            dx = 80
            mx += 1

        if dx != 0 or dy != 0:
            yuka += 1
            moving = True
            smooth_move(dx, dy)

    if yuka == 30:
        canvas.update()
        tkinter.messagebox.showinfo('おめでとう！', '全ての床を塗り終わりました！')
    else:
        root.after(50, main_proc)

root = tkinter.Tk()
root.title('一筆がきゲーム')
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)

canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,0,1],
    [1,0,0,1,1,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*80, y*80, x*80+79, y*80+79, fill='skyblue', width=0)

img = tkinter.PhotoImage(file='neko.png').subsample(5, 5)
canvas.create_image(mx*80+40, my*80+40, image=img, tag='MYCHR')

main_proc()
root.mainloop()
