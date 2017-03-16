import pygame
from pygame.locals import *
import random, math, sys
pygame.init()

# Easy access variables to adjust player traits
PlayerSize = 20;
PlayerSpeed = 5.0;
WindowSize = 1000;


class Player:
    def __init__(self):
        self.size = PlayerSize;
        self.speed = PlayerSpeed;
        self.vector = [0,0];
        self.color = (188, 188, 33);
        self.x = WindowSize/2.0;
        self.y = WindowSize/2.0;
        self.axes = {'x': self.x, 'y': self.y, '-x': self.x, '-y': self.y};

    def move(self):
        self.x += self.vector[0] * self.speed;
        self.y += self.vector[1] * self.speed;
        self.vector = [0,0];
        self.speed = PlayerSpeed;

    def update(self, gameScreen):
        pygame.draw.circle(gameScreen, (self.color), (int(self.x), int(self.y)), self.size);

class Game(Player):
    def __init__(self, Player):
        self.color = (0,0,0);
        self.window = pygame.display.set_mode((WindowSize, WindowSize));
        self.currentPlayer = Player;

    def update(self):
        self.window.fill(self.color);
        self.currentPlayer.update(self.window);
        pygame.display.flip();

    def process_input(self):
        KeyState = pygame.key.get_pressed();
        if KeyState[pygame.K_DOWN]:
            self.currentPlayer.vector[1] += 1;
        if KeyState[pygame.K_UP]:
            self.currentPlayer.vector[1] += -1;
        if KeyState[pygame.K_RIGHT]:
            self.currentPlayer.vector[0] += 1;
        if KeyState[pygame.K_LEFT]:
            self.currentPlayer.vector[0] += -1;
        if KeyState[pygame.K_SPACE]:
            self.currentPlayer.speed  *= 2;
            print("BOOOOOOOOOOOST");
        self.currentPlayer.move();
        for event in pygame.event.get():
            if event.type == QUIT or KeyState[pygame.K_ESCAPE]:
                print("over and out!");
                pygame.quit(); sys.exit();


def main():
    newPlayer = Player();
    newGame = Game(newPlayer);
    playing = True;
    counter = 1;
    while playing:
        newGame.process_input();
        newGame.update();
        if counter % 40 == 0:
            print("tick " + str(counter));
        counter += 1;

if __name__ == '__main__': main();
