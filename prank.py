import pyttsx3

def Talk(speech):
    engine = pyttsx3.init()
    voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',voice)
    engine.say(speech)
    engine.runAndWait()


text1 = "Hello Faiz Alam. How are you?"
text2 = "I am your Girl Friend. I miss you Faiz Alam"
text3 = "This is my number. Save it. And tell me that you miss me too."
text4 = "I Hate you. You forgot me?"
text5 = "Guess who am I?"
Talk(text1)
