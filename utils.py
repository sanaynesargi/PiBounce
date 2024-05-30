from screeninfo import get_monitors


# position plot on right side of screen
def get_window_size():
    monitors = get_monitors()

    return [monitors[0].width, monitors[0].height]


w, h = get_window_size()

S_WIDTH = w//2
S_HEIGHT = h

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_COLOR = (255, 246, 0)
WALL_COLOR = (252, 225, 1)

GROUND_H = S_HEIGHT // 5
WALL_W = S_WIDTH // 10