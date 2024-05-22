**To run the application, follow below steps**
- Install python in your pc or laptop.
- Clone the application to your local environment
  - **git clone https://github.com/datascientistshiva/genai-web.git**
- **cd genai-web/**
- Create a virtual environment
  - **python -m venv /venv-name** or **python3 -m venv /venv-name**
- To install all the library from requirements.txt file.
  - **pip install -r requirements.txt**
- To run the streamlit application.
  - **streamlit run app.py**


**About the application**
***Structure of the application***
1. **requirements.txt**
    - streamlit : ***Build application for Data sharing.***
    - python-dotenv : ***Used to load all the environments such as .env***
    - pathlib : ***Used to handle the path containing information***
    - youtube_transcript_api : ***Libraries to generate trascript of Youtube Video***
    - google-generativeai : ***Libraries to use google generative ai model***

2. **app.py**
    - This is the main python file which is responsible to run our application with streamlit(that handles our frontend and data integration).
    - It consist of sidebar which have the following list **Youtube Video Summary**, **Invoice Extractor**, **Chat Bot with memory**.
    - Clicking on any item will open its respective python file which handles its own functionalities and frontend part.
    
3. **genai.py**
    - This file handles the request to and response from any LLM we use in our application.
    - In this applicaiton we configured GOOGLE_API_KEY for generative ai.
    - We use **gemini-pro** for **youtube transcribed text summary** and **chat bot with history** and **gemini-pro-vision** for **invoice text extractor application with Q/A application**.
    - We created three function for calling the LLM with our request/input and returns the result/output.

4. **ytVideoSummarizer.py**
    - This file is respolsible for the Youtube Video Summary.
    - One special library called "youtube_transcript_api" is used to extract the transcribed text form the youtube video. This library takes video_id for transcribing the text for a video.
    - Then we used **gemini-pro** with the **transcribed text** and **prompt** which we created.
    - ***Working Flow***
      - First with the help of YouTubeTranscriptApi we extracted the transcribed text.
      - Then with the help of gemini-pro model we extracted the summary.
      
      -  Context : ***transcribed text***
      -  Prompt : ***"""You are youtube video summarizer. 
  You will be taking the transcript text ans summarizing 
  the entire cideo and providing the important summary in points within 250 words. 
  Please provide the summary of the text given below."""***

5. **invoiceExtractor.py**
   - This file is responsible for invoice extractor with question answering functionalities.
   - Upload the invoice images.
   - Uploaded images is conveted to bytes_data.
   - gemini-pro-vision model is used for extracting the important data from the invoice images with the help of:
     - image_parts = [
       {
                "mime_type": uploaded_file.type, 
                "data":bytes_data
            }
        ]
     - prompt : ***""" Your are an expert in understanding invoices. 
We will upload a image as an invoice and 
you will have to answer any questions based 
on the uploaded invoice image. """***
   
6. **qaChatBot.py**
   - This application is used for creating chatbot with memory/history features.
   - gemini-pro model is used to handle the user input and create a conversational chatbot.
   - genai.GenerativeModel("gemini-pro").start_chat(history=[]) is used for creating chatbot model.
   - This store the history for conversation.
   

