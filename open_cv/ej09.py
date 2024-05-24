import cv2
image_paths = ["myimage_20240522_162233.png", "myimage_20240522_162247.png", "myimage_20240522_162255.png", "myimage_20240522_162304.png"]
#initialized a list of images
imgs = []

for i in range (len(image_paths)):
    imgs.append(cv2.imread(image_paths[i]))
    imgs[i] = cv2.resize(imgs[i], (0,0), fx=0.4, fy=0.4)
    #this is optional if your input images aren't too large. You don't need to scale down the image
    #In my case, the input images are of dimensions 3000x1200 abd due to this the resultant image
    #won't fit the screen scaling down the images
#showing the original pictures
cv2.imshow('1', imgs[0])
cv2.imshow('2', imgs[1])
cv2.imshow('3', imgs[2])
cv2.imshow('4', imgs[3])

stitchy = cv2.Stitcher.create()
(dummy, output) = stitchy.stitch(imgs)

if dummy != cv2.STITCHER_OK:
    #Checking if the stitching procedure is successful .stitch() function returns true value if
    #stitching is done successfully
    print("Stitching isn't successful")
else:
    print("Your Panorama is ready!!!")

#Final output
cv2.imshow("Final result", output)
cv2.waitKey(0)
