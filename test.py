import pygame
pygame.init() 

win = pygame.display.set_mode((700, 500))  # set
# win.fill((123, 76, 31))
back = pygame.transform.scale(pygame.image.load("shaurma.jpg"), (700, 500))
win.blit(back, (0, 0))
clock = pygame.time.Clock()

while True:
    pygame.display.update()
    clock.tick(60)