import pygame
import game_config as gc

from pygame import display, event, image
from time import sleep
from animal import Animal

def find_index_from_xy(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return row, col, index
def showGameOverScreen():
	gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
	gameOverText = gameOverFont.render('Game Over', True, (0,200,100))
	gameOverRect = gameOverText.get_rect()
	totalscoreFont = pygame.font.Font('freesansbold.ttf', 40)
	gameOverRect.midtop = (300, 230)
	
	screen.blit(gameOverText, gameOverRect)
	pygame.display.update()
pygame.init()
display.set_caption('My Game')
screen = display.set_mode((gc.SCREEN_SIZE, gc.SCREEN_SIZE))
point = image.load('other_assets/point.png')
pygame.mixer.init()
match_sound = pygame.mixer.Sound(r"sound/click sound.wav")
running = True
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
current_images_displayed = []

while running:
    current_events = event.get()
#to quit the game window
    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
#to get the position of mouse to use it with index of image
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row, col, index = find_index_from_xy(mouse_x, mouse_y)
            #for displaying only 2 images of animals at a time
            if index not in current_images_displayed: #to avoid getting point when we click on same image 
                if len(current_images_displayed) > 1:
                    current_images_displayed = current_images_displayed[1:] + [index]
                else:
                    current_images_displayed.append(index)

    # Display animals
    screen.fill((0,0,0))

    total_skipped = 0
# now decide that the box will be image of animal or will be filled box
    for i, tile in enumerate(tiles):
        current_image = tile.image if i in current_images_displayed else tile.box
        #to check if image of animal is not displayed skip is the method defined in animal file
        if not tile.skip:
            screen.blit(current_image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped += 1 #to append index when mouse button is clicked

    display.flip()

    # Check for matches
    if len(current_images_displayed) == 2:
        idx1, idx2= current_images_displayed
        if (tiles[idx1].name == tiles[idx2].name):
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            
            # display point message
            sleep(0.2)
            #(image,(dist from left,dist from top))
            match_sound.play()
            screen.blit(point, (100,150))
            #to update screen display.flip
            display.flip()
            sleep(0.5)
            current_images_displayed = []

    if total_skipped == len(tiles):
        showGameOverScreen()
        display.set_caption('Game Over')
        
        running = False
        
print('Goodbye!')
