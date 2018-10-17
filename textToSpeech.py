import os, time
from gtts import gTTS 
from pygame import mixer

def speak(object):
  # object = 'Hello World!'

  myobj = gTTS(text=object, lang='en-uk') 
  myobj.save("object.mp3")

  mixer.init()
  mixer.music.load('./object.mp3')
  print("Speaking "+str(object))
  mixer.music.play()
  time.sleep(2)

  # os.remove('./object.mp3')