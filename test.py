import pygame as pg
import numpy as np

pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
colors = [[120, 250, 90], [250, 90, 120], [255, 255, 255]]
gridarray = np.random.randint(3, size=(20, 20))
surface = pg.surfarray.make_surface(colors[gridarray])
surface = pg.transform.scale(surface, (200, 200))  # Scaled a bit.

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((30, 30, 30))
    screen.blit(surface, (100, 100))
    pg.display.flip()
    clock.tick(60)