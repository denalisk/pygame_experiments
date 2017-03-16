import pygame
from pygame.locals import *
import random, math, sys
pygame.init()

# Easy access variables to adjust player traits
PlayerSize = 20;
PlayerSpeed = 5.0;
WindowSize = 1000;
ProctileSpeed = PlayerSpeed * 5;
ProctileSize = PlayerSize/2.0;


class Player:
    def __init__(self):
        self.size = PlayerSize;
        self.speed = PlayerSpeed;
        self.vector = [0,0];
        self.color = (188, 188, 33);
        self.x = WindowSize/2.0;
        self.y = WindowSize/2.0;

    def __str__(self):
        return "Player";

    def move(self):
        self.x += self.vector[0] * self.speed;
        self.y += self.vector[1] * self.speed;
        self.vector = [0,0];
        self.speed = PlayerSpeed;

    def process_input(self, currentKeyState):
        if currentKeyState[pygame.K_DOWN]:
            self.vector[1] += 1;
        if currentKeyState[pygame.K_UP]:
            self.vector[1] += -1;
        if currentKeyState[pygame.K_RIGHT]:
            self.vector[0] += 1;
        if currentKeyState[pygame.K_LEFT]:
            self.vector[0] += -1;
        if currentKeyState[pygame.K_SPACE]:
            self.speed  *= 2;
        self.move();

    def update(self, gameScreen):
        pygame.draw.circle(gameScreen, (self.color), (int(self.x), int(self.y)), self.size);

class Game():
    def __init__(self):
        self.color = (0,0,0);
        self.window = pygame.display.set_mode((WindowSize, WindowSize));
        self.objectDictionary = {};
        self.player = Player();

    def __str__(self):
        return "Game";

    def update(self):
        self.check_exist();
        self.window.fill(self.color);
        self.player.update(self.window)
        for key, value in self.objectDictionary.items():
            value.update(self.window);
        pygame.display.flip();

    def process_input(self):
        KeyState = pygame.key.get_pressed();
        self.player.process_input(KeyState);
        for key, value in self.objectDictionary.items():
            value.process_input(KeyState);
        for event in pygame.event.get():
            if event.type == QUIT or KeyState[pygame.K_ESCAPE]:
                print("over and out!");
                pygame.quit(); sys.exit();

    def check_exist(self):
        RemoveArray = [];
        for key, value in self.objectDictionary.items():
            if abs(value.x) - value.origin[0] > WindowSize or abs(value.y) - value.origin[1] > WindowSize:
                RemoveArray.append(key);
        for gameObject in RemoveArray:
            del self.objectDictionary[gameObject];

    # def add_object(self, objectName, newObject):
    #     self.objectDictionary[objectName] = newObject;

class Projectile():
    def __init__(self):
        self.size = ProjectileSize;
        self.speed = ProjectileSpeed;
        self.vector = [0,0];
        self.color = (200, 0, 0);
        self.x = 0;
        self.y = 0;
        self.origin = [0,0];

    def __str__(self):
        return "Projectile";

    def move(self):
        self.x += self.vector[0] * self.speed;
        self.y += self.vector[1] * self.speed;

    def process_input(self, currentKeyState):
        pass;

    def update(self, gameScreen):
        self.move();
        pygame.draw.line(gameScreen, (self.color), (int(self.x), int(self.y)), ((int(self.x) + self.vector[0]), (int(self.y) + self.vector[1])), self.size);


def main():
    newGame = Game();
    # newPlayer = Player();
    # newGame.add_object('player', newPlayer);
    playing = True;
    counter = 1;
    while playing:
        newGame.process_input();
        newGame.update();
        if counter % 40 == 0:
            print("tick " + str(counter));
        counter += 1;

if __name__ == '__main__': main();
