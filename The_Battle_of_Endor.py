from pgzrun import *
import random

WIDTH = 1400
HEIGHT = 800

shot = []
shot2 = []
current_life = 10
max_life = 10
k = 0

bg = Actor("ds.png")
TIE = Actor("xt.png")
X_wing = Actor("tx.png")
DV = Actor("dv.png")
AS = Actor("as.png")
AS.x = 1400
AS.y = random.randint(100,700)
failed = False
deadInvoked = False

def dead():
    global current_life,deadInvoked
    if deadInvoked:
        return
#    screen.draw.text("Lord Vader,your star fighter was destroyed,do you want to start over?", (0, 400), color="white",fontsize=50)
    TIE.image = "boom.png"
    sounds.explosion.play()
    sounds.imperialmarch.stop()
    clock.schedule_unique(recovery,2.0)
    deadInvoked = True

def recovery():
    global failed,k,current_life, max_life,deadInvoked
    TIE.image = "xt.png"
    failed = False
    k = 0
    current_life = max_life
    deadInvoked = False
    sounds.imperialmarch.play()

def draw():
    global failed
    global current_life,max_life
    global k
    global n
    screen.clear()
    bg.draw()
    TIE.draw()
    X_wing.draw()
    DV.draw()
    AS.draw()
    for i in shot:
        i.draw()
        #sounds.laser.play()
    for i in shot2:
        i.draw()
    screen.draw.text(f"life:{current_life}/{max_life}  score:{k}", (60, 10), color="white", fontsize=40)
    if failed:
        dead()
        #failed = False

def update():
    global failed
    global k
    global current_life
    global n
    screen.clear()
    if failed:
        return
    #bg.x -= 10
    AS.x -= 10
    if AS.x < 0:
        AS.x = 1400
        AS.y = random.randint(100,700)
    elif AS.colliderect(TIE):
        # TIE.image = "bird.png"
        current_life = 0
    #if bg.x < 0:
        #bg.x = 1400
    X_wing.x -= 10
    if X_wing.x < 0:
        X_wing.x = 1400
        X_wing.y = random.randint(100,720)
    for j in shot:
        j.x += 30
        if j.x > 1400:
            shot.remove(j)
        elif j.colliderect(X_wing):
            sounds.explosion.play()
            X_wing.x = 1400
            X_wing.y = random.randint(100, 720)
            k += 1
    for j in shot2:
        j.x -= 20
        if j.x < 0:
            shot2.remove(j)
        elif j.colliderect(TIE):
            #TIE.image = "bird.png"
            shot2.remove(j)
            current_life -= 1
    if current_life <= 0:
        failed = True
        #dead()
        #l = 1

def X_xing_shot():
    s2 = Actor("red.png")
    s2.pos = X_wing.pos
    shot2.append(s2)

def on_mouse_down(pos):
    s = Actor("green.png")
    s.pos = TIE.pos
    shot.append(s)
    sounds.laser.play()

def on_mouse_move(pos):
    TIE.y = pos[1]
    if TIE.y < 80:
        TIE.y = 80
    elif TIE.y > 780:
        TIE.y = 780

clock.schedule_interval(X_xing_shot, 0.2)
sounds.imperialmarch.play()
go()
