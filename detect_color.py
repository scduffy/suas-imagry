# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [
	([100, 70, 128], [140, 100, 255]),  #red
	([102, 26, 0], [255, 159, 128]),  	#blue
	([0, 128, 128], [100, 255, 255]), 	#yellow
	([64, 64, 64], [217, 217, 217])   	#gray
]

i = 0
# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)

	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	#cv2.imshow("images", output)
	name = "test_img_" + str(i) + ".png"

	cv2.imwrite(name, output)
	cv2.waitKey(0)
	i = i + 1
