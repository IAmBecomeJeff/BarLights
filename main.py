#!/usr/bin/python

import time
from dotstar import Adafruit_DotStar

numpixels = 144 # Number of LEDs in strip
stepRange = 256 # length of program iteration

LEDcolors={'red':0x00FF00, 'green':0xFF0000, 'blue':0x0000FF, 'yellow':0xAAFF00,'pink':0x00FFBB,'white':0xFFFFFF}

Wheelcolors={'red':0,'orange':20,'yellow':50,'lime':60,'green':80,'teal':120,'blue':150,'violet':180,'pink':220,'hot pink':250}

strip     = Adafruit_DotStar(numpixels, 12000000)
strip.begin()           # Initialize pins for output
strip.setBrightness(34) # Limit brightness to ~1/4 duty cycle

def Wheel(WheelPos):
    WheelPos = 255 - WheelPos;
    if WheelPos < 85:
        return strip.Color(0,255 - WheelPos * 3, WheelPos * 3)
    if WheelPos < 170:
            WheelPos -= 85
            return strip.Color(WheelPos * 3, 0, 255 - WheelPos * 3)
    WheelPos -= 170
    return strip.Color(255 - WheelPos * 3, WheelPos * 3, 0)

def show():
    strip.show()    
    
def setAllRGB(r,g,b):
    for i in range(0,numpixels):
        strip.setPixelColor(i,r,g,b)
    
def setAll(color):
    for i in range(0,numpixels):
        strip.setPixelColor(i,color)        
        
def off():
    for i in range(0,numpixels):
            strip.setPixelColor(i,0)
    strip.show()
    strip.show()

def rainbow(j):
    for i in range(0,numpixels):
        strip.setPixelColor(i,Wheel(((i*256//numpixels)+j)&255))
    
def rainbow_split(j):
    for i in range(0,numpixels/2):
        strip.setPixelColor(numpixels/2-1-i, Wheel(((i*256//numpixels)+j)&255))
    for k in range(numpixels/2,numpixels):
        strip.setPixelColor(k, Wheel((((k-numpixels/2)*256//numpixels)+j)&255))

def regular_dots(interval,color):
    for dot in range(0,numpixels,interval):        
        strip.setPixelColor(dot,color)

def moving_dots(interval,color,j):
    move = j%interval
    for dot in range(0,numpixels,interval):
        strip.setPixelColor(dot+move,color)        

def cylon(step,stepRange,length,color):
    fraction = (numpixels + length) // (stepRange/2) # set a fraction to scale the lights
    if step <= stepRange // 2:      #let the first half go forward
        head = step * fraction      #scale the starting pixel
        for pix in range(head-length,head+1):       #turn on the range of lights
            strip.setPixelColor(pix,color)          
        strip.setPixelColor(head-length,0)          #turn off the end
    if step > stepRange // 2:                       #let the second half go backward
        head = numpixels - (step * fraction)%(stepRange//2)
        for pix in range(head,head+length):         #turn on the pixels
            strip.setPixelColor(pix,color)
        strip.setPixelColor(head+length,0)          #turn off the end
            
#def brightAndDim(step,stepRange):
#    totRange = stepRange*10
#    if step 
    
    
#try:
#    while True:
##        inc = 0
#        for step in range(0,stepRange):   
#            rainbow_split(step)
#            regular_dots(10,Wheel(step))
#            regular_dots(20,LEDcolors['blue'])
#            moving_dots(13,0,step)
##            brightAndDim(step + inc*stepRange,stepRange)
#            show()
#            time.sleep(.005)
##        inc + 1
##        if inc > 9:
##            inc = 0
#except:
#    off()

try:
    while True:
        for step in range(0,stepRange):
            rainbow_split(step)
            moving_dots(12,LEDcolors['red'],step)
            show()
            time.sleep(.005)
except:
    off()

#try:
#    while True:
#        for col in LEDcolors:
#            setAll(LEDcolors[col])
#            show()
#            time.sleep(.2)
#            off()
#            time.sleep(.1)
#            
#        for col in Wheelcolors:
#            setAll(Wheel(Wheelcolors[col]))
#            show()
#            time.sleep(.2)
#            off()
#            time.sleep(.1)            
#except:
#    off()
#    
    

