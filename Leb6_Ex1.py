import sys
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
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
        if pg.mouse.get_pressed()[0]:
            return True
        else:
            return False


# -----------------------------------------------------------

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100)

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        btn.r = 169
        btn.g = 169
        btn.b = 169
        if btn.isMouseClick():
            btn.r =180
            btn.g = 28
            btn.b = 205
        else:
            btn.r = 169
            btn.g = 169
            btn.b = 169
            pass
    else:
        btn.r = 139
        btn.g = 0
        btn.b = 0
        pass
    
    btn.draw(screen)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        


