import pygame,random

pygame.init()


WINDOW_WIDTH= 800
WINDOW_HEIGHT=600

display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

FPS=60
clock=pygame.time.Clock()

#Define classes

class Game():
    def __init__(self,monster_group,knight_group):

        self.monster_group=monster_group
        self.knight_group=knight_group

    def update(self):
        self.check_collisions()

    def check_collisions(self):

        pygame.sprite.groupcollide(self.knight_group,self.monster_group,False,True)
        

class Monster(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.image = pygame.image.load("blue_monster.png")
        self.rect= self.image.get_rect()
        self.rect.topleft=(x,y)

        self.velocity = random.randint(1,5)

    def update(self):
        """Update and Move the monster"""
        self.rect.y += self.velocity

        
class Knight(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.image=pygame.image.load("knight.png")
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

        self.velocity= random.randint(1,5)

    def update(self):

        self.rect.y -= self.velocity

#create monster group
monster_group=pygame.sprite.Group()
for i in range(10):
    monster=Monster(i*80,32)
    monster_group.add(monster)

#create Knight group
knight_group=pygame.sprite.Group()
for i in range(10):
    knight=Knight(i*80,WINDOW_HEIGHT-64)
    knight_group.add(knight)

#create a game object
my_game=Game(monster_group,knight_group)
running = True

while running:

    monster_group.update()
    knight_group.update()
    my_game.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    display_surface.fill((0,0,0))
    monster_group.draw(display_surface)
    knight_group.draw(display_surface)
    

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()