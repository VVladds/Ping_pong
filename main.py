from pygame import *
from random import *

window = display.set_mode((700,500))
display.set_caption('Shooter')

background = transform.scale(image.load('354282-admin.jpg'), (700,500))
background.set_alpha(45)

'''mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')'''

font.init()

game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self,imag,x,y,speed):
        self.image = transform.scale(image.load(imag),(25,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self,imag,x,y,speed,num):
        super().__init__(imag,x,y,speed)
        self.num = num

    def update(self):
        keys_pressed = key.get_pressed()
        if self.num == 1:     
            if keys_pressed[K_s] and self.rect.y < 400:
                self.rect.y += self.speed
            if keys_pressed[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
        else:
            if keys_pressed[K_DOWN] and self.rect.y < 400:
                self.rect.y += self.speed
            if keys_pressed[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed






clock = time.Clock()
FPS = 60
        
class Bullet(GameSprite):
    def __init__(self,imag,x,y,speed):
        super().__init__(imag,x,y,speed)  
        self.image = transform.scale(image.load(imag),(25,25))
        self.speed_x = speed
        self.speed_y = speed
    def update(self):
        self.rect.y -= self.speed_y
        self.rect.x -= self.speed_x
        if self.rect.y <= 0 or self.rect.y >=475:
            self.speed_y*=-1
        


hero = Player('fffs.png', 20, 10, 10,0)
hero2 = Player('fffs.png', 650, 10, 10,1)

ball = Bullet('ball.png',100,100,5)
Players = list()
Players.append(hero)
Players.append(hero2)


win = font.Font(None,70).render('YOU WIN!', True,(255,215,0))
lose = font.Font(None,70).render('YOU LOSE!', True,(255,215,0))

while game:
    while finish != True:

        for e in event.get():
                if e.type == QUIT:
                    game = False
        clock = time.Clock()
        window.blit(background,(0,0))
        ball.reset()
        ball.update()

        for hero in Players:
            hero.update()
            hero.reset()
            if sprite.collide_rect(ball, hero):
                ball.speed_x*=-1

        if ball.rect.x <=0:
            finish = True
            window.blit(lose,(0,0))




        clock.tick(FPS)
        display.update()




    
    










    