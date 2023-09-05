import sys
import re
from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET

extension = input("Enter the .xml/png extension: ")

tree = ET.parse(extension + '.xml')
root = tree.getroot()

#Used for global list variable
class Globe:
    leafList = list()

#Recursively checks if the given node is a leaf node
def check(node):
    #Returns a list of all the node's children
    childList = node.findall("*")
    
    if len(childList) > 0:
        
        for child in childList:
            #Recursively check the child node            
            check(child)
    
    #Add the leaf node to the global list
    else:
        Globe.leafList.append(node)
        
#Checking if the root is a leaf node
check(root)

#Open the image        
with Image.open(extension + ".png") as img:

    for i in Globe.leafList:
    
        #Get the bounds of the leaf node
        boundString = i.attrib.get("bounds")

        #Convert the bounds into a list of ints to be used as the coordinates
        coords = re.findall(r'\d+', boundString)

        #Draw the rectangle
        draw = ImageDraw.Draw(img)
        draw.rectangle([(int(coords[0]), int(coords[1])), (int(coords[2]), int(coords[3]))], fill = None, outline = (255, 255, 0), width = 5)

    img.show()