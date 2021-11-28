import itertools, math, random, sys, time
import pygame

# Color constants.
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Define some constants.
fps = 60
screen_scale = 2
ww, wh = screen_scale*640, screen_scale*480
gravity = 0.3
bg_color = BLACK
debug = False
wireframe_color = YELLOW

# Initialize the game.
pygame.init()
screen = pygame.display.set_mode((ww, wh))
pygame.mouse.set_visible(False)

# Load images.
ball_files = [
    'ball-beach.gif',
    'ball-cricket.png',
    'ball-exercise.png',
    'ball-foam.png',
    'ball-stripes.png',
]
ball_images = [pygame.image.load(f) for f in ball_files]


class MouseCursor:
    def __init__(self):
        self.image = pygame.image.load('thumbtack.png')
        self.rect = self.image.get_rect()
        self.offset = (19, 0)

    @property
    def x(self):
        return pygame.mouse.get_pos()[0]

    @property
    def y(self):
        return pygame.mouse.get_pos()[1]

    def draw(self):
        self.rect.x = self.x - self.offset[0]
        self.rect.y = self.y - self.offset[1]
        screen.blit(self.image, self.rect)


cursor = MouseCursor()


class Thing:
    def __init__(self, rect, mass=None, bounce_coeff=(1, 1)):
        self.rect = rect
        self.mass = mass if mass is not None else rect.width * rect.height
        self.velocity = [0, 0]
        self.bounce_coeff = bounce_coeff # HACK for collision with non-round objects.

    @property
    def alive(self):
        return self.rect.width > 0 and self.rect.height > 0

    @property
    def dims(self):
        return len(self.velocity)

    @property
    def cx(self):
        return self.rect.x + self.rect.width / 2

    @property
    def cy(self):
        return self.rect.y + self.rect.width / 2

    def accelerate(self, vector):
        for i in range(self.dims): self.velocity[i] += vector[i]

    def move(self):
        # Move at the current trajectory.
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def collide(self, other):
        # Crash two things into each other.
        if self.rect.colliderect(other.rect):
            nv_self = Thing._bounce(self.mass, other.mass, self.velocity, other.velocity)
            nv_other = Thing._bounce(other.mass, self.mass, other.velocity, self.velocity)
            self.velocity = [other.bounce_coeff[i] * nv_self[i] for i in range(self.dims)]
            other.velocity = [self.bounce_coeff[i] * nv_other[i] for i in range(self.dims)]

    @staticmethod
    def _bounce(m1, m2, v1, v2):
        # Conservation of momentum: m1*v1 + m2*v2 = m1*nv1 + m2*nv2
        # where m is mass, v is current velocity, and nv is new velocity
        # -> nv1 = [2*m2*v2 + v1*(m1 - m2)] / (m1 + m2)
        # -> nv2 = [2*m1*v1 + v2*(m2 - m1)] / (m1 + m2)
        # Credit: https://www.toppr.com/guides/physics/work-energy-and-power/collisions/
        return [(2*m2*v2[i] + v1[i]*(m1 - m2)) / (m1 + m2) for i in range(len(v1))]

    def draw(self):
        if debug:
            # In debug mode, draw a wireframe around the object.
            tl = (self.rect.x, self.rect.y)
            tr = (self.rect.x + self.rect.width - 1, self.rect.y)
            bl = (self.rect.x, self.rect.y + self.rect.height - 1)
            br = (self.rect.x + self.rect.width - 1, self.rect.y + self.rect.height - 1)
            pygame.draw.line(screen, wireframe_color, tl, tr)
            pygame.draw.line(screen, wireframe_color, tr, br)
            pygame.draw.line(screen, wireframe_color, br, bl)
            pygame.draw.line(screen, wireframe_color, bl, tl)


class Wall(Thing):
    def __init__(self, x, y, w, h, coeff):
        Thing.__init__(self, rect=pygame.Rect(x, y, w, h), bounce_coeff=coeff)

    def move(self):
        # Walls don't move!
        self.velocity = [0, 0]


class Poppable(Thing):
    def __init__(self, image):
        self.image = image
        Thing.__init__(self, self.image.get_rect())
        # Start in a random location.
        self.rect.x = random.randint(0, ww - self.rect.width)
        self.rect.y = random.randint(0, wh - self.rect.height)
        # Start with a random velocity in [-1, 1].
        self.velocity[0] = 2 * random.random() - 1
        self.velocity[1] = 2 * random.random() - 1
        self.dying = False

    def move(self):
        # If mouse is inside the poppable thing...
        if self.rect.collidepoint(cursor.x, cursor.y):
            self.dying = True

        if self.dying:
            # Crunch it!
            self.scale(0.9)

        # Then move like usual.
        Thing.move(self)

        # And slow down a little from friction / air resistance / etc.
        for i in range(self.dims): self.velocity[i] *= 0.999

    def draw(self):
        screen.blit(self.image, self.rect)
        Thing.draw(self)

    def scale(self, factor):
        nw = int(factor * self.rect.width)
        nh = int(factor * self.rect.height)
        self.image = pygame.transform.scale(self.image, (nw, nh))
        self.rect.x += (self.rect.width - nw) / 2
        self.rect.y += (self.rect.height - nh) / 2
        self.rect.width = nw
        self.rect.height = nh


