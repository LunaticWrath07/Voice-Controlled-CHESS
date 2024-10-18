import speech_recognition as sr

# Recognize chess move from voice input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your move...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        
        # Only accept valid chess moves by filtering the recognized text
        return filter_valid_moves(text.lower())
        
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return None

# Filter function to ensure only valid chess move commands are accepted
def filter_valid_moves(text):
    # Accept simple commands like "move e2 to e4"
    if "move" in text:
        move = text.replace("move ", "").strip()
        return move if len(move) in (4, 5) else None
    # You can add more cases to handle additional formats.
    return None