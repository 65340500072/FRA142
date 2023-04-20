import sys
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = r
        self.g = g
        self.b = b

    def draw(self,screen):
        pg.draw.rect(screen,(self.r, self.g, self.b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mx, my = pg.mouse.get_pos()
        if mx >= self.x and mx <= self.w + self.x and my >= self.y and my <= self.h + self.y:
            return True
        else:
            return False
    def isMouseClick(self):
        # for event in pg.event.get():
        if pg.mouse.get_pressed()[0]:
            return True
        else:
            return False


# -----------------------------------------------------------

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
a = 0
w = 0
s = 0
d = 0
btn = Button(win_x/2-50,win_y/2-50,100,100)
Ca = False
Cw = False
Cs = False
Cd = False


while(run):
    screen.fill((255, 255, 255))
    btn.r = 0
    btn.g = 197
    btn.b = 205
    btn.x -= a
    btn.x += d
    btn.y -= w
    btn.y += s
    btn.draw(screen)
    if Ca:
        a += 1
    else:
        a = 0
    if Cd:
        d += 1
    else:
        d = 0
    if Cw:
        w += 1
    else:
        w = 0
    if Cs:
        s += 1
    else:
        s = 0
    pg.time.delay(10)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            Ca = True
        if event.type == pg.KEYUP and event.key == pg.K_a:
            Ca = False
        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            Cw = True
        if event.type == pg.KEYUP and event.key == pg.K_w:
            Cw = False
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            Cs = True
        if event.type == pg.KEYUP and event.key == pg.K_s:
            Cs = False
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            Cd = True
        if event.type == pg.KEYUP and event.key == pg.K_d:
            Cd = False
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        
            


