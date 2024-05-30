

COLLISIONS = 0


def increment_collisions(v1, v2, m1, m2):
    global COLLISIONS

    COLLISIONS += 1

    # print(COLLISIONS)

    with open("data.txt", "a") as data:
        data.write(f"{v1}, {v2}, {m1}, {m2}\n")


def run_sim(pow):
    import pygame
    import os

    from utils import GROUND_H, WHITE, BLACK, S_WIDTH, S_HEIGHT, GROUND_COLOR, WALL_COLOR, WALL_W
    from Ground import Ground
    from Wall import Wall
    from Cube import Cube, update_c, collide_cubes

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)

    pygame.init()

    WIN = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    CLOCK = pygame.time.Clock()

    GROUND = Ground(WIN, S_WIDTH, S_HEIGHT, GROUND_H, GROUND_COLOR)
    WALL = Wall(WIN, S_WIDTH, S_HEIGHT, WALL_W, GROUND_H, WALL_COLOR)

    COLL_FONT = pygame.font.SysFont("ComicSans", 25)

    speed_mass_ratio = pow
    C_1_W = 25
    C_2_W = WALL_W * speed_mass_ratio

    CUBE1 = Cube(WIN, WALL_W + 40, S_HEIGHT - GROUND_H, C_1_W, 1, WHITE, 0, WALL_W, increment_collisions)
    CUBE2 = Cube(WIN, WALL_W + 140, S_HEIGHT - GROUND_H, C_2_W, 100 ** speed_mass_ratio, WHITE, -0.1, WALL_W,
                 increment_collisions,
                 C_1_W)

    def draw():
        WIN.fill(BLACK)
        GROUND.draw()
        WALL.draw()
        CUBE1.draw()
        CUBE2.draw()

        text = COLL_FONT.render(f"Collisions: {COLLISIONS}", True, WHITE)
        WIN.blit(text, (S_WIDTH * 3 / 8, S_HEIGHT * 1 / 8))

        pygame.display.update()

    def update():
        update_c(CUBE1, CUBE2)
        collide_cubes(CUBE1, CUBE2)

    def start():
        pygame.display.set_caption("PiBounce")

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False

            update()
            draw()
            CLOCK.tick(60)

    start()
