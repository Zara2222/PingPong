from pygame import*

PLAYER_SIZE = (20, 100)
FPS = 60
WINDOW_SIZE = (700, 500)
VECTOR = Vector2



RED = (255, 0, 0)
DARK_RED = (181, 16, 16)

window = display.set_mode(WINDOW_SIZE)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), PLAYER_SIZE)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self,  player_image, player_x, player_y, player_speed, typee):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.typee = typee
    def update_position(self):
        keys = key.get_pressed()
        if self.typee == "left":
            if keys[K_w] and self.rect.y >= 0:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < WINDOW_SIZE[1] - self.rect.height:
                self.rect.y += self.speed
        elif self.typee == "right":
            if keys[K_UP] and self.rect.y >= 0:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < WINDOW_SIZE[1] - self.rect.height:
                self.rect.y += self.speed

        self.reset()
    
class Ball:
    def __init__(self):
        self.color = DARK_RED
        self.radius = 20
        self.speed = 10
        self.rect = Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.x = WINDOW_SIZE[0] / 2
        self.rect.y = WINDOW_SIZE[1] / 2
        self.dir = VECTOR(self.speed, self.speed / 2)

    def draw(self):
        draw.circle(window, self.color, (self.rect.x, self.rect.y), self.radius)

    def move(self, player1, player2):
        self.rect.move_ip(self.dir)

        if sprite.collide_rect(player1, self) or sprite.collide_rect(player2, self):
            self.dir[0] *= -1.1
        if self.rect.y >= WINDOW_SIZE[1] - self.radius or self.rect.y <= 0:
            self.dir[1] *= -1.1
