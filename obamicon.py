from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
usaPallet = [darkBlue, red, lightBlue, yellow]

darkGreen = (21, 140, 28)
pink = (188, 54, 163)
lightGreen = (58, 214, 47)
lightYellow = (255, 243, 84)
springPallet = [darkGreen, pink, lightGreen, lightYellow]

image = ""
continueOn = True
while continueOn:
    image = input("Please enter a file (with file type)")
    try: Image.open(image)
    except FileNotFoundError: continueOn = True
    else: continueOn = False

pallet = ""
while pallet != "usa" and pallet != "spring":
    pallet = input("Please enter a pallet (spring or usa)").lower()

# Import image.
my_image = Image.open("drWho.jpg")
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.
recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.

def recolorImage (colors):
    for rgb in image_list:
        intensity = rgb[0] + rgb[1] + rgb[2]
        if intensity < 182: recolored.append(colors[0])
        elif intensity < 364: recolored.append(colors[1])
        elif intensity < 546: recolored.append(colors[2])
        else: recolored.append(colors[3])

if pallet == "usa": recolorImage (usaPallet)
else: recolorImage (springPallet)


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
