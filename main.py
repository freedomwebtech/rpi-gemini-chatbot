
import google.generativeai as genai
from gtts import gTTS
import io
import tempfile
import pygame
from pydub import AudioSegment
from pydub.playback import play
import os
# Configure the Generative AI API with your API key
genai.configure(api_key="")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to generate AI response
def generate_ai_response(query):
    # Generate content based on the user's query
    response = model.generate_content(query)
    return response.text

# Function to convert AI response text to speech and play it directly
def speak(text):
    # Create a gTTS object in memory (without saving to a file)
    tts = gTTS(text, lang='en')
    
    # Create a temporary file to store the audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file_name = temp_file.name
        tts.save(temp_file_name)  # Save the speech to the temporary file
        
        # Convert the MP3 file to WAV using pydub
        audio = AudioSegment.from_mp3(temp_file_name)
        
        # Play the audio using pydub's playback module
        play(audio)
        
        # Clean up the temporary file (delete it after use)
        os.remove(temp_file_name)

# Main program
if __name__ == "__main__":
    print("Welcome to the AI prompt generator!")
    print("Type your question or query below (type 'exit' to quit):")
    
    while True:
        user_query = input("\nYou: ")
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            ai_response = generate_ai_response(user_query)
            print(f"\nAI: {ai_response}")
            speak(ai_response)  # Convert AI response to speech and play directly
        except Exception as e:
            print(f"An error occurred: {e}")


