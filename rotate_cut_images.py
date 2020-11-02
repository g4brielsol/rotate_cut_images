""" Program to scan 4 pictures at once and separete them into 4 images """

import PIL
from PIL import Image

# amount of scans
quantity = 52
# counter for separate images
counter = 0
for i in range(1, quantity + 1):
    image = Image.open("Scan{}.jpg".format(i))

    # rotate image 90 degrees
    #image_90_degrees = image.rotate(-90)

    # save image
    #image_90_degrees.save('test.jpg')

    # comun photos
    #left,top,right,bottom
    top_left = (0,0,3452,2400)
    top_right = (3453,0,7014,2400)
    bottom_left = (0,2740,3453,5100)
    bottom_right = (3453,2740,7014,5100)

    # marriage size
    #left,top,right,bottom
    top_left_dif = (0,0,2795,2085)
    top_right_dif = (4112,0,7014,2085)
    bottom_left_dif = (0,3048,2795,5100)
    bottom_right_dif = (4100,3048,7014,5100)

            
    counter += 1
    #left,top,right,bottom -> values based on image sizes get from paint
    image.crop(top_left).save("{}.jpg".format(counter)) # top left
    counter += 1
    image.crop(top_right).save("{}.jpg".format(counter))  # top right
    counter += 1
    image.crop(bottom_left).save("{}.jpg".format(counter))  # bottom left
    counter += 1
    image.crop(bottom_right).save("{}.jpg".format(counter))  # bottom right


print("finished")