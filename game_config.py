import os

IMAGE_SIZE = 128
SCREEN_SIZE = 800
NUM_TILES_SIDE = 6
NUM_TILES_TOTAL = 36
MARGIN = 12 #this is space between each tile

ASSET_DIR = 'assets'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR)  if x[-3:].lower() == 'png']

