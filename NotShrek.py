import pygame
import os

WIDTH, HEIGHT = 1000, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("spbu student simulator")

WHITE = (255, 255, 255)

FPS = 60
VEL = 4
STUDENT_HEIGHT, STUDENT_WIDTH = 269/3, 251/3

STUDENT_PIC = pygame.image.load(os.path.join('materials', 'Shrek.png')).convert()
STUDENT = pygame.transform.scale(STUDENT_PIC, (STUDENT_HEIGHT, STUDENT_WIDTH))

MAX_HEALTH = 1000


def draw_window(st):
    WIN.fill(WHITE)
    WIN.blit(STUDENT, (st.x, st.y))
    pygame.display.update()


def main():
    st = pygame.Rect(200, 300, STUDENT_WIDTH, STUDENT_HEIGHT)
    run = True
    clock = pygame.time.Clock()


    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and st.x - VEL > 0:
            st.x -= VEL
        if keys_pressed[pygame.K_s] and st.y + VEL + st.height < HEIGHT:
            st.y += VEL
        if keys_pressed[pygame.K_d] and WIDTH - st.x > st.width + 10:
            st.x += VEL
        if keys_pressed[pygame.K_w] and st.y - VEL > 0:
            st.y -= VEL
        draw_window(st)

    pygame.quit()


if __name__ == "__main__":
    main()
