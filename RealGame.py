import pygame
import sys
from Player import Player

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PLAYER_SIZE = 50
GOAL_WIDTH = 100
GOAL_HEIGHT = 150

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Window setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Soccer Game')

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def update(self, players):
        self.x += self.vx
        self.y += self.vy

        # Friction/Deceleration
        self.vx *= 0.98
        self.vy *= 0.98

        # Boundary checks
        if self.x < BALL_RADIUS or self.x > WIDTH - BALL_RADIUS:
            self.vx = -self.vx
        
        if self.x < BALL_RADIUS:
            self.x = BALL_RADIUS

        if self.x > WIDTH - BALL_RADIUS:
            self.x = WIDTH - BALL_RADIUS

        if self.y < BALL_RADIUS or self.y > HEIGHT - BALL_RADIUS:
            self.vy = -self.vy

        if self.y < BALL_RADIUS:
            self.y = BALL_RADIUS

        if self.y > HEIGHT - BALL_RADIUS:
            self.y = HEIGHT - BALL_RADIUS

        for player in players:
            dist = ((player.x - self.x) ** 2 + (player.y - self.y) ** 2) ** 0.5
            if dist < BALL_RADIUS + PLAYER_SIZE // 2:
                self.vx = (self.x - player.x) / (dist+0.1) * 10
                self.vy = (self.y - player.y) / (dist+0.1) * 10

    def render(self, screen):
        pygame.draw.circle(screen, GREEN, (int(self.x), int(self.y)), BALL_RADIUS)

red1 = Player(WIDTH//4, HEIGHT//2, RED)
blue1 = Player(WIDTH*3//4, HEIGHT//2, BLUE)
red2 = Player(WIDTH//4, HEIGHT//3, RED)
blue2 = Player(WIDTH*3//4, HEIGHT//3, BLUE)
ball = Ball(WIDTH//2, HEIGHT//2)
def game_loop():

    tick =0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        red = [red1, red2]
        blue = [blue1, blue2]
        
        red1.update(ball, red, blue)
        red2.update(ball, red, blue)
        blue1.update(ball, blue, red)
        blue2.update(ball, blue, red)
        ball.update([red1, red2, blue1, blue2])

        screen.fill(WHITE)

        # Drawing goals
        pygame.draw.rect(screen, BLACK, (0, HEIGHT//2 - GOAL_HEIGHT//2, 5, GOAL_HEIGHT))
        pygame.draw.rect(screen, BLACK, (WIDTH - 5, HEIGHT//2 - GOAL_HEIGHT//2, 5, GOAL_HEIGHT))

        goal = None

        # Check for goals
        if ball.x - BALL_RADIUS <= 0 and HEIGHT//2 - GOAL_HEIGHT//2 <= ball.y <= HEIGHT//2 + GOAL_HEIGHT//2:
            print("Blue team scored!")
            ball.x, ball.y = WIDTH//2, HEIGHT//2
            ball.vx, ball.vy = 0, 0
            red1.x, red1.y = WIDTH//4, HEIGHT//2
            red2.x, red2.y = WIDTH//4, HEIGHT//3
            blue1.x, blue1.y = WIDTH*3//4, HEIGHT//2
            blue2.x, blue2.y = WIDTH*3//4, HEIGHT//3
            goal = "Blue"

        if ball.x + BALL_RADIUS >= WIDTH and HEIGHT//2 - GOAL_HEIGHT//2 <= ball.y <= HEIGHT//2 + GOAL_HEIGHT//2:
            print("Red team scored!")
            ball.x, ball.y = WIDTH//2, HEIGHT//2
            ball.vx, ball.vy = 0, 0
            red1.x, red1.y = WIDTH//4, HEIGHT//2
            red2.x, red2.y = WIDTH//4, HEIGHT//3
            blue1.x, blue1.y = WIDTH*3//4, HEIGHT//2
            blue2.x, blue2.y = WIDTH*3//4, HEIGHT//3
            goal = "Red"

        blue1.render(screen)
        blue2.render(screen)
        red1.render(screen)
        red2.render(screen)
        ball.render(screen)

        red1.post_game_loop(ball, red, blue, goal)
        red2.post_game_loop(ball, red, blue, goal)
        blue1.post_game_loop(ball, blue, red, goal)
        blue2.post_game_loop(ball, blue, red, goal)

        pygame.display.flip()
        pygame.time.Clock().tick(100000000)
        tick = tick + 1

game_loop()
