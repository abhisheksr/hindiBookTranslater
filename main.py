# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from PIL import Image
import cv2
import re
import pytesseract
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound

def Text_to_speech(Message):
    speech = gTTS(text = Message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sruth\OneDrive\Documents\tesseract.exe'

def book_translate(images_path, source_lang, dest_lang, split_char):
    img = cv2.imread(images_path)
    # img = cv2.resize(img, (600, 500))
    # cv2.imshow("originalimage", img)
    text = pytesseract.image_to_string(img, lang=source_lang)
    lines = text.split(split_char)
    translator = GoogleTranslator(source='auto', target=dest_lang)
    for line in lines:
        if line != '':
            pattern = r'[0-9]'
            spl_chars = [';', ':', '!', "*", '/', '(', ')']
            line = re.sub(pattern, '', line)
            for i in spl_chars:
                line = line.replace(i, '')
            engoutput = translator.translate(line)
            print(line + " Meaning : " + engoutput)

            if line != '':
                Text_to_speech(line + " Meaning : " + engoutput)

# book_translate(r'C:\Users\sruth\OneDrive\book-training\hindibook\samarth-hindi-book-page.jpg', 'hin', 'en', "।")
book_translate(r'C:\Users\sruth\OneDrive\book-training\kannadabook\Poem.jpg', 'kan', 'en', '\n')