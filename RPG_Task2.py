import pygame

# Global varaible

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)


# initialise PyGame
pygame.init()

# Walls
wall_size = (10,10)

# Screen
size = (500,500)
screen = pygame.display.set_mode(size)

# Class of Player
class Player(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,color,width,height):
        super().__init__()
        self.speed = 0
        self.Hori = True 
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = size[0]/2
        self.rect.y = size[1]/2
        self.width = width
        self.height = height

    def update(self):
        if self.Hori:
            self.rect.x = self.rect.x + self.speed
            if self.rect.x > size[0]- wall_size[0] - self.height:
                self.rect.x = size[0]- wall_size[1] - self.height
            elif self.rect.x < wall_size[0]:
                self.rect.x = wall_size[0]
        else:
            self.rect.y = self.rect.y + self.speed
            if self.rect.y > size[1] - wall_size[1] - self.width:
                self.rect.y = size[1] - wall_size[1] - self.width
            elif self.rect.y < wall_size[1]:
                self.rect.y = wall_size[1]
        
    
    def player_set_speed(self,speed):
        self.speed = speed


# Class of wall
class Wall(pygame.sprite.Sprite):
    def __init__(self,color,width,height,x_pos,y_pos):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos



# Title of window
pygame.display.set_caption('Title')

# Exit Game Flag
done = False

# Manage how fast screen refreshes
clock = pygame.time.Clock()

# create a list of walls
walls_group = pygame.sprite.Group()


all_sprites_group = pygame.sprite.Group()
player = Player(WHITE,10,10)
all_sprites_group.add(player)

# addition of all walls into the group
x_pos = 0

while True:
    if x_pos > size[0]:
        break
    elif x_pos == 0 or x_pos == size[0] - wall_size[0]:
        for y_pos in range(size[1]):
            wall = Wall(RED,wall_size[0],wall_size[1],x_pos,y_pos)
            walls_group.add(wall)
            all_sprites_group.add(wall)
    else:
        for y_pos in [0,size[1] - wall_size[1]]:
            wall = Wall(RED,wall_size[0],wall_size[1],x_pos,y_pos)
            walls_group.add(wall)
            all_sprites_group.add(wall)
    x_pos += 1

# Game loop
while not done:
    # User input and controls
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                player.player_set_speed(-20)
                player.Hori = True
            elif event.key == pygame.K_RIGHT:
                player.player_set_speed(20)
                player.Hori = True
            elif event.key == pygame.K_UP:
                player.player_set_speed(-20)
                player.Hori = False
            elif event.key == pygame.K_DOWN:
                player.player_set_speed(20)
                player.Hori = False
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]:
                player.player_set_speed(0)
                
    # Game logic    
    all_sprites_group.update()
    


    screen.fill(BLACK)

    all_sprites_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
                

    
    
