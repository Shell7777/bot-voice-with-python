    #pywhatkit.sendwhatmsg("+51970110165","Hola Soy Karla el asistente de voz de Elvis",18,32)
import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import responseBot as bt

listener = sr.Recognizer()
engine = pyttsx3.init()

name = 'alexa'

def voiceSpeak(texto):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(texto)
    engine.runAndWait()

def listenerMicro():
    try:
        with sr.Microphone()as source:
            print ('Escuchando...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.record(source,duration=3)
            rec = listener.recognize_google(voice)
            rec =rec.lower()
            return  "{}".format(rec)
                
    except Exception as e:
        print(e)    


def comand_atomatice (rec):
    if rec is  None :
        voiceSpeak('Disculpa no te escucho bien ')
        return 
    elif 'buenos dias' in rec:
        voiceSpeak('Buenos dias Jefe')
        voiceSpeak('¿Que planes para hoy?')
    
    elif 'reproduce' in rec:
        rec = rec.replace('reproduce','')
        voiceSpeak(f'Reproduciendo a {rec}')
        pywhatkit.playonyt(rec)
        
    elif 'hora' in rec :
        hora_actual = datetime.datetime.now().strftime('%H:%M %p')  
        voiceSpeak(f'Son las {hora_actual}')

    elif 'busca' in rec :
        rec = rec.replace('busca','')
        rec  = rec.replace(' ','')
        print (rec)
        wikipedia.set_lang("es")
        info = wikipedia.summary(rec,sentences=1)
        voiceSpeak(info)
    else :
        bot = bt.Botty()
        voiceSpeak( bot.RespuestasBot(rec))
        
        #voiceSpeak(f'Informacion. {info}')
        
        
