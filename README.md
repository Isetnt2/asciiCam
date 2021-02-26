# asciiCam
A python programm to create an ascii filter for webcams. \n

Requirements: \n
  Linux \n
  V4l2loopback \n
  openCV \n
  Pillow(A fork of PIL) \n
  pyfakewebcam \n
  
 What happens: \n
  Caputures a frame from the webcam default is /dev/video0 \n
  Takes that frame and turns it into asciiArt which it saves as a txt file \n
  Turning that txt file and turning it into a jpeg thanks to OpenCV and saves it as a Jpeg \n
  Pushes/Writes that jpeg to the virtual dummy webcam created by v4l2 \n
  Repeat \n
Default file names are content.txt/.jpeg
