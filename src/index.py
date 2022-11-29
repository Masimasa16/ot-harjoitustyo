from __future__ import annotations
import sys
import pygame
import numpy as np

from logic import create_arrows
from logic import Tile

RED = 255, 0, 0
GREEN = 0, 255, 0
BLACK = 0, 0, 0
WHITE = 255, 255, 255

HEX_DIST_FROM_CENTER = 30
ARROW_SIZE = 70


WIDTH = 2*640
HEIGHT = 2*480

CENTER_POS = [WIDTH//2, HEIGHT//2]


def draw_polygon(screen, color, line_color, points):
    pygame.draw.polygon(screen, color, points + CENTER_POS)
    pygame.draw.polygon(screen, line_color, points + CENTER_POS, 2)


GRID = np.zeros((20, 20, 20))


def draw_grid(screen):
    points = []
    theta = np.radians(60)
    for i in range(6):
        x_pos = HEX_DIST_FROM_CENTER*np.cos(i*theta + np.radians(30))
        y_pos = HEX_DIST_FROM_CENTER*np.sin(i*theta + np.radians(30))
        points.append([x_pos, y_pos])

    points = np.array(points)

    for i in range(-10, 10):
        for j in range(-10, 10):
            for k in range(-10, 10):
                x_center = 2*(HEX_DIST_FROM_CENTER - 4) * \
                    (i + j*np.cos(theta) - k*np.cos(theta)) + WIDTH//2
                y_center = 2*(HEX_DIST_FROM_CENTER - 4) * \
                    (j*np.sin(theta) + k*np.sin(theta)) + HEIGHT//2

                pygame.draw.polygon(
                    screen, WHITE, points + [x_center, y_center])
                pygame.draw.polygon(screen, BLACK, points +
                                    [x_center, y_center], 2)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    draw_grid(screen)

    tile = Tile(HEX_DIST_FROM_CENTER)

    arrows = create_arrows(0, ARROW_SIZE)
    for arrow in arrows:
        arrow.move([-400, 280])

    while True:

        for hexagon in tile.hexes:
            draw_polygon(screen, WHITE, BLACK, hexagon.points)

        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    tile.rotate(60)

                if event.key == pygame.K_LEFT:
                    tile.rotate(-60)

                if event.key == pygame.K_SPACE:
                    if tile.test_cordinates((GRID)):
                        tile.place(GRID)
                        for hexagon in tile.hexes:
                            draw_polygon(screen, GREEN, RED, hexagon.points)
                        tile = Tile(HEX_DIST_FROM_CENTER)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for arrow in arrows:
                    arrow.click([mouse_pos_x - CENTER_POS[0],
                                mouse_pos_y - CENTER_POS[1]], tile)

        for hexagon in tile.hexes:
            draw_polygon(screen, GREEN, RED, hexagon.points)

        for arrow in arrows:
            if arrow.point_in_polygon([mouse_pos_x - CENTER_POS[0], mouse_pos_y - CENTER_POS[1]]):
                draw_polygon(screen, GREEN, RED, arrow.points)
            else:
                draw_polygon(screen, RED, GREEN, arrow.points)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
