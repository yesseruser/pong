import pygame
pygame.init()

window = pygame.display.set_mode((800, 600))

left_pos = 150
left_speed = 0

right_pos = 150
right_speed = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_speed = -1
            elif event.key == pygame.K_s:
                left_speed = +1
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    left_speed = 0

    left_pos = left_pos + left_speed

    window.fill("black")
    pygame.draw.rect(window, "white", (0, left_pos, 30, 150))
    pygame.display.flip()