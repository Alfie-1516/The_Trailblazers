import os
import sys

import speech_recognition as sr
import pyttsx3
from word_dictionary import get_defination
from Pronunciation import pronounce
from App_snap_test import set_layout
# Initialize the recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define the wake-up word
wake_up_word = "activate"
cur_state = "inactive"

def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                myText = r.recognize_google(audio2).lower()
                print(myText)
                analyze_text(myText)
        except sr.RequestError as e:
            print("Could not request result; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred")
            sys.exit()

def get_last_word(text):
    words = text.split()
    if words:
        return words[-1]
    else:
        return None
def analyze_text(text: str):
    print(" i have been called")
    global cur_state
    if(cur_state == "active"):
        if "open developer mode" in text:
            # pronounce("Opening Developer Mode")
            set_layout()
            sys.exit()
        if "meaning" or "definition" in text:
            print(get_last_word(text))
            get_defination(get_last_word(text))
            sys.exit()
    if(text == "activate"):
        cur_state = "active"
        # pronounce("I am activated and ready to receive commands.")



def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()

def main():
    while True:

        print("Listening for wake-up word...")
        # pronounce("Listening for wake-up word...")
        record_text()





if __name__ == "__main__":
    while True:
        main()
