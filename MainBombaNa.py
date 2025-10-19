import pygame
from assets import Assets
from game import Game
import gamesetting as gs

class Bomberman:
  def __init__(self):
    pygame.init()

    self.screen = pygame.display.set_mode((gs.SCREENWIDTH, gs.SCREENHEIGHT))
    pygame.display.set_caption("Bomba~ Na!")

    self.ASSETS = Assets()
    self.GAME = Game(self, self.ASSETS)
    self.FPS = pygame.time.Clock()

    self.running = True


  def input(self):
    # for event in pygame.event.get():
    #   if event.type == pygame.QUIT:
    #     self.running = False
    self.GAME.input()
        

  def update(self):
    self.FPS.tick(gs.FPS)

  def draw(self,window):
    window.fill(gs.BLACK)
    # window.blit(self.ASSETS.sprite_sheet,(0,0))
    self.GAME.draw(window)
    pygame.display.update()

  def rungame(self):
    while self.running == True:
      self.input()
      self.update()
      self.draw(self.screen)    

if __name__ == "__main__":
  game = Bomberman()
  game.rungame()
  pygame.quit()
