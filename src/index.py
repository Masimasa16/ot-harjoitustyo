from __future__ import annotations
import pygame, sys
import numpy as np


RED = 255, 0, 0
GREEN = 0, 255, 0
BLACK = 0, 0, 0
WHITE = 255, 255, 255

RADIUS = 60

VECTORS = np.array([
    [1, 0],
    [np.cos(np.radians(120)), np.sin(np.radians(120))],
    [np.cos(np.radians(240)), np.sin(np.radians(240))]
])


def rotation_matrix(theta):
    theta_radians = np.radians(theta)
    return np.array([
        [np.cos(theta_radians), -np.sin(theta_radians)],
        [np.sin(theta_radians), np.cos(theta_radians)]
    ])

class Hex:
    def __init__(self, radius, center):
        self.radius = radius
        self.dist_center = np.array([0.0, 0.0])

        self.points = []
        theta = np.radians(60)
        for i in range(6):
            x_pos = radius*np.cos(i*theta + np.radians(30)) + radius*center[0]
            y_pos = radius*np.sin(i*theta + np.radians(30)) + radius*center[1]
            self.points.append([x_pos, y_pos])
        self.points = np.array(self.points)

    def move(self, vector):
        if isinstance(vector, list):
            vector = np.array(vector)
        self.dist_center += vector*self.radius
        self.points += self.radius*vector
    
    def draw(self,screen, remove):
        if remove:
            pygame.draw.polygon(screen, BLACK, self.points + [640, 480])
            pygame.draw.polygon(screen, BLACK, self.points + [640, 480], 3)
        else:
            pygame.draw.polygon(screen, GREEN, self.points + [640, 480])
            pygame.draw.polygon(screen, RED, self.points + [640, 480], 3)


class Tile:
    def __init__(self, radius):
        vectors = np.array([
            [np.cos(np.radians(30)), 0.0],
            [-np.cos(np.radians(30)), 0.0],
            [0.0, 3/2],
            [0.0, -3/2]
        ])

        self.hexes = [
            Hex(radius, vector) for vector in vectors
        ]

    def move(self, vector):
        hex:Hex
        for hex in self.hexes:
            hex.move(vector)
    
    def rotate(self, theta):
        r = rotation_matrix(theta)
        hex:Hex
        for hex in self.hexes:
            for i, point in enumerate(hex.points):
                pos = point - hex.dist_center
                hex.points[i] = r @ (point - hex.dist_center) + hex.dist_center
    
    def draw(self, screen, remove):
        hex:Hex
        for hex in self.hexes:
            hex.draw(screen, remove)
(0, 0, 0), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100))

class Arrow:
    def __init__(self):
        self.poits = np.array([
            [0, 20.0],
            [0, 40.0],
            [40.0, 40.0],
            [40.0, 60.0],
            [60.0, 30.],
            [40.0, 0.0],
            [40.0, 20.0]
        ])

    def rotate(self, theta):
        r = rotation_matrix(theta)
        for i, point in enumerate(self.poits):
            self.poits[i] = r @ point
    
    def draw(self, screen):
        pygame.draw.polygon(screen, RED, self.poits + [640, 240])
        



def main():
    pygame.init()

    size = width, height = 2*640, 2*480
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    tile = Tile(RADIUS)
    arrow = Arrow()


    while True:

        tile.draw(screen, True)
        #arrow.draw(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    tile.move(VECTORS[0])

                if event.key == pygame.K_RIGHT:
                    tile.rotate(30)

                if event.key == pygame.K_LEFT:
                    tile.rotate(-30)
                
                if event.key == pygame.K_SPACE:
                    tile.draw(screen, False)
                    tile = Tile(RADIUS)

        tile.draw(screen, False)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()