import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to recognize speech and detect user's voice
def recognize_speech_and_detect_voice():
    with sr.Microphone() as source:
        print("Speak your name...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: ", text)
            # Detect user's voice
            if "heip" in text.lower():
                print("help me please")
                engine.say("help me please")
                engine.runAndWait()
            elif "madad" in text.lower():
                print("madad madad!")
                engine.say("madad madad!")
                engine.runAndWait()
            else:
                print("I didn't recognize your voice.")
                engine.say("I didn't recognize your voice.")
                engine.runAndWait()
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            engine.say("Sorry, could not understand audio.")
            engine.runAndWait()
        except sr.RequestError as e:
            print("Error: Could not request results from Google Speech Recognition service; {0}".format(e))
            engine.say("Error: Could not request results from Google Speech Recognition service; {0}".format(e))
            engine.runAndWait()

# Call the function
recognize_speech_and_detect_voice()