import streamlit as st
from PIL import Image
import genai

# Used to get the response for our scenario.
prompt = """
Your are an expert in understanding invoices. 
We will upload a image as an invoice and 
you will have to answer any questions based 
on the uploaded invoice image.
"""


def main():
    ## Initialize our streamlit app 
    # st.set_page_config(page_title="MultiLanguage Invoice Extractor")
    st.title("Invoice Extractor")       
    st.header("MultiLanguage Invoice Extractor")

    # Create a file upload section which accept images in jpg, jpeg and png file format.
    uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])
    
    image=""

    if uploaded_file is not None:
        image= Image.open(uploaded_file)
        # Display the image.
        st.image(image, caption="Uploaded image.", use_column_width=True)
    
    input = st.text_input("Input Prompt: ", key="input")
    submit = st.button("Tell me about the invoice.")
    
    if submit:
        image_data = input_image_details(uploaded_file)
        response = genai.get_gemini_pro_vision_response(prompt, image_data, input)
        st.subheader("The response is ::: ")
        st.write(response)

# Function used to convert uploaded image into bytes.
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes.
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type, #Get the mime type of the uploaded file.
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded.")



if __name__ == "__main__":
    main()