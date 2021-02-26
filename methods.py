import pygame

from Buttons import Button
from Colours import Colors


def timer_run(window, window_dimensions, window_colour, timer_num):
    timer_font = pygame.font.SysFont("comicsansms.ttf", 150)
    while timer_num > 0:
        pygame.time.delay(150)
        timer_text = timer_font.render(str(timer_num), False, Colors["white"])
        window.blit(timer_text, (375, 175))
        pygame.display.flip()
        pygame.time.delay(900)
        draw_window_background(window, window_dimensions, window_colour)
        timer_num -= 1
    return True, pygame.time.get_ticks()


def draw_window_background(window, window_dimensions, window_colour):
    window.fill(window_colour)

    pygame.draw.circle(window, Colors["lightGrey"], (window_dimensions[0]//2, window_dimensions[1]//2), 50, width=1)
    pygame.draw.aaline(window, Colors["lightGrey"], (window_dimensions[0]//2, 0), (window_dimensions[0]//2,
                                                                                   window_dimensions[1]))


def draw_window(window, window_dimensions, window_colour, buttons_array, paddle_player, paddle_opponent, ball,
                player_score, opponent_score, game_start, game_over):

    draw_window_background(window, window_dimensions, window_colour)

    if game_start and not game_over and paddle_opponent is not None:
        paddle_player.redraw(window)
        paddle_opponent.redraw(window, ball)
        player_score, opponent_score = ball.redraw(window, paddle_player, paddle_opponent, player_score, opponent_score)
        # pygame.draw.rect(window, Colors["lightGrey"], paddle_player)
        # # pygame.draw.rect(window, Colors["lightGrey"], paddle_opponent)
        # # pygame.draw.ellipse(window, Colours["lightGrey"], ball)

    Button.button_draw(buttons_array)
    return player_score, opponent_score
