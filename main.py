import pygame
import time

from pygame import color

pygame.init()


class Color:
    yellow = pygame.image.load('E:/Python Online/Jalase 13/brick breaker/image/Yellow.png')
    gray = pygame.image.load('E:/Python Online/Jalase 13/brick breaker/image/Gray.png')
    green =pygame.image.load('E:/Python Online/Jalase 13/brick breaker/image/Green.png')
    red =pygame.image.load('E:/Python Online/Jalase 13/brick breaker/image/Red.png')
    blue = pygame.image.load('E:/Python Online/Jalase 13/brick breaker/image/Blue.png')
    rocket = pygame.image.load('E:/Python Online/Jalase 13/brick breaker/image/Rocket.png')
    ball = pygame.image.load('E:/Python Online/Jalase 13/brick breaker/image/Ball.png')
    black = (0,0,0)
    white =(255,255,255)

class Rocket:
    def __init__(self):
        self.w = 70
        self.x = Game.height/2
        self.y = Game.width - 40
        self.color = Color.rocket
        self.rect = self.color.get_rect()
        self.speed = 15
        self.score = 0
        self.area = Game.screen.blit(self.color,[self.x,self.y])

    def show(self):
        self.area = Game.screen.blit(self.color,[self.x,self.y])



class Brick :
    def __init__(self):

        self.y = 60
        self.x = 90
        self.bricks = []
        self.area = Game.screen.blit(Color.yellow,[self.x,self.y])

        for i in range(6):
            self.x = 90
            for j in range(7):
                self.bricks.append(Game.screen.blit(Color.yellow,[self.x,self.y]))
                self.x +=  62
            self.y += 23
             
    def show(self):

        for brick in self.bricks:
            self.area = Game.screen.blit(Color.yellow,brick)


class Ball :
    def __init__(self):

        self.x = Game.height/2
        self.y = Game.width /2
        self.speed = 10
        self.color = Color.ball
        self.x_dir = 1
        self.y_dir = -1
        self.area = Game.screen.blit(self.color,[self.x,self.y])
        

    def show(self):
        self.area = Game.screen.blit(self.color,[self.x,self.y])

    def move(self):
        
        self.x += 10 * self.x_dir
        self.y -= 10 * self.y_dir

        if self.y < 10 :
            self.y_dir *= -1
        
        if self.x < 10 :
            self.x_dir *= -1

        if self.x > Game.width -10:
            self.x_dir *= -1

        
    def new(self):
        self.x = Game.height/2
        self.y = Game.width /2
        time.sleep(1)
        

class Game:
    width = 600
    height = 600
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Brick breaker')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("calibri",20)
    fps = 30

    @staticmethod
    def play():
        xbr = Brick()
        rocket = Rocket()
        ball = Ball()
    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    
                if event.type == pygame.MOUSEMOTION:
                    rocket.x = pygame.mouse.get_pos()[0]

                    if rocket.x > Game.width :
                        rocket.x = Game.width - rocket.w
                    print(rocket.x)
                      
            ball.move()

            if ball.y > Game.height:
                ball.new()
                ball.x_dir *= -1


            Game.screen.fill(Color.black)
            pygame.draw.rect(Game.screen,Color.white,(0,0,Game.width,Game.height),8)

            rocket.show()
            ball.show()
            xbr.show()

            if ball.area.colliderect(rocket.area) :
                ball.y_dir *= -1

            for brick in xbr.bricks:
                if ball.area.colliderect(brick):
                    ball.x_dir *= -1
                    ball.y_dir *= -1
                    xbr.bricks.remove(brick)
                    rocket.score += 1
                    
            score1 = Game.font.render('Score : '+str(rocket.score),True,Color.white)
            Game.screen.blit(score1,[Game.width // 2 , 15])
            pygame.display.update()
            Game.clock.tick(Game.fps)

if __name__ == "__main__":
    Game.play()

