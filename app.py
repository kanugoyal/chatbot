from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
import pyttsx3 
import speech_recognition as sr
from PIL import ImageTk, Image
import pyaudio
import threading

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
engine.setProperty('rate', 170)

def speak(word): 
    engine.say(word)
    engine.runAndWait()

chatbot = ChatBot('Chatbot')
trainer= ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

main = Tk()

main.geometry("500x650")
main.title("ChatBot")
img= ImageTk.PhotoImage(Image.open("bot.jpg"))
photoL = Label(main, image=img)

photoL.pack(pady=5)
def takecommand():
    r= sr.Recognizer()
    r.pause_threshold=1
    print("your bot is listening try to speak")
    with sr.Microphone() as m:
        try:
           audio = r.listen(m)
           query = r.recognize_google(audio, language='en-in')
           print(query)
           textF.delete(0, END)
           textF.insert(0, query)
           ask_from_bot()
        except Exception as e:
            print("not recognized")



def ask_from_bot():
   query= textF.get()
   answer_from_bot = chatbot.get_response(Statement(query))
   msgs.insert(END," you : " +query)
   msgs.insert(END, "bot: "+ str(answer_from_bot))
   speak(answer_from_bot)
   textF.delete(0, END)
   msgs.yview(END)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame,width= 80,height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side= LEFT,fill=BOTH,pady=10)
frame.pack()

textF= Entry(main, font=("Verdana",20))
textF.pack(fill=X , pady=10)

butn = Button(main,text="Ask from Bot",font=("Verdana", 20), command = ask_from_bot)
butn.pack()


#creating enter
def enter_func(event):
    butn.invoke() 

main.bind('<Return>', enter_func)

def repeatL():
    while True:
        takecommand()

t= threading.Thread(target= repeatL)
t.start

main.mainloop()