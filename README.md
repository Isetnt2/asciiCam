# asciiCam
A python program to create an ascii filter for webcams.

Requirements:
  
    Linux
  
    V4l2loopback
  
    openCV
  
    Pillow(A fork of PIL)
  
    pyfakewebcam
  
 What happens:
  
    Caputures a frame from the webcam. Default is /dev/video0
  
    Takes that frame and turns it into asciiArt which gets saves as a txt file
  
    Turn that txt file into a jpeg thanks to OpenCV and saves it
  
    Pushes/Writes that jpeg to the virtual dummy webcam created by v4l2
  
    Repeat

Default file names are content.txt/.jpeg
