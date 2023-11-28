from UI import *
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
pygame.init()

if __name__ == "__main__":
    pygame.display.set_caption("Boid simulation")
    screen = pygame.display.set_mode((config.Width, config.Height))
    setup_Flock(100)
    UI = UserInterface()
    while (config.running):
        update_timestep()
        screen.fill((20, 20, 20))
        UI.event_handler()
        for Boid in config.Flock:
            Boid.update()
            Boid.draw(screen)
        for obstacle in config.Obstacle:
            obstacle.draw(screen)
        if config.Show_UI == True:
            UI.draw(screen)
        pygame.display.update()




