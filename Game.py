import pygame
pygame.init()

SCREEN_WITH = 800
SCREEN_HEIGHT  = int(SCREEN_WITH * 0.8)
screen = pygame.display.set_mode((SCREEN_WITH,SCREEN_HEIGHT))
pygame.display.set_caption("My gmae Bắn Súng Đùng Đùng")


clock = pygame.time.Clock()
FPS = 60
# định nghĩa biến hành động người chơi
moving_left = False
moving_right = False

BG = (144, 201, 120)

def draw_bg():
	screen.fill(BG)

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type ,x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.char_type = char_type
        self.direction = 1
        self.flip = False
        img = pygame.image.load(f'img/{self.char_type}/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):
        # reset movement variables
        dx = 0
        dy = 0
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


player = Soldier('player',200,200,3,3)
enemy = Soldier('enemy',400,200,3,3)

run = True
while run:

    clock.tick(FPS)
    draw_bg()   
    player.draw()
    player.move(moving_left, moving_right)
    enemy.draw()
    enemy.move(moving_left, moving_right)
    
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        # Keyboard Preseses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False
        # Keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    pygame.display.update()         
                      
pygame.quit()
