from aproxColor import *
from reformtxt import *
import os
from PIL import Image

def hexcon(num):
    key = "0123456789abcdef"  # hex key
    h = ""
    h16 = int(num / 16)
    h1 = num % 16
    h = key[h16] + key[h1]
    return h


def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return r, g, b

def main():
    skipValue = 16
    #print("At this point only an 80x80 pixel image.")
    img_name = input("Input the image name to be processed : ")
    length = int(input("Length of Image (Height): "))
    width = int(input("Width of Image (Across): "))
    outfilename = img_name + ".txt"
    with open(outfilename, "w") as outfile:
        for y in range(0, length):
            for x in range(0, width):
                r, g, b = rgb_of_pixel(img_name, x, y)
                # print(r,g,b," ",end="")
                rhex = hexcon(r);
                ghex = hexcon(g);
                bhex = hexcon(b)
                hexval = rhex + ghex + bhex
                cathexval = "#" + hexval
                print(x, y, cathexval)
                outfile.write(cathexval + "\n")
            outfile.write("endline\n")
    return outfilename

file = main()

file2name = "placeholder"
file2name = file2name + ".mc.txt"
open(file2name, "x")


with open(file, 'r') as f:
    array = [line.strip() for line in f]


for i in range(0, len(array)):
    n = array[i]
    a = colorIdentify(n)
    print(str(i) + ": " + n + " | " + a)
    array[i] = a

print(array)

with open(file2name, "w") as f2:
    for line in array:
        f2.write("".join(line) + "\n")

# Create final file
newfilename = input("Name of new text file (no extension): ")
newfilename = newfilename + ".mcf.txt"
reformTextFile(file2name, newfilename)

os.remove(file)



