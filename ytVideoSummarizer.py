import streamlit as st

from youtube_transcript_api import YouTubeTranscriptApi
import genai 

# Used to get the response for our scenario.
prompt = """You are youtube video summarizer. 
You will be taking the transcript text ans summarizing 
the entire cideo and providing the important summary in points within 250 words. 
Please provide the summary of the text given below.

And also provide the code for the project discussed in the video with the title of the filename.
"""

def main():
    ## Initialize our streamlit app 
    st.title("Youtube Video Summarizer")
    st.header("Youtube Video to Detailed Notes Converter")
    # Input field to receive the link of the youtube video.
    youtube_link = st.text_input("Enter YouTube Video Link:")

    if youtube_link:
        video_id = youtube_link.split("=")[1]
        # Display the image of the youtube video.
        st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)

    if st.button("Get Detailed Notes"):
        # Call the method extract_transcript_details to get the transcript of the video.
        transcript_text = extract_transcript_details(youtube_link)

        if transcript_text:
            summary = genai.get_gemini_pro_response(transcript_text, prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)   


# getting the transcript from the youtube video
def extract_transcript_details(youtube_video_url):
    print("Transcript extraction is started.")
    try:
        # Get the video_id from the url.
        video_id = youtube_video_url.split("=")[1]
        # Generate transcript of the youtube videos.
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        
        return transcript

        
    
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()