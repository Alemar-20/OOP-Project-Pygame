SCREENWIDTH = 1280
SCREENHEIGHT = 692

# GAME FRAMES PER SECONDS
FPS = 60

# ACTUAL SPRITE SIZE FROM YOUR SHEET
SPRITE_WIDTH = 32.5   # Most common size for this style
SPRITE_HEIGHT = 32.125

# GAME MATRIX 
SIZE = 64  # SIZE OF EACH TILE IN PIXELS
#SIZE = 32  # SIZE OF EACH TILE IN PIXELS
# SIZE = 48  # SIZE OF EACH TILE IN PIXELS
# SIZE = 96  # SIZE OF EACH TILE IN PIXELS


# COLOURS
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
LIGHTGREEN = (144, 238, 144)
DARKGREY = (64, 64, 64)
LIGHTGREY = (192, 192, 192)

# SPRITE COORDINATES
# PLAYER = {"walk_left":[(0,1),(0,0),(0,2)],
#           "walk_down":[(0,4),(0,3),(0,5)],
#           "walk_right":[(0,7),(0,6),(0,8)],
#           "walk_up":[(0,10),(0,9),(0,11)],
#           "dead_anim":[(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6)]} 


# SPRITE COORDINATES

PLAYER = {
    # Row 0: Walking
    "walk_down": [(0, 4), (0, 3), (0, 5)], 
    "walk_left": [(0, 1), (0, 0), (0, 2)],
    "walk_right": [(0, 7), (0, 6), (0, 8)],
    "walk_up": [(0, 10), (0, 9), (0, 11)],
    
    # Row 2: Idling (Assuming these are the stand-still frames)
    "idle_down": [(2, 3)],
    "idle_left": [(2, 0)],
    "idle_right": [(2, 6)],
    "idle_up": [(2, 9)],
    
    # Row 1: Dead/Vulnerable (Adjusting based on observation)
    "dead_anim": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)], 
    
    # Row 3: Bomb/Kick Animation (Example)
    "kick_anim": [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)],
    
    # Row 4: Happy/Win
    "win_anim": [(4, 0), (4, 1), (4, 2), (4, 3)],
    
    # Row 5: Sleep
    "sleep_anim": [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4)],
}
