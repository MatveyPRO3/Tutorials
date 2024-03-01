import pygame
import pymunk
import pymunk.pygame_util
from random import randint, random
from math import atan2, dist, cos, sin, pi, sqrt
from math import isinf

pygame.init()

WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)


def draw(space, window, draw_options):
    window.fill("white")

    space.debug_draw(draw_options)

    pygame.display.update()


G = 1


def gravity_velocity(body, gravity, damping, dt):
    gravity = pygame.Vector2(0, 0)
    for another_body in space.bodies:
        if another_body is body or another_body.body_type is pymunk.Body.STATIC:
            continue
        force = G*body.mass*another_body.mass / \
            dist(body.position, another_body.position)**2
        angle = atan2(another_body.position[1]-body.position[1],
                      another_body.position[0]-body.position[0])
        acceleration = force/body.mass
        gravity += pygame.Vector2(cos(angle)*acceleration,
                                  sin(angle)*acceleration)

    pymunk.Body.update_velocity(body, tuple(gravity), damping, dt)


def create_ball(space, radius, mass, pos):
    body = pymunk.Body()
    body.position = pos
    body.velocity_func = gravity_velocity
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.elasticity = 0.999999
    shape.friction = 0.2
    shape.color = (randint(0, 255), randint(0, 255), randint(0, 255), 100)
    space.add(body, shape)
    return body


def get_total_impulse(space):
    total_impulse = [0, 0]
    for body in space.bodies:
        if not isinf(body.mass):
            total_impulse += body.velocity*body.mass
    return total_impulse


def create_boundaries(space, width, height):
    rects = [
            [(width//2, height - 10), (width, 20)],
            [(width//2, 10), (width, 20)],
            [(10, height//2), (20, height)],
            [(width - 10, height//2), (20, height)]
    ]

    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)


clock = pygame.time.Clock()
fps = 60
dt = 1 / fps
balls = []

space = pymunk.Space()
# space.gravity = (0, 981)

draw_options = pymunk.pygame_util.DrawOptions(window)

# create_boundaries(space, WIDTH, HEIGHT)


create_ball(space,50,500*pi*50**2,(300,200))
for _ in range(3):
    ball = create_ball(space, r := 5, 500*pi*r **
                       2, (randint(10, WIDTH), randint(10, HEIGHT)))
    ball.apply_impulse_at_local_point((700000, -1800000))

while 1:

    impulse = list(get_total_impulse(space))
    impulse = list(map(round, impulse, [8 for _ in range(2)]))
    print(impulse, sqrt(impulse[0]**2+impulse[1]**2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit()
    draw(space, window, draw_options)
    space.step(dt)
    clock.tick(fps)
