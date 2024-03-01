import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))


def draw(space, window, draw_options):
    window.fill("white")

    space.debug_draw(draw_options)

    pygame.display.update()


def create_ball(space, radius, mass, pos):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.elasticity = 0.9
    shape.friction = 0.4
    shape.color = (255, 0, 0, 100)
    space.add(body, shape)
    return shape


clock = pygame.time.Clock()
fps = 60
dt = 1 / fps

space = pymunk.Space()
space.gravity = (0, 981)

draw_options = pymunk.pygame_util.DrawOptions(window)

create_ball(space,50,100,(250,350))

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit()

    draw(space, window, draw_options)
    space.step(dt)
    clock.tick(fps)

pygame.quit()
