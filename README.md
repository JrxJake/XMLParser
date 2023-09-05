# XMLParser
Parses XML file to determine the leaf nodes in the XML Element Tree, then draws a yellow rectangle around each of them.

It is a python file, so it is compiled automatically. Assuming you have Python downloaded, simply run the python file and input the title/extension of the XML/PNG pair you want to analyse. 

I chose to use three different libraries to help me with this project. I used the xml etree library to help traverse through the tree, making it easier to idenitify the leaf nodes. I used the pillow library to draw the yellow rectangles on to the png files. And I used the re library to simply get the coordinates of the leaf nodes from their respective "bounds" attributes. 
