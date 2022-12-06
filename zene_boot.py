import pywhatkit as kit
import time
import pyttsx3
from datetime import datetime
time_now = datetime.now()
current_time = time_now.strftime("%H:%M")
# The current date and time is 10:27:45
kit.playonyt("Illés igen")
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.50)
time.sleep(3)
ido = str(current_time)
ido_szak = ""
if "00" <= ido[:1] <= "10":
                    ido_szak = "Good Morning"
elif "10" <= ido[:1] <= "16":
                    ido_szak = "Good Afternoon"
else:
                    ido_szak = "Good evening"


engine.say(f'{ido_szak} sir the time is {current_time}')
time.sleep(1)
engine.say('good coding sir enjoy yourself')
print(ido_szak)
engine.runAndWait()









