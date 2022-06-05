import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import requests
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisUI import Ui_jarvisGui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)

# text to speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()
# To convert voice into text

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=3, phrase_time_limit=8)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"user said: {self.query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        return self.query

    def TaskExecution(self):
        # if __name__ == "__main__":  # main program
        wish()
        while True:
            # if 1:

            self.query = self.takecommand().lower()

            # logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif 'hi' in self.query or 'hello' in self.query:
                speak('Hello sir, how may I help you?')

            elif "open adobe reader" in self.query:
                apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                # print(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "send whatsapp message" in self.query:
                kit.sendwhatmsg("+919179643277",
                                "this is testing protocol", 4, 13)
                time.sleep(120)
                speak("message has been sent")

            elif "song on youtube" in self.query:
                kit.playonyt("see you again")

            elif 'timer' in self.query or 'stopwatch' in self.query:
                speak("For how many minutes?")
                timing = self.takeCommand()
                timing = timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                timing = float(timing)
                timing = timing * 60
                speak(f'I will remind you in {timing} seconds')

                time.sleep(timing)
                speak('Your time has been finished sir')

            elif "email to abhishek" in self.query:
                try:
                    speak("what should i say?")
                    content = self.takecommand().lower()
                    to = "EMAIL OF THE OTHER PERSON"
                    sendEmail(to, content)
                    speak("Email has been sent to abhishek")
                except Exception as e:
                    print(e)
                    speak("sorry sir, i am not able to sent this mail to avi")

            elif "no thanks" in self.query:
                speak("thanks for using me sir, have a good day.")
                sys.exit()

    # to close any application
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

    # to set an alarm
            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music_dir = 'E:\\music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
    # to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    ###########################################################################################################################################
    ###########################################################################################################################################

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("please wait sir, feteching the latest news")
                news()

            elif "email to abhishek" in self.query:

                speak("sir what should i say")
                self.query = self.takecommand().lower()
                if "send a file" in self.query:
                    email = 'your@gmail.com'  # Your email
                    password = 'your_pass'  # Your email account password
                    send_to_email = 'To_person@gmail.com'  # Whom you are sending the message to
                    speak("okay sir, what is the subject for this email")
                    self.query = self.takecommand().lower()
                    subject = self.query   # The Subject in the email
                    speak("and sir, what is the message for this email")
                    self.query2 = self.takecommand().lower()
                    message = self.query2  # The message in the email
                    speak(
                        "sir please enter the correct path of the file into the shell")
                    # The File attachment in the email
                    file_location = input("please enter the path here")

                    speak("please wait,i am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    # Setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',
                                    "attachment; filename= %s" % filename)

                    # Attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to avinash")

                else:
                    email = 'your@gmail.com'  # Your email
                    password = 'your_pass'  # Your email account password
                    send_to_email = 'To_person@gmail.com'  # Whom you are sending the message to
                    message = self.query  # The message in the email

                    # Connect to the server
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()  # Use TLS
                    # Login to the email server
                    server.login(email, password)
                    server.sendmail(email, send_to_email,
                                    message)  # Send the email
                    server.quit()  # Logout of the email server
                    speak("email has been sent to avinash")

            # speak("sir, do you have any other work")

# to wish


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am jarvis ma'am. please tell me how may i help you")


# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL ADDRESS', 'YOUR PASSWORD')
    server.sendmail('YOUR EMAIL ADDRESS', to, content)
    server.close()


# for news updates
def news():
    main_url = 'https://newsapi.org/v2/everything?q=keyword&apiKey=41b42f6a1ca44044a3c47c754a4ba183'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisGui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie(
            "D:/jarvis_bot_gui/JarvisGUI/Gifs/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(
            "D:/jarvis_bot_gui/JarvisGUI/Gifs/Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
