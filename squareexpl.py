import numpy as np
import pygame
from networkx.generators.lattice import grid_graph
from pygame import Surface, surface, math
from pygame.examples.moveit import WIDTH
import random

from sympy import vectorize
import math
import time
import cProfile
import timeit
import numpy as np
pygame.init()

WIDTH = 1100
HEIGHT = 800
FPS = 60

GRID_SIZE = 8
SQUARE_SIZE = 320
CELL_SIZE = SQUARE_SIZE // GRID_SIZE

GRAVITY = 450

BACKGROUND = (30, 20, 20)
SQUARE_COLOR = (245, 245, 255)
GRID_COLOR = (50, 50, 60)

square_position = None

Square_base = SQUARE_SIZE * GRID_SIZE / HEIGHT

class Fragment:

    def __init__(self, position, size):
        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(0, 0)
        self.size = size


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square Explosion")
clock = pygame.time.Clock()

square = pygame.Rect(
    (WIDTH - SQUARE_SIZE) // 2,
    (HEIGHT - SQUARE_SIZE) // 2,
    SQUARE_SIZE,
    SQUARE_SIZE
)

square_position = pygame.math.Vector2(square.x, square.y)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):

            x = square.x + col * CELL_SIZE
            y = square.y + row * CELL_SIZE

            cell = pygame.Rect(
                x,
                y,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(screen, SQUARE_COLOR, cell)
            pygame.draw.rect(screen, GRID_COLOR, cell, 1)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
