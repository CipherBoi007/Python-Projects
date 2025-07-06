import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female voice

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

# Function to greet based on time
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")  
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you today?")

# Main function
if __name__ == "__main__":
    greet()
    while True:
        query = take_command()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")
            
        elif 'date' in query:
            str_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {str_date}")
            
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
            
        elif 'exit' in query or 'quit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day.")
            exit()
            
        else:
            speak("I didn't understand that. Can you please repeat?")