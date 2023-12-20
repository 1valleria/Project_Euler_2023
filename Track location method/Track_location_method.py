#import os
#os.system("pip install pygame")
import random
import pygame

import webbrowser

pygame.init()
pygame.font.init()

def scoreDisplay():
    # Subtracting startTime ensures our score represents the elapsed time since the game started.
    time = int(pygame.time.get_ticks() / 1000) - startTime  # Divided by 1000, so it just shows as single digits
    scoreSurf = font.render(f'Score: {time}', False, 'Black')
    scoreRect = scoreSurf.get_rect(center=(312.5, 50))
    pygame.draw.rect(screen, 'Pink', scoreRect)
    screen.blit(scoreSurf, scoreRect)

# Constants
width, height = 625, 300
groundHeight = 250
playerJumpHeight = 20
playerGravity = 0
font = pygame.font.Font('font/BACKTO1982.ttf', 25)
gameActive = True
startTime = 0file 'font/BACKTO1982.ttf' found in working directory 'C:\Users\S2301890\OneDrive - Notre Dame Catholic Sixth Form College\Attachments\First Phyton Program\PythonApplication1\Track location method'.

# Loading all the images and adding rectangles to them
skySurface = pygame.image.load('images/sky.png')
groundSurface = pygame.image.load('images/ground.png')

turtleSurface = pygame.image.load('images/turtle.png')
wT, hT = turtleSurface.get_width(), turtleSurface.get_height()
turtle2 = pygame.transform.scale(turtleSurface, (int(wT * 0.18), int(hT * 0.18)))  # Resizing the image
turtleRect = turtle2.get_rect(midbottom=(width + wT * 0.18, 270))
turtleMask = pygame.mask.from_surface(turtle2)

playerSurface = pygame.image.load('images/player.png')
wP = playerSurface.get_width()
player2 = pygame.transform.scale(playerSurface, (90, 135))  # Resizing the image
playerRect = player2.get_rect(midbottom=(80 + wP * 0.05, 270))
playerMask = pygame.mask.from_surface(player2)

screen = pygame.display.set_mode([width, height])  # This is the display size of the screen
pygame.display.set_caption("Infinite Running")
clock = pygame.time.Clock()  # For the frame rate

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if gameActive:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playerRect.bottom == groundHeight:
                    playerGravity = -playerJumpHeight

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if playerRect.bottom == groundHeight:
                        playerGravity = -playerJumpHeight

        else:  # When the player collides, it will end. This will restart the game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True
                turtleRect.left = 600
                startTime = int(pygame.time.get_ticks() / 1000) - startTime  # Records the starting time of the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gameActive = True
                turtleRect.left = 600
                startTime = int(pygame.time.get_ticks() / 1000) - startTime

    screen.blit(skySurface, (0, 0))
    screen.blit(groundSurface, (0, groundHeight))

    if gameActive:
        playerGravity += 1
        playerRect.y += playerGravity

        if playerRect.bottom >= groundHeight:
            playerRect.bottom = groundHeight

        turtleRect.x -= 4
        if turtleRect.right <= 0:
            turtleRect.left = width + wT * 0.18

        overlap = playerMask.overlap(turtleMask, (turtleRect.x - playerRect.x, turtleRect.y - playerRect.y))
        if overlap:
            gameActive = False

        screen.blit(turtle2, turtleRect)
        screen.blit(player2, playerRect)
        score = scoreDisplay()
    else:
        screen.fill((143, 188, 143))


    pygame.display.update()
    clock.tick(60)

pygame.quit()