class Balloon(Poppable):
    def __init__(self, color, label, offset, action):
        Poppable.__init__(self, pygame.image.load(f"balloon-{color}.png"))
        self.label = label
        self.font = pygame.font.SysFont(None, 14 * screen_scale)
        self.size = self.font.size(self.label)
        self.action = action

    def move(self):
        # Gently float around.
        for i in range(self.dims):
            self.velocity[i] += (random.random() - 0.5)
            self.velocity[i] = min(self.velocity[i], 2)
            self.velocity[i] = max(self.velocity[i], -2)

        Poppable.move(self)

    def draw(self):
        Poppable.draw(self)
        # Center the label over the balloon with an outline.
        x = self.rect.x + (self.rect.width - self.size[0]) / 2
        y = self.rect.y + (self.rect.height - self.size[1]) / 2
        label_image_bg = self.font.render(f'{self.label}', True, BLACK)
        label_image_fg = self.font.render(f'{self.label}', True, WHITE)
        for dx in (-2, -1, 0, 1, 2):
            for dy in (-2, -1, 0, 1, 2):
                screen.blit(label_image_bg, (x + dx, y + dy))
        screen.blit(label_image_fg, (x, y))

    def scale(self, factor):
        Poppable.scale(self, factor)
        if not self.alive:
            self.action()


class Ball(Poppable):
    def __init__(self):
        Poppable.__init__(self, random.choice(ball_images))

        # GIANT BALLS OMG
        #self.scale(factor=2)

    def move(self):
        # Respond to the mouse's gravitational pull.
        ax = gravity / abs((cursor.x - self.cx) / ww + 1) ** 2
        ay = gravity / abs((cursor.y - self.cy) / wh + 1) ** 2
        if cursor.x < self.rect.x: ax = -ax
        if cursor.y < self.rect.y: ay = -ay
        self.accelerate((ax, ay))

        # And then move like normal.
        Poppable.move(self)


class Stopwatch:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 24 * screen_scale)
        self.elapsed = None
        self.running = False

    def start(self):
        self.initial = time.time_ns()
        self.elapsed = 0
        self.running = True

    def stop(self):
        self.initial = None
        self.running = False

    def draw(self):
        if self.elapsed is None: return # never started
        if self.running:
            self.elapsed = (time.time_ns() - self.initial) / 1000000000
        img = self.font.render(f'{self.elapsed:.3f}', True, WHITE)
        screen.blit(img, (ww - img.get_width() - 20, 20))


def main():
    # Start the music!
    # TODO: Why doesn't this work?
    #pygame.mixer.music.load("hamster.mid")
    #pygame.mixer.music.play()

    walls = [
        Wall(-ww, -wh, 3 * ww,     wh, (-1, 1)), # top wall
        Wall(-ww,  wh, 3 * ww,     wh, (-1, 1)), # bottom wall
        Wall(-ww, -wh,     ww, 3 * wh, (1, -1)), # left wall
        Wall( ww, -wh,     ww, 3 * wh, (1, -1)), # right wall
    ]

    clock = pygame.time.Clock()
    stopwatch = Stopwatch()
    objects = []

    def start_game(ball_count):
        objects.clear()
        objects.extend(walls)
        for i in range(ball_count): objects.append(Ball()) # balls to the walls!
        stopwatch.start()

    def quit_game():
        sys.exit()

    def title_screen():
        objects.clear()
        objects.extend(walls)
        objects.append(Balloon("blue", "5", [55, 80], lambda: start_game(5)))
        objects.append(Balloon("yellow", "10", [45, 80], lambda: start_game(10)))
        objects.append(Balloon("red", "15", [55, 80], lambda: start_game(15)))
        objects.append(Balloon("purple", "Quit", [55, 80], lambda: quit_game()))
        stopwatch.stop()

    title_screen()

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: quit_game()

        # move objects
        for obj in objects: obj.move()

        # collision detection
        for obj1, obj2 in itertools.combinations(objects, 2):
            obj1.collide(obj2)

        # remove dead objects
        objects = [obj for obj in objects if obj.alive]
        if len(objects) <= len(walls):
            # No more objects left. Game over!
            title_screen()

        # redraw scene
        screen.fill(bg_color)
        cursor.draw()
        stopwatch.draw()
        for obj in objects: obj.draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()
