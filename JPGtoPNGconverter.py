from PIL import Image, ImageFilter
import sys
import os

# grab the 1st and 2nd argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]



# check if "new" folder exist, if not create
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

# loop through pokidex folder


for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png','png')
	print('Complete :)')
	print(f'{clean_name}.png')

  
# python JPGtoPNGconverter.py Pokedex\ pngconverted\