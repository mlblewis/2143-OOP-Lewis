"""
Michael Lewis
Program:
    Assignment 3 - Image Edit
Description:
    The purpose of this program is to take an image and edit it with some cool effects
that may or may not be suprising with the outcome and either overwrite the file it was
created from or write to a new file depending on user specifications 
"""
from PIL import Image
from io import StringIO 
import urllib
from urllib.request import urlopen
import random
from pathlib import Path
import os.path

class ImageEd(object):
    """
    Class: ImageEd
    Methods: __init__, glass_effect, flip, warhol, posterize, solerize, __snap_color__, blur
    Attributes:
        string(fp) file path for Image
        img ummm it's an Image
        string(outfile) name of the file that will be output in the same filepath as the input file()
        tuple(size) the Height and Width of the Image
        int(width) the width of the Image
        int(height) the height of the image
    """
    def __init__(self, fp, file_name, outfile = None):
        self.fp = fp
        self.img = Image.open(fp + file_name)
        self.outfile = outfile
        self.pixels = list(self.img.getdata())
        self.size = self.img.size
        self.width = self.img.size[0] 
        self.height = self.img.size[1]
    """
    Method: glass_effect
    takes the image and a distance variable to randomly move pixels in the image and make it look as if 
    it is being viewed through tempered glass.
    Takes: self, distance
    Returns: Nothing, does save an image though
    """
    def glass_effect(self,distance = 5):  
        dist = distance      
        self.altImg = self.img
        for y in range(dist,(self.img.height-dist)):
            for x in range(dist,(self.img.width-dist)):
                rgb = self.img.getpixel((x,y))
                a = int((x + random.randint(0,dist)) % self.img.height)
                b = int((y + random.randint(0,dist)) % self.img.width)
                cord = (a, b)
                srgb = self.img.getpixel(cord)
                self.altImg.putpixel((x,y), srgb)
                self.altImg.putpixel(cord, tuple(rgb))
        self.altImg.save(self.fp + self.outfile)
        self.altImg.show()
    """
    Method: flip
    takes the image and flips it horizontaly and verticaly.
    Takes: self
    Returns: Nothing, does save an image though
    """
    def flip(self):
        self.altImg = self.img
        for y in range(self.img.height//2):
            for x in range(self.img.width):
                rgb = self.img.getpixel((x,y))                
                ny = self.height - (y+1)
                srgb = self.img.getpixel((x,ny))
                self.altImg.putpixel((x, ny), rgb)
                self.altImg.putpixel((x,y), srgb)
        self.altImg.save(self.fp + self.outfile)
        self.altImg.show()
    """
    Method: warhol
    takes the image and posterizes the pixels and returns a snaped color then greyscales the color and compairs it to a list of color
    choices and replaces the pixel with that color
    Takes: self
    Returns: Nothing, does save an image though
    """
    def warhol(self):
        self.altImg = self.img
        colors = [(255,0,0), (0,255,0), (0,0,255),(128,0,0), (0,128,0), (0,0,128), (128,128,128), (127,0,130), (0,127,200), (100,200,50), (0,0,0),(255,255,255) ]
        for y in range(self.img.height):
            for x in range(self.img.width):
                rgb = self.img.getpixel((x,y))
                r = self.__snap_color__(rgb[0], len(colors))
                g = self.__snap_color__(rgb[1], len(colors))
                b = self.__snap_color__(rgb[2], len(colors))
                prgb = (r,g,b)                
                grey = (prgb[0] + prgb[1] + prgb[2]) // 3
                choice = grey % len(colors)
                self.altImg.putpixel((x, y), colors[choice])
        self.img.save('File.jpg')
        self.altImg.save(self.fp + self.outfile)
        self.altImg.show()
        
    """
    Method: posterize
    takes the image and snaps the values to a modulated value and makes pixels near the same color the same color...
    Takes: self, int(mod)
    Returns: Nothing, does save an image though
    """
    def posterize(self,mod = 32):       
        self.altImg = self.img
        for y in range(self.img.height):
            for x in range(self.img.width):
                rgb = self.img.getpixel((x,y))
                r = self.__snap_color__(rgb[0], mod)
                g = self.__snap_color__(rgb[1], mod)
                b = self.__snap_color__(rgb[2], mod)
                prgb = (r,g,b)
                self.altImg.putpixel((x, y), prgb)
        self.altImg.save(self.fp + self.outfile)
        self.altImg.show()
    """
    Method: blur
    takes the image and a blur_power variable to make the pixels in the +/- blur_power range the same
    Takes: self, int(blur_power)
    Returns: Nothing, does save an image though
    """
    def blur(self,blur_power=5):   
        width = self.img.size[0]
        height = self.img.size[1]
        r = 0
        g = 0
        b = 0
        d = 2 * blur_power * 2 * blur_power
        for x in range(blur_power,width-blur_power):
            for y in range(blur_power,height-blur_power):
                for i in range(-blur_power,blur_power):
                    for j in range(-blur_power,blur_power):
                        pix = self.img.getpixel((x+i,y+j))
                        r += pix[0]
                        g += pix[1]
                        b += pix[2]
                self.img.putpixel((x,y),(int(r/d),int(g/d),int(b/d)))
                r = 0
                g = 0
                b = 0
        self.img.save(self.fp + self.outfile)
        self.img.show()

    """
    Method: __snap_color__
    takes a tuple(color) and a snap_val to group colors within the snap_val to the same value.
    Takes: self, tuple(color), and int(snap_val)
    Returns: int(color)
    """
    def __snap_color__(self,color,snap_val):
        color = int(color)
        m = color % snap_val
        if m < (snap_val // 2):
            color -= m
        else:
            color += (snap_val - m)                    
        return int(color)
    """
    Method: solarize
    takes the image and an exposure variable to alter the value of the color.
    Takes: self, exposure
    Returns: Nothing, does save an image though
    """
    def solarize(self, exposure = 32):
        exp = exposure * .01
        self.altImg = self.img
        for y in range(self.img.height):
            for x in range(self.img.width):
                rgb = self.img.getpixel((x,y))
                r = int(rgb[0] * exp)
                g = int(rgb[1] * exp)
                b = int(rgb[2] * exp)
                prgb = (255 - r, 255 - g, 255 - b)
                self.altImg.putpixel((x, y), prgb)
        self.altImg.save(self.fp + self.outfile)
        self.altImg.show()

if __name__=='__main__':
    """
    ImageEd is called with ("the file path","filename.extension","outfilename.extension")
    """
    ie = ImageEd("C:\\Users\\downw\\Downloads\\","download.jpg", "File.jpg")
    """uncomment to run, accepts a value for blur range, defaults to 5"""
    #ie.blur()
    """uncomment to run, can accept a value for the distance, defaults as 5"""
    #ie.glass_effect()
    """uncomment to run, can accept a value that is percentalized in the method so 64 turns into 64%
    defaults to 32"""
    #ie.solarize(64)
    """uncomment to run, can accept a value for mod, defaults to 32"""
    #ie.posterize()
    """uncomment to run"""
    #ie.warhol()
    """uncomment to run"""
    #ie.flip()
