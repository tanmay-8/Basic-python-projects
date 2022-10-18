from time import strftime
from pygame import mixer
import datetime
from plyer import notification

def audio_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        from_user = input()
        if from_user == stopper:
            mixer.music.stop()
            exit()
            

present=strftime('%H:%M:%S \n')
print(present)
print("ENTER TIME HERE:\n")
hour=int(input("ENTER HOUR:\n"))
minute=int(input("\nENTER MINUTES:\n"))
seconds=int(input("\nENTER SECONDS:\n"))


while True:
    if hour==datetime.datetime.now().hour and minute==datetime.datetime.now().minute and seconds==datetime.datetime.now().second:
        notification.notify(title="wakeup",message="message",app_icon= None,timeout=10,toast="false")
        audio_loop("exercise.mp3","done")   
        break 
    
     

