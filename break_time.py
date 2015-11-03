import webbrowser
import time

# short program to run in the background of your computer to remind you to take breaks at x intervals

n = 0

while  n < 3:
    time.sleep()
    webbrowser.open("http://www.youtube.com")
    n += 1
