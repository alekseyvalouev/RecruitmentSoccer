import pygame

WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PLAYER_SIZE = 50

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def controlled_move(self, keys):
        speed = 1  # You can adjust this for faster/slower movement
        vx = 0
        vy = 0
        if keys[pygame.K_UP]:
            vy = -speed
        if keys[pygame.K_DOWN]:
            vy = speed
        if keys[pygame.K_LEFT]:
            vx = -speed
        if keys[pygame.K_RIGHT]:
            vx = speed
        self.update_velocity(vx, vy)

    def update_velocity(self, vx, vy):
        self.vx = vx
        self.vy = vy
        self.x += self.vx * 5
        self.y += self.vy * 5

        # Boundary checks
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH:
            self.x = WIDTH
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT:
            self.y = HEIGHT
    
    def update(self, ball, friendly_players, enemy_players):
        if ball.x > self.x:
            vx = 1
        elif ball.x < self.x:
            vx = -1
        else:
            vx = 0

        if ball.y > self.y:
            vy = 1
        elif ball.y < self.y:
            vy = -1
        else:
            vy = 0

        self.update_velocity(vx, vy)

    # runs after all players have moved
    def post_game_loop(self, ball, friendly_players, enemy_players, scored):
        pass

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x - PLAYER_SIZE // 2, self.y - PLAYER_SIZE // 2, PLAYER_SIZE, PLAYER_SIZE))
