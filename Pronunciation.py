from gtts import gTTS
from playsound import playsound
import tempfile
import os



def do_tts(text):
    tts = gTTS(text)
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete= False)
    tts.save(temp_file.name)
    file_url = os.path.abspath(temp_file.name)
    temp_file.close()
    return file_url

def pronounce(text):
    file_path = do_tts(text)
    playsound(file_path)
    os.remove(file_path)
