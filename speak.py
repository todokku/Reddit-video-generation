from gtts import gTTS

def speak(myText,language):
    output = gTTS(text=myText, lang = language, slow=False)
    return output

