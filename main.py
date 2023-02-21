import pygame
import os
from pygame.locals import *

# global varibles
WIDTH = HEIGHT = 750

class ship:
    def load_ship(self):
        PATH_TO_SHIP = os.path.join(os.path.dirname(__file__), "./data/images/ship.png")
        ship = pygame.image.load(PATH_TO_SHIP).convert()
        ship = pygame.transform.scale(ship, (self.WIDTH, self.HEIGHT))
        return ship

    def __init__(self, size, windowsSize_WIDTH, windowsSize_HEIGHT) -> None:
        self.WIDTH = self.HEIGHT = size
        # position of ship
        self.x_pos = (windowsSize_HEIGHT / 2)
        self.y_pos = (windowsSize_WIDTH / 2)

        # velocity of ship
        self.x_vel = 0
        self.y_vel = 0

        # speed method
        self.SPEED = 0.05

        # angle of the ship
        self.angle = 0.0

    def __repr__(self):
        return f'x_pos: {self.x_pos}, y_pos: {self.x_pos}\nx_vel: {self.x_vel} y_vel: {self.y_vel}\nx_speed: {self.x_pos + self.x_vel} y_speed: {self.y_pos + self.y_vel}\n'



# gamme loop

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    pygame.display.set_caption('First game')


    #creating the ship/player
    player = ship(60, windowsSize_WIDTH=WIDTH, windowsSize_HEIGHT=HEIGHT)

    while True:
        for event in pygame.event.get():
                if event.type == QUIT: return

        # black background
        screen.blit(background, (0, 0))

        # player/ship
        playerShip = player.load_ship()
        playerShip = pygame.transform.rotate(playerShip, player.angle)

        # wrap the ship around the screen edges
        if player.x_pos < -player.WIDTH/2: player.x_pos = WIDTH + player.WIDTH/2
        elif player.x_pos > WIDTH + player.WIDTH/2: player.x_pos = -player.WIDTH/2
        if player.y_pos < -player.HEIGHT/2: player.y_pos = HEIGHT + player.HEIGHT/2
        elif player.y_pos > HEIGHT + player.HEIGHT/2: player.y_pos = -player.HEIGHT/2

        player.x_pos = player.x_pos + player.x_vel
        player.y_pos = player.y_pos + player.y_vel
        screen.blit(playerShip, ((player.x_pos), (player.y_pos)))

        pressed = pygame.key.get_pressed()
        if (pressed[K_LEFT] or pressed[K_a]) : player.angle = player.angle + 0.5
        if (pressed[K_RIGHT] or pressed[K_d]) : player.angle = player.angle - 0.5

        if (pressed[K_UP] or pressed[K_w]) : player.y_vel = player.y_vel - player.SPEED
        if (pressed[K_DOWN] or pressed[K_s]) : player.y_vel = player.y_vel + player.SPEED

        # dev feature REMOVE AFTERWARDS
        if (pressed[K_l]): player.x_pos, player.y_pos = (WIDTH / 2), (HEIGHT / 2)

        print(player)
            
        
        #EOF or in this case the loop
        pygame.display.update()


if __name__ == "__main__": main()
