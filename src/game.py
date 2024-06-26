import pygame

from src.player import Player
from src.scene.sceneManager import SceneManager
from src.utils.fontHelper import initFonts

"""Game class defines global variables and game loop
"""

class Game:
    SCREEN_WIDTH=1000
    SCREEN_HEIGHT=800
    FPS=144
    WINDOW_TITLE="Plane Game"
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()
    player = Player()
    running = True
    
    def __init__(self):
        pygame.init()
        initFonts()
        self.sceneManager = SceneManager(Game.screen)
        
    def onEvents(self):
        self.sceneManager.onKeyDown(pygame.key.get_pressed())
        for event in pygame.event.get():
            if event.type == pygame.QUIT or not Game.running:
                self.quitGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sceneManager.onClick(event.pos)
            else:
                self.sceneManager.onEvent(event.type)
                
    def gameLoop(self):
        while Game.running:
            self.onEvents()
            self.sceneManager.onTick()
            pygame.display.flip()
            Game.clock.tick(Game.FPS)

    def quitGame(self):
        pygame.quit()