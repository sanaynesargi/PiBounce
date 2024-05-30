import pygame


def update_c(self, other):
    t1 = False
    t2 = False

    # if (self.x + self.width + self.velocity >= other.x) and (self.x + self.velocity <= other.x + other.width):
    #     # other.x += other.velocity
    #     print("ASQSASAS", self.velocity, other.velocity)
    #     self.x += self.velocity
    #     other.x += other.velocity
    #     t1 = True
    #
    # if (other.x + other.width + other.velocity >= self.x) and (other.x + other.velocity <= self.x + self.width):
    #     print("HRERE", self.velocity, other.velocity)
    #     other.x += other.velocity
    #     self.x += self.velocity
    #     t2 = True

    self.x += self.velocity
    other.x += other.velocity


def collide_cubes(self, c2):
    self.colliding = False
    c2.colliding = False

    # Check for collision
    if (self.x + self.width >= c2.x) and (self.x <= c2.x + c2.width):
        # Elastic collision equations
        v1 = (((self.mass - c2.mass) * self.velocity) + (2 * c2.mass * c2.velocity)) / (self.mass + c2.mass)
        v2 = (((c2.mass - self.mass) * c2.velocity) + (2 * self.mass * self.velocity)) / (self.mass + c2.mass)

        self.velocity = v1
        c2.velocity = v2

        self.callback(v1, v2, self.mass, c2.mass)

        self.colliding = True
        c2.colliding = True

    if self.x < self.wall_x:
        # self.x = self.wall_x
        self.velocity = -self.velocity  # Bounce back with same speed but opposite direction
        self.callback(self.velocity, c2.velocity, self.mass, c2.mass)

        self.colliding = True
        c2.colliding = True

    # if c2.x < self.wall_x + self.width:
    #     c2.x = c2.wall_x + self.width
    #     self.colliding = True
    #     c2.colliding = True


class Cube:
    def __init__(self, window, start_x, start_y, side, mass, color, initial_vel, wall_x, collision_callback, c_w=0):
        self.width = side
        self.height = side
        self.wall_x = wall_x
        self.x = start_x
        self.y = start_y - side
        self.og_color = color
        self.color = color
        self.surface = window
        self.mass = mass
        self.velocity = initial_vel
        self.callback = collision_callback
        self.cw = c_w
        self.colliding = False

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height), 0, border_radius=5)




