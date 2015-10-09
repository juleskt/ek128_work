import pygame, sys, random
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

jif ="carruthers.png" #hero image
#bg = pygame.image.load("game_background.jpg").convert_alpha()
zmb = "anish.jpg"

normalmsc = '-Yakety Sax- Music.wav'
fruitmsc = pygame.mixer.Sound('smw_coin.wav')
deathscream = pygame.mixer.Sound('wilhelm.wav')

x,y = (500,300) #starting coordinates of prof
a,b = (1,1) #starting coordinates of first zombie
zs = 1.7 #zombie movement speed
hs = 3 #hero movement speed

xscreen = 1024 #screen size
yscreen = 680 #screen size

screen = pygame.display.set_mode((xscreen,yscreen),0,32) #makes windoW
timefactor = pygame.time.get_ticks()
screen.fill((255,255,255)) #background
#screen.blit(bg)
pygame.mixer.music.load(normalmsc)
pygame.mixer.music.play(-1, 0)

class Anish: #The Anish class inherits all of zombies' attributes.
##    def thing():
##        __init__(self,a=1,b=1)
##        self.a = a
##        self.b = b
    zm = pygame.image.load(zmb).convert() #get Nushnish and assigns

class player:
    pic = player = pygame.image.load(jif).convert_alpha() #gets Carruthers and assigns

q = random.randint(0, 1000)
w = random.randint(0, 590)
fruit_pos = (q,w) #makes random position
fruit_image = pygame.image.load("cointhing.jpg").convert() #makes coin/fruit 

s = 0 #init score

def game(a,b,x,y,q,w,score):
    
    fruit_pos = (q,w) #position of fruit/coin

    while True: #game code is run inside here
        timefactor = pygame.time.get_ticks()
        

        font=pygame.font.SysFont('Arial', 30) #creates font
        text=font.render('Score:'+str(score), True, (0, 0, 0)) #makes score
        screen.blit(text, (800,0)) #displays score

        clock = pygame.time.Clock() #creates clock
        change = 1000 #rate of change of time
        clock.tick(change) #makes clock tick
        
        screen.blit(fruit_image,(fruit_pos))#puts fruit/coin onto screen

        screen.blit(Anish.zm,(a,b)) #allows for location update of Nush
        screen.blit(player.pic,(x,y)) #allows for location update of Carruthers

        if (((abs((x+45)-q))**2)+(((abs((y+40)-w))**2)))**(1/2) < 50: #collects fruit
            q = random.randint(0,1000) #creates rand coordinates for coin
            w = random.randint(0,590)
            fruit_pos = (q,w) 
            fruitmsc.set_volume(1) #coin sound
            fruitmsc.play(0,0,0)
            score+= 1
            
        if abs((x-a)) < 70 and abs((y-b)) < 70: #hitboxes
            deathscream.play(0,0,0) #plays death scream
            gameover() #game over

        if (a,b) != (x,y): #zombie movement
                if x > a:
                    a += zs
                if x < a:
                    a -= zs
                if y > b:
                    b += zs
                if y < b:
                    b -= zs

        key = pygame.key.get_pressed() #hero movement
        if (key[K_w]) or (key[K_UP]):
            y -= hs
        elif (key[K_s]) or (key[K_DOWN]):
            y += hs
        elif(key[K_a]) or (key[K_LEFT]):
            x -= hs
        elif(key[K_d]) or (key[K_RIGHT]):
            x += hs
##        elif(key[K_SPACE]): #drops bomb
##            zs = 1
            
        if x < - 70: #screen jukes
            x = xscreen
        elif x > xscreen:
            x = -30
        elif y > yscreen:
            y = -70
        elif y < -70:
            y = yscreen

        pygame.display.update() #updates display
        screen.fill((255,255,255)) #puts background back up (covers up past images [no trail]) 
            
        for event in pygame.event.get(): #implements events
            if event.type == QUIT: #exiting conditions
                pygame.quit()
                sys.quit()
            elif event.type == KEYDOWN: #key inputs --> change pos/clicks
                if event.key == K_ESCAPE: #makes ESC an exit
                    pygame.quit()

def gameover():
    while True:
        screen.fill((255,255,255))
        font=pygame.font.SysFont('Arial', 30)
        text=font.render('Game Over, press enter to play again.', True, (0, 0, 0))
        screen.blit(text, (300,260))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    s = 0
                    game(a,b,x,y,q,w,s)
                elif event.key == K_ESCAPE:
                    pygame.quit()
game(a,b,x,y,q,w,s)
