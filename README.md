# Automate-Volume
This project will help us to control volume of our system by a wave of our hands.
The volume is controlled by the x coordinates of our wrist.
The range of the volume is between 0 and 100.
The project is written in python and basic libraries like Pycaw , OpenCV and Mediapipe are used.
OpenCV helped in video capture and processing.
Mediapipe helped in landmark capturing and real-time hand detection.
pycaw controls system audio.
comtypes is a dependency for pycaw to interact with Windows' audio devices.
Using the above mentioned libraries we scan map the hand on camera and show it using a dotted map, we then locate the wrist and use that point as our marker on the X-axis increase or decrease the volume.
This simple project can be modified to have many more applications such as changing windows, having special gestures to do special tasks and anything else we can think of, all of which we will try and make too.
For anyone trying out our little program on their own system, to exit the program press the enter key.
