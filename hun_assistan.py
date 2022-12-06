from google_speech import Speech
import time
from datetime import datetime
import pywhatkit as kit

time_now = datetime.now()
current_time = time_now.strftime("%H:%M")

kit.playonyt("Highway to hell")

ido = str(current_time)
ido_szak = ""
if "00" <= ido[:1] <= "10":
                    ido_szak = "Jóreggelt"
elif "10" <= ido[:1] <= "16":
                    ido_szak = "jónapot"
else:
                    ido_szak = "jóestét"
text = f"{ido_szak} Levente {current_time} van"
lang = "hu"
speech = Speech(text, lang)
speech.play()
time.sleep(0.5)
text = "Jó kódolást kivánok"
lang = "hu"
speech = Speech(text, lang)
speech.play()
