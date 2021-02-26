import random

import pygame

import Colours


class Ball(pygame.rect.Rect):
    def __init__(self, window, window_dimensions):
        self.diameter = 16
        self.radius = self.diameter//2
        self.width, self.height = self.diameter, self.diameter
        self.x = window_dimensions[0]//2 - self.radius
        self.y = window_dimensions[1]//2 - self.radius
        self.speed = 7
        self.speed_x = self.speed
        self.speed_y = self.speed
        self.window_height = window_dimensions[1]
        self.window_width = window_dimensions[0]
        self.window = window

    def home_pos(self):
        self.x = self.window_width//2 - self.radius
        self.y = self.window_height//2 - self.radius
        self.speed_x *= random.choice((-1, 1))
        self.speed_y *= random.choice((-1, 1))

    def redraw(self, window, paddle_player, paddle_opponent, player_score, opponent_score):
        if self.top <= 0 or self.bottom >= self.window_height:
            self.speed_y *= -1
        if self.left <= 0:
            player_score += 1
            self.home_pos()
        if self.right >= self.window_width:
            opponent_score += 1
            self.home_pos()

        if self.colliderect(paddle_player):
            if abs(self.right - paddle_player.left) < 10:
                self.speed_x *= -1
            elif abs(self.bottom - paddle_player.top) < 10 and self.speed_y > 0:
                self.speed_y *= -1
            elif abs(self.top - paddle_player.bottom) < 10 and self.speed_y < 0:
                self.speed_y *= -1

        if self.colliderect(paddle_opponent):
            if abs(self.left - paddle_opponent.right) < 10:
                self.speed_x *= -1
            elif abs(self.bottom - paddle_opponent.top) < 10 and self.speed_y > 0:
                self.speed_y *= -1
            elif abs(self.top - paddle_opponent.bottom) < 10 and self.speed_y < 0:
                self.speed_y *= -1

        self.x += self.speed_x
        self.y += self.speed_y
        pygame.draw.ellipse(window, Colours.Colors["lightGrey"], self)

        return player_score, opponent_score
