#This program reminds us to take a break every two hours


#algo
#sleep for two hours and then start


import webbrowser
import time

totalBreaks=2
breakCount=0

print("This program started on "+time.ctime())
while(breakCount < totalBreaks):
    time.sleep(2*60*60)   # since we want to take a break after evrey two hours
    webbrowser.open("https://www.youtube.com/watch?v=9enLstJ0LGQ")
    breakCount = breakCount + 1
