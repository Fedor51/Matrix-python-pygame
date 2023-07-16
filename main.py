from pygame import time, display, font,event, Color, FULLSCREEN, QUIT, init
from random import choice,randrange

# symbol class
class Symbol:
    def __init__(self, x, y,speed):
        self.x, self.y = x, y
        self.speed = speed 
        self.value = choice(gkat)
        self.interval = randrange(5,30)

    def draw(self):
        frames = time.get_ticks()
        if not frames % self.interval:
            self.value = choice(gkat)
        self.y = self.y + self.speed if self.y < HEIGHT else - font_size
        screen.blit(self.value,(self.x,self.y))

class Column:
    def __init__(self, x, y):
        self.column_height = randrange(20,40)
        self.speed = randrange(3,10)
        self.symbols = [Symbol(x,i,self.speed) for i in range(y,y - font_size * self.column_height,-font_size)]
    
    def draw(self):
        [symbol.draw() for symbol in self.symbols]

# basic
SIZE = WIDHT,HEIGHT  = 1920,1200
screen = display.set_mode(SIZE,FULLSCREEN)
display.set_caption('А что ты хотел?')
fps = 60
clock = time.Clock()

# for matrix 
init()

font_size = 20
katakana = [chr(int('0x30a0',16) + i) for i in range(96)]
font = font.Font('ms_mincho.ttf',font_size)
gkat = [font.render(char, True, Color('green')) for char in katakana]

symbol_columns = [Column(x,randrange(-HEIGHT,0)) for x in range(0,WIDHT,font_size)]

# main cycle
while True:

    # fps, exit, background
    clock.tick(fps)
    for ev in event.get():
        if ev.type == QUIT:
            raise SystemExit 
    screen.fill(Color('black'))

    # drawing
    [sc.draw() for sc in symbol_columns]

    display.flip()
    
    


