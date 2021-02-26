import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw
import timeit

PIXEL_ON = (255, 255, 255)  # PIL color to use for "on"
PIXEL_OFF = (0, 0, 0)  # PIL color to use for "off"


def convert(content, font_path=None):
	image = text_image(content, font_path)
	print(image.size)
	image = image.resize((1280, 720))
	print(image.size)
	image.save("content.jpeg")


def text_image(text_path, font_path=None):
	"""Convert text file to a grayscale image with black characters on a white background.

	arguments:
	text_path - the content of this file will be converted to an image
	font_path - path to a font file (for example impact.ttf)
	"""
	# parse the file into lines
	with open(text_path) as text_file:  # can throw FileNotFoundError
		lines = tuple(l.rstrip() for l in text_file.readlines())

	# choose a font (you can see more detail in my library on github)
	large_font = 30  # get better resolution with larger size
	font_path = font_path or 'cour.ttf'  # Courier New. works in windows. linux may need more explicit path
	#test_string = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
	#test_string = "█▓▒░ "
	test_string = "#. "
	colormode = 'RGB'
	try:
		font = PIL.ImageFont.truetype(font_path, size=large_font)
	except IOError:
		font = PIL.ImageFont.load_default()
		print('Could not use chosen font. Using default.')
	t1 = timeit.default_timer()
	# make the background image based on the combination of font and lines
	pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
	max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
	# max height is adjusted down because it's too large visually for spacing	
	max_height = pt2px(font.getsize(test_string)[1])
	max_width = pt2px(font.getsize(max_width_line)[0])
	height = max_height * len(lines) # perfect or a little oversized
	width = int(round(max_width))  # a little oversized
	image = PIL.Image.new(colormode, (width, height), color=PIXEL_ON)
	draw = PIL.ImageDraw.Draw(image)
	t2 = timeit.default_timer()
	print('Image prefs time: {}'.format(t2-t1))
	# draw each line of text
	t1 = timeit.default_timer()
	vertical_position = 5
	horizontal_position = 5
	line_spacing = int(round(max_height * 0.8))  # reduced spacing seems better
	for line in lines:
		draw.text((horizontal_position, vertical_position),
				  line, fill=PIXEL_OFF, font=font)
		vertical_position += line_spacing
	t2 = timeit.default_timer()
	print('draw time: {}'.format(t2-t1))
	# crop the text
	c_box = PIL.ImageOps.invert(image).getbbox()
	image = image.crop(c_box)
	return image
