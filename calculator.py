import speech_recognition as sr
import gtts
import pyglet
import time, os 

r = sr.Recognizer()

def speakOut(text, lang):
    file = gtts.tts.gTTS(text = text, lang = lang)
    filename = '/tmp/temp.mp3'
    file.save(filename)

    music = pyglet.media.load(filename, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)

def operation(oper, a, b):
    if (oper == "add" or oper == "plus"):
        return(a+b)
    elif (oper == "substract" or oper == "minus"):
        return(a-b)
    elif (oper == "multiply" or oper == "product"):
        return(a*b)
    elif (oper == "divide" or oper == "divides"):
        return(a/b)
    else:
        return("Please input a valid operation")


with sr.Microphone() as source:
    text = "Tell the first number"
    print(text)
    speakOut(text, "en")
    audio1 = r.listen(source)

    text = 'Tell the second word'
    print(text)
    speakOut(text, 'en')
    audio2 = r.listen(source)
    
    text = 'Specify the operation. add, substract, multiply, divide'
    print(text)
    speakOut(text, 'en')
    audio3 = r.listen(source)

try:
    var1 = r.recognize_google(audio1)
    print("The first number is " + var1)
    var2 = r.recognize_google(audio2)
    print("Your second number is "+ var2)
    oper=r.recognize_google(audio3)
    print("Your operation "+ oper)

    result = operation(oper, var1, var2)
    speakOut(result, "en")

except:
    pass
