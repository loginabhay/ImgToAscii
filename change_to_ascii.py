import cv2
import os
import numpy as np
import argparse


def main():
	parser = argparse.ArgumentParser(description='Img file')
	parser.add_argument("-i","--image", type=str, help='Path of the image', default='./img.jpg')
	args = parser.parse_args()

	img = cv2.imread(args.image,0)
	width, height = img.shape
	aspect_ratio = height/width
	new_width = 90
	new_height = int(aspect_ratio* new_width* 0.55)
	res_img = cv2.resize(img,(new_width,new_height))
	nparr = np.array(res_img)
	pixels = nparr.flatten()	
	chars = ["/","^","#","&","@","$","%","*","!",":","."]
	new_pixels = [chars[pixel//25] for pixel in pixels]
	new_pixels = ''.join(new_pixels)
	new_pixels_len = len(new_pixels)
	ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_len, new_width)]
	ascii_image = "\n".join(ascii_image)
	print(ascii_image)

	with open('ascii_img.txt','w') as i:
		i.write(ascii_image)
		
if __name__ == "__main__":
	main()
