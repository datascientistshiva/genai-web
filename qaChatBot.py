import streamlit as st
import genai


st.header("Gemini pro chatbot.")


def main():
    # Initialize session state for chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    input = st.text_input("Input: ", key="input")
    submit = st.button("Ask the question.")

    if submit and input:
        response = genai.get_gemini_pro_chatbot_response(input)
        ## Add user query and response to session chat history.
        st.session_state['chat_history'].append(("You", input))
        st.subheader("The response is :")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))
    st.subheader("The Chat history is : ")

    for role, text in st.session_state['chat_history']:
        st.write(f"{role} : {text}")

if __name__ == "__main__":
    main()