import pygame
from character import Character
import gamesetting as gs

class Game:
  def __init__(self, main, assets):
    # LINK WITH MAIN CLASS AND ASSETS
    self.MAIN = main
    self.ASSETS = assets

    self.PLAYER = Character(self,self.ASSETS.player_char)


  def input(self):
    # for event in pygame.event.get():
    #   # CHECK IF RED CROSS IS CLICKED
    #   if event.type == pygame.QUIT:
    #     self.MAIN.running = False  
    #   elif event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_ESCAPE:
    #       self.MAIN.running = False
    self.PLAYER.input()

  def update(self):
    self.PLAYER.update()


  def draw(self,window):
    # self.PLAYER.draw(window)
    self.PLAYER.draw(window)
