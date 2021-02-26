import math
import sys
import pygame

from Ball import Ball
from Buttons import *
from Colours import *
from Paddle import *
from methods import *

pygame.init()
clock = pygame.time.Clock()

winWidth, winHeight = 800, 450
winDimensions = (winWidth, winHeight)
win = pygame.display.set_mode(winDimensions)
pygame.display.set_caption("Pong")
winColor = pygame.Color('grey12')

playerPaddle = Player(win, winDimensions)
opponentPaddle = None
ball = Ball(win, winDimensions)

playerScore = 0
opponentScore = 0
scoreFont = pygame.font.Font("freesansbold.ttf", 20)
finalScoreFont = pygame.font.Font("freesansbold.ttf", 30)

pvpButton = PvPButton(win, winDimensions)
compButton = CompButton(win, winDimensions)
onlineButton = PvPOnlineButton(win, winDimensions)
buttonArray = [pvpButton, compButton, onlineButton]

gameStart = False
gameOver = False
while True:
    # handling input
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pvpButton.is_over(pygame.mouse.get_pos()):
                opponentPaddle = PvPOpponent(win, winDimensions)
            if compButton.is_over(pygame.mouse.get_pos()):
                opponentPaddle = CompOpponent(win, winDimensions)
            for button in buttonArray:
                if button.is_over(pygame.mouse.get_pos()):
                    Button.button_disappear(buttonArray)
                    gameMode = button.get_mode()
                    gameStart = True
                    timer_run(win, winDimensions, winColor, 3)

    playerScore, opponentScore = draw_window(win, winDimensions, winColor, buttonArray, playerPaddle, opponentPaddle,
                                             ball, playerScore, opponentScore, gameStart, gameOver)
    if gameStart:
        playerScoreText = scoreFont.render(str(playerScore), False, Colors["white"])
        opponentScoreText = scoreFont.render(str(opponentScore), False, Colors["white"])
        win.blit(playerScoreText, (410, 220))
        win.blit(opponentScoreText, (380, 220))

    if playerScore == 10 or opponentScore == 10:
        gameOver = True
        gameStart = False
        finalScore = str(max(playerScore, opponentScore))
        loserScore = str(min(playerScore, opponentScore))
        if playerScore == finalScore:
            winner = "Player 1"
        else:
            winner = "Player 2"
        scoreText = finalScoreFont.render(f"{winner} wins! Score: {finalScore} vs. {loserScore}", False, Colors["white"])
        win.blit(scoreText, (win.get_width()//2 - scoreText.get_width()/2, win.get_height()//2 - scoreText.get_height()//2) )

    # Updating the window
    pygame.display.flip()
    clock.tick(60)

