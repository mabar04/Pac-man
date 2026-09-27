import pygame


class MazeRender():

    def maze_render(self, cells):
        pygame.init()
        screen = pygame.display.set_mode((1000, 800))
        event = pygame.event.get()
        running = True
        clock = pygame.time.Clock()

        while running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            clock.tick(60)