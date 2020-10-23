"""
Text-to-Speech program with GOOGLE TEXT-TO-SPEECH ENGINE(gTTS).

!!!The program needs a stable internet connection to run!!!

OS: Ubuntu

Dependencies:
1. gTTS(pip install gTTS)
2. mpg321(sudo apt install mpg321)

Main Audio File: ./audios/main.mp3
"""
import os
import time
from gtts import gTTS


def create_extra_audios():
    """
    This function will create the intros, outros and all other extra audios needed for the text-to-speech program.

    The extra audios will be created on it's own; just run the program with wifi on.
    """

    """
    Extra Audios:
    ./audios/intro.mp3: Hello.   This is a demo of the GOOGLE TEXT-TO-SPEECH ENGINE
    ./audios/intro2.mp3: Enter any text:
    ./audios/try_again.mp3: If you'd like to try again: enter Y.    Else enter N: to quit.
    ./audios/outro.mp3: Bye Bye!
    """
    print("Checking all files...")
    audio_files = os.listdir("./audios")
    if "intro.mp3" not in audio_files:
        print("Creating Intro...")
        my_obj=gTTS(text="Hello.   This is a demo of the GOOGLE TEXT-TO-SPEECH ENGINE")
        my_obj.save("./audios/intro.mp3")
    if "intro2.mp3" not in audio_files:
        print("Creating Intro2...")
        my_obj=gTTS(text="Enter any text: ")
        my_obj.save("./audios/intro2.mp3")
    if "outro.mp3" not in audio_files:
        print("Creating Outro...")
        my_obj=gTTS(text="Bye Bye!")
        my_obj.save("./audios/outro.mp3")
    if "try_again.mp3" not in audio_files:
        print("Creating Try again audio...")
        my_obj=gTTS(text="If you'd like to try again: enter Y.    Else enter N: to quit.")
        my_obj.save("./audios/try_again.mp3")


# main execution starts here
if "audios" not in os.listdir():
    os.mkdir("./audios")
create_extra_audios()
os.system("mpg321 ./audios/intro.mp3")
time.sleep(0.5)

while(True):
    os.system("mpg321 ./audios/intro2.mp3")
    my_text = input("\nYour answer: ")
    my_text = "You entered: " + my_text
    my_obj = gTTS(text=my_text)
    my_obj.save("./audios/main.mp3")
    os.system("mpg321 ./audios/main.mp3")
    time.sleep(0.8)
    os.system("mpg321 ./audios/try_again.mp3")
    answer = input("\nIf you'd like to try again enter Y, else enter N: ")
    if answer == 'y' or answer == 'Y':
        time.sleep(0.5)
        continue
    else:
        os.system("mpg321 ./audios/outro.mp3")
        print("\nBye Bye!")
        break
