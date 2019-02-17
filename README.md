 autoscripter
==============

This is a simple script that will record the users inputs until the Esc button is pressed. It will then create a new Python script that will carry out the recorded actions, with the same time delay between clicks.

Uses the pynput module to record the users inputs, and the pyautogui to action them.

Creates the script in the same directory as autoscripter

### TO-DO ###

os.sysarg as the name of the created script
drag and scroll functionality
~3 second delay, then beep to announce recording has started.
"Duration"- (mouse-moving) and simple time-delays both supported

### Install ###

Just clone the repository, change the name of the desired script in autoscripter.py, and then run it. Make sure you have installed pyautogui and pynput with pip.
