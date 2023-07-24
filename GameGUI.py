import pygame

class GameGUI:
    def __init__(self):
        pygame.init()
        self.window_width = 960
        self.window_height = 960

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        # bg is too bright
        background_image = pygame.image.load("wood_texture.jpeg")
        self.window.blit(background_image, (0, 0))

        pygame.display.set_caption("Parcheesi")

        self.step_long_dim = 130
        self.step_short_dim = 30

        self.red = (220, 50, 50)
        self.blue = (50, 50, 220)
        self.green = (5, 130, 50)
        self.yellow = (220, 220, 0)
        self.default_color = (50, 50, 50) # black
        # self.default_color = (220, 220, 220) # white
        self.bottom_edge = self.window_height - self.step_short_dim - 20
        self.top_edge = 20
        self.left_edge = 20
        self.right_edge = self.window_width - self.step_short_dim - 20
        self.horizontal_center = (self.window_width - self.step_long_dim)/2
        self.vertical_center = (self.window_height - self.step_long_dim)/2

        self.draw_steps()
        pygame.display.flip()

        # loop until window is closed
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
                # if you close window, close game
                if event.type == pygame.QUIT:
                    running = False

    def draw_steps(self):
        self.draw_horizontal_steps()
        self.draw_vertical_steps()
        self.draw_jails()
        # self.draw_diagonal_steps()

    def draw_horizontal_step(self, color, x_coord, y_coord):
        pygame.draw.rect(self.window, color, pygame.Rect(x_coord, y_coord, self.step_long_dim, self.step_short_dim), 2)
        pygame.draw.rect(self.window, color, pygame.Rect(x_coord-2, y_coord-2, self.step_long_dim+4, self.step_short_dim+4), 2)

    def draw_vertical_step(self, color, x_coord, y_coord):
        pygame.draw.rect(self.window, color, pygame.Rect(x_coord, y_coord, self.step_short_dim, self.step_long_dim), 2)
        pygame.draw.rect(self.window, color, pygame.Rect(x_coord-2, y_coord-2, self.step_short_dim+4, self.step_long_dim+4), 2)

    def draw_horizontal_steps(self):
        # bottom half of board
        # draw yellow finish steps
        color = self.yellow
        x_coord = self.horizontal_center
        y_coord = self.bottom_edge
        for i in range(8):
            self.draw_horizontal_step(color, x_coord, y_coord)
            y_coord -= self.step_short_dim + 10
        # draw surrounding horizontal steps
        color = self.default_color
        x_coord = self.horizontal_center + self.step_long_dim + 20
        y_coord = self.bottom_edge
        # to yellow start
        for i in range(5):
            if i == 4:
                color = self.yellow
            self.draw_horizontal_step(color, x_coord, y_coord)
            y_coord -= self.step_short_dim + 10
        # to green end
        color = self.default_color
        x_coord = self.horizontal_center - self.step_long_dim - 20
        y_coord = self.bottom_edge
        for i in range(5):
            if i == 4:
                color = self.green
            self.draw_horizontal_step(color, x_coord, y_coord)
            y_coord -= self.step_short_dim + 10
            
        # top half of board
        # draw blue finish steps
        color = self.blue
        x_coord = self.horizontal_center
        y_coord = self.top_edge
        for i in range(8):
            self.draw_horizontal_step(color, x_coord, y_coord)
            y_coord += self.step_short_dim + 10
        # to blue start
        color = self.default_color
        x_coord = self.horizontal_center - self.step_long_dim - 20
        y_coord = self.top_edge
        for i in range(5):
            if i == 4:
                color = self.blue
            self.draw_horizontal_step(color, x_coord, y_coord)
            y_coord += self.step_short_dim + 10
        # to red end
        color = self.default_color
        x_coord = self.horizontal_center + self.step_long_dim + 20
        y_coord = self.top_edge
        for i in range(5):
            if i == 4:
                color = self.red
            self.draw_horizontal_step(color, x_coord, y_coord)
            y_coord += self.step_short_dim + 10

    def draw_vertical_steps(self):
        # left half of board
        # draw green finish steps
        color = self.green
        x_coord = self.left_edge
        y_coord = self.vertical_center
        for i in range(8):
            self.draw_vertical_step(color, x_coord, y_coord)
            x_coord += self.step_short_dim + 10
        # to blue end
        color = self.default_color
        x_coord = self.left_edge
        y_coord = self.vertical_center - self.step_long_dim - 20
        for i in range(5):
            if i == 4:
                color = self.blue
            self.draw_vertical_step(color, x_coord, y_coord)
            x_coord += self.step_short_dim + 10
        # to green start
        color = self.default_color
        x_coord = self.left_edge
        y_coord = self.vertical_center + self.step_long_dim + 20
        for i in range(5):
            if i == 4:
                color = self.green
            self.draw_vertical_step(color, x_coord, y_coord)
            x_coord += self.step_short_dim + 10

        # right half of board
        # draw red finish steps
        color = self.red
        x_coord = self.right_edge
        y_coord = self.vertical_center
        for i in range(8):
            self.draw_vertical_step(color, x_coord, y_coord)
            x_coord -= self.step_short_dim + 10
        # to red start
        color = self.default_color
        x_coord = self.right_edge
        y_coord = self.vertical_center - self.step_long_dim - 20
        for i in range(5):
            if i == 4:
                color = self.red
            self.draw_vertical_step(color, x_coord, y_coord)
            x_coord -= self.step_short_dim + 10
        # to yellow end
        color = self.default_color
        x_coord = self.right_edge
        y_coord = self.vertical_center + self.step_long_dim + 20
        for i in range(5):
            if i == 4:
                color = self.yellow
            self.draw_vertical_step(color, x_coord, y_coord)
            x_coord -= self.step_short_dim + 10

    def draw_diagonal_steps(self):
        pass

    def draw_jails(self):
        # red jail
        pygame.draw.rect(self.window, self.red, pygame.Rect(self.right_edge - 150, self.bottom_edge - 150, 150, 150), 2)
        pygame.draw.rect(self.window, self.red, pygame.Rect(self.right_edge - 152, self.bottom_edge - 152, 154, 154), 2)

        pygame.draw.rect(self.window, self.red, pygame.Rect(self.right_edge - 160, self.bottom_edge - 160, 150, 150), 2)
        pygame.draw.rect(self.window, self.red, pygame.Rect(self.right_edge - 162, self.bottom_edge - 162, 154, 154), 2)
        # blue jail

        # green jail

        # yellow jail

        # make all of these with the corners facing the centre of the board
