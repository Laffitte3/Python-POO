import pygame,random

pygame.init()


WINDOW_WIDTH= 800
WINDOW_HEIGHT=600

display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

FPS=60
clock=pygame.time.Clock()

#Define classes

class Monster(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.image.load("blue_monster.png")
        self.rect= self.image.get_rect()
        self.rect.topleft=(x,y)

        self.velocity = random.randint(1,5)

    def update(self):
        """Update and Move the monster"""
        self.rect.y += self.velocity


class Player(pygame.sprite.Sprite):

    def __init__(self,x,y,monster_group):

        super().__init__()

        self.image=pygame.image.load("knight.png")
        self.rect= self.image.get_rect()
        self.rect.topleft=(x,y)

        self.velocity=5
        self.monster_group= monster_group

    def update(self):

        self.move()
        self.check_collisions()

    def move(self):
        """Move the player"""

        keys= pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity

        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity

        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity

    def check_collisions(self):
        
        if pygame.sprite.spritecollide(self,self.monster_group,True):
            print(len(self.monster_group))

#Create a monster group an add 10 monster

monster_group= pygame.sprite.Group()
player_group=pygame.sprite.Group()

player=Player(64,400,monster_group)
player_group.add(player)


for i in range(10):
    monster=Monster(i*64,32)
    monster_group.add(monster)

    
running = True

while running:

    monster_group.update()
    player_group.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    display_surface.fill((0,0,0))

    monster_group.draw(display_surface)
    player_group.draw(display_surface)

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()