import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM: 
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            # Only use environment variable for API key
            groq_api_key = os.environ.get("GROQ_API_KEY", "")
            selected_groq_model = self.user_controls_input.get("selected_groq_model")
            
            if not groq_api_key:
                st.error("❌ GROQ_API_KEY environment variable is not set. Please configure it in your deployment settings.")
                return None

            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
        
        except Exception as e:
            raise ValueError(f"Error Occured With Exception: {e}")
        return llm
