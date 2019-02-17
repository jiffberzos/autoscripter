from pynput import mouse
from pynput import keyboard
import time
import sys
import subprocess

class Scripter():

    def __init__(self,filename):
        self.array = []
        self.start = time.time()
        self.filename = filename

    def on_press(self,key):
        if key == keyboard.Key.esc:
            # Stop listener
            return False
        try:
            self.array.append("pyautogui.press('{}')\n".format(key.char))
        except AttributeError:
            self.array.append("pyautogui.press('{}')\n".format(key))
        self.array.append("time.sleep({})\n".format(time.time()-self.start))
        self.start = time.time()



    def on_click(self,x, y, button, pressed):
        if pressed:
            self.array.append("pyautogui.click({},{})\n".format(x, y))
            self.array.append("time.sleep({})\n".format(time.time()-self.start))
            self.start = time.time()

    def on_scroll(self,x, y, dx, dy):
        return False

    def Listen(self):

        with mouse.Listener(
                on_click=self.on_click,
                on_scroll=self.on_scroll) as listener:
                    with keyboard.Listener(on_press=self.on_press) as listener:
                        listener.join()


    def CreateScript(self):
        with open(filename, 'w') as f:
            f.write("import pyautogui \n")
            f.write("import time \n")

            for entry in self.array:
                f.write(entry)

filename = input("What name would you like to name this script? Don't include an extension.\n")  + ".py"
print('Recording begins after the sound plays (in 3 seconds).')
time.sleep(3)
subprocess.call(['/usr/bin/canberra-gtk-play','--id','message'])
scripter = Scripter(filename)
scripter.Listen()
scripter.CreateScript()
