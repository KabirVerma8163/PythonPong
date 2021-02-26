import pygame
import Colours


class Paddle(pygame.rect.Rect):
    def __init__(self, x, y, window, speed):
        super().__init__(x, y, 10, 90)
        self.color = Colours.Colors['lightGrey']
        self.window = window
        self.x = x
        self.y = y
        self.rect = (x, y, self.width, self.height)
        self.speed = speed


class Player(Paddle):
    def __init__(self, window, window_dimensions):
        self.width = 10
        self.height = 100
        self.window_height = window_dimensions[1]
        x = window_dimensions[0] - (10 + self.width)
        y = window_dimensions[1]//2 - self.height//2
        super(Player, self).__init__(x, y, window, 5)
        self.width = 10
        self.height = 90

    def redraw(self, window):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and self.y - self.speed >= 0:
            self.y -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.y + self.speed + self.height <= self.window_height:
            self.y += self.speed

        pygame.draw.rect(window, Colours.Colors["lightGrey"], self)


class OpponentPaddle(Paddle):
    def __init__(self, window, window_dimensions):
        self.width = 10
        self.height = 100
        x = 10
        y = window_dimensions[1]//2 - self.height//2
        self.window_height = window_dimensions[1]
        super(OpponentPaddle, self).__init__(x, y, window, 5)


class PvPOpponent(OpponentPaddle):
    def __init__(self, window, window_dimensions):
        super().__init__(window, window_dimensions)

    def redraw(self, window, ball):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and self.y - self.speed >= 0:
            self.y -= self.speed
        if keys_pressed[pygame.K_s] and self.y + self.speed + self.height <= self.window_height:
            self.y += self.speed

        pygame.draw.rect(window, Colours.Colors["lightGrey"], self)


class CompOpponent(OpponentPaddle):
    def __init__(self, window, window_dimensions):
        super().__init__(window, window_dimensions)

    def redraw(self, window, ball):
        keys_pressed = pygame.key.get_pressed()
        if ball.centery > self.centery:
            self.y += self.speed
        if ball.centery < self.centery:
            self.y -= self.speed

        pygame.draw.rect(window, Colours.Colors["lightGrey"], self)


