import pygame
pygame.init()

window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

left_pos = 255
left_speed = 0

right_pos = 255
right_speed = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_speed = -5
            elif event.key == pygame.K_s:
                left_speed = +5
            elif event.key == pygame.K_UP:
                right_speed = -5
            elif event.key == pygame.K_DOWN:
                right_speed = +5
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    left_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    right_speed = 0

    left_pos = left_pos + left_speed
    right_pos = right_pos + right_speed
    if left_pos < 0:
        left_pos = 0
    if left_pos > 450:
        left_pos = 450
    if right_pos < 0:
        right_pos = 0
    if right_pos > 450:
        right_pos = 450

    window.fill("black")
    pygame.draw.rect(window, "white", (0, left_pos, 30, 150))
    pygame.draw.rect(window, "white", (770, right_pos, 30, 150))
    pygame.display.flip()

    clock.tick(60)