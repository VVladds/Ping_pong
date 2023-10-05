from pygame import *
from random import *

window = display.set_mode((700,500))
display.set_caption('Shooter')

background = transform.scale(image.load('galaxy.jpg'), (700,500))


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')

font.init()

game = True
finish = False
lost = 0
kills = 0
class GameSprite(sprite.Sprite):
    def __init__(self,imag,x,y,speed):
        self.image = transform.scale(image.load(imag),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self,imag,x,y,speed):
        super().__init__(imag,x,y,speed)
        self.destroyed = 0
        self.Missed = 0
        self.delay = 0
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

    def fire(self):
        keys = key.get_pressed()
        if keys[K_SPACE] and self.delay<=0:
            self.delay = 30
            bullet = Bullet('bullet.png',self.rect.x+12,self.rect.y,15)
            Bullets.append(bullet)
            fire.play()
        self.delay -= 1

class Enemy(GameSprite):
    def __init__(self,imag,x,y,speed):
        super().__init__(imag,x,y,speed)
    def update(self):
        global lost
        global bullet
        if self.rect.y < 500:
            self.rect.y += self.speed
        if self.rect.y > 490:
            self.rect.y = 10
            self.rect.x = randint(100,600)
            self.speed = randint(1,5)
            lost += 1

        
        
class Bullet(GameSprite):
    def __init__(self,imag,x,y,speed):
        super().__init__(imag,x,y,speed)  
        self.image = transform.scale(image.load(imag),(25,25))
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y >= 0:
            self.kill



hero = Player('rocket.png',325,440,10)
enemys = list()
for i in range(5):

    enemy = Enemy('ufo.png',randint(100,600),0,randint(1,5))
    enemys.append(enemy)
monsters = sprite.Group()
Bullets = list()


score = font.Font(None,30).render('Счет: ' + str(kills), True,(255,255,255))
miss = font.Font(None,30).render('Пропущено: ' + str(lost), True,(255,255,255))
win = font.Font(None,70).render('YOU WIN!', True,(255,215,0))
lose = font.Font(None,70).render('YOU LOSE!', True,(255,215,0))

while game:
    if finish != True:
        window.blit(background,(0,0))
        
        hero.update()
        hero.delay-=1
        hero.reset()
        hero.fire()
        for bullet in Bullets:
            bullet.reset()
            bullet.update()
            for enemy in enemys:
                if sprite.collide_rect(bullet,enemy):
                    Bullets.remove(bullet)
                    enemys.remove(enemy)
                    enemys.append(Enemy('ufo.png',randint(100,600),0,randint(1,5)))
                    kills +=1

                if sprite.collide_rect(enemy,hero):
                    window.blit(lose,(230,210))
                    mixer.music.pause()
                    finish = True

        
    
        for enemy in enemys:
            enemy.reset()
            enemy.update()

        


        

        if lost >= 3:
            window.blit(lose,(230,210))
            mixer.music.pause()
            finish = True
        
        if kills >= 10:
            window.blit(win,(230,210))
            mixer.music.pause()
            finish = True

    score = font.Font(None,30).render('Счет: ' + str(kills), True,(255,255,255))
    miss = font.Font(None,30).render('Пропущено: ' + str(lost), True,(255,255,255))
    window.blit(score,(10,20))
    window.blit(miss,(10,50))


    for e in event.get():
            if e.type == QUIT:
                game = False
    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)










    display.update()