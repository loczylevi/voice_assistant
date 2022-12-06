from google_speech import Speech
import time
from datetime import datetime
import pywhatkit as kit

time_now = datetime.now()
current_time = time_now.strftime("%H:%M")

#kit.playonyt("Highway to hell")

ido = str(current_time)
ido_szak = ""
if "00" <= ido[:1] <= "10":
                    ido_szak = "Jóreggelt"
elif "10" <= ido[:1] <= "16":
                    ido_szak = "jónapot"
else:
                    ido_szak = "jóestét"
figy = ""
if ido[:1] >= "10":
                    figy = "Ideje lefeküdni"

text = f"{ido_szak} Levente {current_time} van"
lang = "hu"
speech = Speech(text, lang)
speech.play()
if len(figy) > 0:
                    time.sleep(0.5)
                    text = f"{figy}"
                    lang = "hu"
                    speech = Speech(text, lang)
                    speech.play()
time.sleep(0.5)
if len(figy) > 0:
                    pass
else:
                    text = "Jó kódolást kivánok"
                    lang = "hu"
                    speech = Speech(text, lang)
                    speech.play()
