import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Bomba Na!") #yung sa window


class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    def update(self):
        pass
    
class Player(GameObject):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def update(self):
      old_x = self.rect.x
      old_y = self.rect.y

      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
          self.rect.x -= self.speed
      if keys[pygame.K_RIGHT]:
          self.rect.x += self.speed
      if keys[pygame.K_UP]:
          self.rect.y -= self.speed
      if keys[pygame.K_DOWN]:
          self.rect.y += self.speed


      # Tingnan kung may banggaan sa obstacles pahirozontal
      for obstacle in obstacles:
        if self.rect.colliderect(obstacle.rect):
            # Ibalik sa dating posisyon kung may banggaan
            self.rect.x = old_x
            break

      # Tingnan kung may banggaan sa obstacles pahirozontal
      for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                # Ibalik sa dating posisyon kung may banggaan
                self.rect.y = old_y
                break  

          # Panatilihing nasa loob ng screen ang player
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > 1000:
                self.rect.right = 800
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > 600:
                self.rect.bottom = 600


class Wall(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def update(self):
        pass




all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

player = Player(85, 85)
wall1 = Wall(500, 50, 500, 50)
wall2 = Wall(385, 50, 50, 300)
wall3 = Wall(385, 400, 200, 50)
wall4 = Wall(700, 150, 50, 300)
wall5 = Wall(600, 150, 100, 50)


all_sprites.add(player, wall1, wall2, wall3, wall4, wall5)
obstacles.add(wall1, wall2,wall3, wall4, wall5)

clock = pygame.time.Clock()
running = True
collision_message = ""
message_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    if pygame.sprite.spritecollide(player, obstacles, False):
        collision_message = "Banggaan!"
        print(collision_message)
        message_timer = 60  # Ipakita ang mensahe sa loob ng 60 frames


    if message_timer > 0:
        message_timer -= 1
        if message_timer == 0:
            collision_message = ""    

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    if collision_message:
        font = pygame.font.Font(None,36)
        text = font.render(collision_message, True, (255,0,0))        
        screen.blit(text, (400, 50))

    font_small = pygame.font.Font(None, 24)
    instructions = font_small.render("Gamitin ang arrow keys para gumalaw", True, (0, 0, 0))
    screen.blit(instructions, (350, 18))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()    
