import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the chatbot model
chatbot = pipeline("text-generation", model="distilgpt2")

# Define the chatbot function
def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']

# Define the main function
def main():
    st.title("Healthcare Assistant Chatbot")
    
    # Input field for user input
    user_input = st.text_input("How can I assist you today?")
    
    # Button to submit the input
    if st.button("Submit"):
        if user_input:  # Ensure user input is not empty
            st.write("User:", user_input)  # Display user input
            
            # Show spinner while processing
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)  # Get chatbot response
                st.write("Healthcare Assistant:", response)  # Display response
        else:
            st.write("Please enter a message to get a response.")

# Run the app
if __name__ == "__main__":
    main()

