# 导入所需要的模块，其中自建的manager模块中直接导入类Havefun当中的所有方法及属性
import random, sys, copy, os, pygame, manager
from pygame.locals import *
from manager.Havefun import *

FPS = 60  # 设定一个刷新频率，一般60足够
WINWIDTH = 800  # 所创建窗口的宽度，单位像素
WINHEIGHT = 600  # 窗口高度，单位像素
HALF_WINWIDTH = int(WINWIDTH / 2) # 设置半宽与半高全局变量
HALF_WINHEIGHT = int(WINHEIGHT / 2)

# 设置整个的标题的宽度和高度
TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 40

CAM_MOVE_SPEED = 5  # how many pixels per frame the camera moves

# The percentage of outdoor tiles that have additional
# decoration on them, such as a tree or rock.
OUTSIDE_DECORATION_PCT = 20

BRIGHTBLUE = (0, 170, 255)
WHITE = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage

    # Pygame initialization and basic set up of the global variables.
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    # Because the Surface object stored in DISPLAYSURF was returned
    # from the pygame.display.set_mode() function, this is the
    # Surface object that is drawn to the actual computer screen
    # when pygame.display.update() is called.
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

    pygame.display.set_caption('Star Pusher')
    BASICFONT = pygame.font.SysFont('', 18)

    # A global dict value that will contain all the Pygame
    # Surface objects returned by pygame.image.load().
    IMAGESDICT = {'uncovered goal': pygame.image.load('./source/RedSelector.png'),
                  'covered goal': pygame.image.load('./source/Selector.png'),
                  'star': pygame.image.load('./source/Star.png'),
                  'corner': pygame.image.load('./source/Wall_Block_Tall.png'),
                  'wall': pygame.image.load('./source/Wood_Block_Tall.png'),
                  'inside floor': pygame.image.load('./source/Plain_Block.png'),
                  'outside floor': pygame.image.load('./source/Grass_Block.png'),
                  'title': pygame.image.load('./source/star_title.png'),
                  'solved': pygame.image.load('./source/star_solved.png'),
                  'princess': pygame.image.load('./source/princess.png'),
                  'boy': pygame.image.load('./source/boy.png'),
                  'catgirl': pygame.image.load('./source/catgirl.png'),
                  'horngirl': pygame.image.load('./source/horngirl.png'),
                  'pinkgirl': pygame.image.load('./source/pinkgirl.png'),
                  'rock': pygame.image.load('./source/Rock.png'),
                  'short tree': pygame.image.load('./source/Tree_Short.png'),
                  'tall tree': pygame.image.load('./source/Tree_Tall.png'),
                  'ugly tree': pygame.image.load('./source/Tree_Ugly.png')}

    # These dict values are global, and map the character that appears
    # in the level file to the Surface object it represents.
    TILEMAPPING = {'x': IMAGESDICT['corner'],
                   '#': IMAGESDICT['wall'],
                   'o': IMAGESDICT['inside floor'],
                   ' ': IMAGESDICT['outside floor']}
    OUTSIDEDECOMAPPING = {'1': IMAGESDICT['rock'],
                          '2': IMAGESDICT['short tree'],
                          '3': IMAGESDICT['tall tree'],
                          '4': IMAGESDICT['ugly tree']}

    # PLAYERIMAGES is a list of all possible characters the player can be.
    # currentImage is the index of the player's current player image.
    currentImage = 0
    PLAYERIMAGES = [IMAGESDICT['princess'],
                    IMAGESDICT['boy'],
                    IMAGESDICT['catgirl'],
                    IMAGESDICT['horngirl'],
                    IMAGESDICT['pinkgirl']]

    manager.startScreen()  # show the title screen until the user presses a key

    # Read in the levels from the text file. See the readLevelsFile() for
    # details on the format of this file and how to make your own levels.
    levels = manager.readLevelsFile('starPusherLevels.txt')
    currentLevelIndex = 0

    # The main game loop. This loop runs a single level, when the user
    # finishes that level, the next/previous level is loaded.
    while True:  # main game loop
        # Run the level to actually start playing the game:
        result = manager.runLevel(levels, currentLevelIndex)

        if result in ('solved', 'next'):
            # Go to the next level.
            currentLevelIndex += 1
            if currentLevelIndex >= len(levels):
                # If there are no more levels, go back to the first one.
                currentLevelIndex = 0
        elif result == 'back':
            # Go to the previous level.
            currentLevelIndex -= 1
            if currentLevelIndex < 0:
                # If there are no previous levels, go to the last one.
                currentLevelIndex = len(levels) - 1
        elif result == 'reset':
            pass  # Do nothing. Loop re-calls runLevel() to reset the level


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
