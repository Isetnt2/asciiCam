import cv2
import numpy as np
import math
def asciify(img, out_width = 96):
	# convert image to greyscale format
	img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


	# resize the image
	height, width = img.shape
	# print(img.shape)
	aspect_ratio = width/height
	new_width = out_width
	new_height = int(new_width/aspect_ratio*.55)
	img = cv2.resize(img, (new_width, new_height))

	# reshape image into row vector
	flatImg = np.reshape(img, -1)

	# replace each pixel with a character from array
	#chars = "$@B%8WM#**oahkbpqmZO0QLJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!;:,\"^`'.  "
	#chars = "█▓▒░ "
	chars = "#. "
	repeatN = math.ceil(255/len(chars))+1
	chars = "".join([x*repeatN for x in chars])

	new_pixels = [chars[pixel] for pixel in flatImg]
	# new_pixels = [chars[pixel//25] for pixel in flatImg]
	rows = ["".join(new_pixels[x*new_width:(x+1)*new_width]) for x in range(len(img))]
	finalImg = "\n".join(rows)

	return finalImg
