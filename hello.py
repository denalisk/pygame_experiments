import pygame
from pygame.locals import *
import random, math, sys
pygame.init()

Surface = pygame.display.set_mode((800,600))

Circles = []
Colliders = []
class Circle:
    def __init__(self):
##        self.radius = int(random.random()*50) + 1
        self.radius = 20
        self.x = random.randint(self.radius, 800-self.radius)
        self.y = random.randint(self.radius, 600-self.radius)
        self.speedx = 0.5*(random.random()+1.0)
        self.speedy = 0.5*(random.random()+1.0)
        self.colliding = False;
##        self.mass = math.sqrt(self.radius)
for x in range(20):
    Circles.append(Circle())

def CircleCollide(ArrayOfCollisions):
    for Collision in ArrayOfCollisions:
        hold1x = Collision[0].speedx;
        hold1y = Collision[0].speedy;
        Collision[0].speedx = Collision[1].speedx;
        Collision[0].speedy = Collision[1].speedy;
        # C2.speedx = hold1x;
        # C2.speedy = hold1y;
        Collision[1].speedx = hold1x
        Collision[1].speedy = hold1y
        Collision[1].colliding = False;
        Collision[0].colliding = False;
    ArrayOfCollisions = []
# All this needs to work is that the circles upon collision get removed from a collision table, because the double for loop is finding them once, swapping their velocity vectors, and finding them again, and swapping back. If you made a unique "collision" list, that checked for duplicates, you could add them to that and then loop through the collision list to assign new V vectors

def Move():
    for Circle in Circles:
        Circle.x += Circle.speedx
        Circle.y += Circle.speedy
def CollisionDetect():
    for Circle in Circles:
        if Circle.x < Circle.radius or Circle.x > 800-Circle.radius:    Circle.speedx *= -1
        if Circle.y < Circle.radius or Circle.y > 600-Circle.radius:    Circle.speedy *= -1
    for Circle in Circles:
        for Circle2 in Circles:
            if Circle != Circle2:
                if math.sqrt(  ((Circle.x-Circle2.x)**2)  +  ((Circle.y-Circle2.y)**2)  ) <= (Circle.radius+Circle2.radius):
                    if Circle.colliding == False:
                        Circle.colliding = True;
                        Circle2.colliding = True;
                        Colliders.append([Circle, Circle2]);
    CircleCollide(Colliders);

def Draw():
    Surface.fill((25,0,0))
    for Circle in Circles:
        pygame.draw.circle(Surface,(0,0,150),(int(Circle.x),int(600-Circle.y)),Circle.radius)
    pygame.display.flip()
def GetInput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or keystate[K_ESCAPE]:
            pygame.quit(); sys.exit()
def main():
    while True:
        GetInput()
        Move()
        CollisionDetect()
        Draw()
if __name__ == '__main__': main()
