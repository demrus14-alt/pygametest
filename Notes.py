import pygame

a = 3
W = 400
H = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

player = [W // 2, H // 2, 50, 50]

while True:
    clock.tick(60)

    screen.fill(WHITE)

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        player[0] -= a

    if key[pygame.K_LSHIFT]:
        player[0] += 10

    if key[pygame.K_RIGHT]:
        player[0] += a

    pygame.draw.rect(screen, BLACK, player)
    pygame.display.update()
