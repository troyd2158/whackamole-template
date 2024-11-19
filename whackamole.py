import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if event.pos[0]//32 == mole_x//32 and event.pos[1]//32 == mole_y//32:
                        mole_x = random.randrange(0,20)*32
                        mole_y = random.randrange(0,16)*32
            screen.fill("light green")
            for x in range(20):
                pygame.draw.line(screen, (0, 0, 0), (x*32, 0), (x*32, 512))
            for y in range(16):
                pygame.draw.line(screen, (0, 0, 0), (0, y*32), (640, y*32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
