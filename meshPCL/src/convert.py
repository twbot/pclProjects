#!/usr/bin/env python3
import cv2 
import os 
import glob 



def main():
	img_dir = "/Volumes/HADI_256GB/ABQ1071" 
	data_path = os.path.join(img_dir,'*g')
	files = glob.glob(data_path)
	print(len(files))
	width = 1024
	height = 1024
	dim = (width, height)
	data = [] 
	for f1 in files[800:]:
		img = cv2.imread(f1) 
		base_name = os.path.basename(f1)
		name = os.path.splitext(base_name)[0] + ".bmp"
		resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
		out_img = cv2.imwrite(name, resized)


if __name__ == '__main__':
	main()