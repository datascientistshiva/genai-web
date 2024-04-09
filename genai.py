from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import os

# Configure api key to access the generative ai models.
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to use gemini-pro-vision model api.
# Used to get the response according to the document or image based on the provided prompt.
def get_gemini_pro_vision_response(prompt, image, input):
    print("Gemini pro vision is started:::")
    gemini_pro_model = genai.GenerativeModel("gemini-pro-vision")
    response = gemini_pro_model.generate_content([prompt, image[0], input])
    return response.text

# Function to use gemini-pro model api.
# Content Generation
def get_gemini_pro_response(transcript_text, prompt):
    print("Gemini pro is started:::")
    gemini_pro_vision_model = genai.GenerativeModel('gemini-pro')
    response = gemini_pro_vision_model.generate_content(prompt+transcript_text)
    return response.text

# Function to use gemini-pro model api.
# chatbot with memory.
def get_gemini_pro_chatbot_response(question):
    print("Gemini pro chat history.")
    gemini_pro_chatbot_model = genai.GenerativeModel("gemini-pro")
    chat = gemini_pro_chatbot_model.start_chat(history=[])
    response = chat.send_message(question, stream=True)
    return response



if __name__ == "__main__":
    main()